d = {}
user_input = input().split()
while user_input:
    for x in user_input:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    user_input = input().split()
for x, y in d.items():
    print(x, y)
