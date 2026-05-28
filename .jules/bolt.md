# Bolt Journal

## 2024-05-24 - Redundant File I/O in Document-Verification Tests
**Learning:** In a repository focused on documentation, tests often perform redundant read operations on the same static files (e.g., README.md) because they use `setUp()` instead of `setUpClass()`.
**Action:** Use `@classmethod setUpClass` to read static file content once per test class to reduce system calls and disk I/O.
