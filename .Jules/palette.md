## 2026-07-06 - Icon-only buttons Accessibility
**Learning:** The application's UI components, particularly modals and quick actions, frequently use icon-only buttons (like 🌙 or ✕) without accessible names. This creates barriers for screen reader users relying on localized French content.
**Action:** When adding or updating icon-only interactive elements in this codebase, ensure they receive localized `aria-label` attributes (e.g., `aria-label="Fermer"`, `aria-label="Changer de thème"`).
