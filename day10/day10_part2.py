file = open("day10/input.txt", "r")

array = file.read().splitlines()

opening_chars = '([{<'
char_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
points_dict = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []

for line in array:
    stack = []
    score = 0
    incomplete = True
    for char in line:
        if char in opening_chars:
            stack.append(char)
        else:
            if stack[len(stack)-1] == char_dict[char]:
                stack.pop()
            else:
                incomplete = False
                break
    if incomplete:
        for i in range(len(stack)):
            score *= 5
            score += points_dict[stack.pop()]
        scores.append(score)

sorted_scores = sorted(scores)
print(sorted_scores[int((len(sorted_scores) - 1) / 2)])