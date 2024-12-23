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


def safe(report):
    levels = [int(x) for x in report.split()]
    safe_sign = sign(levels[1] - levels[0])

    for a, b in zip(levels, levels[1:]):
        step = b - a
        if sign(step) != safe_sign or abs(step) > MAX_STEP:
            return False

    return True


num_safe = 0
for report in open('input'):
    if safe(report):
        num_safe += 1
print(num_safe)
