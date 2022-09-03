class TicTacToe:
    def __init__(self):
        self.board = [' 'for _ in range(9)] # we use a single list to rep 3x3 board
        self.current_winner = None  # keep track of winner
        
    def print_board(self):
        # this only gets the rows
        for row in [self.board[ i*3: (i+1)*3] for i in range(3)]:   # [i*3 to (i+1)* 3]
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tell us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def avaiable_move(self):    # return empty spots
        # moves = []
        # for (i, spot) in enumerate(self.board):    
        # # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':     # if spot is blank
        #         moves.append(i)
        # return moves
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
    
    def empty_squares(self):    # check if there is any square
        return ' ' in self.board    # return boolean
    
    def num_empty_squares(self):
        # return len(self.available_moves())  # count how many empty spots
        return self.board.count(' ')    # count number of spaces in the board
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return move. if invalid, return false
        if self.board[square] == ' ':   # if nothing is there
            self.board[square] = letter
            return True
        return False
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_boards_nums() # tell us which number corresponds to which box
        
    letter = 'X'    # set a starting number
    # iterate while the game still has empty squares
    # we do not worry about the winner because we will just return that
    # which breaks the loop
    while game.empty_squares:
        # get the move from appropriate player
        if letter == "0":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        

