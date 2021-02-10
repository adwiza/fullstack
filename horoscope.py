import random as r


def generate_prophecies():

    generated_prophecies = []
    i = 0
    while i < 2:
        times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
        advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
        promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника",
                    "приятных перемен"]
        time = r.choice(times)
        advices = r.choice(advices)
        promises = r.choice(promises)
        generated_prophecies.append(time.capitalize() + ' ' + advices + ' ' + promises + '.')
        i += 1

    return generated_prophecies

print(generate_prophecies())
# z = 0
# my_list = []
# while z < 6:
#     my_list += generate_prophecies()
#     print(z)
#     z += 1
#
# print(my_list)
