## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2024-05-25 - Use canonical URLs for standard resources
**Learning:** Hardcoded links to documentation or style guides can become stale. Using canonical URLs ensures that users are always directed to the most up-to-date and authoritative version of a resource, preventing confusion and maintaining trust in the project's guidance.
**Action:** Review documentation for links to external GitHub resources and replace them with their canonical equivalents where available.
