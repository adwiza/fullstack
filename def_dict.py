from collections import defaultdict
def default():
    return 0

data = [2, 4, 7, 7, 8, 9, 2, 10]
d = defaultdict(default)

for el in data:
    d[el] += 1
    print("Элементы в данных которые встречаются больше одного раза:")

for k in d:
    if d[k] >= 2:
        print(f' "{k}" (встречается "{d[k]}" раз)')
