def month(n, lang):
    d1 = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    d2 = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
    n = n - 1
    if lang == 'ru':
        return d1[n]
    elif lang == 'en':
        return d2[n]

print(month(1, "en"))