grid = [line.strip() for line in open('input')]
rows, cols = len(grid), len(grid[0])
print('\n'.join(grid))


def get(x, y):
    if 0 <= x < cols and 0 <= y < rows:
        return grid[y][x]
    return '#'


def is_mas(x, y, dx, dy):
    return all(get(x + i * dx, y + i * dy) == c for i, c in enumerate('MAS', -1))


def is_x_mas(x, y):
    back = is_mas(x, y, -1, -1) or is_mas(x, y, 1, 1)
    forth = is_mas(x, y, 1, -1) or is_mas(x, y, -1, 1)
    return back and forth


total = 0
for x in range(cols):
    for y in range(rows):
        if is_x_mas(x, y):
            total += 1
print(total)
