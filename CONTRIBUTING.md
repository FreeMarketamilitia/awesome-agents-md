# Contributing to Awesome Agents MD

Thank you for your interest in contributing to the Awesome Agents MD repository! This project aims to provide a comprehensive collection of guides, workflows, and resources for software development and related domains. Contributions are welcome and help make this repository a more valuable resource for the community.

## How to Contribute

### 1. Fork the Repository
- Fork the repository on GitHub to your own GitHub account.
- Clone your forked repository to your local machine: `git clone https://github.com/yourusername/awesome-agents-md.git`

### 2. Set Up Your Development Environment
- Ensure you have a Git client installed.
- Open the project in your preferred code editor (e.g., VSCode, as referenced in many of our guides).

### 3. Create a New Branch
- Create a new branch for your changes: `git checkout -b feature/your-feature-name`
- This helps keep your changes organized and separate from the main branch.

### 4. Add or Edit Content
- Navigate to the appropriate directory based on the topic of your contribution (see README.md for folder structure).
- If you're adding a new guide or resource, create the necessary folder structure. For example:
  - For a new domain (e.g., "cybersecurity"), create a new folder under `domains/` and add your content.
  - For a new framework (e.g., "Angular"), create a folder under `frameworks/` and add your content.
  - For language-specific content, add to the appropriate directory under `languages/`.
- Write your content in Markdown format (.md files).
- Follow the naming conventions used in the repository (e.g., lowercase with hyphens for file names).

### 5. Update index.yaml (if applicable)
- If you're adding new guides that should be indexed, add an entry to `index.yaml` following the existing structure:
  ```yaml
  agents:
    - name: "Your Guide Name"
      source: "path/to/your-file.md"
      target: "AGENTS.md"
  ```

### 6. Commit Your Changes
- Stage your changes: `git add .`
- Commit with a descriptive message: `git commit -m "Add new guide for [topic]"`

### 7. Push and Create a Pull Request
- Push your branch to your forked repository: `git push origin feature/your-feature-name`
- Create a Pull Request (PR) on the original repository, providing a clear description of your changes and why they're valuable.

## Guidelines for Contributions

### Content Quality
- Ensure your contribution is accurate, well-researched, and relevant to software development or related domains.
- Write in clear, concise English. Use headings, lists, and code blocks where appropriate to improve readability.
- Include examples or code snippets where relevant to demonstrate concepts.

### File and Folder Structure
- Create new folders as needed to organize content logically (e.g., if there's a new programming language, create a folder under `languages/`).
- Use `.gitkeep` files in empty directories to maintain the folder structure in the repository.
- Avoid creating redundant or overlapping content; check existing files to see if your contribution fits better within an existing guide.

### Naming Conventions
- Use lowercase for file and folder names.
- Use hyphens (-) instead of underscores (_) or spaces for multi-word names (e.g., `business-analysis.md`).
- File names should be descriptive and indicate the content (e.g., `python-asyncio-guide.md`).

### Pull Request Best Practices
- Provide a clear title and description for your PR.
- If your changes are extensive, break them into multiple PRs for easier review.
- Be open to feedback and willing to make revisions based on reviewer comments.

## Reporting Issues
- If you find bugs, inconsistencies, or areas for improvement, create an issue on GitHub with detailed information.
- Label your issue appropriately (e.g., "bug", "enhancement", "documentation").

## Code of Conduct
- Be respectful and inclusive in all interactions.
- Focus on constructive feedback and collaboration.

## Questions?
If you have any questions about contributing, feel free to open an issue or start a discussion in the GitHub repository.

We appreciate your contributions and look forward to building a better resource together!
