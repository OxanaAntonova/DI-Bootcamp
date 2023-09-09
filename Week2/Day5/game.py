board = list(range(1, 10))

def draw_board(board):
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#draw_board(board)

def take_input(player):
    valid = False
    while not valid:
        player_answer = input("Where will you put it? " + player + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Invalid input. Are you sure you entered a number?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player
                valid = True
            else:
                print("This place is already taken")
        else:
            print("Invalid input. Enter a number from 1 to 9.")

def check_win(board):
    win_options = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_options:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):6
counter = 0
win = False
while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "You are the winner!")
            win = True
            break
        if counter == 9:
            print("Draw!")
            break
draw_board(board)

main(board)

input("Press Enter to exit!")            
            
            