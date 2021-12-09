file = open("day9/input.txt", "r")

array = file.read().splitlines()

ocean_map = []

for line in array:
    ocean_map.append([int(numeric_string) for numeric_string in line])

height, width = len(array), len(array[0])

result = 0

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
            result += ocean_map[y][x] + 1

print(result)
