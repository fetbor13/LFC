with open('Term_chapitre7.html', 'r', encoding='utf-8') as f:
    text = f.read()

if r'\(\frac{T^2}{a^3}\)' in text:
    print("Fraction update success!")
else:
    print("Fraction update failed")

if 'id="panel-cours"' in text and 'id="panel-quiz"' in text:
    print("Panels preserved successfully.")
else:
    print("Panels missing!")
