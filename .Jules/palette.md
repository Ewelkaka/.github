## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-05-15 - Use warning alert blocks for critical security reporting instructions
**Learning:** Security reporting instructions are critical and must not be ignored. Using a standard bold font is less effective than a GitHub-native `> [!WARNING]` alert block, which provides a distinct visual treatment and semantic meaning, ensuring users are properly cautioned against public disclosure of vulnerabilities.
**Action:** When documenting security policies or critical safety instructions, use the `> [!WARNING]` or `> [!CAUTION]` alert blocks to ensure high visibility and appropriate semantic weight.
