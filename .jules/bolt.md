# Bolt Journal

## 2026-05-20 - Redundant file I/O in document-heavy test suite
**Learning:** In a documentation-focused repository where tests primarily verify static file content, using the instance-level `setUp` method leads to excessive `openat` calls (e.g., 19 vs 3) as files are re-read for every test method.
**Action:** Use `@classmethod setUpClass` to read static files once per test class and store them as class attributes.
