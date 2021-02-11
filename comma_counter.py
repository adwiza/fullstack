import re

with open('data/m5-line-by-line.txt', 'r') as df:
    data = df.read()
    data_comma = re.findall(r',', data)
    data_all_words = data.split()
    result = len(data_comma) / len(data_all_words) * 100
    print(len(data_comma))
    print(int(result))
