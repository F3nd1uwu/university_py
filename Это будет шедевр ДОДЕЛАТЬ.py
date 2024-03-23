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

# Комментарии от Елены Евгеньевны
# Во первых, жутко нерациональное решение. Ршайте с помощью множеств.
# Во-вторых, кто сказал, что ингредиенты, преобразованные в строку, и там и там идут в одинаковом порядке?
#
# Комментарий от Алии Владимировны
# Это задачка на множества. 
# Самая большая ошибка в этом решении, что ингедиенты, преобразованные в строку, могут быть в другом порядке, чем продукты в холодильнике, преобразованные в строку.