from collections import defaultdict
from itertools import permutations
import numpy as np

file = open("day19/input.txt", "r")

array = file.read().splitlines()

scanner_readings = [[]]
point_remaps = list(permutations((0,1,2)))
point_negations = [(1,1,1), (-1,1,1), (1,-1,1), (1,1,-1), (-1,-1,1), (1,-1,-1), (-1,1,-1), (-1,-1,-1)]

i = 0
for line in array:
    if line == '':
        i += 1
        scanner_readings.append([])
    else:
        if 'scanner' not in line:
            points = [int(i) for i in line.split(',')]
            scanner_readings[i].append((points[0], points[1], points[2]))


def get_diff(beacon1, beacon2):
    x_diff = beacon1[0] - beacon2[0]
    y_diff = beacon1[1] - beacon2[1]
    z_diff = beacon1[2] - beacon2[2]
    return (x_diff, y_diff, z_diff)


def translate(beacon, offset):
    return (beacon[0] + offset[0], 
            beacon[1] + offset[1], 
            beacon[2] + offset[2])


def rotate(beacon, remap, negate):
    return (negate[0]*beacon[remap[0]], 
            negate[1]*beacon[remap[1]], 
            negate[2]*beacon[remap[2]])


def get_offset(scanner1, scanner2, remap, negate):
    offset_dict = defaultdict(int)
    for beacon1 in scanner1:
        for beacon2 in scanner2:
            offset_dict[get_diff(beacon1, rotate(beacon2, remap, negate))] += 1

    if max(offset_dict.values()) >= 12:
        correct_offset = max(offset_dict, key=offset_dict.get)
        return (True, correct_offset)
    else:
        return (False, (0,0,0))


def add_points_to_known(scanner1, scanner2, offset, remap, negate):
    for point in scanner2:
        p = (point[0], point[1], point[2])
        p = rotate(p, remap, negate)
        p = translate(p, offset)
        scanner1.add(p)


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


known_points = set(scanner_readings[0])
scanners = scanner_readings[1:]

all_scanner_positions = []

while scanners:
    move_to_back = True

    for r in point_remaps:
        for n in point_negations:
            result = get_offset(known_points, scanners[0], r, n)
            if result[0]:
                add_points_to_known(known_points, scanners[0], result[1], r, n)
                all_scanner_positions.append(result[1])
                scanners.pop(0)
                move_to_back = False
                break
        
        if not move_to_back:
            break
    
    if move_to_back:
        scanners.append(scanners.pop(0))

largest_distance = 0
for i in all_scanner_positions:
    for j in all_scanner_positions:
        a = np.asarray(i)
        b = np.asarray(j)
        largest_distance = max(largest_distance, manhattan_distance(a,b))

print(largest_distance)