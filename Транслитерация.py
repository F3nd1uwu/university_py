d = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 
     'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 
     'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'}

s = input()
s = s.replace('ъ', '')
s = s.replace('Ъ', '')
s = s.replace('ь', '')
s = s.replace('Ь', '')

res = ''
for x in s:
    if x == x.upper():
        flag = True
    else:
        flag = False
        pass
    if x.upper() not in d:
        res = f'{res}{x}'
    elif flag:
        x = x.upper()
        x = d[x]
        res = f'{res}{x}'
    else:
        x = x.upper()
        x = d[x]
        res = f'{res}{x.lower()}'
print(res)
