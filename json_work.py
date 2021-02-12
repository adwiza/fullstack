import pandas as pd
import json
import collections

data = pd.read_csv('data/m5-access-log-all.csv')

count = collections.Counter()
for addr in data['ip']:
    count[addr] += 1

total_visits = 0
visits = count.values()
most_common_visitor = count.most_common(1)
for visit in visits:
    total_visits += int(visit)

my_list = []
for i in data.values:
    if i[1] == most_common_visitor[0][0]:
        my_list.append(i)

last_one = my_list[-1]
last_one_user_agent = ''.join(last_one[2:])
time_stamp_of_last_one = ''.join(last_one[0])

suspicious_agent = {
    'ip': most_common_visitor[0][0],
    'fraction': round(int(most_common_visitor[0][1]) * 100 / total_visits, 2),
    'count': total_visits,
    'last':
        {'agent': last_one_user_agent,
         'timestamp': time_stamp_of_last_one,
         },
}

with open('data/suspicious_agent.json', 'w') as outfile:
    json.dump(suspicious_agent, outfile, indent=4)
print(json.dumps(suspicious_agent, indent=4))
