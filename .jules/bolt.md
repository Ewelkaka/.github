# Bolt Journal

## 2026-05-16 - Redundant File I/O in Documentation Tests
**Learning:** In a documentation-heavy repository where tests verify static file content, using `setUp` results in redundant `openat` calls for every test method. Using `@classmethod setUpClass` to read files once per class significantly reduces system call overhead.
**Action:** Always prefer `setUpClass` for reading static assets in test suites to minimize disk I/O.

## 2026-05-16 - Python Bytecode Contamination
**Learning:** Running Python tests generates `__pycache__` directories which are not currently excluded by the repository's `.gitignore`. Committing these binaries is a major quality issue.
**Action:** Manually purge `__pycache__` and `*.pyc` files after running tests and before submission until `.gitignore` is updated.
