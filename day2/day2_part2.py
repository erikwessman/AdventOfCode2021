file = open("day2/input.txt", "r")

array = file.read().splitlines()

aim = 0
result_horizontal = 0
result_depth = 0

for line in array:
    command = line.split(" ")
    if command[0] == "forward":
        result_horizontal += int(command[1])
        result_depth += aim * int(command[1])
    if command[0] == "up":
        aim -= int(command[1])
    if command[0] == "down":
        aim += int(command[1])

print(result_depth * result_horizontal)