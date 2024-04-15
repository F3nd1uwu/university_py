# На одной строке записаны целые числа, разделённые пробельными символами.
# 16. Для каждой пары подряд идущих чисел найти такие цифры, которые не встречаются ни в одном из них.

m = list(map(int, input().split()))
res = []
res_set = set()
temp = set()

for x, y in zip(m[:-1], m[1:]):
    for digit in str(x):
        temp.add(int(digit))
    for digit in str(y):
        temp.add(int(digit))
    for digit in '1234567890':
        if int(digit) not in temp:
            res_set.add(int(digit))
    if res_set:
        res.append(res_set)
    else:
        res.append('None')
    res_set = set()
    temp = set()

print(res)