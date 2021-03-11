import time
from urllib.request import urlopen

class LoudStopWatch:
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.delta = self.end - self.start


with LoudStopWatch() as s:
    for _ in range(10000000):
        pass

# print(f"Код выполнился за {s.delta:.03f} секунд")


url = "http://www.ya.ru"
with LoudStopWatch() as s:
    f = urlopen(url)
    f.read()

print(f"Код выполнился за {s.delta:.03f} секунд")