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
        for agent in data['agents']:
            if not isinstance(agent, dict) or 'name' not in agent:
                errors.append(f"Invalid agent entry: {agent} (must be dict with 'name')")

            # Check if source file exists (if present)
            if 'source' in agent and isinstance(agent['source'], str):
                if not os.path.exists(agent['source']):
                    errors.append(f"Source file not found: {agent['source']}")

    return errors

def main():
    errors = []

    if is_branch_behind_main():
        errors.append("Branch is behind main - please rebase or merge main into your branch")

    errors.extend(validate_index_yaml())

    # Print JSON for workflow to pick up
    print(json.dumps(errors))

    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
