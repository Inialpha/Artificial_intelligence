target = (0, 3)
min_c = float('inf')
choices = [(3, 1), (2, 2), (3, 3)]
for c in choices:
    pos = [t1 - t2 for t1, t2 in zip(target, c)]
    pos = abs(pos[0]) + abs(pos[1])
    min_c = min(pos, min_c)
print(min_c)

#print(((0, 3) - (3, 2)) > ((0, 3) - (3, 1)))
