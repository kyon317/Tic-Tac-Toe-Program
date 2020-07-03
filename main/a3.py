"""
Tic-Tac-Toe Chess program:
1. make a list of all legal moves
2. for each of the moves it does some number of random playouts
3. During a random playout, the computer makes random moves for each player until a win, loss, or draw is reached.
4.
"""
import random

'''
Chess
'''
chess = {1:'x',2:'o'}
x = 1
o = 2
'''
Chess
'''
states = {3:'Win',
          4:'Loss',
          5:'Draw',
          6:'Continue'}
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
        print(' ', *row, ' ', sep='|' )

'''
Place a chess on a given coordinate
'''
def make_moves(board, coordinate, chess):
    board[coordinate[0]][coordinate[1]] = chess

'''
Judge the current status, decide if a game is over
'''
def judge(board, chess1, chess2):
    # Check rows
    for j in range(len(board)):
        if board[j][0] != ' ':
            piece = board[j][0]
            if (board[j][1] == piece) and (board[j][2] == piece):
                return WIN, piece

    # Check columns
    for i in range(len(board[0])):
        if board[0][i] != ' ':
            piece = board[0][i]
            if (board[1][i] == piece) and (board[2][i] == piece):
                return WIN, piece

    # Check Diagonal Down
    if board[0][0] != ' ':
        piece = board[0][0]
        if (board[1][1] == piece) and (board[2][2] == piece):
            return WIN, piece

    # Check Diagonal Up
    if board[0][2] != ' ':
        piece = board[0][2]
        if (board[1][1] == piece) and (board[2][0] == piece):
            return WIN, piece

    # Check if board is full
    if len(return_legal_moves(board)) == 0:
        return DRAW, None
    else:
        chess1_counter = 0
        chess2_counter = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == chess1:
                    chess1_counter+=1
                if board[i][j] == chess2:
                    chess2_counter+=1
        if chess1_counter>chess2_counter:
            next_chess = chess2
        else:
            next_chess = chess1
        return CONTINUE, next_chess

'''
Return a list of legal moves based on current status
'''

def return_legal_moves(board):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                legal_moves.append([i,j])
    return legal_moves

'''
make one single simulation
'''

def make_a_random_play(current_board):
    dummy_board = current_board
    while judge(dummy_board, 'x', 'o')[0] == CONTINUE:
        legal_moves = return_legal_moves(dummy_board)
        index = random.randint(0,len(legal_moves)-1)
        dummy_move = legal_moves[index]
        next_chess = judge(dummy_board,'x','o')[1]
        make_moves(dummy_board,dummy_move,next_chess)
        dummy_board[dummy_move[0]][dummy_move[1]] = next_chess
    return judge(dummy_board, 'x', 'o')

'''
multiple simulations to find the best move that avoids losing
'''
def make_random_playouts(board, MAX_PLAYOUT=20000):
    """
    for each legal_moves, make simulation until the game finished and return win or lose or draw
    :param legal_moves:
    :return: coordinate of legal_move
    """
    current_chess = judge(board, 'x', 'o')[1]
    legal_moves_list = return_legal_moves(board)
    print("available moves: ",legal_moves_list)
    current_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(len(board)):
        for j in range(len(board)):
            current_board[i][j] = board[i][j]
    resultRate = [0]*len(legal_moves_list)

    for i in range(len(legal_moves_list)):
        make_moves(current_board,legal_moves_list[i],current_chess)
        playout_count = 0
        while playout_count<MAX_PLAYOUT:
            result = make_a_random_play(current_board)
            if result[0] == DRAW:
                resultRate[i] += 0.1
            elif result[1] == current_chess:
                resultRate[i] += 0
            elif result[1] != current_chess:
                resultRate[i] -= 0.1
            playout_count+=1

    index = resultRate.index(max(resultRate))
    print(index)
    print(legal_moves_list[index])
    print("win table: ", resultRate)
    make_moves(board, legal_moves_list[index], current_chess)

def switch_case(i):
    return {
        '0': (0, 0),
        '1': (0, 1),
        '2': (0, 2),
        '3': (1, 0),
        '4': (1, 1),
        '5': (1, 2),
        '6': (2, 0),
        '7': (2, 1),
        '8': (2, 2)
    }.get(i,"Nothing")

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print_board(board)
while judge(board, 'x', 'o')[0] == CONTINUE:
    print("It's your turn")
    player_input = input()
    player_move = switch_case(player_input)
    print(player_move[0],player_move[1])
    while board[player_move[0]][player_move[1]]!=' ':
        print("Invalid input, block already taken!\nReenter:")
        player_input = input()
        player_move = switch_case(player_input)
    make_moves(board, player_move, 'x')
    if judge(board, 'x', 'o')[0] != CONTINUE:
        break
    print_board(board)
    make_random_playouts(board)
    if judge(board, 'x', 'o')[0] != CONTINUE:
        break
    print_board(board)
print_board(board)