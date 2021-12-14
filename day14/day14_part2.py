import math

file = open("day14/input.txt", "r")

array = file.read().splitlines()

polymer_template = array[:1]

polymer_template = polymer_template[0]

insertion_rules = array[2:]

insertion_dict = {}

pair_dict = {}

empty_pair_dict = {}

occurence_dict = {}

steps = 40

for line in insertion_rules:
    pair, result = line.split(' -> ')
    insertion_dict[pair] = result
    pair_dict[pair] = 0
    occurence_dict[result] = 0
    empty_pair_dict[pair] = 0

for i in range(len(polymer_template) - 1):
    pair = polymer_template[i:i+2]
    pair_dict[pair] += 1

for i in range(steps):
    new_pair_dict = dict(empty_pair_dict)
    for key in pair_dict:
        nr_occurences = pair_dict[key]
        if nr_occurences > 0:
            new_letter = insertion_dict[key]
            new_pair_dict[key[0] + new_letter] += nr_occurences
            new_pair_dict[new_letter + key[1]] += nr_occurences
    pair_dict = new_pair_dict

for key in pair_dict:
    nr_occurences = pair_dict[key]
    occurence_dict[key[0]] += nr_occurences
    occurence_dict[key[0]] += nr_occurences

for key in occurence_dict:
    new_value = math.ceil(occurence_dict[key] / 2)
    occurence_dict[key] = new_value

occurence_list = []
for key in occurence_dict:
    occurence_list.append(occurence_dict[key])

#Have to decrement by 1 for some reason
occurence_list.sort()
print(occurence_list[len(occurence_list)-1] - occurence_list[0] - 1)