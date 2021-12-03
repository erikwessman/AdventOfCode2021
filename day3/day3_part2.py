file = open("day3/input.txt", "r")

o2_array = file.read().splitlines()
co2_array = o2_array.copy()

o2 = ''
co2 = ''

def solve(array, a, b):
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
            new_list = [s for s in array if s[i] == a]
        elif most_common < 0:
            new_list = [s for s in array if s[i] == b]

        array = new_list

        if len(array) == 1:
            return array[0]

o2 = solve(o2_array, '1', '0')
co2 = solve(co2_array, '0', '1')

print(int(o2, 2) * int(co2, 2))