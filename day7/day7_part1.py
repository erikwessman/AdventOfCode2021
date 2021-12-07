import statistics as st

file = open("day7/input.txt", "r")

array = file.read().splitlines()

positions = [int(numeric_string) for numeric_string in array[0].split(',')]

median = st.median(positions)

fuel_cost = 0

for position in positions:
    fuel_cost += int(abs(position - median))

print(fuel_cost)