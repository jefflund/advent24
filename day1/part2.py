import collections

left, right = [], collections.defaultdict(int)
for line in open('input'):
    left_entry, right_entry = line.split()
    left.append(int(left_entry))
    right[int(right_entry)] += 1

total = 0
for entry in left:
    total += entry * right[entry]
print(total)
