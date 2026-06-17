## 2026-06-17 - Added aria-label to theme button
**Learning:** Found that many files missed accessibility labels on buttons with only emojis, and modifying a static HTML codebase requires careful string replacement (using simple string replacement instead of regex strings with backslashes is safer).
**Action:** Always add aria-labels to buttons that contain only icons to support screen readers, and test string replacements to avoid inserting escaped slashes.
