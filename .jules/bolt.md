# Bolt's Journal - Critical Learnings Only

## 2026-07-17 - Preloading suites and O(1) space tracking in meta-test runners
**Learning:** When building programmatic meta-test runners or regression guards in Python unittest, loading test suites repeatedly inside test methods creates redundant objects and re-evaluation overhead. Furthermore, using subset checks on dynamically-created sets can introduce extra memory allocations. Preloading suites inside `setUpClass` and validating already executed tests using a generator expression with `all()` on the global cache maintains O(1) space complexity.
**Action:** Always preload suites in class-level `setUpClass` and verify completed test execution status using lightweight O(1) generator expressions over sets.

## 2026-07-16 - Eliminate redundant test suite executions in meta-testing
**Learning:** Meta-tests designed as regression guards to programmatically run other test suites can result in severe performance overhead by executing those suites twice (once during standard discovery, and once inside the programmatic runner). We can eliminate this redundancy by using a global tracking dictionary/set of successfully executed test IDs in a tracking base class.
**Action:** When executing test suites programmatically as regression guards, check if the suite's test cases have already run and passed in the outer runner. If so, return a mock successful result to bypass execution.

## 2026-07-15 - Reduce redundant file I/O in test suites
**Learning:** In Python `unittest`, using `setUp()` to read static data files causes a read operation before every single test method. For large test suites or slow filesystems, this adds significant overhead. Refactoring to `@classmethod setUpClass(cls)` allows reading the file once per class and sharing the content across all test methods.
**Action:** Always prefer `setUpClass` for reading static, read-only test data to minimize system calls and improve test execution speed.
