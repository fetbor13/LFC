## 2026-10-23 - French ARIA Labels for Icon-Only Buttons
**Learning:** Icon-only buttons (such as theme toggles and modal close buttons) frequently lack accessible names in this app's components, making them difficult to use with screen readers, particularly in a French localization context.
**Action:** Always verify and add explicit French `aria-label` attributes (e.g., `aria-label="Changer de thème"`, `aria-label="Fermer"`) to icon-only buttons across all UIs to ensure full accessibility.
