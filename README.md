<!-- ========== HERO ========== -->
<div align="center">

  <h1>🚀 Awesome Agents MD</h1>

  <p><strong>Modern, beautiful, and practical docs powering AgentFetch — generate root or nested AGENTS.md bundles by changing a single target path in <a href="index.yaml"><code>index.yaml</code></a>.</strong></p>

  <p>
    <a href="https://github.com/FreeMarketamilitia/agent-fetch"><img alt="AgentFetch" src="https://img.shields.io/badge/AgentFetch-CLI-0aa?style=for-the-badge"></a>
    <img alt="Docs: Curated" src="https://img.shields.io/badge/Docs-Curated-1f6feb?style=for-the-badge">
    <img alt="PRs: Welcome" src="https://img.shields.io/badge/PRs-Welcome-ff69b4?style=for-the-badge">
    <img alt="Markdown" src="https://img.shields.io/badge/Made%20with-Markdown-1f425f?style=for-the-badge">
  </p>

  <p>
    <a href="https://buymeacoffee.com/freemm">
      <img alt="Buy Me A Coffee" src="https://img.shields.io/badge/Support-%E2%98%95%EF%B8%8F%20Buy%20Me%20A%20Coffee-orange?style=for-the-badge">
    </a>
  </p>

  <p align="center">
    <sub>AgentFetch reads this repository’s index and builds elegant <code>AGENTS.md</code> bundles: global or per-subdirectory — zero boilerplate.</sub>
  </p>
</div>

<br/>

<!-- ========== PUNCHLINE / HIGHLIGHTS ROW ========== -->
<div align="center">
  <table>
    <tr>
      <td>
        <b>Single source</b><br/>
        Keep docs modular and let AgentFetch assemble the right bundle.
      </td>
      <td>
        <b>Targets, not tooling</b><br/>
        Send output anywhere by editing one <code>target</code> path.
      </td>
      <td>
        <b>Nested by design</b><br/>
        Generate per-domain <code>AGENTS.md</code> that follow the nearest-file rule.
      </td>
    </tr>
  </table>
</div>

---

<!-- ========== TOC ========== -->
<div align="center">

|  |
|--|
| <a href="#features">Features</a> • <a href="#agentfetch-in-60-seconds">AgentFetch in 60s</a> • <a href="#quick-start">Quick start</a> • <a href="#indexyaml-format">index.yaml</a> • <a href="#nested-agentsmd-with-targets">Nested targets</a> • <a href="#agentsmd-standard-how-agents-use-it">AGENTS.md standard</a> • <a href="#examples">Examples</a> • <a href="#best-practices">Best practices</a> • <a href="#faq">FAQ</a> • <a href="#contributing">Contributing</a> • <a href="#support">Support</a> |

</div>

---

## Features

- 🎯 Targeted bundles with one-line target changes in <a href="index.yaml"><code>index.yaml</code></a>
- 🧩 Modular sources; compose without duplication
- ⚡ Fast onboarding for agents via <code>AGENTS.md</code> convention
- 🧭 Clear, modern layout and linkable sections
- 🔒 CI-agnostic and tool-agnostic — just Markdown + AgentFetch

---

## AgentFetch in 60 seconds

- Add entries to <a href="index.yaml"><code>index.yaml</code></a>
- Choose where the bundle should go via <code>target</code>
- Run AgentFetch (see usage in the project repo)
- Commit the generated <code>AGENTS.md</code>

Minimal example:

```yaml
agents:
  - name: Business Analysis Guide
    source: domains/business-analysis/ba.md
    target: AGENTS.md

  - name: Web Dev UI
    source: domains/web-dev/cline-for-webdev-ui.md
    target: domains/web-dev/AGENTS.md
```

---

## Quick start

1) Fork this repository  
2) Create a new branch  
3) Add your AI rule file  
4) Update <a href="index.yaml"><code>index.yaml</code></a>  
5) Pick a <code>target</code>:
   - <code>AGENTS.md</code> for a single root bundle  
   - <code>path/to/AGENTS.md</code> for nested bundles  
6) Commit and push your changes  
7) Use AgentFetch to add to your codebase:
   - https://github.com/FreeMarketamilitia/agent-fetch  
---

## index.yaml format

Each entry maps one source to an output destination.

```yaml
agents:
  - name: Human-friendly title
    source: path/to/source.md
    target: path/to/AGENTS.md
```

Authoring tips:
- Required strings: <code>name</code>, <code>source</code>, <code>target</code>
- <code>target</code> ends with <code>.md</code>
- Keep entries atomic; avoid over-bundling
- Prefer explicit names so bundles self-document

---

## Nested AGENTS.md with targets

AgentFetch writes bundles exactly where <code>target</code> points.

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

Result: global guidance at the root, focused guidance where work actually happens.

---

## AGENTS.md standard (how agents use it)

1) Add an <code>AGENTS.md</code> at your repository root  
2) Cover what matters:
   - Project overview
   - Build and test commands
   - Code style guidelines
   - Testing instructions
   - Security considerations  
3) Add extra instructions (PR guidelines, deployments, data notes)  
4) Large monorepo? Use nested files:
   - Place an <code>AGENTS.md</code> inside each package/subproject
   - Agents typically read the nearest file in the directory tree
   - Nearest file wins; root acts as a fallback

With AgentFetch, you generate these files by picking <code>target</code> locations in <a href="index.yaml"><code>index.yaml</code></a>.

---

## Examples

- Minimal root bundle

```yaml
agents:
  - name: Starter
    source: docs/starter.md
    target: AGENTS.md
```

- Shared source, multiple bundles

```yaml
agents:
  - name: Guidelines (root)
    source: docs/guidelines.md
    target: AGENTS.md

  - name: Guidelines (web)
    source: docs/guidelines.md
    target: domains/web-dev/AGENTS.md
```

---

## Best practices

- Keep sources short and purpose-built
- Use nested bundles for subprojects to lower cognitive load
- Treat <code>AGENTS.md</code> as living docs; update alongside code
- Avoid deep cross-linking inside the same bundle; flatten where useful
- Choose distinct <code>name</code> fields for clarity in reviews

---

## FAQ

<details>
  <summary><strong>Do I need one monolithic AGENTS.md?</strong></summary>
  <br/>
  No. Keep a slim root and generate nested files with <code>target</code> paths per area.
</details>

<details>
  <summary><strong>Nearest file precedence?</strong></summary>
  <br/>
  Agents usually read the closest <code>AGENTS.md</code> in the tree; the root acts as fallback.
</details>

<details>
  <summary><strong>Reuse the same source in multiple bundles?</strong></summary>
  <br/>
  Yes. Create multiple entries with the same <code>source</code> but different <code>target</code> paths.
</details>

<details>
  <summary><strong>Do I need CI?</strong></summary>
  <br/>
  No. This repo is CI-agnostic. AgentFetch is a standalone CLI that reads and writes based on <code>index.yaml</code>.
</details>

---

## Contributing

Contributions are welcome:
- Keep sources small, focused, and reusable
- Map each entry with clear <code>name</code>/<code>source</code>/<code>target</code> in <a href="index.yaml"><code>index.yaml</code></a>
- Follow best practices in <a href="general/best-practices/"><code>general/best-practices/</code></a>

See <a href="CONTRIBUTING.md"><code>CONTRIBUTING.md</code></a>.

---

## Support

If this helps you ship better agents and docs:
- ☕ Buy me a coffee: <a href="https://buymeacoffee.com/freemm"><strong>https://buymeacoffee.com/freemm</strong></a>

<p>
  <a href="https://buymeacoffee.com/freemm">
    <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy me a coffee" />
  </a>
</p>
