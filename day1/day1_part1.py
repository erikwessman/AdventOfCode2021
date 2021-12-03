file = open("day1/input.txt", "r")

array = file.read().splitlines()

for i in range(len(array)):
   array[i] = int(array[i])

result = 0

for i in range(len(array)):
    if i != 0:
        if array[i] > array[i-1]:
            result += 1

print(result)