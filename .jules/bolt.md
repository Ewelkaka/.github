## 2025-05-14 - Optimized Test Suite File I/O
**Learning:** Python's unittest `setUp` method runs before every test case, leading to redundant file I/O when reading static documentation files. Refactoring to `@classmethod setUpClass` reduces redundant `openat` calls.
**Action:** Always prefer `setUpClass` for immutable test fixtures to minimize system call overhead as the test suite grows.
