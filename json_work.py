from pprint import pprint

import pandas as pd
import json
import collections

data = pd.read_csv('data/m5-access-log-all.csv')

count = collections.Counter()
for addr in data['ip']:
    count[addr] += 1

total_visits = 0
visits = count.values()
for visit in visits:
    total_visits += int(visit)

most_common_visitor = count.most_common(1)
print(int(most_common_visitor[0][1]) / total_visits * 100)

