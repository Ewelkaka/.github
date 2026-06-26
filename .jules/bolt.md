## 2024-05-24 - Optimizing Python test suites with `setUpClass` and pre-compiled regex
**Learning:** For test suites that perform repetitive file I/O or regular expression operations, using `@classmethod setUpClass` to load data once per class and pre-compiling regex at the module level significantly reduces execution overhead.
**Action:** Identify redundant disk access in `setUp` methods and replace them with `setUpClass`. Pre-compile complex regular expressions used across multiple test cases.
