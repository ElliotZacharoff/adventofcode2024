file = open("input.txt", "r").readlines()

lines = []
for line in file:
    numbers = line.split()
    lines.append([int(n) for n in numbers])

safe_count = 0

for line in lines:
    is_safe = True
    increasing = None  # will determine if repor is increasing or decreasing

    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]  # differene between the numbers

        if abs(diff) < 1 or abs(diff) > 3:
            is_safe = False  # if the range is outside of scope (1-3)
            break

        if increasing is None:
            increasing = diff > 0 

        if (increasing and diff <= 0) or (not increasing and diff >= 0):
            is_safe = False  # Criteria violation
            break 

    if is_safe:
        safe_count += 1

print(f"Number of safe reports: {safe_count}")