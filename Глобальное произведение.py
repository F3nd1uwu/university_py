mas = []
def add_number(number):
    mas.append(number)

def get_prod():
    res = 0
    for x in mas:
        if res == 0:
            res = x
        else:
            res = res * x
    return (f'{' * '.join(str(x) for x in mas)} = {res}')


add_number(7)
add_number(2)
print(get_prod())
add_number(5)
print(get_prod())