file = open("day3/input.txt", "r")

array = file.read().splitlines()

gamma = ''
epsilon = ''
result_array = [0] * 12

for line in array:
    for index, bit in enumerate(line):
        bit = int(bit)
        if bit == 0:
            result_array[index] -= 1
        elif bit == 1:
            result_array[index] += 1

for index, bit in enumerate(result_array):
    if bit >= 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))