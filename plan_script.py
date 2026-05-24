import re
import glob

def review_colors(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # Is the background completely azur?
    match = re.search(r'--blue:\s*([^;]+);', content)
    if match:
        print(f"{f}: {match.group(1)}")

review_colors("3eme_chapitre1.html")
review_colors("Term_chapitre1.html")
