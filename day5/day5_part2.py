file = open("day5/input.txt", "r")

array = file.read().splitlines()

lines = []
all_points = {}

for input_line in array:
    line = input_line.split(' ')

    point1 = line[0]
    point2 = line[2]
    
    x1, y1 = [int(numeric_string) for numeric_string in point1.split(',')]
    x2, y2 = [int(numeric_string) for numeric_string in point2.split(',')]
    
    lines.append([[x1, y1], [x2, y2]])


def get_points_on_straight_line(line):
    x_diff = line[1][0] - line[0][0]
    y_diff = line[1][1] - line[0][1]

    point = [line[0][0], line[0][1]]
    points = [point]
    iterations = x_diff if x_diff != 0 else y_diff
    iterations = abs(iterations)
    x_steps = int(x_diff / iterations)
    y_steps = int(y_diff / iterations)

    for i in range(iterations):
        new_x = point[0] + x_steps
        new_y = point[1] + y_steps
        point = [new_x, new_y]
        points.append(point)
    
    return points

for line in lines: 
    line_points = get_points_on_straight_line(line)
    for point in line_points:
        if tuple(point) in all_points:
            all_points[tuple(point)] += 1
        else:
            all_points[tuple(point)] = 1

nr_overlapping_lines = 0

for key, value in all_points.items():
    if value > 1:
        nr_overlapping_lines += 1

print(nr_overlapping_lines)
