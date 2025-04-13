N, M = map(lambda x: int(x), input().split())
X_array = sorted(map(lambda x, y: {
    'pos': x,
    'val': int(y),
    'room': 0
}, range(1, N + 1), input().split()), key=lambda z: -z['val'])
Y_array = sorted(map(lambda x, y: {
    'pos': x,
    'val': int(y)
}, range(1, M + 1), input().split()), key=lambda z: -z['val'])
P = 0
cur_index = 0
for i in X_array:
    if i['val'] + 1 <= Y_array[cur_index]['val']:
        i['room'] = Y_array[cur_index]['pos']
        P += 1
        cur_index += 1
    else:
        continue
print(P)
rooms = map(lambda y: y['room'], sorted(X_array, key=lambda x: x['pos']))
print(*rooms, sep=' ')
