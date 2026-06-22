---
name: update-dependency-lockfile
description: Workflow command scaffold for update-dependency-lockfile in async-ytmusicapi.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-dependency-lockfile

Use this workflow when working on **update-dependency-lockfile** in `async-ytmusicapi`.

## Goal

Updates the dependency lockfile (pdm.lock), likely after changing dependencies or updating environments.

## Common Files

- `pdm.lock`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Run the dependency manager to update pdm.lock.
- Commit the updated pdm.lock file.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.