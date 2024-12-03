def read_left_right():
    file = open("ex.txt", "r").readlines()
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
distance = 0
for i in range(len(right)):
    left.sort()
    right.sort()
    distance += abs(left[i] - right[i])

print(distance)