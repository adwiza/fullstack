import random as r


def generate_prophecies():
    """Функция генерирует предсказание."""
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника",
                "приятных перемен"]
    generated_prophecies = []
    i = 0
    while i < 6:
        j = 0
        forecast = []
        while j < 2:
            random_times = r.choice(times)
            random_advices = r.choice(advices)
            random_promises = r.choice(promises)
            full_sentence = random_times.capitalize() + " " + random_advices + " " + random_promises + "."
            forecast.append(full_sentence)
            j += 1
        generated_prophecies.append(forecast[0] + " " + forecast[1])
        i += 1

    return generated_prophecies
