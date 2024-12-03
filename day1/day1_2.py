def read_left_right():
    file = open("input.txt", "r").readlines()
    pairs, left, right = [], [], []
    for line in file:
        line.strip("\n")
        pair = line.split()
        pairs.append(pair)

    for pair in pairs:
        left.append(int(pair[0]))
        right.append(int(pair[1]))
    return left, right

left, right = read_left_right()

count = 1
right_dupe_count = {}
for num in right:
    _dict = {num: count}
    right_dupe_count.update(_dict)

seen = set()
for num in right:
    if num in seen:
        right_dupe_count[num] = right_dupe_count.get(num) + 1
    else:
        seen.add(num)

print(right_dupe_count)

similarity = 0
for i in range(len(left)):
    num_left = left[i]
    num_right = right[i]

    if num_left in right_dupe_count:
        dupe_count_left = right_dupe_count[num_left]
        result = dupe_count_left*num_left
        similarity += num_left*dupe_count_left

print(f"similarity_score: {similarity}")
