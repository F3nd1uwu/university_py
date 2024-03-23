n = int(input())
d = {}
for _ in range(n):
    temp = input().split()
    d[temp[0]] = temp[1:]
search = input()
d = d.items()
k = 0
for x, y in sorted(d):
    if search in y:
        print(x)
        k += 1
if k == 0:
    print('Таких нет')
