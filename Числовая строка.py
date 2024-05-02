def split_numbers(n):
    res = []
    for x in n.split():
        res.append(int(x))
    return tuple(res)

print(split_numbers("1 -2 3 -4 5"))
