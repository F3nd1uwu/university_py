n = int(input())
mas = []
res = []
for _ in range(n):
    mas = []
    x = input()
    while x != 'end':
        mas.append(int(x))
        x = input()
    res.append(sum(x for x in mas) / len(mas))
print(f'{min(res):.2f}')
