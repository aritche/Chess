import numpy as np

BLACK = {
    'PAWN':   1,
    'ROOK':   2,
    'KNIGHT': 3,
    'BISHOP': 4,
    'QUEEN':  5,
    'KING':   6
}

WHITE = {
    'PAWN':   7,
    'ROOK':   8,
    'KNIGHT': 9,
    'BISHOP': 10,
    'QUEEN':  11,
    'KING':   12
}

#NUM_TO_CHAR = ['.','BP','BR','BKn','BB','BQ','BKi','WP','WR','WKn','WB','WQ','WKi']
NUM_TO_CHAR = ['.','♟︎','♜','♞','♝','♛','♚','♙','♖','♘','♗','♕','♔']

def getPlayer(piece):
    if piece in BLACK:
        return 'black'
    elif piece in WHITE:
        return 'white'
    else:
        return 'none'

def validMoves(piece, curr_row, curr_col, board):
    moves = []
    if piece == WHITE['PAWN']:
        if curr_row < 7:
            # Empty space in front
            if board[curr_row+1][curr_col] == 0:
                moves.append([curr_row+1, curr_col])

            # Empty spaces 2 ahead, and still in start row
            if curr_row == 1 and board[curr_row+1][curr_col] == 0 and board[curr_row+2][curr_col] == 0:
                moves.append([curr_row+2, curr_col])

            # Enemy piece diagonal
            # Cannot take king
            if curr_col > 0 and board[curr_row+1][curr_col-1] != 0 and getPlayer(board[curr_row+1][curr_col-1]) != getPlayer(piece) and board[curr_row+1][curr_col-1] != BLACK['KING'] and board[curr_row+1][curr_col-1] != WHITE['KING']:
                moves.append([curr_row+1, curr_col-1])
            if curr_col < 7 and board[curr_row+1][curr_col+1] != 0 and getPlayer(board[curr_row+1][curr_col+1]) != getPlayer(piece) and board[curr_row+1][curr_col+1] != BLACK['KING'] and board[curr_row+1][curr_col+1] != WHITE['KING']:
                moves.append([curr_row+1, curr_col+1])
    elif piece == BLACK['PAWN']:
        if curr_row > 0:
            # Empty space in front
            if board[curr_row-1][curr_col] == 0:
                moves.append([curr_row-1, curr_col])

            # Empty spaces 2 ahead, and still in start row
            if curr_row == 6 and board[curr_row-1][curr_col] == 0 and board[curr_row-2][curr_col] == 0:
                moves.append([curr_row-2, curr_col])

            # Enemy piece diagonal
            if curr_col > 0 and board[curr_row-1][curr_col-1] != 0 and getPlayer(board[curr_row-1][curr_col-1]) != getPlayer(piece) and board[curr_row-1][curr_col-1] != BLACK['KING'] and board[curr_row-1][curr_col-1] != WHITE['KING']:
                moves.append([curr_row-1, curr_col-1])
            if curr_col < 7 and board[curr_row-1][curr_col+1] != 0 and getPlayer(board[curr_row-1][curr_col+1]) != getPlayer(piece) and board[curr_row-1][curr_col+1] != BLACK['KING'] and board[curr_row-1][curr_col+1] != WHITE['KING']:
                moves.append([curr_row-1, curr_col+1])
    elif piece == BLACK['ROOK'] or piece == WHITE['ROOK']:
        # move up/down all rows
        row = curr_row+1
        while row < 8 and board[row][curr_col] == 0:
            moves.append([row, curr_col])
            row += 1
        if row < 8:
            if getPlayer(board[row][curr_col]) != getPlayer(piece):
                moves.append([row, curr_col])

        row = curr_row-1
        while row > 0 and board[row][curr_col] == 0:
            moves.append([row, curr_col])
            row -= 1
        if row >= 0:
            if getPlayer(board[row][curr_col]) != getPlayer(piece):
                moves.append([row, curr_col])

        # move across all columns
        col = curr_col+1
        while col < 8 and board[curr_row][col] == 0:
            moves.append([curr_row, col])
            col += 1
        if col < 8:
            if getPlayer(board[curr_row][col]) != getPlayer(piece):
                moves.append([curr_row, col])

        col = curr_col-1
        while col > 0 and board[curr_row][col] == 0:
            moves.append([curr_row, col])
            col -= 1
        if col >= 0:
            if getPlayer(board[curr_row][col]) != getPlayer(piece):
                moves.append([curr_row, col])
    elif piece == BLACK['KNIGHT'] or piece == WHITE['KNIGHT']:
        row, col = curr_row, curr_col

        # row+1, col+2
        if (row+1)<8 and (col+2)<8 and (getPlayer(board[row+1][col+2]) != getPlayer(piece) or board[row+1][col+2] == 0):
            moves.append([row+1, col+2])
            
        # row+1, col-2
        if (row+1)<8 and (col-2)>=0 and (getPlayer(board[row+1][col-2]) != getPlayer(piece) or board[row+1][col-2] == 0):
            moves.append([row+1, col-2])

        # row-1, col+2
        if (row-1)>=0 and (col+2)<8 and (getPlayer(board[row-1][col+2]) != getPlayer(piece) or board[row-1][col+2] == 0):
            moves.append([row-1, col+2])

        # row-1, col-2
        if (row-1)>=0 and (col-2)>=0 and (getPlayer(board[row-1][col-2]) != getPlayer(piece) or board[row-1][col-2] == 0):
            moves.append([row-1, col-2])

        # row+2, col+1
        if (row+2)<8 and (col+1)<8 and (getPlayer(board[row+2][col+1]) != getPlayer(piece) or board[row+2][col+1] == 0):
            moves.append([row+2, col+1])

        # row+2, col-1
        if (row+2)<8 and (col-1)>=0 and (getPlayer(board[row+2][col-1]) != getPlayer(piece) or board[row+2][col-1] == 0):
            moves.append([row+2, col-1])

        # row-2, col+1
        if (row-2)>=0 and (col+1)<8 and (getPlayer(board[row-2][col+1]) != getPlayer(piece) or board[row-2][col+1] == 0):
            moves.append([row-2, col+1])

        # row-2, col-1
        if (row-2)>=0 and (col-1)>=0 and (getPlayer(board[row-2][col-1]) != getPlayer(piece) or board[row-2][col-1] == 0):
            moves.append([row-2, col-1])

    elif piece == BLACK['BISHOP'] or piece == WHITE['BISHOP']:
        row, col = curr_row+1, curr_col+1
        while row < 8 and col < 8:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row+1, col+1

        row, col = curr_row-1, curr_col-1
        while row >= 0 and col >= 0:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row-1, col-1

        row, col = curr_row+1, curr_col-1
        while row < 8 and col >= 0:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row+1, col-1
            
        row, col = curr_row-1, curr_col+1
        while row >= 0 and col < 8:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row-1, col+1

    elif piece == BLACK['QUEEN'] or piece == WHITE['QUEEN']:
        row, col = curr_row+1, curr_col+1
        while row < 8 and col < 8:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row+1, col+1

        row, col = curr_row-1, curr_col-1
        while row >= 0 and col >= 0:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row-1, col-1

        row, col = curr_row+1, curr_col-1
        while row < 8 and col >= 0:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row+1, col-1
            
        row, col = curr_row-1, curr_col+1
        while row >= 0 and col < 8:
            if board[row][col] != 0:
                if getPlayer(board[row][col]) != getPlayer(piece):
                    moves.append([row, col])
                break
            moves.append([row,col])
            row, col = row-1, col+1

        # move up/down all rows
        row = curr_row+1
        while row < 8 and board[row][curr_col] == 0:
            moves.append([row, curr_col])
            row += 1
        if row < 8:
            if getPlayer(board[row][curr_col]) != getPlayer(piece):
                moves.append([row, curr_col])

        row = curr_row-1
        while row > 0 and board[row][curr_col] == 0:
            moves.append([row, curr_col])
            row -= 1
        if row >= 0:
            if getPlayer(board[row][curr_col]) != getPlayer(piece):
                moves.append([row, curr_col])

        # move across all columns
        col = curr_col+1
        while col < 8 and board[curr_row][col] == 0:
            moves.append([curr_row, col])
            col += 1
        if col < 8:
            if getPlayer(board[curr_row][col]) != getPlayer(piece):
                moves.append([curr_row, col])

        col = curr_col-1
        while col > 0 and board[curr_row][col] == 0:
            moves.append([curr_row, col])
            col -= 1
        if col >= 0:
            if getPlayer(board[curr_row][col]) != getPlayer(piece):
                moves.append([curr_row, col])

    elif piece == BLACK['KING'] or piece == WHITE['KING']:
        for row in [-1,0,1]:
            for col in[-1,0,1]:
                if not (row == 0 and col == 0) and curr_row+row < 8 and curr_col+col < 8 and curr_row+row >= 0 and curr_col+col >= 0:
                    if board[curr_row+row][curr_col+col] == 0 or getPlayer(board[curr_row+row][curr_col+col]) != getPlayer(piece):
                        moves.append([curr_row+row,curr_col+col])


    final_moves = []
    for row, col in moves:
        # Cannot take a king
        if board[row][col] == WHITE['KING'] or board[row][col] == BLACK['KING']:
            continue

        # Cannot move a king within range of another king
        if (piece == WHITE['KING'] or piece == BLACK['KING']):
            for row_offset in [-1,0,1]:
                for col_offset in [-1,0,1]:
                    if not (row_offset == 0 and col_offset == 0) and row+row_offset < 8 and col+col_offset < 8 and row+row_offset >= 0 and col+col_offset >= 0:
                        if board[row+row_offset][col+col_offset] == WHITE['KING'] or board[row+row_offset][col+col_offset] == BLACK['KING']:
                            continue
                
        final_moves.append([row,col])


    
    return final_moves
    

class Board:
    def __init__(self):
        self.board = np.zeros((8,8))

        self.board[-1,:] = np.array([BLACK['ROOK'], 
                                     BLACK['KNIGHT'], 
                                     BLACK['BISHOP'], 
                                     BLACK['QUEEN'],
                                     BLACK['KING'],
                                     BLACK['BISHOP'],
                                     BLACK['KNIGHT'],
                                     BLACK['ROOK']])
        self.board[-2,:] = np.array([BLACK['PAWN'], 
                                     BLACK['PAWN'], 
                                     BLACK['PAWN'], 
                                     BLACK['PAWN'],
                                     BLACK['PAWN'],
                                     BLACK['PAWN'],
                                     BLACK['PAWN'],
                                     BLACK['PAWN']])
        self.board[0,:] = np.array([WHITE['ROOK'], 
                                     WHITE['KNIGHT'], 
                                     WHITE['BISHOP'], 
                                     WHITE['QUEEN'],
                                     WHITE['KING'],
                                     WHITE['BISHOP'],
                                     WHITE['KNIGHT'],
                                     WHITE['ROOK']])
        self.board[1,:] = np.array([WHITE['PAWN'], 
                                     WHITE['PAWN'], 
                                     WHITE['PAWN'], 
                                     WHITE['PAWN'],
                                     WHITE['PAWN'],
                                     WHITE['PAWN'],
                                     WHITE['PAWN'],
                                     WHITE['PAWN']])


    # Given a col (A-H, row 1-8), move the specified piece to this spot 
    def moveTo(curr_col, curr_row, new_col, new_row):
        self.board[new_row, new_col] = self.board[curr_row, curr_col]
        self.board[curr_row, curr_col] = 0

    def getState(self):
        return self.board

    def printBoard(self):
        for row in range(len(self.board)):
            print(str(row) + ' |', end='\t')
            for col in range(len(self.board[row])):
                print(NUM_TO_CHAR[int(self.board[row][col])], end='\t')
            print('\n-----------------------------------------------------------------')
        print('\tA\tB\tC\tD\tE\tF\tG\tH')

class Game:
    def __init__(self):
        pass
    
    def isOver(turn, board):
        # Game is over if no valid moves for king, and no moves by other pieces remove check

        # Find white king
        found = False
        for row in range(8):
            for col in range(8):
                if turn == 0:
                    if board[row][col] == WHITE['KING']:
                        found = True
                        break
                else:
                    if board[row][col] == BLACK['KING']:
                        found = True
                        break
            if found == True:
                break
                
        # Checkmate if no valid moves for king
        if len(validMoves(curr_state[row][col])) == 0:
            return True
        else:
            return False
        

    def proposeMove(turn, curr_col, curr_row, new_col, new_row):
        pass
        # Can only move if one of your OWN pieces exists at [curr_col, curr_row]

        # Can only move if new_col, new_row is a valid position for your piece

        # Can NOT move if moving the piece results in check

        # Can NOT move if you are currently in check and moving the piece does NOT remove check

        # King cannot move within range of another king



b = Board()
curr_state = b.getState()
#g = Game()

turn = 0
while not g.isOver(b.getState()):
    while g.proposeMove(turn, 0, 2, 0, 3) == False:
        print('proposing new move...')
    turn = (turn+1)%2
#b.printBoard()
#for row in [6,7]:
#    for col in range(8):
#        moves = validMoves(curr_state[row][col], row, col, curr_state)
#        for move in moves:
#            print(move)
