file = open("day3/input.txt", "r")

array = file.read().splitlines()

array_copy = array.copy()

o2 = ''
co2 = ''

for i in range(12):
    most_common = 0
    for line in array:
        bit = int(line[i])
        if bit == 1:
            most_common += 1
        else:
            most_common -= 1
    
    new_list = []
    if most_common >= 0:
        new_list = [s for s in array if s[i] == '1']
    elif most_common < 0:
        new_list = [s for s in array if s[i] == '0']

    array = new_list

    if len(array) == 1:
        o2 = array[0]
        break

array = array_copy

for i in range(12):
    most_common = 0
    for line in array:
        bit = int(line[i])
        if bit == 1:
            most_common += 1
        else:
            most_common -= 1
    
    new_list = []
    if most_common >= 0:
        new_list = [s for s in array if s[i] == '0']
    elif most_common < 0:
        new_list = [s for s in array if s[i] == '1']

    array = new_list

    if len(array) == 1:
        co2 = array[0]
        break
    
print(int(o2, 2) * int(co2, 2))