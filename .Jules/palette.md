## 2024-05-21 - Initial Accessibility Learnings
**Learning:** This app heavily uses custom HTML/JS modals without native `<dialog>` elements and relies entirely on placeholders for input labels.
**Action:** Always ensure `role="dialog"`, `aria-modal="true"`, and `aria-label`/`aria-labelledby` are explicitly added when modifying or creating modals and inputs in this codebase.
