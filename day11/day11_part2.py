file = open("day11/input.txt", "r")

array = file.read().splitlines()

energy_levels = []
total_flashes = 0
step = 0
synchronized_step = 0

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

def check_synchronized_flash():
    for y in range(height):
        for x in range(width):
            if energy_levels[y][x][0] != 0:
                return False
    return True

def reset_flashes():
    for y in range(height):
        for x in range(width):
            if energy_levels[y][x][1] == True:
                energy_levels[y][x][1] = False

while True:
    step += 1
    increment_energy_levels()

    for y in range(height):
        for x in range(width):
            check_flashes(x,y)

    if check_synchronized_flash():
        synchronized_step = step
        break

    reset_flashes()

print(synchronized_step)