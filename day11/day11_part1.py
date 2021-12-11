file = open("day11/input.txt", "r")

array = file.read().splitlines()

energy_levels = []
steps = 100
total_flashes = 0

for line in array:
    energy_levels.append([[int(numeric_string), False] for numeric_string in line])

height = len(energy_levels)
width = len(energy_levels[0])

def increment_energy_levels():
    for y in range(height):
        for x in range(width):
            energy_levels[y][x][0] += 1

def check_flashes(x,y):
    if energy_levels[y][x][1] == False:
        if energy_levels[y][x][0] > 9:
            energy_levels[y][x][0] = 0
            energy_levels[y][x][1] = True
            neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    if energy_levels[n[1]][n[0]][1] == False:
                        energy_levels[n[1]][n[0]][0] += 1
                    check_flashes(n[0], n[1])

def count_and_reset_flashes():
    flashes = 0
    for y in range(height):
        for x in range(width):
            if energy_levels[y][x][1] == True:
                flashes += 1
                energy_levels[y][x][1] = False
    return flashes

def print_energy():
    for y in range(height):
        for x in range(width):
            print(str(energy_levels[y][x][0]) + ' ', end = '')
        print('')

for i in range(steps):
    increment_energy_levels()

    for y in range(height):
        for x in range(width):
            check_flashes(x,y)

    total_flashes += count_and_reset_flashes()

print(total_flashes)