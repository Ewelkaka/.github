## 2025-05-14 - Redundant File I/O in Test Suite
**Learning:** In Python's `unittest` framework, using `setUp` to read static files causes a disk read for every single test method. For large test suites or files, this adds up to significant redundant I/O.
**Action:** Use `@classmethod setUpClass` to read static files once per test class and store them as class attributes.
