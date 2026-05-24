import re
import glob
import os

# 1. Read Term_chapitre1.html CSS
with open("Term_chapitre1.html", "r", encoding="utf-8") as f:
    term_html = f.read()

styles = re.findall(r'(<style.*?>.*?</style>)', term_html, flags=re.DOTALL)
lycee_css = styles[0]

# 2. Modify to "azur intense lumineux"
# Replace blue variables with bright azure
azur_css = re.sub(r'--blue:\s*#[0-9a-fA-F]+;', '--blue: #007fff;', lycee_css)
azur_css = re.sub(r'--blue2:\s*#[0-9a-fA-F]+;', '--blue2: #005ce6;', azur_css)
azur_css = re.sub(r'--blue3:\s*#[0-9a-fA-F]+;', '--blue3: #e6f2ff;', azur_css)
azur_css = re.sub(r'--blue3:\s*rgba\([^)]+\);', '--blue3: rgba(0, 127, 255, 0.12);', azur_css) # for dark mode

# Replace the first dark mode blue (if present)
azur_css = re.sub(r'(--blue:\s*)#[0-9a-fA-F]+(.*?\[data-theme="dark"\])', r'\1#3399ff\2', azur_css, count=1, flags=re.DOTALL)

with open("azur_theme.css", "w") as f:
    f.write(azur_css)

print("Extracted and saved base azur CSS")
