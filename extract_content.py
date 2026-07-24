import bs4
import copy
import re

with open('Term_chapitre7.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Fix mathjax delimiters in original html before parsing if needed, but bs4 handles it fine.
# Replace inline slashes with fractions where necessary, per user request.
# The user specifically mentioned: `\frac{}{}` and fraction exposant, so we look for things like \(T^2/a^3\)
orig = orig.replace(r'\(T^2/a^3\)', r'\(\frac{T^2}{a^3}\)')
# Let's do a more general regex if needed, but it's safer to target specific ones we find.
orig = orig.replace(r'\(v = \sqrt{G M / r}\)', r'\(v = \sqrt{\frac{G M}{r}}\)')


soup_orig = bs4.BeautifulSoup(orig, 'html.parser')

# We need the astrolabe_template.html again. Let me create it.
