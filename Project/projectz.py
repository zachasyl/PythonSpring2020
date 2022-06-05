'''
CS5001 
Spring 2020
Zachary Sylvane
Project
April 8, 2020
'''


import turtle
import copy
from class_board import *
from class_player import *
from functions import *

BLACKFILE = 'score_file_black.txt'
REDFILE = 'score_file_red.txt'

def main():


    def column_clicked(col1_x,col1_y):
        '''
        Function column_clicked
        Parameters: col1_x and col1_y, ints
        Returns: none
        Does: detects the chosen column and
              passes it to turn_switcher as parameter
        '''

        # clear  method of turnrs object (turtle)
        # prevents score from overlappying by clearing after each click
        turns.clear()

        # if the game is over(True), clicking is disabled.
        if game_board.over == False:
             
            chosen_column = 0
            print('turn: ', game_board.turn)
            turns.penup()
            turns.write(game_board.turn, font=("Arial", 15, "bold"))
            


            # for whichever column is clicked
            # turn switcher is triggered for that column
            if col1_x < -290:
                 chosen_column = chosen_column
                 turn_switcher(chosen_column)

            elif col1_x < -240 :
                 chosen_column +=1
                 turn_switcher(chosen_column)

            elif col1_x < -190 :
                 chosen_column +=2
                 turn_switcher(chosen_column)

            elif col1_x < -140 :
                 chosen_column +=3
                 turn_switcher(chosen_column)

            elif col1_x < -90 :
                 chosen_column +=4
                 turn_switcher(chosen_column)

            elif col1_x < -40 :
                 chosen_column +=5
                 turn_switcher(chosen_column)

            elif col1_x < 10 :
                 chosen_column +=6
                 turn_switcher(chosen_column)
                 
            game_board.turn +=1

    def turn_switcher(chosen_column):
        '''
        Function turn_switcher
        Parameters: chosen_column, int
        Returns: none
        Does: if the turn is even, player ones turn 
              if the turn is odd, player twos turn.
              
        '''
        if game_board.turn % 2 !=0:
            # this is triggered on player 1 turn AFTER player 1 makes a click
            # (after which everything is updated and it is player 2's turn).
            empty = player_1.turn_start(board, maximum, chosen_column, x_coordinates_rows, y_coordinates_rows)
            
            player = player_1
            
            print('Player 1, Black')


        if game_board.turn % 2 == 0:
            empty = player_2.turn_start(board, maximum, chosen_column, x_coordinates_rows, y_coordinates_rows)
            
            player = player_2
            print('Player 2, Red')
        
        
        # after turn, updates board object w/ list containing last move
        game_board.board = board
        # after turn, checks win conditions for player that just moved and current board
        game_board.win_conditions(game_board.board, player)
        

    # initializing player objects and setting specific
    # color for player_2 different from class color
    player_1 = Player()
    player_2 = Player()
   
    player_2.color = 'Black'
    
    screen = turtle.Screen()
    screen.setup(800,565)
    screen.bgcolor('yellow')
    turtle.penup()
    x = -300
    y =170
    turtle.setposition(x,y)
    turtle.speed(10)


    
    column = []

    board = []
    menu = []
    x_coordinates= []
    y_coordinates = []

    x_coordinates_rows = []
    y_coordinates_rows = []

    # creates an 7x6 board filled with e for empty
    row_fill = 0
    while row_fill < 6:
        row = ['e','e','e','e','e','e', 'e']
        board.append(row)
        row_fill+=1

    # initial x coordinates that pair with empty spaces
    for i in range (len(board)):
        x = -300
        if i >0:
            y-=50
            x_coordinates_rows.append(x_coordinates)
                    
        # clears so we dont repeat taking rows we already took   
        x_coordinates = []
        y_coordinates = [] 
       
        turtle.setposition(x,y)

        
        for j in range (len(board[i])):

            x_coordinates.append(x)
            y_coordinates.append(y)

            if i == 0 and j == 6:
                x_coordinates_rows.append(x_coordinates)

            # note that the below code cannot go under the for i loop
            # because it would append an empty [] as the first sublist
            if j == 6:
                y_coordinates_rows.append(y_coordinates)
               
            turtle.setposition(x,y)
            turtle.dot(50, 'white')
            x+=50
            
    # creates board object
    game_board = Board()
    maximum = 5
    print('Player 1, Black')
    print('turn: ', game_board.turn)
    game_board.turn +=1
    col1_x = -300
    col1_y = 220

    # initializing turns to write turns on screen
    # needs to be done after making game_board object
    turns = turtle.Turtle()
    turns.setposition(125,170)
    turns.penup()
    # writes turn before column click
    turns.write(game_board.turn - 1, font=("Arial", 15, "bold"))
    turtle.setposition(70,170)
    turtle.write( 'Turn: ', font=("Arial", 15, "bold"))
    
    
    # sets 7 clickable circles one per each column
    # on click, the column_clicked function is triggered
    for c in range (7):
         c = turtle.Turtle()
         c.penup()
         c.speed(10)
         c.setposition(col1_x,col1_y)
         c.dot(50, 'gray')
         c.onclick(column_clicked)
         col1_x+=50

    # these turtle functions specifically read the file
    # for the sole purpose of printing wins on turtle screen
    turtle_read_file_black(BLACKFILE, REDFILE)


main()

    

