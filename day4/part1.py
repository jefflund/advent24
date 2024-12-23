grid = [line.strip() for line in open('input')]
rows, cols = len(grid), len(grid[0])
print('\n'.join(grid))


def get(x, y):
    if 0 <= x < cols and 0 <= y < rows:
        return grid[y][x]
    return '#'


def is_xmas(x, y, dx, dy):
    return all(get(x + i * dx, y + i * dy) == c for i, c in enumerate('XMAS'))


dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

total = 0
for x in range(cols):
    for y in range(rows):
        for dx, dy in dirs:
            if is_xmas(x, y, dx, dy):
                total += 1
print(total)
