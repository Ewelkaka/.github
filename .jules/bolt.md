## 2025-05-15 - Optimize test suite file I/O
**Learning:** Redundant file I/O in unit tests can be significantly reduced by using `@classmethod setUpClass` to load static resources once per class instead of once per test method.
**Action:** Always check if files being read in `setUp` are static and can be moved to `setUpClass`.
