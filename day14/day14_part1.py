file = open("day14/input.txt", "r")

array = file.read().splitlines()

polymer_template = array[:1]

polymer_template = polymer_template[0]

insertion_rules = array[2:]

insertion_dict = {}

steps = 10

for line in insertion_rules:
    pair, result = line.split(' -> ')
    insertion_dict[pair] = result

for i in range(steps):
    new_word = ''
    for j in range(len(polymer_template) - 1):
        pair = polymer_template[j:j+2]
        new_word += polymer_template[j]
        new_word += insertion_dict[pair]
    polymer_template = new_word + polymer_template[len(polymer_template)-1]

occurences = []
set_of_characters = set(polymer_template)
for c in set_of_characters:
    occurences.append(polymer_template.count(c))

occurences.sort()
print(occurences[len(occurences) - 1] - occurences[0])