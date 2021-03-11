import pandas as pd


# План
# 1 Вычислить среднюю площадь участка с округлением до целого числа
# 2 Вычислить самый большой участок
# 3 Какой ID у самого большого участка в данных файлах (если их несколько, берем только первый)
# 4 Какой ID у самого вытянутого участка в данных файлах (если их несколько, берем только первый)

data = []
with open('data/m7-map-1.txt') as ff:
    for row in ff:
        if row[:3] == 'ID#':
            row = row.replace('x', ',')
            row = row.replace(' :: ', ',')
            row = row.replace('ID#', '')
            row = row.replace('\n', '')
            data.append(row)

with open('data/m7-map-2.txt') as ff:
    for row in ff:
        if row[:3] == 'ID#':
            row = row.replace('x', ',')
            row = row.replace(' :: ', ',')
            row = row.replace('ID#', '')
            row = row.replace('\n', '')
            data.append(row)

df = pd.DataFrame(data, columns=['data'])
df[['ID', 'x', 'y', 'length', 'width']] = df.data.str.split(',', expand=True)
df = df.drop(['data'], axis=1)
df = df.astype('int')
df['square'] = df['length'] * df['width']
df['length_div_width'] = df['length'] / df['width']
mean_square = round(df['square'].mean())
max_square = df['square'].max()
max_length_div_width = df['length_div_width'].max()

print(df.head())

print('Средняя площать участков: ', mean_square)
print('Самый большой участок: ', max_square)

for i in range(len(df)):
    if df.loc[i, 'square'] == max_square:
        print('ID самого большого участка: ', df.loc[i, 'ID'])
        # print(df.iloc[i, :])
        break

for i in range(len(df)):
    if df.loc[i, 'length_div_width'] == max_length_div_width:
        print('ID у самого вытянутого участка: ', df.loc[i, 'ID'])
        # print(df.iloc[i, :])
        break
