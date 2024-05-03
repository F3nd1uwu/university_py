n = int(input())
kasha = []
for _ in range(n):
    kasha.append(input())
n1 = int(input())
for i in range(0, n1):
    print(kasha[i % n])