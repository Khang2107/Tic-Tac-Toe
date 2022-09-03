import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    # we want all players to get their next move
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):     # initialise superclass
        super().__init__(letter)    # call initialier in the superclass Player
        
    def get_move(self, game):
        # get a random valid spot that is empty for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):     # initialise superclass
        super().__init__(letter)    # call initialier in the superclass Player
        
    def get_move(self, game):
        valid_square = False    
        val = None  # user has not input value yet
        
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-9): ")
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it is not, then we say it is invalid
            try:
                val = int(square)   
                # raise error when they do not pass in int
                # raise if spot input not available
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True     # if it is successful
                
            except ValueError:
                print("Invalid square. Try again")
                
        return val