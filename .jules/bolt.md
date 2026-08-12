# Bolt's Journal - Critical Learnings Only

## 2024-05-24 - Optimizing Test Suite I/O with setUpClass
**Learning:** In Python `unittest`, using `setUp()` for file I/O causes the file to be re-opened and read for every single test method in a class. For documentation-heavy test suites, this leads to O(N_tests) system calls.
**Action:** Use `@classmethod setUpClass(cls)` to read static data once per test class, reducing system calls to O(1) per class and significantly improving efficiency for large test suites.
## 2026-07-17 - Optimize Test Suite Loading and Meta-Test Suite Checks
**Learning:** Instantiating `unittest.TestLoader()` and loading suites dynamically using `loadTestsFromModule()` repeatedly adds memory allocation and search overhead. Moving suite loading to class-level `setUpClass` and replacing $O(N)$ test ID set checks with an $O(1)$ space, short-circuiting `all()` generator significantly decreases memory usage and execution overhead.
**Action:** Always load dynamic sub-suites once at the class-level instead of repeatedly in test methods, and prefer short-circuiting generators with `all()` or `any()` over materializing large lists/sets when comparing elements.
## 2026-07-17 - Optimize meta-test execution with class-level caching and O(1) generators
**Learning:** Programmatic test suite execution under `unittest` can be optimized by caching loaded TestSuites at the class level inside `setUpClass()` rather than dynamically reloading them for every assertion method. Additionally, checking if all tests have already passed can be done in O(1) space with a generator expression passed directly to `all()`, completely avoiding intermediate set or list allocations.
**Action:** Preload programmatic test suites at the class level via `setUpClass()`, and use generator-based traversal with `all()` instead of set comprehension to minimize memory churn.
## 2026-07-17 - Preloading suites and O(1) space tracking in meta-test runners
**Learning:** When building programmatic meta-test runners or regression guards in Python unittest, loading test suites repeatedly inside test methods creates redundant objects and re-evaluation overhead. Furthermore, using subset checks on dynamically-created sets can introduce extra memory allocations. Preloading suites inside `setUpClass` and validating already executed tests using a generator expression with `all()` on the global cache maintains O(1) space complexity.
**Action:** Always preload suites in class-level `setUpClass` and verify completed test execution status using lightweight O(1) generator expressions over sets.

## 2026-07-16 - Eliminate redundant test suite executions in meta-testing
**Learning:** Meta-tests designed as regression guards to programmatically run other test suites can result in severe performance overhead by executing those suites twice (once during standard discovery, and once inside the programmatic runner). We can eliminate this redundancy by using a global tracking dictionary/set of successfully executed test IDs in a tracking base class.
**Action:** When executing test suites programmatically as regression guards, check if the suite's test cases have already run and passed in the outer runner. If so, return a mock successful result to bypass execution.

## 2026-07-15 - Reduce redundant file I/O in test suites
**Learning:** In Python `unittest`, using `setUp()` to read static data files causes a read operation before every single test method. For large test suites or slow filesystems, this adds significant overhead. Refactoring to `@classmethod setUpClass(cls)` allows reading the file once per class and sharing the content across all test methods.
**Action:** Always prefer `setUpClass` for reading static, read-only test data to minimize system calls and improve test execution speed.
