d = {}
while x := input().split():
    if x[0] not in d:
        d[x[0]] = {x[1]}
    else:
        d[x[0]].add(x[1])
    if x[1] not in d:
        d[x[1]] = {x[0]}
    else:
        d[x[1]].add(x[0])
d_2 = dict.fromkeys(d, set())
for friend in d:
    for n in d[friend]:
        d_2[friend] = d_2[friend].union(d[n])
    d_2[friend].discard(friend)
    for z in d[friend]:
        d_2[friend].discard(z)
data = []
for friend in d_2:
    data.append(f'{friend}: {", ".join(sorted(d_2[friend]))}')
data.sort()
for string in data:
    print(string)
