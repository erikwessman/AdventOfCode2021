file = open("day1/input.txt", "r")

array = file.read().splitlines()

for i in range(len(array)):
   array[i] = int(array[i])

result = 0
previous_sum = 0

for i in range(len(array)-2):
    current_sum = array[i] + array[i+1] + array[i+2]
    if current_sum > previous_sum and i != 0:
        result += 1
    previous_sum = current_sum

print(result)