d = {}
n = int(input())
for _ in range(n):
    temp = input()
    if temp in d:
        d[temp] += 1
    else:
        d[temp] = 1
k = 0
for x in sorted(d):
    if d[x] != 1:
        print(f'{x} - {d[x]}')
        k += 1
if k == 0:
    print('Однофамильцев нет')
