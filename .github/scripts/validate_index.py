import os
import sys
import subprocess
import yaml

ALLOWED_EXTENSIONS = {".md", ".yaml", ""}  # "" means directory

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def check_branch_up_to_date():
    try:
        run("git fetch origin main")
        base = run("git merge-base HEAD origin/main")
        main = run("git rev-parse origin/main")
        if base != main:
            return ["❌ Branch is behind main. Rebase or merge main into your branch."]
        return []
    except Exception as e:
        return [f"❌ Failed to check branch sync with main: {e}"]

def load_index():
    with open("index.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_files():
    errors = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".github" in root:
            continue
        for name in files:
            _, ext = os.path.splitext(name)
            if ext not in ALLOWED_EXTENSIONS:
                errors.append(f"❌ Invalid file type: {os.path.join(root, name)}")
    return errors

def validate_index(index):
    errors = []
    if not isinstance(index, dict) or "agents" not in index or not isinstance(index["agents"], list):
        return ["❌ index.yaml must have a top-level 'agents' list."]

    for i, agent in enumerate(index["agents"], start=1):
        if not isinstance(agent, dict):
            errors.append(f"❌ Entry {i} in agents must be a mapping, got: {agent}")
            continue

        required = {"name", "source", "target"}
        extra_keys = set(agent.keys()) - required
        missing_keys = required - set(agent.keys())

        if missing_keys:
            errors.append(f"❌ Entry {i} is missing fields: {', '.join(missing_keys)}")
        if extra_keys:
            errors.append(f"❌ Entry {i} has unexpected fields: {', '.join(extra_keys)}")

        for key in required:
            if key in agent and (not isinstance(agent[key], str) or not agent[key].strip()):
                errors.append(f"❌ Entry {i} has invalid {key}: must be a non-empty string.")

        if "source" in agent:
            source_path = agent["source"]
            if not os.path.exists(source_path):
                errors.append(f"❌ Entry {i} source file not found: {source_path}")

    return errors

def main():
    errors = []

    print("🔍 Running pre-merge validation checks...")

    # Critical check - ensure branch is not behind main
    print("📋 Checking if branch is behind main...")
    sync_errors = check_branch_up_to_date()
    if sync_errors:
        errors.extend(sync_errors)
        print("❌ Branch sync check failed - merge would introduce conflicts or outdated code")
    else:
        print("✅ Branch is up-to-date with main")

    # Load and validate index.yaml
    print("📄 Validating index.yaml structure...")
    try:
        index = load_index()
    except Exception as e:
        print(f"❌ Failed to parse index.yaml: {e}")
        sys.exit(1)

    # Validate files in repo
    print("📁 Validating repository file structure...")
    errors.extend(validate_files())
    errors.extend(validate_index(index))

    if errors:
        print("\n❌ VALIDATION FAILED - The following issues must be resolved:")
        for error in errors:
            print(f"  {error}")
        print("\n💡 To fix sync issues: rebase or merge main into your branch")
        sys.exit(1)
    else:
        print("\n✅ ALL VALIDATION CHECKS PASSED")
        print("✅ Branch is up-to-date with main")
        print("✅ Repository structure is valid")
        print("✅ Ready for merge")

if __name__ == "__main__":
    main()
