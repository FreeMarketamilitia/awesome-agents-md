import json
import os
import subprocess
import sys
import yaml


def run(cmd: str) -> str:
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}\nError: {e.output}")
        return ""


def get_changed_files():
    run("git fetch origin main")
    out = run("git diff --name-status origin/main...HEAD")
    changed = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split(None, 1)
        if len(parts) == 2:
            changed.append((parts[0].strip(), parts[1].strip()))
    return changed


def index_yaml_changed(changed) -> bool:
    return any(p == "index.yaml" for _, p in changed)

def new_non_doc_md_added(changed) -> bool:
    skip = {"readme.md", "contributing.md"}
    for status, path in changed:
        if status and status[0].upper() == "A" and path.lower().endswith(".md"):
            if os.path.basename(path).lower() not in skip:
                return True
    return False

def is_behind_main() -> bool:
    run("git fetch origin main")
    behind = run("git rev-list --count HEAD..origin/main")
    try:
        return int(behind) > 0
    except Exception:
        return False

def validate_index_yaml(require_source_exists: bool = False):
    errors = []
    if not os.path.exists("index.yaml"):
        return ["Missing index.yaml file"]

    try:
        with open("index.yaml", "r") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"Invalid YAML in index.yaml: {e}"]

    if not isinstance(data, dict):
        errors.append("index.yaml must be a YAML mapping (dictionary) at the top level")
        return errors

    agents = data.get("agents")
    if agents is None:
        errors.append("Missing 'agents' key in index.yaml")
        return errors
    if not isinstance(agents, list):
        errors.append("'agents' must be a list in index.yaml")
        return errors

    for i, agent in enumerate(agents):
        if not isinstance(agent, dict):
            errors.append(f"Agent entry {i+1} must be a mapping (dictionary)")
            continue

        for key in ("name", "source", "target"):
            v = agent.get(key)
            if not isinstance(v, str) or not v.strip():
                errors.append(f"Agent entry {i+1} '{key}' must be a non-empty string")

        target = str(agent.get("target", "")).strip()
        if target and not target.lower().endswith(".md"):
            errors.append(f"Agent entry {i+1} 'target' must end with .md")

        if require_source_exists:
            source = str(agent.get("source", "")).strip()
            if source:
                norm = os.path.normpath(source)
                if os.path.isabs(norm) or norm.startswith(".."):
                    errors.append(
                        f"Agent entry {i+1} invalid 'source' path: must be relative and not traverse parents"
                    )
                elif not os.path.exists(norm):
                    errors.append(
                        f"Agent entry {i+1} 'source' file not found in commit: {source}"
                    )

    return errors


def main():
    pr_number = os.getenv("GITHUB_PR_NUMBER", "unknown")
    changed = get_changed_files()
    idx_changed = index_yaml_changed(changed)
    new_md = new_non_doc_md_added(changed)

    errors = []
    if is_behind_main():
        errors.append("Branch is behind main - please rebase or merge main into your branch")

    if not idx_changed and not new_md:
        print(f"PR #{pr_number}: No changes to index.yaml or new non-doc .md files; validation skipped")
        print(json.dumps(errors))
        sys.exit(1 if errors else 0)

    errors.extend(validate_index_yaml(require_source_exists=idx_changed))
    if errors:
        print(f"PR #{pr_number}: Validation failed with errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print(f"PR #{pr_number}: Validation passed")

    print(json.dumps(errors))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
