# Repository Guidelines

## Project Structure & Module Organization

This repository stores configuration files. Keep each tool or application in its existing top-level directory, and place shared documentation at the repository root. Preserve the destination layout expected by the consuming tool; avoid moving files solely for cosmetic organization. Keep generated files, local caches, credentials, and machine-specific state out of version control. When adding a new configuration area, include a short README if installation or linking is not obvious.

## Validation & Development Commands

There is no repository-wide build step. Validate the files you change with the owning application's parser or check command when one is available. Before submitting changes, run:

```sh
git status --short
git diff --check
git diff
```

These commands identify unexpected files, whitespace errors, and the exact patch under review. If a directory provides its own script, formatter, or validation instructions, run those from that directory and document any new command alongside the configuration.

## Coding Style & Naming Conventions

Match the surrounding file's syntax, indentation, quoting, and key ordering. Prefer small, focused edits over broad reformatting. Use lowercase, descriptive names for new directories and files unless the target application requires another convention. Add comments only where they explain intent, compatibility constraints, or a non-obvious value. Use UTF-8 text and keep line endings consistent with nearby files.

## Testing Guidelines

Treat successful parsing and application startup as the minimum test. For behavior changes, verify the affected feature in a safe local environment and note the result in the pull request. Do not test destructive settings against production data. Where automated tests exist, keep fixtures free of secrets and name tests after the behavior they verify.

## Commit & Pull Request Guidelines

Write concise, imperative commit subjects, for example `Update shell aliases` or `Fix editor formatting defaults`. Keep unrelated tools or applications in separate commits. Pull requests should explain the purpose, list affected configuration areas, describe validation performed, and call out platform-specific behavior. Include screenshots only when a visual interface changes, and link the relevant issue when one exists.

## Security & Configuration Tips

Never commit passwords, API tokens, private keys, personal identifiers, or unredacted host-specific paths. Use environment variables, ignored local override files, or documented placeholders instead. Review staged changes carefully before every commit.
