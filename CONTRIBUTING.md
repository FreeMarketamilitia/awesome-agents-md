<!-- ========== HERO ========== -->
<div align="center">

  <h1>🤝 Contributing to Awesome Agents MD</h1>

  <p><strong>Help build a modern, beautiful, and practical knowledge base that powers AgentFetch.</strong><br/>Everything is Markdown and indexed through <a href="index.yaml"><code>index.yaml</code></a> to generate root or nested <code>AGENTS.md</code> bundles.</p>

  <p>
    <img alt="Good First Issues" src="https://img.shields.io/badge/Good%20First%20Issues-Welcome-4c1?style=for-the-badge">
    <img alt="Docs: Markdown" src="https://img.shields.io/badge/Docs-Markdown-1f425f?style=for-the-badge">
    <img alt="AgentFetch Ready" src="https://img.shields.io/badge/AgentFetch-Ready-0aa?style=for-the-badge">
  </p>

  <p align="center">
    <sub>First time here? Scroll to “Quick start” and “PR checklist”. Want to add content to bundles? See “index.yaml authoring”.</sub>
  </p>
</div>

---

## Principles

- Keep sources small, focused, and reusable
- Prefer clarity over cleverness; write for agents and humans
- Default to additive changes; avoid breaking links and paths
- Embrace nested bundles: put guidance where the work happens

---

## What you can contribute

- Guides and rulefiles under:
  - <a href="domains/"><code>domains/</code></a>, <a href="frameworks/"><code>frameworks/</code></a>, <a href="general/best-practices/"><code>general/best-practices/</code></a>, <a href="workflows/"><code>workflows/</code></a>
- Best-practice docs (naming, testing, security, workflows)
- Examples/snippets and improved explanations
- Updates to <a href="index.yaml"><code>index.yaml</code></a> to shape which bundles are produced and where

If you’re unsure where something fits, open a small PR and we’ll help route it.

---

## Quick start

1) Fork and clone  
2) Create a branch:
   - <code>git checkout -b docs/short-topic-name</code>  
3) Add or update Markdown content in the right directory  
4) If your content should be bundled by AgentFetch, add an entry in <a href="index.yaml"><code>index.yaml</code></a>  
5) Commit and open a Pull Request

---

## PR checklist

- Scope is focused and reviewable (small PRs > large)
- Filenames: lowercase, hyphen-separated (e.g., <code>naming-conventions-best-practices.md</code>)
- Content is succinct, actionable, and formatted for scan-ability
- Links are relative and valid
- If bundled, an <a href="index.yaml"><code>index.yaml</code></a> entry exists with the correct <code>target</code>

Optional but helpful:
- Add a brief rationale in the PR description
- If you moved/renamed files, note it clearly

---

## Writing style guide

- Use descriptive H2/H3 headings
- Start with a short “When to use” or “Context” blurb
- Prefer bullet lists and short paragraphs
- Provide examples where possible
- Keep tone direct and professional; avoid fluff
- Use code fences for commands and YAML

Example:

```md
## When to use
Short context to help readers decide quickly.

## Steps
- Step 1
- Step 2

## Example
```bash
your command here
```
```

---

## Naming and structure

- Lowercase, hyphenated filenames: <code>short-descriptive-name.md</code>
- Place content in the closest, most relevant folder
- Use <code>.gitkeep</code> for empty but intentional directories
- Avoid duplication; refactor into shared docs if necessary

---

## index.yaml authoring

AgentFetch reads <a href="index.yaml"><code>index.yaml</code></a> to build <code>AGENTS.md</code> bundles. Each entry maps one source to an output destination.

```yaml
agents:
  - name: Human-friendly title
    source: path/to/source.md        # relative to repo root
    target: path/to/AGENTS.md        # where AgentFetch writes the bundle
```

Authoring rules:
- Required non-empty strings: <code>name</code>, <code>source</code>, <code>target</code>
- <code>target</code> ends with <code>.md</code>
- Keep entries atomic to avoid cross-bundling surprises

### Nested AGENTS.md with targets

Create root or nested bundles by adjusting the <code>target</code> path.

- Root-only bundle:
  ```yaml
  agents:
    - name: Overview
      source: docs/overview.md
      target: AGENTS.md
  ```

- Per-domain bundles:
  ```yaml
  agents:
    - name: Web Dev UI
      source: domains/web-dev/cline-for-webdev-ui.md
      target: domains/web-dev/AGENTS.md

    - name: Slides
      source: domains/presentation/comprehensive-slide-dev-guide.md
      target: domains/presentation/AGENTS.md
  ```

- Mixed (root + nested):
  ```yaml
  agents:
    - name: Overview
      source: docs/overview.md
      target: AGENTS.md

    - name: Web Dev UI
      source: domains/web-dev/cline-for-webdev-ui.md
      target: domains/web-dev/AGENTS.md
  ```

Nearest-file precedence:
- Agents generally read the nearest <code>AGENTS.md</code> in the directory tree
- Nested files take precedence; root acts as fallback

---

## Commit messages

- Use imperative mood and keep it short, e.g.:
  - <code>docs: add quick start for AgentFetch targets</code>
  - <code>guide: clarify naming conventions and examples</code>
- Reference impacted areas (docs/guide/workflow/etc.)
- If fixing a link or path, say so explicitly

---

## FAQ

<details>
  <summary><strong>Do I need a single monolithic AGENTS.md?</strong></summary>
  <br/>
  No. Keep a slim root and create nested subproject files by setting different <code>target</code> paths in <code>index.yaml</code>.
</details>

<details>
  <summary><strong>Can I reuse the same source in multiple bundles?</strong></summary>
  <br/>
  Yes. Use multiple entries sharing the same <code>source</code> but with different <code>target</code> paths.
</details>

<details>
  <summary><strong>Where should a new topic live?</strong></summary>
  <br/>
  Prefer the closest domain or framework directory. If in doubt, open the PR and we’ll help place it.
</details>

---

## Reporting issues

- Open a GitHub issue with a clear title and reproduction or context
- Label as <em>bug</em>, <em>documentation</em>, or <em>enhancement</em>
- Include links to impacted files where possible

---

## Code of Conduct

- Be respectful and inclusive
- Prefer constructive, actionable feedback
- Assume good intent; collaborate openly

---

## See also

- Project entry point: <a href="README.md"><code>README.md</code></a>  
- Manifest for bundles: <a href="index.yaml"><code>index.yaml</code></a>  
- Example best practices:  
  - <a href="general/best-practices/naming-conventions-best-practices.md"><code>general/best-practices/naming-conventions-best-practices.md</code></a>  
  - <a href="general/best-practices/workflow-rules.md"><code>general/best-practices/workflow-rules.md</code></a>  
  - <a href="general/best-practices/writing-effective-clinerules.md"><code>general/best-practices/writing-effective-clinerules.md</code></a>

---

## Questions?

Open an issue or discussion in the repository. We appreciate your contributions — thanks for helping builders and agents ship with confidence.
