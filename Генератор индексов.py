def index(text):
    res = {}
    temp = set()
    for x in text:
        if x.isalpha():
            temp.add(x)
    temp = sorted(temp)
    for x in temp:
        res[x] = text.find(x)
    for char, index in res.items():
        yield char, index

text = "The quick brown fox jumps over a lazy dog."
for letter, i in index(text):
    print(letter, i, sep="-", end=", ")