import re

with open("fixed.html", "r") as f:
    lines = f.read().split('\n')

for i, line in enumerate(lines):
    if line.startswith("body > section.page:nth-of-type(") and line.endswith(","):
        # If it doesn't have a space before the comma, it's just the page selector
        if " " not in line.split("nth-of-type(")[1]:
            print(f"Line {i+1}: {line}")

