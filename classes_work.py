
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name} <{self.email}>'

    def __eq__(self, other):
        return self.email.lower() == other.email.lower()


u1 = User('Алексей', email='ADWIZ@ya.ru')
u2 = User(name='Иван', email='adwiz@ya.ru')
print(u1, u2)
print('Это один и тот же пользователь?', u1 == u2)

print(dir(u1))