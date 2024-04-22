# Задание 1
# 
# n = int(input())
# for _ in range(n):
#     t = ''
#     s = input().split('%')
#     t = s[1][int(s[0])::-3]
#     t = t[:int(s[2])]
#     t = t[::-1]
#     print(t)

# Задание 2

# d = {}
# s = input()
# while s != '':
#     for x in s.split():
#         try:
#             d[len(x)].append(x)
#         except Exception:
#             d[len(x)] = [x]
#     s = input()
# for x in d:
#     t = ''
#     for y in reversed(sorted(x.upper() for x in d[x])):
#         if t != '':
#             if y.upper() not in t:
#                 t = f'{t}; {y.upper()}'
#         else:
#             t = f'{x}: {y.upper()}'
#     print(t)
# 
# Задание 3
# 
# [x for x in ints if int(str(x)[-1]) > 3] + [x for x in ints if int(str(x)[-1]) <= 3]
# 
# Задание 4
#  
# from itertools import product
# n = int(input())
# letters = []
# for _ in range(n):
#     line = input().strip().split('-')
#     letters.append(line)
# words = set()
# for combination in product(*letters):
#     word = ''.join(combination)
#     words.add(''.join(sorted(word)))
# for word in sorted(words):
#     print(word)
