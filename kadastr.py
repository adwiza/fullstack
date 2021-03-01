from pprint import pprint

# План
# 1 Вычислить среднюю площадь участка с округлением до целого числа
# 2 Вычислить самый большой участок
# 3 Какой ID у самого большого участка в данных файлах
data = []
with open('data/m7-map-1.txt', 'r') as df:
    for row in df:
        if row[:2] == 'ID':
            id, xy, size = row.split(' :: ')
            data += id, xy, size



# print(data[:3])

for elem in data:
    id = elem
    x = elem[:3]
    y = elem[3:]

print(id, x, y)
