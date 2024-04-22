def divisor(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return(sorted(res))


s = {}
res = {}
n = map(int, input().split('; '))
for digit in n:
    if divisor(digit):
        s[digit] = divisor(digit)
    else:
        s[digit] = None



# for k, v in s.items():
#     print(f"{k} - {v}")
