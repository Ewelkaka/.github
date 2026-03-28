## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-03-28 - Documentation UX and Accessibility Standards
**Learning:** For documentation-heavy repositories, accessibility is improved by adhering to specific style guides (like GitHub's), which recommend descriptive alt text with proper punctuation and prefixes like "Illustration of...". Furthermore, semantic alert blocks (e.g., > [!NOTE], > [!TIP]) significantly enhance UX by providing visual cues and structural clarity for critical information.
**Action:** Use "Illustration of..." prefixes and trailing punctuation for alt text. Implement semantic Markdown alerts for call-to-actions and disclaimers to ensure they are accessible and visually distinct.
