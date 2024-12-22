left, right = [], []
for line in open('input'):
    left_entry, right_entry = line.split()
    left.append(int(left_entry))
    right.append(int(right_entry))
aligned = zip(sorted(left), sorted(right))
print(sum(abs(x - y) for x, y in aligned))
