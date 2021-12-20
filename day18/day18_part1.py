import math

file = open("day18/input.txt", "r")

array = file.read().splitlines()

def add_lines(line1, line2):
    return '[' + line1 + ',' + line2 + ']'


def can_explode(line):
    stack = []
    for i, c in enumerate(line):
        if c == '[':
            stack.append('[')
        elif c == ']':
            stack.pop()
        else:
            if len(stack) == 5:
                return True, i
    return False, 0

def explode_line(line, i):
    start = i
    stop = i
    while True:
        if line[stop] == ']':
            break
        else:
            stop += 1

    num1, num2 = line[start:stop].split(',')

    left_side = line[0:start-1]
    right_side = line[stop+1:len(line)]

    for c in range(len(left_side)-1, -1, -1):
        if left_side[c].isnumeric():
            if left_side[c-1].isnumeric():
                left_side = left_side[0:c-1] + str(int(left_side[c-1] + left_side[c]) + int(num1)) + left_side[c+1:len(left_side)]
                break
            else:
                left_side = left_side[0:c] + str(int(left_side[c]) + int(num1)) + left_side[c+1:len(left_side)]
                break

    for c in range(len(right_side)):
        if right_side[c].isnumeric():
            if right_side[c+1].isnumeric():
                right_side = right_side[0:c] + str(int(right_side[c] + right_side[c+1]) + int(num2)) + right_side[c+2:len(right_side)]
                break
            else:
                right_side = right_side[0:c] + str(int(right_side[c]) + int(num2)) + right_side[c+1:len(right_side)]
                break

    return left_side + '0' + right_side


def can_split(line):
    for i, c in enumerate(line):
        if c.isnumeric():
            num = line[i] + line[i+1]
            if num.isnumeric() and int(num) > 9:
                return True, i
    return False, 0

def split_line(line, i):
    num = int(line[i] + line[i+1])
    left_num = math.floor(num/2)
    right_num = math.ceil(num/2)
    left_side = line[0:i]
    right_side = line[i+2:len(line)]
    return left_side + '[' + str(left_num) + ',' + str(right_num) + ']' + right_side


def calculate_magnitude(line):
    while True:

        for i,c in enumerate(line):
            if c == ',' and line[i-1].isnumeric() and line[i+1].isnumeric():
                start = i
                stop = i
                while True:
                    if line[stop] == ']':
                        break
                    else:
                        stop += 1

                while True:
                    if line[start] == '[':
                        break
                    else:
                        start -= 1
                    
                num1, num2 = line[start+1:stop].split(',')
                result = int(num1)*3 + int(num2)*2
                left_side = line[0:start]
                right_side = line[stop+1:len(line)]
                line = left_side + str(result) + right_side

                if '[' not in line and ']' not in line:
                    return line

                break

line = add_lines(array[0], array[1])
next_line = 2

while True:
    ce, i = can_explode(line)
    if ce:
        line = explode_line(line, i)
    else:
        cs, i = can_split(line)
        if cs:  
            line = split_line(line, i)
        else:
            if next_line == len(array):
                break
            else:
                line = add_lines(line, array[next_line])
                next_line += 1

print(calculate_magnitude(line))