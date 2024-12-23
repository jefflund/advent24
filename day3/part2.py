import re

matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', open('input').read())

total = 0
for match in matches:
    x, y = [int(x) for x in match.groups()]
    total += x * y
print(total)
