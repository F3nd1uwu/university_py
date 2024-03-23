res = []
s = map(int, input().split())
for x in s:
    x = bin(x)[2:]
    d = {'digits': len(x), 'units': x.count('1'), 'zeros': x.count('0')}
    res.append(d)
print(res)