# Bolt's Journal - Critical Learnings Only

## 2026-07-15 - Reduce redundant file I/O in test suites
**Learning:** In Python `unittest`, using `setUp()` to read static data files causes a read operation before every single test method. For large test suites or slow filesystems, this adds significant overhead. Refactoring to `@classmethod setUpClass(cls)` allows reading the file once per class and sharing the content across all test methods.
**Action:** Always prefer `setUpClass` for reading static, read-only test data to minimize system calls and improve test execution speed.

## 2026-07-16 - Share global file cache across independent test cases
**Learning:** Even when `setUpClass` is used, multiple independent TestCase classes (such as `TestReadmeUX` and `TestCodeOfConductUX`) may read the exact same static files. Furthermore, structural validation suites that dynamically invoke `.setUpClass()` on target classes will trigger multiple duplicate reads of those files. A centralized `_read_cached` helper ensures each static file is loaded from disk exactly once, reducing overall `openat` system calls to the absolute theoretical minimum.
**Action:** For test suites checking static files, use a central, shared in-memory dictionary cache to guarantee single-pass file reading.
