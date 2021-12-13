file = open("day13/input.txt", "r")

array = file.read().splitlines()

split_index = array.index('')

points = array[:split_index]

instructions = array[split_index+1:]

for index,point in enumerate(points):
    x,y = point.split(',')
    points[index] = [int(x),int(y)]

for line in instructions:
    axis,coord = line.split(' ')[2].split('=')
    coord = int(coord)
    if axis == 'x': 
        axis = 0
    else:
        axis = 1

    new_points = []

    for point in points:
        if point[axis] > coord:
            new_point = [point[0], point[1]]
            diff = new_point[axis] - coord
            new_point[axis] = new_point[axis] - 2*diff
            if not new_point in new_points:
                new_points.append(new_point)
        else:
            if not point in new_points:
                new_points.append(point)

    points = new_points
    break

print(len(points))
