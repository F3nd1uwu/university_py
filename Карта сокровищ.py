n = int(input())
tresures = [tuple(map(int, input().split())) for _ in range (n)]
tresure_group = {}

for x in tresures:
    for x_i in x:
        print(x_i)
    

print(tresure_group)
