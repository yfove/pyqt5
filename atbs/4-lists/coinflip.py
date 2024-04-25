# coin flip streaks

import random
numberOfStreaks = 0 
streak_length = 6
total_experiments = 10000


for experimentNumber in range(total_experiments):
    # code that creates a list of 100 head or tails values
    flips = ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(100)]
    # code that checks if there is a streak of 6 heads or tails in a row
    # increment that to list 
    for i in range(len(flips) - streak_length + 1):
        if all(flips[i+j] == flips[i] for j in range(1, streak_length)):
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / total_experiments * 100))
