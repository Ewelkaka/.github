# Bolt's Journal - Critical Learnings Only

## 2026-07-17 - Optimize Test Suite Loading and Meta-Test Suite Checks
**Learning:** Instantiating `unittest.TestLoader()` and loading suites dynamically using `loadTestsFromModule()` repeatedly adds memory allocation and search overhead. Moving suite loading to class-level `setUpClass` and replacing $O(N)$ test ID set checks with an $O(1)$ space, short-circuiting `all()` generator significantly decreases memory usage and execution overhead.
**Action:** Always load dynamic sub-suites once at the class-level instead of repeatedly in test methods, and prefer short-circuiting generators with `all()` or `any()` over materializing large lists/sets when comparing elements.

## 2026-07-16 - Eliminate redundant test suite executions in meta-testing
**Learning:** Meta-tests designed as regression guards to programmatically run other test suites can result in severe performance overhead by executing those suites twice (once during standard discovery, and once inside the programmatic runner). We can eliminate this redundancy by using a global tracking dictionary/set of successfully executed test IDs in a tracking base class.
**Action:** When executing test suites programmatically as regression guards, check if the suite's test cases have already run and passed in the outer runner. If so, return a mock successful result to bypass execution.

## 2026-07-15 - Reduce redundant file I/O in test suites
**Learning:** In Python `unittest`, using `setUp()` to read static data files causes a read operation before every single test method. For large test suites or slow filesystems, this adds significant overhead. Refactoring to `@classmethod setUpClass(cls)` allows reading the file once per class and sharing the content across all test methods.
**Action:** Always prefer `setUpClass` for reading static, read-only test data to minimize system calls and improve test execution speed.
