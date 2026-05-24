import re

with open("3eme_chapitre1.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's see how many style tags are in 3eme_chapitre1.html now
styles = re.findall(r'<style.*?>.*?</style>', text, flags=re.DOTALL)
print("Number of styles:", len(styles))
