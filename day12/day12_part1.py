import copy

file = open("day12/input.txt", "r")

array = file.read().splitlines()

node_dict = {}

for line in array:
    nodes = line.split('-')
    if nodes[0] in node_dict:
        node_dict[nodes[0]].append(nodes[1])
    else:
        node_dict[nodes[0]] = [nodes[1]]
    if nodes[1] in node_dict:
        node_dict[nodes[1]].append(nodes[0])
    else:
        node_dict[nodes[1]] = [nodes[0]]

def traverse_path(node1, node2, visited, current_path, all_paths):
    if node1.islower():
        visited[node1] = True

    current_path.append(node1)

    if node1 == node2:
        all_paths.append(copy.deepcopy(current_path))
    else:
        for node in node_dict[node1]:
            if visited[node] == False:
                traverse_path(node, node2, visited, current_path, all_paths)

    current_path.pop()
    visited[node1] = False

def get_all_paths(start, end):
    visited_dict = {}
    current_path = []
    all_paths = []

    for key in node_dict:
        visited_dict[key] = False

    traverse_path(start, end, visited_dict, current_path, all_paths)

    return all_paths

all_paths = get_all_paths('start', 'end')
print(len(all_paths))