import re

filepath = '/Users/milkyway/Desktop/Dev/deck-maker/decks/kfcpa_knpa_bonanza_cooperation.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Cover Date
content = content.replace(
    '.cover-date{margin-top:5mm;font-size:13pt;font-weight:900;color:#3f4a5f;letter-spacing:.04em}',
    '.cover-date{margin-top:14mm;font-size:17pt;font-weight:900;color:#3f4a5f;letter-spacing:.04em}'
)

# 2. Add specific logo classes to the style tag
style_addition = '''
.header .logos img.l-kfcpa { height: 5.5mm !important; margin-top: 1mm; width: auto !important; }
.header .logos img.l-knpa { height: 7.5mm !important; width: auto !important; }
.header .logos img.l-bonanza { height: 5.5mm !important; margin-top: 1mm; width: auto !important; }
'''
if '.l-kfcpa' not in content:
    content = content.replace('</style>', style_addition + '</style>')

# 3. Standardize all headers
# Find all <div class="logos">...</div> and replace them with the standard 3 logos
standard_logos = '<div class="logos"><img src="../materials/KFCPA-logo.svg" class="l-kfcpa"/><img src="../materials/knpa/knpa-logo.webp" class="l-knpa"/><img src="../materials/bonanza_Factory_logo.jpg" class="l-bonanza"/></div>'

# We'll use regex to replace `<div class="logos">.*?</div>` with `standard_logos`
content = re.sub(r'<div class="logos">.*?</div>', standard_logos, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('✅ Updated cover date and standardized all header logos.')
