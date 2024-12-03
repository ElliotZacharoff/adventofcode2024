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
