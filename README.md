# Awesome Agents MD

## Folder/File Structure

This repository is organized into several main directories, each containing resources and guides for different aspects of software development, workflows, and best practices. The structure is hierarchical and categorized to make navigation and discovery easier.

### Root Level Files
- `index.yaml`: A configuration file that indexes various guides and resources (explained in detail below).
- `README.md`: This file, providing an overview of the repository structure.

### Directory Structure

- **`domains/`**: Contains domain-specific guides and resources.
  - `business-analysis/`: Resources for business analysis, including guides like `ba.md`.
  - `data-science/`: Placeholder for data science resources (currently empty except for `.gitkeep`).
  - `game-development/`: Placeholder for game development resources.
  - `machine-learning/`: Placeholder for machine learning resources.
  - `mobile/`: Placeholder for mobile development resources.
  - `presentation/`: Guides for presentation-related tasks, such as slide creation and development (`cline-for-slides.md`, `comprehensive-slide-dev-guide.md`).
  - `web-dev/`: Web development UI guides (`cline-for-webdev-ui.md`).

- **`frameworks/`**: Resources for specific software frameworks.
  - `django/`: Placeholder for Django-related guides.
  - `express/`: Placeholder for Express.js resources.
  - `flask/`: Placeholder for Flask documentation.
  - `netxjs/`: Contains Next.js-related content, like `next-js-supabase.md` (note: appears to be a typo for "nextjs" in the directory name).
  - `pytest/`: Placeholder for Pytest testing guides.
  - `react/`: Placeholder for React framework resources.
  - `unittest/`: Placeholder for unit testing guides.
  - `vite/`: Placeholder for Vite build tool resources.
  - `vue/`: Placeholder for Vue.js resources.

- **`general/`**: General-purpose resources and best practices.
  - `best-practices/`: Comprehensive guides on software engineering, including Gemini AI tools, MCP development, workflow rules, and writing effective rules.

- **`languages/`**: Resources for programming languages.
  - Directories for various languages like `go/`, `java/`, `javascript/`, `python/`, `r/`, `rust/`, `typescript/` (all contain placeholder `.gitkeep` files).

- **`libraries/`**: Guides for specific software libraries.
  - Directories for libraries such as `asyncio/`, `axios/`, `fastapi/`, `lodash/`, `numpy/`, `pandas/`, `pyodbc/` (all with placeholders).

- **`templates/`**: Template resources.
  - `code-snippets/`: Placeholder for code snippet templates.

- **`tools/`**: Resources for development tools.
  - `docker/`, `gemini-cli/`, `git/`, `kubernetes/`, `vscode/` (all placeholders).

- **`workflows/`**: Workflow and process guides.
  - Contains multiple markdown files for various workflows like brainstorming, research, memory management, and automation guides (e.g., `baby-steps.md`, `BrainStorming-workspace.md`, etc.).

## Index.yaml Explanation

The `index.yaml` file serves as an index or manifest for the repository's resources. It defines a list of "agents" or guides, each mapped to a specific source file and a target download path (used by `agentfetch`). This file is used for downloading and consolidating markdown content into local files.

### Structure
- **Format**: YAML (Yet Another Markup Language), which is human-readable and structured.
- **Top-Level Key**: `agents` - An array of objects, each representing a single guide or resource.
- **Fields per Agent**:
  - `name`: A human-readable title for the guide.
  - `source`: The file path relative to the repository root where the guide's content is located (e.g., `domains/business-analysis/ba.md`).
  - `target`: The file path where the content will be downloaded when using `agentfetch` in the folder where agentfetch is run (e.g., `AGENTS.md` means the guide will be saved as AGENTS.md in the current directory).

This setup enables easy downloading and management of guides using `agentfetch`, allowing users to retrieve specific or batch content locally.

## Support the Project

Help maintain this growing collection of software development guides and best practices! 🌟

Your support keeps all content **free and accessible** while funding:
- Regular updates for emerging technologies
- Automated quality assurance tools
- Community-driven documentation improvements

**☕ Buy me a coffee:** Support ongoing development and help developers worldwide!

[![](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/freemm)
