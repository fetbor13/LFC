## 2026-05-19 - Enhance Modals and Forms with ARIA
**Learning:** Found custom modal dialogs missing essential a11y attributes like `role="dialog"` and `aria-modal="true"`. Text inputs relying solely on placeholders were fixed by adding `aria-label`.
**Action:** When implementing custom modals, always include `role="dialog"`, `aria-modal="true"`, and a title linkage via `aria-labelledby`. Always ensure inputs have an accessible name, especially when visual labels are missing.
