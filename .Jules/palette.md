## 2024-05-24 - French ARIA labels for global components
**Learning:** Icon-only utility buttons (like `#themeBtn`) in this app are heavily duplicated across static HTML files without a shared templating engine. Missing ARIA labels in these components cause widespread accessibility issues for screen readers.
**Action:** When updating or creating global UI components like theme toggles or modals, always ensure appropriate localized French ARIA labels (e.g., `aria-label="Changer de thème"`) are included to maintain accessibility standards across all duplicated files.
