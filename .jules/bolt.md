## 2024-05-24 - Optimizing test suite file I/O with setUpClass
**Learning:** Using `setUpClass` instead of `setUp` in Python `unittest` significantly reduces redundant file system operations for read-only test data.
**Action:** Always favor `@classmethod setUpClass` for loading static resources or reading files once per test class to improve performance.
