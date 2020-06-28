"""
Tic-Tac-Toe Chess program:
1. make a list of all legal moves
2. for each of the moves it does some number of random playouts
3. During a random playout, the computer makes random moves for each player until a win, loss, or draw is reached.
4.
"""

'''
Chess class
class Chess(type, coordinate=None):
    type = {'X', 'O'}
    coordinate = None
'''





'''
Print a board with chess on it.
'''


def print_board(board):
    print("    a b c")
    for count, row in enumerate(board):
        print(count,' ', *row, ' ', sep='|' )

'''
Judge the current status
'''


def judge(current_status):
    print("test")

'''
Return a list of legal moves based on current status
'''


def return_legal_moves(board):
    print()

'''
Given a list of legal_moves, do simulation for each until game finished
'''
def make_random_playouts(legal_moves):
    """
    for each leagal_moves, make simulation until the game finished and return win or lose or draw
    :param legal_moves:
    :return:
    """
'''
Update board with chess
'''
def make_moves(board,coordinate):
    board[coordinate[0]][coordinate[1]] = 'x'


board = [['-','-','-'],['-','-','-'],['-','-','-']]
print_board(board)
coordinate = (0,0)

make_moves(board,coordinate)
print_board(board)