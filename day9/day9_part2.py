import math

file = open("day9/input.txt", "r")

array = file.read().splitlines()

ocean_map = []
basin_sizes = []
height, width = len(array), len(array[0])
result = 0

for line in array:
    ocean_map.append([int(numeric_string) for numeric_string in line])

def flood_fill(x, y, size):
    if ocean_map[y][x] == 9:
        return size
    else:
        size += 1
        ocean_map[y][x] = 9
        neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for n in neighbors:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                size = flood_fill(n[0], n[1], size)
        return size

def is_low_point(x, y):
    value = ocean_map[y][x]
    u,d,l,r = 9,9,9,9
    if y > 0 : u = ocean_map[y-1][x]
    if y < height-1 : d = ocean_map[y+1][x]
    if x > 0 : l = ocean_map[y][x-1]
    if x < width-1 : r = ocean_map[y][x+1]
    return value < u and value < d and value < l and value < r

for y in range(height):
    for x in range(width):
        if is_low_point(x,y):
            basin_sizes.append(flood_fill(x,y,0))

sorted_basins = sorted(basin_sizes)
print(math.prod(sorted_basins[-3:]))
