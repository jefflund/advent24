import re

matches = re.finditer(r'(don\'t\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))', open('input').read())

total = 0
enabled = True
for match in matches:
    command, arg1, arg2 = match.groups()
    match command:
        case 'do()':
            enabled = True
        case 'don\'t()':
            enabled = False
        case _:
            if enabled:
                total += int(arg1) * int(arg2)
print(total)
