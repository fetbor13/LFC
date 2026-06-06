## 2024-05-19 - Added ARIA labels to Theme and Close buttons
**Learning:** Common UI components like theme toggles (`#themeBtn`) and modal close buttons (`✕`) were missing proper accessible names, making them difficult for screen reader users to identify since they only contain icons/symbols.
**Action:** Always verify that icon-only buttons include an `aria-label` attribute (e.g., `aria-label="Changer de thème"` or `aria-label="Fermer"`) in French to ensure localization and screen reader compatibility.
