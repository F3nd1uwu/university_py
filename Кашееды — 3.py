n = int(input())
m = int(input())
deti = []
for i in range(n + m):
    deti.append(input())
counts = {}
for elem in deti:
    if elem in counts:
        counts[elem] += 1
    else:
        counts[elem] = 1
k = 0
flag = False
res = []
for elem in counts:
    if counts[elem] == 1:
        res.append(elem)
        flag = True
if flag is False:
    print('Таких нет')
else:
    res.sort()
    for elem in res:
        print(elem)
