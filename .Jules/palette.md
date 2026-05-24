## 2024-05-24 - Modal & Icon Button Accessibility
**Learning:** This application extensively uses custom HTML/CSS modals (`.modal-overlay` > `.modal`) and icon-only buttons (`themeBtn`, `.close` buttons) without native dialog elements. These frequently lack necessary ARIA roles, making them opaque to screen readers.
**Action:** When working on this specific project's custom UI, always manually apply `role="dialog"`, `aria-modal="true"`, and connect them to a title via `aria-labelledby`. Ensure all icon-only action buttons (like theme toggles or close icons) have descriptive `aria-label`s.
