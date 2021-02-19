import pandas as pd
import collections
from db import LogEntry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data/access_log.db')
Session = sessionmaker(bind=engine)
s = Session()


count = collections.Counter()
query = s.query(LogEntry.ip_addr).order_by(LogEntry.ip_addr)

data = []

for row in query:
    data.append(row)

data = pd.DataFrame(data)

for addr in data['ip_addr']:
    count[addr] += 1

visits = count.values()
most_common_visitor = count.most_common(10)

print('10 наиболее часто встречающихся адресов: ')
for address in most_common_visitor:
    print(f'{address[0]: >55}'.format('right aligned'))

print('Количество визитов c адреса 109.234.35.42:', most_common_visitor[0][1])
