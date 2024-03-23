n = int(input())
spisok_blyud = []
d = set()
res = set()
for _ in range(n):
    spisok_blyud.append(input())
m = int(input())
for _ in range(m):
    c = int(input())
    for __ in range(c):
        d.add(input())
for blyudo in spisok_blyud:
    if blyudo not in d:
        res.add(blyudo)
if len(blyudo) == 0:
    print('Готовить нечего')
else:
    res = sorted(res)
    print(*res, sep='\n')
5
Овсянка
Рис
Суп
Манная каша
Рыба
2
3
Рис
Суп
Рыба
2
Рис
Рыба