import random

import numpy as np


def lotto_gen():
    numbers = np.arange(1,46)
    rand_numbers = np.empty(6)
    for i in range(0,6):
        x = random.randrange(0,44-i)
        rand_numbers[i] = numbers[x]
        numbers[x], numbers[44-i] = numbers[44-i], numbers[x]
    return rand_numbers


def lotto_stats():
    stats = {}

    for i in range(1,46):
        stats[i] = 0

    for i in range(0,1000):
        x = lotto_gen()
        for i in range(0,6):
            stats[x[i]] = stats[x[i]] + 1

    for x, y in stats.items():
        print(str(x) + " => " + str(y) + " mal")

print(lotto_gen())
lotto_stats()