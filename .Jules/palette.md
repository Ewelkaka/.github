## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-05-27 - Enhance critical security instructions with alert blocks and mailto links
**Learning:** Security reporting instructions are high-priority but can be overlooked in plain Markdown. Using a `> [!WARNING]` alert block improves visual hierarchy and urgency. Furthermore, providing a direct `mailto:` link for security email addresses reduces friction for reporters, making the process more accessible and intuitive.
**Action:** In `SECURITY.md` or similar sensitive files, wrap critical reporting instructions in a prominent alert block and ensure email addresses are interactive via `mailto:` links.

## 2026-05-29 - GitHub-native alert blocks for surfacing high-value resources
**Learning:** External links and community call-to-actions can often be lost in plain bulleted lists or standard paragraphs. Using GitHub-native alert blocks (e.g., `> [!TIP]` or `> [!NOTE]`) creates a distinct visual region that draws the user's eye to high-value resources, improving the scannability and "helpfulness" of the documentation without overwhelming the main content.
**Action:** Identify groups of external resources or critical community entry points in documentation and consider wrapping them in a semantic alert block to enhance their visibility and perceived utility.
