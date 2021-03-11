from collections import Counter

words_list = []

with open('data/m8-sirotlivo.txt') as book:
    for line in book:
        words_list += line.lower().split()

c = Counter(words_list)

print(c.most_common(10))
