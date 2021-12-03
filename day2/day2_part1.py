file = open("day2/input.txt", "r")

array = file.read().splitlines()

result_horizontal = 0
result_depth = 0

for line in array:
    command = line.split(" ")
    if command[0] == "forward":
        result_horizontal += int(command[1])
    if command[0] == "up":
        result_depth -= int(command[1])
    if command[0] == "down":
        result_depth += int(command[1])

print(result_horizontal * result_depth)