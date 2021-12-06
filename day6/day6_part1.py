import numpy as np

file = open("day6/input.txt", "r")

array = file.read().splitlines()

starting_fish = [int(numeric_string) for numeric_string in array[0].split(',')]

all_fish = [0] * 9

for fish in starting_fish:
    all_fish[fish] += 1

def simulate_day(all_fish):
    old_fish = all_fish[:-2]
    new_fish = all_fish[-2:]
    born_fish = all_fish[0]

    old_fish = np.roll(old_fish, -1).tolist()

    old_fish[6] += new_fish[0]
    new_fish[0] = new_fish[1]
    new_fish[1] = born_fish

    return old_fish + new_fish

for day in range(80):
    all_fish = simulate_day(all_fish)

total_nr_fish = 0

for fish in all_fish:
    total_nr_fish += fish

print(total_nr_fish)
