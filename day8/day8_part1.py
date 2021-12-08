file = open("day8/input.txt", "r")

array = file.read().splitlines()

outputs = []

for line in array:
    outputs.extend(line.split('|')[1].split(' ')[1:])

result = 0

for output_value in outputs:
    length = len(output_value)
    if length == 7 or length == 4 or length == 3 or length == 2:
        print(output_value, length)
        result += 1

print(result)