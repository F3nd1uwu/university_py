n = int(input())
d = {}
res = {}

for _ in range(n):
    s = input().split(':')
    d[s[0]] = s[1][1:].split(', ')

for x in d:
    for y in set(d[x]):
        if y not in res:
            res[y] = 1
        else:
            res[y] += 1

print(*sorted([x for x in res if res[x] == 1]), sep='\n')
