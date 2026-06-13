## 2026-06-13 - [Aria Labels on Custom Modals]
**Learning:** The project relies on custom HTML modals (.modal-overlay with inner .modal) across many static files. Because they lack native dialog elements, they require explicit ARIA attributes (role="dialog", aria-modal="true", aria-labelledby) to be correctly announced by screen readers as modal dialogs.
**Action:** When creating or modifying custom modals in this static HTML architecture, always ensure the overlay container has role="dialog", aria-modal="true", and an aria-labelledby attribute pointing to the modal's heading ID.
