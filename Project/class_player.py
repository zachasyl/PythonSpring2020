import turtle
import copy

            

class Player:
    ''' Class: Player
        Attributes: color, turn, maximum, number, score
        Methods: turn_start
    '''

    def __init__(self, score = 0, turn = True, color = 'Red'):
        '''
        Constructor -- creates an new instance of a game
        Parameters:
           self -- the current object
           color -- the color of players pieces
           score -- how many wins player has
        '''
        self.color = color
        self.turn = turn
        self.score = score



    def turn_start(self, board, maximum, chosen_column, x_coordinates_rows, y_coordinates_rows):
        '''
        Method -- sets the coordinate position of a piece once player chooses a column
        Parameters:
           self -- the current object
           board -- list of spaces on board
           maximum -- amount of rows, int
           chosen_column -- int column
           x_cooridnate_rows -- list of all x coordinates, same size as / corresponding to board
           y_coordinate_rows -- list of all y coordinates, same size as / corresponding to board
        Returns nothing
        '''
        
        # if the 'bottom' row of the board is not empty
        while board[maximum][chosen_column] != 'e':
            if maximum == 0:
                # prevents error message if you put a checker in a column
                # that is already full. doing so 'passes' your turn
                break
            #decrease the bottom of the board by one (check to see if one row higher is empty)
            maximum-=1
        # if the max row is empty, make it the color of player on column click in the board list
        if board[maximum][chosen_column] == 'e':
            board[maximum][chosen_column] = self.color
            # then change turtle position to corresponding coordinates of the board list
            turtle.setposition(x_coordinates_rows[maximum][chosen_column],y_coordinates_rows[maximum][chosen_column])
            turtle.dot(50, self.color)

  


    # PLEASE NOTE THIS IS A REPLICA OF THE ABOVE METHOD BUT WITHOUT TURTLE
    # MY TEST FUNCTIONS USE THIS TO TEST board[maximum][chosen_column] = self.color
    # WITHOUT TURTLE ERRORS. THIS IS NOT ACTUALLY USED BY THE PROGRAM.
    # I ALSO TESTED BY COMMENTING OUT THE TURTLE CODE ABOVE TO ENSURE THE REST IS IDENTICAl.
    def copied_turn_start(self, board, maximum, chosen_column, x_coordinates_rows, y_coordinates_rows):
            '''
            Method -- sets the coordinate position of a piece once player chooses a column
            Parameters:
               self -- the current object
               board -- list of spaces on board
               maximum -- amount of rows, int
               chosen_column -- int column
               x_cooridnate_rows -- list of all x coordinates, same size as / corresponding to board
               y_coordinate_rows -- list of all y coordinates, same size as / corresponding to board
            Returns nothing
            '''
            
            # if the 'bottom' row of the board is not empty
            while board[maximum][chosen_column] != 'e':
                if maximum == 0:
                    # prevents error message if you put a checker in a column
                    # that is already full. doing so 'passes' your turn
                    break
                #decrease the bottom of the board by one (check to see if one row higher is empty)
                maximum-=1
            # if the max row is empty, make it the color of player on column click in the board list
            if board[maximum][chosen_column] == 'e':
                board[maximum][chosen_column] = self.color
                # then change turtle position to corresponding coordinates of the board list



    



