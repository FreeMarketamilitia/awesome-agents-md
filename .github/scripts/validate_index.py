import os
import sys
import subprocess
import yaml
import json

ALLOWED_FILE_EXTENSIONS = {".md", ".yaml"}

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def check_branch_up_to_date():
    try:
        run("git fetch --prune origin main || git fetch origin main")
        base = run("git merge-base HEAD origin/main")
        main = run("git rev-parse origin/main")
        if base != main:
            return ["Branch is behind main. Rebase or merge main into your branch."]
        return []
    except Exception as e:
        return [f"Failed to check branch sync with main: {e}"]

def load_index():
    with open("index.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_files():
    errors = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".github" in root:
            continue
        for name in files:
            path = os.path.join(root, name)
            _, ext = os.path.splitext(name)
            if ext not in ALLOWED_FILE_EXTENSIONS:
                errors.append(f"Invalid file type: {path}")
    return errors

def validate_index(index):
    errors = []
    if not isinstance(index, dict) or "agents" not in index or not isinstance(index["agents"], list):
        errors.append("index.yaml must have a top-level 'agents' list.")
        return errors

    for i, agent in enumerate(index["agents"], start=1):
        if not isinstance(agent, dict):
            errors.append(f"Entry {i} in agents must be a mapping, got: {agent}")
            continue

        required = {"name", "source", "target"}
        extra_keys = set(agent.keys()) - required
        missing_keys = required - set(agent.keys())

        if missing_keys:
            errors.append(f"Entry {i} is missing fields: {', '.join(missing_keys)}")
        if extra_keys:
            errors.append(f"Entry {i} has unexpected fields: {', '.join(extra_keys)}")

        for key in required:
            if key in agent and (not isinstance(agent[key], str) or not agent[key].strip()):
                errors.append(f"Entry {i} has invalid {key}: must be a non-empty string")

        if "source" in agent:
            source_path = os.path.join(os.getcwd(), agent["source"])
            if not os.path.exists(source_path):
                errors.append(f"Entry {i} source file not found: {agent['source']}")

    return errors

def main():
    errors = []

    errors.extend(check_branch_up_to_date())

    try:
        index = load_index()
    except Exception as e:
        errors.append(f"Failed to parse index.yaml: {e}")
        print(json.dumps(errors))
        sys.exit(1)

    errors.extend(validate_files())
    errors.extend(validate_index(index))

    # Print JSON for workflow to pick up
    print(json.dumps(errors))

    if errors:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
