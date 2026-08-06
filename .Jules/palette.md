## 2026-08-13 - Enhance main README footer with localized policy and support links
**Learning:** Highlighting localized links for critical support paths and safety guidelines (such as `SECURITY.md` and `SUPPORT.md`) directly in the main repository entry point (`README.md`) footer vastly improves the user journey and navigation discoverability, especially for developers looking for help or reporting issues offline.
**Action:** Always localize and elevate key policy, license, and support links directly in the footer of the central `README.md` to establish a safe and highly discoverable navigation baseline.

## 2026-08-12 - Descriptive anchor text for accessible legal and policy links
**Learning:** Generic or un-descriptive link text like "released" or "click here" fails Web Content Accessibility Guidelines (WCAG) for link purpose. Providing descriptive link text (e.g., "released under the GitHub Terms of Service") ensures that screen reader users listing links out of context can understand the purpose and destination of each hyperlink without parsing surrounding text.
**Action:** Always audit documentation files for generic link texts and rewrite them to describe the destination or purpose of the link, improving raw scannability and screen-reader context.

## 2026-08-11 - Use prominent tip alert blocks in issue templates
**Learning:** Prominent GitHub-native alert blocks (e.g., `> [!TIP]`) inside issue templates are highly effective at guiding contributors to search existing issues/discussions first. Highlighting these instructions visually prevents duplicate issues and improves overall repository maintenance UX.
**Action:** Embed friendly search instructions in a `> [!TIP]` alert block at the top of issue templates, with proper newline spacing.

## 2026-08-10 - Elevate hidden template comments to visible alert blocks
**Learning:** Hidden developer comments in pull request templates can easily be ignored or overlooked during PR creation. Converting these into visible GitHub-native alert blocks (e.g., `> [!NOTE]`) significantly improves the visual experience and scannability of issue linking guidelines.
**Action:** Identify commented-out instructions inside templates and elevate them to prominent, visible GitHub-native alert blocks with proper newline spacing.

## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-05-27 - Enhance critical security instructions with alert blocks and mailto links
**Learning:** Security reporting instructions are high-priority but can be overlooked in plain Markdown. Using a `> [!WARNING]` alert block improves visual hierarchy and urgency. Furthermore, providing a direct `mailto:` link for security email addresses reduces friction for reporters, making the process more accessible and intuitive.
**Action:** In `SECURITY.md` or similar sensitive files, wrap critical reporting instructions in a prominent alert block and ensure email addresses are interactive via `mailto:` links.

## 2026-06-15 - Improve support documentation scannability with semantic alert blocks
**Learning:** Support documentation often contains multiple call-to-actions, such as community forums and maintenance statements. Wrapping these in semantic alert blocks (e.g., `> [!TIP]` for helpful links and `> [!NOTE]` for project status) improves scannability and ensures users can quickly find the help they need.
**Action:** Use appropriate semantic alert blocks to distinguish between different types of support resources and project information in `SUPPORT.md`.

## 2026-07-26 - Localize legal links and secure external pathways for contributors
**Learning:** Navigation inside documentation should be both safe and context-preserving. Localizing standard repository links (such as the MIT License) keeps users inside the project's ecosystem and ensures offline readiness. Similarly, ensuring external links to guides use HTTPS prevents insecure, unencrypted traffic, protecting users when they leave the repository context.
**Action:** Always localize standard project links (like LICENSE files) rather than using external redirects, and verify that all external links are upgraded to HTTPS for secure and seamless user navigation.
