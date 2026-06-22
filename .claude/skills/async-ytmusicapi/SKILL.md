```markdown
# async-ytmusicapi Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill documents the development patterns and workflows used in the `async-ytmusicapi` Python project. It covers coding conventions, file organization, commit styles, and routine project workflows such as documentation and dependency updates. By following these patterns, contributors can maintain consistency and efficiency across the codebase.

## Coding Conventions

### File Naming
- **Style:** CamelCase
- **Example:**  
  ```
  asyncYtMusicApi.py
  utilsHelper.py
  ```

### Import Style
- **Style:** Relative imports are preferred.
- **Example:**
  ```python
  from .utilsHelper import parse_response
  from .models import Track
  ```

### Export Style
- **Style:** Named exports
- **Example:**
  ```python
  __all__ = ["YtMusicClient", "Track", "Playlist"]
  ```

### Commit Patterns
- **Types:** Mixed (features, chores, etc.)
- **Prefixes:** Commonly use `feat` and `chore`
- **Example:**
  ```
  feat: add async search method
  chore: update dependencies
  ```

## Workflows

### Update Documentation
**Trigger:** When you want to update or improve the project documentation.  
**Command:** `/update-docs`

1. Edit `README.rst` to add or clarify documentation.
2. Commit the changes with a message referencing documentation or README.
   - Example commit message:  
     ```
     chore: update README with usage examples
     ```
3. Push your changes and open a pull request if required.

### Update Dependency Lockfile
**Trigger:** When dependencies change or to ensure the lockfile is current.  
**Command:** `/update-lockfile`

1. Run the dependency manager to update `pdm.lock`.
   - Example command:  
     ```
     pdm lock
     ```
2. Commit the updated `pdm.lock` file.
   - Example commit message:  
     ```
     chore: update pdm.lock after dependency changes
     ```
3. Push your changes and open a pull request if required.

## Testing Patterns

- **Framework:** Unknown (not detected)
- **File Pattern:** Test files are named with the `.test.ts` extension.
- **Example:**
  ```
  testAsyncSearch.test.ts
  ```
- **Note:** While the main codebase is Python, some test files may use TypeScript. Ensure you follow the naming convention and place tests in the appropriate directory.

## Commands

| Command           | Purpose                                           |
|-------------------|---------------------------------------------------|
| /update-docs      | Update or clarify project documentation           |
| /update-lockfile  | Update dependency lockfile after changes          |
```
