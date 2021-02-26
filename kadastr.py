from pprint import pprint

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
