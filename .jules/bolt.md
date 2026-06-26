## 2026-04-10 - Optimize test file I/O and regex compilation
**Learning:** Redundant file I/O in test suites (reading the same static file in `setUp` for every test method) is a common but easily fixed bottleneck. Using `@classmethod setUpClass` can significantly reduce `openat` calls and syscall overhead.
**Action:** Always check if test suites are reading static data in `setUp` and refactor to `setUpClass` where safe. Pre-compile regular expressions used in tests at the module level to avoid redundant compilation.
