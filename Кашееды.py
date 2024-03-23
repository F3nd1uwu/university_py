n = int(input())
m = int(input())
man = set()
ovs = set()
for i in range(n):
    man.add(input())
for i in range(m):
    ovs.add(input())
print(len(man & ovs) if len(man & ovs) != 0 else 'Таких нет')