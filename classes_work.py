
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
# print(u1, u2)
# print('Это один и тот же пользователь?', u1 == u2)
#
# print(dir(u1))


class KitchenUtensil:

    def __init__(self):
        pass


class Pan(KitchenUtensil):

    def __init__(self, size):
        self.size = size

    def heat_up(self):
        print('Сковородка подогревается')


class SaucePan(KitchenUtensil):

    def __init__(self, volume, height):
        self.volume = volume
        self.height = height
        self.diameter = (4 * volume / (3.14*height)) ** 0.5

    def heat_up(self):
        print(f'Кастрюля диаметром {self.diameter * 100:.2f} см нагревается')


###
utensils = [Pan(20), SaucePan(3, 0.125)]

# for u in utensils:
#     u.heat_up()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_activate(self):
        return False

    def is_superuser(self):
        return False

    def __str__(self):
        kind = 'пользователь'
        if self.is_superuser():
            kind = 'админ'
        return f'{kind}, {self.name}, {self.email}'


class RegularUser(User):
    pass


class SuperUser(User):

    def is_superuser(self):
        return True


###
u1 = RegularUser("Vasiliy", "vasily@mail.ru")
u2 = SuperUser("Larisa", "larisa@mail.ru")

u1.is_activate = True
print(u1.is_activate)

for u in (u1, u2):
    print(u)
