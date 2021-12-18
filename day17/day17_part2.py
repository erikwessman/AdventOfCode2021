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

velocity_pairs = set()

for x in range(x2+1):
    for y in range(y1, abs(y1)):
        x_pos = 0
        y_pos = 0
        x_change = x
        y_change = y
        step = 0
        while True:
            x_pos += x_change
            y_pos += y_change

            if x1 <= x_pos <= x2 and y1 <= y_pos <= y2:
                velocity_pairs.add((x,y))
                break

            if x_pos > x2 or y_pos < y1:
                break
            
            x_change = max(0, x_change-1)
            y_change -= 1

            step += 1

print(len(velocity_pairs))