class NutritionInfo:

    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def __add__(self, other):
        return self.energy()

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)


tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)
total_calories = apple.energy() + tvorog_9.energy()

print(tvorog_9.energy())
print(apple.energy())
print(total_calories)
