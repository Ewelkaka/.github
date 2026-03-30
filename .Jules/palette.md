## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-03-30 - Semantic Markdown alerts improve scannability and visual hierarchy
**Learning:** For content-heavy documentation, GitHub-native semantic alert blocks (e.g., `> [!NOTE]`, `> [!IMPORTANT]`) provide a standardized way to highlight critical information or helpful tips. They significantly improve scannability and ensure that important callouts are visually distinct and accessible, rather than being buried in standard lists or paragraphs.
**Action:** Use semantic alert blocks to emphasize key takeaways, warnings, or tips in Markdown documentation to enhance the overall reading experience and information architecture.
