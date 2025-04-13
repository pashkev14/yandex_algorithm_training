t = int(input())
splits = [[] for _ in range(t)]
for i in range(t):
    n = int(input())
    arr = map(lambda x: int(x), input().split())
    local_min = n
    length = 0
    for j in arr:
        length += 1
        if j < local_min:
            local_min = j
        if length > local_min:
            splits[i].append(length - 1)
            length = 1
            local_min = j
        elif length == local_min:
            splits[i].append(length)
            length = 0
            local_min = n
    if sum(splits[i]) != n:
        splits[i].append(length)
for i in splits:
    print(len(i))
    print(*i, sep=' ')
