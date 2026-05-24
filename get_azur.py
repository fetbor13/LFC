import re

with open("3eme_chapitre1.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect the first style block to see if it actually replaced it correctly
styles = re.findall(r'<style.*?>.*?</style>', text, flags=re.DOTALL)
print(styles[0][:1000])
