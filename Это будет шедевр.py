n = int(input())
ingridients = [input() for _ in range(n)]
res = []
m = int(input())
for _ in range(m):
    name = input()
    c = int(input())
    ingridients_for_name = [input() for __ in range(c)]
    if str(ingridients_for_name).strip('[]') in str(ingridients).strip('[]'):
        res.append(name)
if res:
    print(*sorted(res), sep='\n')
else:
    print('Готовить нечего')
