# Дано N строк, состоящих из латинских букв в верхнем и нижнем регистре, цифр и различных символов, в том числе пробельных.
# 16. Для каждой строки вывести знаки препинания, которые встречаются ровно один раз. 
# .,!?:;-

n = int(input())
res_set = set()
res = []

for _ in range(n):
    stroka = input()
    for znak in '.,!?:;-':
        if stroka.count(znak) == 1:
            res_set.add(znak)
    if res_set:
        res.append(res_set)
    else:
        res.append('None')
    res_set = set()

print(res)
