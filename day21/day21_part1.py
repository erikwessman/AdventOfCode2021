file = open("day21/input.txt", "r")

array = file.read().splitlines()

class Player:
    position = 0
    score = 0

    def __init__(self, starting_position):
        self.position = int(starting_position)
    
    def move(self, spaces):
        self.position = board[(spaces + self.position - 1) % 10]
        self.score += self.position

nr_dice_rolls = 0
board = [1,2,3,4,5,6,7,8,9,10]

player1 = Player(array[0][-1])
player2 = Player(array[1][-1])

current_player = player1

while max(player1.score, player2.score) < 1000:
    move_spaces = (nr_dice_rolls % 100)*3 + 6
    nr_dice_rolls += 3

    current_player.move(move_spaces)

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    
print(min(player1.score, player2.score) * nr_dice_rolls)