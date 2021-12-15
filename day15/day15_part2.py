from queue import PriorityQueue
import numpy as np

file = open("day15/input.txt", "r")

array = file.read().splitlines()
for index,line in enumerate(array):
    array[index] = ([int(numeric_string) for numeric_string in line])
height = len(array) * 5
width = len(array[0]) * 5

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.costs = {}
        self.neighbors = {}
        self.visited = []

def heuristic(a, b):
    x1,y1 = [a % width, a // height]
    x2,y2 = [b % width, b // height]
    return abs(x1 - x2) + abs(y1 - y2)

#https://www.redblobgames.com/pathfinding/a-star/implementation.html
def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break

        for n in graph.neighbors[current]:
            new_cost = cost_so_far[current] + graph.costs[(current, n)]
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + heuristic(n, goal)
                frontier.put(n, priority)
                came_from[n] = current
    
    return came_from, cost_so_far

new_grid = np.zeros((height,width), dtype=int)

for iy, ix in np.ndindex(new_grid.shape):
    steps_x = int(ix % (width / 5))
    steps_y = int(iy % (height / 5 ))
    increase_x = int(ix // (width / 5))
    increase_y = int(iy // (height / 5))
    new_value = array[steps_y][steps_x] + increase_x + increase_y
    new_value = (new_value % 10) + (new_value // 10)
    new_grid[iy, ix] = new_value

graph = Graph(height * width)

for y in range(height):
    for x in range(width):
        u = y*width + x
        neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for n in neighbors:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                v = n[1]*width + n[0]
                graph.costs[(u,v)] = new_grid[n[1], n[0]]
                if u in graph.neighbors:
                    graph.neighbors[u].append(v)
                else:
                    graph.neighbors[u] = [v]

D = a_star(graph, 0, width*height-1)
print(D[1][width*height - 1])