def divisor(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)


s = {}
res = {}
n = sorted(map(int, input().split('; ')))
for digit in n:
    if divisor(digit):
        s[digit] = divisor(digit)
    else:
        s[digit] = [digit]

temp_d = {}
temp = {}
temp_l = []

for i in s:
    temp = s[i]
    temp_d = {k: v for k, v in s.items() if k != i}
    for y in temp_d:
        no_common_elements = True
        for item in temp:
            if item in temp_d[y]:
                no_common_elements = False
                break
        if no_common_elements:
            temp_l.append(y)
        if temp_l:
            res[i] = str(temp_l)[1:-1]
    temp_l = []

for k, v in res.items():
    print(f"{k} - {v}")
