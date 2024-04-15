# В каждой строке входного файла "input.txt" записано от 0 до 100 чисел
# 11. Для каждой строки найти все различные числа в ней.

res_set = set()
res = []

with open(r'input.txt') as f:
    f = f.readlines()
    for x in f:
        for digit in x.split():
            res_set.add(digit)
        if res_set:
            res.append(res_set)
        else:
            res.append('None')
        res_set = set()

print(res)