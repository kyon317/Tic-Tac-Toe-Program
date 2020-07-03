"""
Tic-Tac-Toe Chess program:
1. make a list of all legal moves;
2. for each of the moves it does some number of random playouts;
3. during a random playout, the computer makes random moves for each player until a win, loss, or draw is reached;
4. the computer makes decision based on the move that has the best simulation result.
"""
import random

'''
Chess
'''
chess = {1: 'x', 2: 'o'}
x = 1
o = 2
'''
States
'''
states = {3: 'Win',
          4: 'Loss',
          5: 'Draw',
          6: 'Continue'}
WIN = 3
LOSS = 4
DRAW = 5
CONTINUE = 6

'''
Print a board with chess on it.
'''


def print_board(board):
    print("   a b c")
    for count, row in enumerate(board):
        print(count, end='')
        print(' ', *row, ' ', sep='|')


'''
Place a chess on a given coordinate
'''


def make_moves(board, coordinate, selected_chess):
    board[coordinate[0]][coordinate[1]] = selected_chess


'''
Judge the current status, decide if a game is over
'''


def judge(current_board, chess1, chess2):
    # Check rows
    for j in range(len(current_board)):
        if current_board[j][0] != ' ':
            piece = current_board[j][0]
            if (current_board[j][1] == piece) and (current_board[j][2] == piece):
                return WIN, piece

    # Check columns
    for i in range(len(current_board[0])):
        if current_board[0][i] != ' ':
            piece = current_board[0][i]
            if (current_board[1][i] == piece) and (current_board[2][i] == piece):
                return WIN, piece

    # Check Diagonal Down
    if current_board[0][0] != ' ':
        piece = current_board[0][0]
        if (current_board[1][1] == piece) and (current_board[2][2] == piece):
            return WIN, piece

    # Check Diagonal Up
    if current_board[0][2] != ' ':
        piece = current_board[0][2]
        if (current_board[1][1] == piece) and (current_board[2][0] == piece):
            return WIN, piece

    # Check if board is full
    if len(return_legal_moves(current_board)) == 0:
        return DRAW, None
    else:
        chess1_counter = 0
        chess2_counter = 0
        for i in range(3):
            for j in range(3):
                if current_board[i][j] == chess1:
                    chess1_counter += 1
                if current_board[i][j] == chess2:
                    chess2_counter += 1
        if chess1_counter > chess2_counter:
            next_chess = chess2
        else:
            next_chess = chess1
        return CONTINUE, next_chess


'''
Return a list of legal moves based on current status
'''


def return_legal_moves(curr_board):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if curr_board[i][j] == ' ':
                legal_moves.append([i, j])
    return legal_moves


'''
make one single simulation
'''


def make_a_random_play(current_board):
    dummy_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(len(current_board)):
        for j in range(len(current_board)):
            dummy_board[i][j] = current_board[i][j]
    while judge(dummy_board, 'x', 'o')[0] == CONTINUE:
        legal_moves = return_legal_moves(dummy_board)
        index = random.randint(0, len(legal_moves) - 1)
        dummy_move = legal_moves[index]
        next_chess = judge(dummy_board, 'x', 'o')[1]
        make_moves(dummy_board, dummy_move, next_chess)
    return judge(dummy_board, 'x', 'o')


'''
multiple simulations to find the best move that avoids losing
'''


def make_random_playouts(board_status, MAX_PLAYOUT=1000):
    """
    for each legal_moves, make simulation until the game finished and return win or lose or draw
    :param MAX_PLAYOUT:
    :param board_status:
    :return: coordinate of legal_move
    """
    current_chess = judge(board_status, 'x', 'o')[1]
    legal_moves_list = return_legal_moves(board_status)
    current_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(len(board_status)):
        for j in range(len(board_status)):
            current_board[i][j] = board_status[i][j]
    resultRate = [0] * len(legal_moves_list)
    for i in range(len(legal_moves_list)):
        make_moves(current_board, legal_moves_list[i], current_chess)
        playout_count = 0
        while playout_count < MAX_PLAYOUT:
            result = make_a_random_play(current_board)
            if result[0] == DRAW:
                resultRate[i] += 0.1
            elif result[1] == current_chess:
                resultRate[i] += 0.2
            elif result[1] != current_chess:
                resultRate[i] -= 0.1
            playout_count += 1
        make_moves(current_board, legal_moves_list[i], ' ')

    index = resultRate.index(max(resultRate))
    make_moves(board_status, legal_moves_list[index], current_chess)


def switch_case(i):
    return {
        '1': (0, 0),
        '2': (0, 1),
        '3': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (2, 0),
        '8': (2, 1),
        '9': (2, 2)
    }.get(i, "Nothing")


def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("AI goes first\n")
    while judge(board, 'x', 'o')[0] == CONTINUE:
        make_random_playouts(board)
        if judge(board, 'x', 'o')[0] != CONTINUE:
            break
        print_board(board)
        print("It's your turn, choose from 1-9 to make a move")
        player_input = input()
        player_move = switch_case(player_input)
        while player_move == "Nothing":
            print("Invalid input! Please enter 1-9\nReenter:")
            player_input = input()
            player_move = switch_case(player_input)
        print(player_move[0], player_move[1])
        while board[player_move[0]][player_move[1]] != ' ':
            print("Invalid input, block already taken!\nReenter:")
            player_input = input()
            player_move = switch_case(player_input)
        make_moves(board, player_move, 'o')
        if judge(board, 'x', 'o')[0] != CONTINUE:
            break
        print_board(board)
        print("\n")
    print("Game Over!")
    print_board(board)
    if judge(board, 'x', 'o')[0] == DRAW:
        print("Draw")
    elif judge(board, 'x', 'o')[1] == 'x':
        print("AI Wins")
    elif judge(board, 'x', 'o')[1] == 'o':
        print("Player Wins")


if __name__ == '__main__':
    main()
