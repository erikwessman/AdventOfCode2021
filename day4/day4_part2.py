file = open("day4/input.txt", "r")

array = file.read().splitlines()

numbers = array[0].split(',')

lines = array[2:]

boards = []
board = []

for line in lines:
    if line != '':
        split_array = line.split(' ')
        row = [i for i in split_array if i]
        board.append(row)
    else:
        boards.append(board)
        board = []
boards.append(board)

def is_board_solved(board):
    for i in range(5):
        row = board[i]
        col = [board[j][i] for j in range(5)]
        complete = ['-1'] * 5

        if row == complete or col == complete :
            return True
    return False

def solve(boards):
    for number in numbers:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == number:
                        board[i][j] = '-1'
                        if is_board_solved(board):
                            
                            new_list = [s for s in boards if s != board]
                            boards = new_list

                            if len(boards) == 0:
                                return [board, number]

solution = solve(boards)

unmarked_sum = 0
for i in range(5):
    for j in range(5):
        if solution[0][i][j] != '-1':
            unmarked_sum += int(solution[0][i][j])

print(unmarked_sum * int(solution[1]))