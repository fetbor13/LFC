## 2024-06-18 - Added ARIA labels to icon-only buttons
**Learning:** In static HTML applications that lack a common UI components architecture, it's very easy for critical accessibility features like `aria-label`s on icon-only buttons (such as theme togglers and modal close buttons) to be missing across many duplicated instances.
**Action:** Always script cross-file replacements when introducing accessibility enhancements to duplicated static UI components to ensure screen readers don't miss any contexts.
