import math

file = open("day7/input.txt", "r")

array = file.read().splitlines()

positions = [int(numeric_string) for numeric_string in array[0].split(',')]

def fuel_cost(start, end):
    steps = abs(start - end)
    return steps*(steps + 1) / 2

min_cost = math.inf

for position_1 in positions:
    cost = 0
    for position_2 in positions:
        cost += fuel_cost(position_1, position_2)
    min_cost = min(min_cost, cost)

print(int(min_cost))