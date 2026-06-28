## 2024-05-24 - Optimized test suite file I/O
**Learning:** In the 'GitHub Skills' test suite, refactoring test classes to use '@classmethod setUpClass(cls)' for reading static Markdown data reduces redundant 'openat()' system calls from O(N_tests) to O(1) per class.
**Action:** Use '@classmethod setUpClass(cls)' to load shared, immutable test data once per class instead of using 'setUp(self)' to load it for every test method.
