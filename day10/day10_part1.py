file = open("day10/input.txt", "r")

array = file.read().splitlines()

opening_chars = '([{<'
char_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
result = 0

for line in array:
    stack = []
    for char in line:
        if char in opening_chars:
            stack.append(char)
        else:
            if stack[len(stack)-1] == char_dict[char]:
                stack.pop()
            else:
                result += points_dict[char]
                break

print(result)