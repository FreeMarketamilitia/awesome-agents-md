import json
import os
import subprocess
import sys
import yaml

def run_git_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        sys.exit(1)

def is_branch_behind_main():
    # Fetch latest main
    run_git_command("git fetch origin main")
    # Check if main has commits not in HEAD
    behind_count = run_git_command("git rev-list --count HEAD..origin/main")
    return int(behind_count) > 0

def is_valid_path(path):
    """Check if path is a valid relative path and allowed type."""
    if not path or not path.strip():
        return False, "Path cannot be empty"

    if os.path.isabs(path):
        return False, "Absolute paths are not allowed"

    # Normalize path
    norm_path = os.path.normpath(path)

    # Disallow dangerous patterns
    if '..' in norm_path or norm_path.startswith('/'):
        return False, "Invalid path patterns (e.g., '..')"

    # Just validate the path format, don't check if it exists
    if norm_path.lower().endswith(('.md', '.yaml', '/')) or '/' not in norm_path:
        return True, None
    else:
        return False, f"Path must be a markdown file (.md), YAML file (.yaml), or directory (end with '/'): {path}"

def get_md_files_in_repo():
    """Get all .md files in the repository."""
    md_files = []
    files_to_skip = ['README.md', 'CONTRIBUTING.md']

    for root, _, files in os.walk('.'):
        for file in files:
            if file.lower().endswith('.md'):
                # Convert to relative path from repo root
                rel_path = os.path.normpath(os.path.join(root, file)).lstrip('./')

                # Skip README and CONTRIBUTING files
                if os.path.basename(rel_path).upper() in [f.upper() for f in files_to_skip]:
                    continue

                # Skip hidden directories like .github
                if rel_path.startswith('.'):
                    continue

                md_files.append(rel_path)
    return md_files

def get_md_files_in_pr():
    """Get .md files added or modified in the PR."""
    # Get files changed in the PR compared to origin/main
    diff_command = "git diff --name-only origin/main...HEAD"
    changed_files = run_git_command(diff_command).splitlines()
    return [f for f in changed_files if f.lower().endswith('.md')]

def check_md_files_in_yaml(data, md_files):
    """Check if all .md files are referenced in the 'source' field of index.yaml."""
    errors = []
    if 'agents' not in data or not isinstance(data['agents'], list):
        return errors  # Errors for missing/invalid agents list are handled in validate_index_yaml

    # Get all source paths from index.yaml
    sources = {agent.get('source') for agent in data['agents'] if isinstance(agent, dict) and 'source' in agent}

    # Check if each .md file is in the sources
    for md_file in md_files:
        if md_file not in sources:
            errors.append(f"Markdown file '{md_file}' is not referenced in the 'source' field of any agent in index.yaml")

    return errors

def validate_index_yaml():
    index_path = 'index.yaml'
    if not os.path.exists(index_path):
        return ["Missing index.yaml file"]

    try:
        with open(index_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"Invalid YAML in index.yaml: {str(e)}"]

    errors = []
    if 'agents' not in data:
        errors.append("Missing 'agents' key in index.yaml")
    elif not isinstance(data['agents'], list):
        errors.append("'agents' must be a list in index.yaml")
    else:
        for i, agent in enumerate(data['agents']):
            if not isinstance(agent, dict):
                errors.append(f"Agent entry {i+1} must be a dictionary")
                continue

            required_keys = {'name', 'source', 'target'}
            missing_keys = required_keys - set(agent.keys())
            if missing_keys:
                errors.append(f"Agent entry {i+1} missing keys: {', '.join(missing_keys)}")

            extra_keys = set(agent.keys()) - required_keys
            if extra_keys:
                errors.append(f"Agent entry {i+1} has extra keys: {', '.join(extra_keys)}")

            if 'name' in agent and not isinstance(agent['name'], str):
                errors.append(f"Agent entry {i+1} 'name' must be a string")

            for field in ['source', 'target']:
                if field in agent:
                    if not isinstance(agent[field], str):
                        errors.append(f"Agent entry {i+1} '{field}' must be a string")
                    else:
                        # For 'target' field, we only check format, not file existence
                        # since targets are output files created on user's system
                        if field == 'target':
                            # Quick format check for target field
                            if not agent[field] or len(agent[field].strip()) == 0:
                                errors.append(f"Agent entry {i+1} 'target' field cannot be empty")
                            elif not os.path.isabs(agent[field]):
                                # Normalize path for target
                                norm_path = os.path.normpath(agent[field])
                                if '..' in norm_path:
                                    errors.append(f"Agent entry {i+1} invalid 'target': Dangerous path patterns (e.g., '..')")
                        else:
                            # For 'source' field, validate file existence
                            valid, msg = is_valid_path(agent[field])
                            if not valid:
                                errors.append(f"Agent entry {i+1} invalid '{field}': {msg}")

    # Check if all .md files are referenced in index.yaml
    # Option 1: Check all .md files in the repo
    md_files = get_md_files_in_repo()
    # Option 2: Check only .md files modified in the PR (uncomment to use)
    # md_files = get_md_files_in_pr()
    errors.extend(check_md_files_in_yaml(data, md_files))

    return errors

def main():
    errors = []

    if is_branch_behind_main():
        errors.append("Branch is behind main - please rebase or merge main into your branch")

    errors.extend(validate_index_yaml())

    # Output as JSON array for the workflow script
    print(json.dumps(errors))
    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
