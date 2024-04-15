n = int(input())
treasures = [tuple(map(int, input().split())) for _ in range (n)]
treasure_group = {}

for x, y in zip(*treasures):
    print(x, y)
    

print(treasures)
