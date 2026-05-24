import re

with open("Term_chapitre1.html", "r", encoding="utf-8") as f:
    term_html = f.read()

# Extract styles from Term_chapitre1.html
styles = re.findall(r'<style.*?>.*?</style>', term_html, flags=re.DOTALL)

# Let's see what styles are there
for i, s in enumerate(styles):
    print(f"Style {i}: length {len(s)}")
