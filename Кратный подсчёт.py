from itertools import combinations

def count_pairs(*numbers, div=10):
    k = 0
    for x, y in combinations(numbers, 2):
        if (x + y) % div == 0:
            print(x, y)
            k += 1
    return k

numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
result = count_pairs(*numbers, div=3)
print(result)