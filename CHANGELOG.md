## 2.0.0 (2026-06-09)

### Feat

- style improvements
- remove mypy hook

### Fix

- **ci**: GitHub Actions fix

### Refactor

- drop all pep refrences
- switch to source layout
- use standardlibary only

## 1.1.2 (2025-09-29)

### Chore

- Update dependencies.

## 1.1.1 (2025-03-04)

### Chore

- Update dependencies.

## 1.1.0 (2024-03-21)

### Feat

- don't constrain to Python 3 versions

## 1.0.3 (2024-03-19)

### Fix

- `default_language_version` is not a valid key in `.pre-commit-hook.yaml`

## 1.0.2 (2023-08-21)

### Fix

- **verify-git-email**: only fail if no email address matches, don't fail eagerly on first

## 1.0.1 (2023-08-16)

### Fix

- **verify-git-email**: since multiple arguments require --domains d --domains d and that is too verbose and domains shoudl then be singular, we go for --domains d1,d2

## 1.0.0 (2023-08-16)

### Feat

- **verify-git-email**: Breaking: Allow multiple domains
- support for python 3.9 as well
- **verify-git-email**: add executable and pre-commit hook for verifying the email used in the git config

### Fix

- **verify-git-email**: link correct executable after renaming of module
- **verify-git-email**: raise proper exit on success
- **verify-git-email**: wrong spelling of pre-commit-hook file
- **verify-git-email**: actually using that hook

### Refactor

- **verify-git-email**: use typer
- **verify-git-email**: re-name test file to reflect source structure
- **verify-git-email**: use git's spelling of email
- **poetry**: use latest release to put version number in `poetry.lock`
- **verify-git-email**: omitting elese if last statement is more pythonic
- **verify-git-email**: more concise error
- end all files with newline
