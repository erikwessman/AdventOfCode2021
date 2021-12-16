import math
from typing import NewType

file = open("day16/input.txt", "r")

array = file.read().splitlines()

hex_dict = {'0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'}

b = "".join([hex_dict[x] for x in array[0]])

def get_packets(b):
    p_version = int(b[:3], 2)
    p_id = int(b[3:6], 2)
    b = b[6:]
    num = ''
    numbers = []

    if p_id == 4:
        while True:
            next_bits = b[:5]
            num += next_bits[1:]
            b = b[5:]
            if next_bits[0] == '0':
                num = int(num, 2)
                break
    else:
        length_type = b[0]
        b = b[1:]
        if length_type == '0':
            num_bits = int(b[:15],2)
            b = b[15:]
            next_bits = b[:num_bits]
            while next_bits:
                m, n = get_packets(next_bits)
                next_bits = m
                numbers.append(n)
            b = b[num_bits:]
        else:
            num_subpackets = int(b[:11],2)
            b = b[11:]
            for _ in range(num_subpackets):
                m, n = get_packets(b)
                b = m
                numbers.append(n)

    if p_id == 0:
        num = sum(numbers)
    elif p_id == 1:
        num = math.prod(numbers)
    elif p_id == 2:
        num = min(numbers)
    elif p_id == 3:
        num = max(numbers)
    elif p_id == 5:
        if numbers[0] > numbers[1]:
            num = 1
        else:
            num = 0
    elif p_id == 6:
        if numbers[0] < numbers[1]:
            num = 1
        else:
            num = 0
    elif p_id == 7:
        if numbers[0] == numbers[1]:
            num = 1
        else:
            num = 0

    return b, num

print(get_packets(b)[1])

