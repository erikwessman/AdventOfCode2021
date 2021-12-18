file = open("day17/input.txt", "r")

array = file.read().splitlines()

array = array[0].split(' ')
array = [array[2], array[3]]
x1,x2 = array[0].split('..')
y1,y2 = array[1].split('..')
x1 = int(x1[2:])
x2 = int(x2[:-1])
y1 = int(y1[2:])
y2 = int(y2)

y_velocities = set()

def check_y():
    velocity = 0
    while velocity > y1:
        all_positions = [0]

        c = velocity-1
        while True:
            if c + all_positions[len(all_positions)-1] < y1:
                break
            all_positions.append(c + all_positions[len(all_positions)-1])
            c -= 1
        
        for pos in all_positions:
            if y1 <= pos <= y2:
                y_velocities.add(abs(velocity))

        velocity -= 1

check_y()
max_y_vel = max(y_velocities)
print(int((max_y_vel * (max_y_vel + 1)) / 2))