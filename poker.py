#
# File      : nguvy056_poker.py
# Author    : Van Khang Nguyen
# Email Id  : nguvy056@mymail.unisa.edu.au
# Description: Assignment 1 - Aa game of Dice Poker agains the computer
#              - A python program enables user to play with computer to roll dices and determine the winner by comparing the rank of each others
#              - Users can play as many games as they want
#              - Each player is dealt 5 playing carsds called a hand
#              - Each hand will be compared against other players to find the winning hand
#              - Each hand will then be ranked and the players with higher rank will win
# This is my own work as defined by the University's 
# Academic Misconduct Policy.
#

import dice_poker
import random

# Stage 1 - Test to ensure that the file works properly
# player_hand = [2,3,4,5,6]
# print("Player's hand: ")
# dice.display_hand(player_hand)

# dealer_hand = [2,3,4,5,6]
# print("Player's hand: ")
# dice.display_hand(dealer_hand)


# Assign variables
again = "y"                             # variable to store user's replay decisions
count_games = 0                         # variable to store how many games user plays
won = 0                                 # variable to store how many won games
lost = 0                                # variable to store how many lost games
drawn = 0                               # variable to store how many drawn games
player_stats = [0,0,0,0,0,0,0]          # list to store player’s hands dealt stats

# Function display_details() to display your details to the screen
def display_details():
    print()
    print("File     : nguvy056_poker.py")
    print("Author   : Van Khang Nguyen")
    print("Email Id : nguvy056@mymail.unisa.edu.au")
    print("This is my own work as defined by the University's")
    print("Academic Misconduct policy.")
    print()

# Function roll_die() to simulate the rolling of 1 die
def roll_die():
    random_number = random.randint(1,6)         # generate random number
    return random_number

# Function deal_hand() to return a list contains randomly generated numbers
def deal_hand(max_dice):
    hand = []                                   # list to store the player's hand
    for index in range(1,max_dice):
        random_number = roll_die()
        hand.append(random_number)              # add random_number to the list hand
    return hand

# Function rank_hand() to determine the rank of hand based on combination of dice values in the list
def rank_hand(hand):
    
    die_count = [0,0,0,0,0,0,0]                 # list to hold how many times each die face value was rolled in
    for index in range (len(hand)):
        die_value = hand[index]
        die_count[die_value] += 1 

    # determine the rank based on the cards       
    if 5 in die_count:
        rank = 6
    elif 4 in die_count:
        rank = 5
    elif 3 in die_count and 2 in die_count:
        rank = 4
    elif 3 in die_count:
        rank = 3
    elif die_count.count(2) == 2:
        rank = 2
    elif 2 in die_count:
        rank = 1
    else:
        rank = 0
        
    return rank

# Function display_rank() display the rank name based on the rank number
def display_rank(rank):
        
    if rank == 6:
        rname = "Five of a kind"
    elif rank == 5:
        rname = "Four of a kind"
    elif rank == 4:
        rname = "Full house"
    elif rank == 3:
        rname = "Three of a kind"
    elif rank == 2:
        rname = "Two pairs"
    elif rank == 1:
        rname = "One pair"
    elif rank == 0:
        rname = "Nothing special"
    
    print(rname)

# Display the details at the start
display_details()

# Ask if player would like to start the game:
start = input("Would you like to play dice poker [y|n]? ")

# Ask user to enter correct input
while start != "y" and start != "n":
    print("Please enter either 'y' or 'n'.\n")
    start = input("Would you like to play dice poker [y|n]? ")

print()
# User does not start
if start == "n":
    print("\nNo worries... another time perhaps... :)")

# User starts to play
else:
    while again == "y":
        count_games += 1

        # Stage 2 - Display the player’s hand
        player_hand = []
        player_hand = deal_hand(6)
        
        print("\nPlayer's hand:")
        dice.display_hand(player_hand)

        print()
        # Display the dealer's hand
        dealer_hand = []
        dealer_hand = deal_hand(6)

        print("\nDealer's hand:")
        dice.display_hand(dealer_hand)

        # Display the rank of player
        player_rank = rank_hand(player_hand)
        print("\n-- Player has ", end = '')
        display_rank(player_rank)
        
        # Display the rank of dealer
        dealer_rank = rank_hand(dealer_hand)
        print("-- Dealer has ", end = '')
        display_rank(dealer_rank)        

        print()
        # Stage 7 - Determine whether the player wins, loses, or draws
        if player_rank > dealer_rank:
            print("** Player wins! **\n")
            won += 1
        elif player_rank < dealer_rank:
            print("** Dealer wins! **\n")
            lost += 1
        else:
            print("** Draw! **\n")
            drawn += 1

        # Update Rank frequency
        player_stats[player_rank] += 1

        # Ask if player wants to replay or not
        again = input('\nPlay again [y|n]? ')

        # Invalid option when user enters to play again
        while again != "n" and again != "y":
            print("Please enter either 'y' or 'n'.\n")
            again = input('\nPlay again [y|n]? ')

    # Display game summary    
    else:
        print("\n\nGame Summary")
        print(len("Game Summary") * "=")
        print("You played", count_games, "games")
        print("  |--> Games won:    ", won)
        print("  |--> Games lost:   ", lost)
        print("  |--> Games drawn:  ", drawn)
        print("\n  Hand Stats: ")
        print("  -----------")
        
        index = 0                       # Add variable to look through numbers in list die_count
        # Print out the player statistics
        while index < len(player_stats):
            if index == 6:
                player_rname = "  Five of a kind:    "
            elif index == 5:
                player_rname = "  Four of a kind:    "
            elif index == 4:
                player_rname = "  Full house:        "
            elif index == 3:
                player_rname = "  Three of a kind:   "
            elif index == 2:
                player_rname = "  Two pairs:         "
            elif index == 1:
                player_rname = "  One pair:          "
            elif index == 0:
                player_rname = "  Nothing special:   "

            # Display the frequency to the screen
            star = ""
            frequency = 0
            while frequency < player_stats[index]:
                star += "* "
                frequency += 1
            print(player_rname, star)
            index += 1

        print("\nThanks for playing!\n")