n = int(input())
res = set()
for i in range(n):
    strok = input().split()
    for x in strok:
        res.add(x)
print(*res, sep='\n')