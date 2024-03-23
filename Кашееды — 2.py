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
for elem in counts:
    if counts[elem] == 1:
        k += 1
if k != 0:
    print(k)
else:
    print('Таких нет')
