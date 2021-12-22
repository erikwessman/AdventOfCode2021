from copy import deepcopy
import numpy as np

file = open("day20/input.txt", "r")

array = file.read().splitlines()

iterations = 2

enhancement_string = array[0]

input_image = array[2:]

for index, value in enumerate(input_image):
    input_image[index] = [char for char in value]


def get_iteration_symbol(iteration):
    if enhancement_string[0] == '.':
        return enhancement_string[0]

    if iteration % 2 == 0:
        return enhancement_string[511]
    else:
        return enhancement_string[0]


def get_number_from_symbol(symbol):
    if symbol == '#':
        return '1'
    else:
        return '0'


def get_iteration_number(iteration):
    return get_number_from_symbol(get_iteration_symbol(iteration))


def extend_image(image, iteration):
    np_image = np.asarray(image)
    h = len(image)
    w = len(image[0])

    extension_height = [get_iteration_symbol(iteration)] * h
    extension_width = [[get_iteration_symbol(iteration)] * (w+2)]

    np_image = np.concatenate((np.array(extension_height)[:, np.newaxis], np_image), axis=1)
    np_image = np.append(np_image, np.array(extension_height)[:, np.newaxis], axis=1)

    np_image = np.concatenate((np.array(extension_width), np_image), axis=0)
    np_image = np.append(np_image, np.array(extension_width), axis=0)
    
    return np_image.tolist(), np_image.shape[0], np_image.shape[1]


def get_pixel(binary_string):
    index = int(binary_string, 2)
    return enhancement_string[index]


def get_total_lit_pixels(image):
    total = 0
    height = len(image)
    width = len(image[0])
    for y in range(height):
        for x in range(width):
            if image[y][x] == '#':
                total += 1
    return total

for i in range(iterations):
    input_image, height, width = extend_image(input_image, i)

    input_copy = deepcopy(input_image)

    for y in range(height):
        for x in range(width):
            binary_string = ''
            neighbors = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
            for n in neighbors:
                if n[0] >= 0 and n[0] < width and n[1] >= 0 and n[1] < height:
                    binary_string += get_number_from_symbol(input_image[n[1]][n[0]])
                else:
                    binary_string += get_iteration_number(i)

            input_copy[y][x] = get_pixel(binary_string)

    input_image = input_copy

print(get_total_lit_pixels(input_image))