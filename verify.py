import re
import glob

def review_colors(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    match = re.search(r'--blue:\s*([^;]+);', content)
    if match:
        print(f"{f}: {match.group(1)}")

for f in glob.glob("*eme_chapitre*.html"):
    review_colors(f)
