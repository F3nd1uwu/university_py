d = {}
n = int(input())
for _ in range(n):
    temp = input()
    if temp in d:
        d[temp] += 1
    else:
        d[temp] = 1
k = 0
for x in d:
    if d[x] != 1:
        k += d[x]
print(k)
