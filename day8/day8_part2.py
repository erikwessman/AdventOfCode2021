file = open("day8/input.txt", "r")

array = file.read().splitlines()

total_sum = 0

def get_pattern_diff(s1, s2):
    ret = []
    for letter in s1:
        if letter not in s2:
            ret.append(letter)
    return ret

#Really ugly but gets the job done
#Definitely better solutions out there
def get_pattern_dictionary(pattern):
    p_dict = {}
    numbers = [''] * 10
    seven_segment = [''] * 7

    for p in pattern:
        length = len(p)
        if length == 2:
            numbers[1] = p
        elif length == 3:
            numbers[7] = p
        elif length == 4:
            numbers[4] = p
        elif length == 7:
            numbers[8] = p

    seven_segment[0] = get_pattern_diff(numbers[7], numbers[1])[0]

    for p in pattern:
        diff = get_pattern_diff(numbers[8], p)
        if len(diff) == 1:
            if diff[0] in numbers[1]:
                seven_segment[2] = diff[0]
                numbers[6] = p
            elif diff[0] in numbers[4]:
                seven_segment[3] = diff[0]
                numbers[0] = p
            else:
                seven_segment[4] = diff[0]
                numbers[9] = p
    
    for p in pattern:
        diff = get_pattern_diff(numbers[8], p)
        if len(diff) == 2:
            new_diff = get_pattern_diff(p, numbers[4])
            if len(new_diff) == 3:
                seven_segment[6] = get_pattern_diff(p, ''.join(seven_segment))[0]
                numbers[2] = p

    diff = get_pattern_diff(numbers[6], ''.join(seven_segment))
    for d in diff:
        if d not in numbers[1]:
            seven_segment[1] = d

    seven_segment[5] = get_pattern_diff(numbers[8], ''.join(seven_segment))[0]

    numbers[3] = ''.join(sorted(seven_segment[0] + seven_segment[2] + seven_segment[3] + seven_segment[5] + seven_segment[6]))
    numbers[5] = ''.join(sorted(seven_segment[0] + seven_segment[1] + seven_segment[3] + seven_segment[5] + seven_segment[6]))

    for index, value in enumerate(numbers):
        p_dict[value] = index

    return p_dict

for line in array:
    line = line.split(' ')
    for i, value in enumerate(line): line[i] = "".join(sorted(value))
    pattern_dict = get_pattern_dictionary(line[:-5])

    output_number = ''

    for p in line[-4:]:
        output_number += str(pattern_dict[p])

    total_sum += int(output_number)

print(total_sum)