class DummyStorage:

    def __init__(self, default=0):
        self.storage = {}
        self.default = default

    def save(self, key, value):
        self.storage[key] = value

    def load(self, key):
        if key in self.storage:
            return print(self.storage[key], True)
        else:
            return print(0, False)


ds = DummyStorage()

ds.save('ip', '192.168.1.1')
ds.load('i')
