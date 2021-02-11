import csv

with open('data/m5-calibration.dat', 'r') as dr:
    data = dr.read().split()

    result = 0
    i = 1
    for value in data:
        if '-' in value:
            digit = value[1:]
            result -= float(digit)

        else:
            result += float(value)
        i += 1
    print('Сумма вычислений: ', result)

