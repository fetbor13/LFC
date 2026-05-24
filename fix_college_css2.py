import re
import glob

def fix_css(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # We replaced `class="flashcard"` with `class="flash-card"`, but JS still references `.flashcard`. Let's fix JS.
    content = content.replace(".querySelector('.flashcard')", ".querySelector('.flash-card')")

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

for f in glob.glob("*eme_chapitre*.html") + glob.glob("5e_chapitre*.html"):
    fix_css(f)
