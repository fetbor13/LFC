## 2024-11-20 - Accessible Modals and Inputs
**Learning:** Custom `div`-based modals and placeholder-only inputs in this application frequently lack native accessibility semantics, making them opaque to screen readers.
**Action:** When implementing or modifying custom modals, ensure `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` are used. For form inputs lacking visible `<label>` elements, always add an `aria-label` attribute.
