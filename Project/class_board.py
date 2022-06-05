import turtle
import copy
from functions import *

SCOREFILE_RED =  'score_file_red.txt'
SCOREFILE_BLACK = 'score_file_black.txt'


class Board:
    ''' Class: Board
        Attributes: board, turn, over
        Methods: winner, win_conditions
    '''
    def __init__(self):
        '''
        Constructor -- creates an new instance of a board
        Parameters:
           self -- the current object
        '''
        self.board = []
        self.turn = 1
        # board object will be true when game is over
        self.over = False

    def winner(self, player):
       '''
       Method -- announces the winner and writes amount of wins
                 player has to txt file (also reads txt file to
                 update past win count)
       Parameters:
           self -- the current object
           player -- PLAYER_1 OR PLAYER_2, ONE OF TWO PLAYER() OBJECTS!
       '''
       if player.color == 'Black':
            # will call read_fie_black to read file
            # and write score from file plus one
            player.score = read_file_black(SCOREFILE_BLACK, player)
            try:
                with open(SCOREFILE_BLACK, 'w') as outfile:
                    outfile.write(str(player.score))

            except OSError:
                print('Sorry for the inconvinience. score cannot be written')

       if player.color == 'Red':
            player.score = read_file_red(SCOREFILE_RED, player)
            try:
                with open(SCOREFILE_RED, 'w') as outfile:
                    #if player.score != None:
                    outfile.write(str(player.score))
                   

            except OSError:
                print('Sorry for the inconvinience. score cannot be written')

        
    def win_conditions(self, board, player):
        '''
        Method -- checks five win conditions: vertical win, horizontal win,
                 diag pos, diag neg, and tie(full board),
                    
        Parameters:
           self -- the current object
           board -- a list that represents each slot on the board,
                    left to right, top to bottom
           player -- PLAYER_1 OR PLAYER_2, ONE OF TWO PLAYER() OBJECTS!
        Returns nothing
        '''
        
        four_counter_horizontal = 0
        four_counter_vertical = 0

        verticals = []
        verticals_grid = []

        diagonals = []
        diagonals_grid = []

        # does not check for win donctions until after the first 6 turns
        # since cant be four in a row yet
        if self.turn > 6: 
            # horizontals. Uses counters and resets counter to 0 when same color is not in a row
            # to avoid combining multiple sequences 
            for i in range(len(board)):
                for j in range(len(board[i])):
                    
                    if j > 0 and board[i][j] == board[i][j-1] and board[i][j] == player.color  :
                        four_counter_horizontal += 1
                    else:
                        four_counter_horizontal = 0

                    if four_counter_horizontal ==3:
                        four_counter_horizontal = 0
                        print(player.color, 'at hori win')
                        self.over = True
                        # uses player as a parameter in the winner method
                        # so that winner method can write/ read files
                        self.winner(player)
                        turtle.setposition(100,-200)
                        turtle.penup()
                        turtle.write(player.color + ' is the winner!', font=("Arial", 25, "bold"))
                        break

            # pos slope diags. Instead of using counters, it checks if four in a row
            # are diags in the conditional itself
            
            for i in range(len(board)):
                for j in range(len(board[i])):
                    
                    
                    if i  < 6 - 3  and j < 7 - 3 and board[i][j] == board[i+1][j+1] == \
                       board[i+2][j+2] == board[i+3][j+3] and board[i][j] == player.color:

                        print(player.color, ' wins')
                        self.winner(player)
                        turtle.setposition(100,170)
                        turtle.penup()
                        turtle.write(player.color + 'wins', font=("Arial", 15, "bold"))

                        self.over = True
            # neg slope diags
            for i in range(len(board)):
                for j in range(len(board[i])):
                    
                    
                    if i  < 6 - 3  and j < 7 + 3 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] \
                       == board[i+3][j-3] and board[i][j] == player.color:

                        print(player.color, ' wins')
                        self.winner(player)
                        turtle.setposition(100,170)
                        turtle.write(player.color + 'wins', font=("Arial", 15, "bold"))

                        self.over = True
            # vertical check
            loop = 0
            v = 0
            # converts board list to new list verticals
            # the rearranged verticals can be used by the horizontal algotithim to find verticals
            # this was my initial strategy but I couldn't get it to work for diagonals
            while loop <= 6:
                for item in board:
                    verticals.append(item[v])
                loop += 1
                v+=1
                verticals_grid.append(verticals)
                verticals = []
            # the horizontal algo, used on the new verticals list
            for i in range(len(verticals_grid)):
                for j in range(len(verticals_grid[i])):
                    
                    if j > 0 and verticals_grid[i][j] == verticals_grid[i][j-1] and \
                       verticals_grid[i][j] == player.color  :
                        
                        four_counter_vertical += 1
                    else:
                        four_counter_vertical = 0

                    if four_counter_vertical ==3:
                        four_counter_vertical = 0
                        print(player.color, 'at verti win')
                        self.over = True
                        turtle.setposition(100,170)
                        self.winner(player)
                        turtle.write(player.color + 'wins', font=("Arial", 15, "bold"))

                        break

            # on turn 43 if none of the above conditions occur, the game must be tied
            # this should work for a board of any dimensions since it works via width * lenth
            # +1 because we start at turn 1 not 0
            if self.turn == (len(board) * len(board[0])) +1:
                print(len(board) * len(board[0]))
                print('tie game')
                turtle.setposition(100,170)
                turtle.penup()
                turtle.write('Tie Game', font=("Arial", 15, "bold"))

                
