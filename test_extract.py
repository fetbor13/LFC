import re
with open('Term_chapitre1_ultimate.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
for s in scripts:
    if "flipCard" in s:
        print("Found flipCard logic!")
        break
else:
    print("Not found in any script tags.")
