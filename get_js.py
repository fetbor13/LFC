import re
with open('Term_chapitre1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all the logic block. In the original files, it's typically between <script> and </script> at the end.
match = re.search(r'</main>\s*(<script>.*?</script>)\s*</body>', text, re.DOTALL)
if match:
    print("Found script logic right before body")
    js = match.group(1)
    if "flipCard" in js:
        print("flipCard is inside this block")
else:
    print("Failed to find main script block")
