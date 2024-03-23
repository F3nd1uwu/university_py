c = list(input().split(' '))
res = set()
while c != ['']:
    for i in range(len(c)):
        if c[i] == 'зайка':
            if (i != 0) and (i != len(c) - 1):
                res.add(c[i - 1])
                res.add(c[i + 1])
            if i == 0:
                res.add(c[i + 1])
            if i == len(c) - 1:
                res.add(c[i - 1])
    c = list(input().split(' '))          
print(*res, sep='\n')
