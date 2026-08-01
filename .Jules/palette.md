## 2024-05-15 - Modals and Inputs Accessibility
**Learning:** Custom modal architectures (`.modal-overlay` > `.modal`) in this project lack native dialog semantics (like `role="dialog"` and `aria-modal="true"`). Additionally, form inputs heavily rely on placeholder text without visible labels, making them inaccessible to screen readers unless `aria-label` is explicitly provided.
**Action:** When working with modals or inputs in this project, always add proper dialog ARIA roles and ensure all inputs have `aria-label` if no visible `<label>` is present.
