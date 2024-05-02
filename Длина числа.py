def number_length(a):
    k = 0
    for x in str(a):
        if x not in '-+,.':
            k += 1
    return k

print(number_length(12345))