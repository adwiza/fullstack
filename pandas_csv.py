import pandas as pd

data = pd.read_csv('data/m5-buckwheat.csv')
s = data[["Крупа манная, кг", "Год"]]
print(s.mean())
