## 2024-05-24 - Accessibility standards for app modals
**Learning:** The custom modals implemented in the project lacked appropriate ARIA attributes for accessibility, such as `role="dialog"`, `aria-modal="true"`, and `aria-labelledby`. Also, inputs relying only on placeholders and icon-only buttons lacked `aria-label`.
**Action:** When creating or modifying modals and forms, ensure proper ARIA attributes are applied for screen reader compatibility.
