import random
import numpy as np


def lotto_gen(mi, ma, anzz):
    numbers = np.arange(mi, ma + 1)
    rand_numbers = np.empty(anzz)
    for i in range(anzz):
        x = random.randrange(len(numbers) - i)
        rand_numbers[i] = numbers[x]
        numbers[x], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[x]
    return rand_numbers


def lotto_stats(mi, ma, anzzieh, anzrand):
    stats = {}

    for i in range(mi, ma + 1):
        stats[i] = 0

    for i in range(anzzieh):
        x = lotto_gen(mi, ma, anzrand)
        for j in range(len(x)):
            stats[x[j]] = stats[x[j]] + 1

    for x, y in stats.items():
        print(str(x) + " => " + str(y) + " mal")


if __name__ == "__main__":
    print(lotto_gen(1, 45, 6))
    lotto_stats(1, 45, 1000, 6)
