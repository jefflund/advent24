MAX_STEP = 3


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def safe_step(step, safe_sign):
    return sign(step) == safe_sign and abs(step) <= MAX_STEP


def safe(levels):
    safe_sign = sign(levels[1] - levels[0])

    for a, b in zip(levels, levels[1:]):
        if not safe_step(b - a, safe_sign):
            return False

    return True


def safe_with_skip(levels):
    # Yes, this O(n^2) algorithm is terribly inefficient, and the O(n)
    # algorithm would be easy, but n is small here, so I don't care...
    for i in range(len(levels)):
        skip_levels = levels[:i] + levels[i+1:]
        if safe(skip_levels):
            return True
    return False


num_safe = 0
for report in open('input'):
    levels = [int(x) for x in report.split()]
    if safe(levels) or safe_with_skip(levels):
        num_safe += 1
print(num_safe)
