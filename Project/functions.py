import turtle
import copy
import os


SCOREFILE_RED =  'score_file_red.txt'
SCOREFILE_BLACK = 'score_file_black.txt'


def read_file_black(filename, player):
    ''' Function read_file
        Parameters: filename,a string
        Returns: points contained in file, an int
    '''
    if os.path.isfile(SCOREFILE_BLACK):
        try:
            # will read file and append number within to list score
            with open(filename, 'r') as infile:
                read_score = []
                lines = infile.readlines()
                for line in lines:
                    read_score.append(line)
                    player.score = read_score[0]
                    player.score = int(player.score)
                    player.score += 1
                    # score will display on terminal but not turtle
                    # this made it easier for me to test functions.
                    # the score will display for the winner UPON WINNING.
                    print('Black score :' ,player.score)
                    return player.score
        # if the file exists but there is an error ensures score will be 0
        # and program will keep running
        except OSError:
            print('sorry')
            #return player.score    
        
    else:
        player.score = 1
        return player.score


def read_file_red(filename, player):
    ''' Function read_file
        Parameters: filename,a string
        Returns: points contained in file, an int
    '''
    if os.path.isfile(SCOREFILE_RED):
        try:
            # will read file and append number within to list score
            with open(filename, 'r') as infile:
                read_score = []
                lines = infile.readlines()
                for line in lines:
                    read_score.append(line)
                    player.score = read_score[0]
                    player.score = int(player.score)
                    player.score += 1
                    print('Black score :', player.score)

                    return player.score
        # if the file exists but there is an error ensures score will be 0
        # and program will keep running
        except OSError:
            print('sorry')
        # score will default to 0 as per attribute and game can continue
        # with corrupt file score will = 0
        # score = 0
        # return score
    else:
        player.score = 1
        return player.score


def turtle_read_file_black(blackfile, redfile):
    if os.path.isfile(SCOREFILE_BLACK):
        try:
            # will read file and append number within to list score
            with open(blackfile, 'r') as infile:
                read_score = []
                lines = infile.readlines()
                for line in lines:
                    read_score.append(line)
                    black = read_score[0]
            
                
        except OSError:
            print('sorry')

        doit = turtle.Turtle()
        doit.penup()
        doit.setposition(70,150)
        doit.write('Black wins: ' + black, font=("Arial", 15, "bold"))
                    
    if os.path.isfile(SCOREFILE_RED):
         try:
            # will read file and append number within to list score
            with open(redfile, 'r') as infile:
                read_score = []
                lines = infile.readlines()
                for line in lines:
                    read_score.append(line)
                    red = read_score[0]
         except OSError:
            print('sorry')

         doit.setposition(70,130)
         doit.write('Reds wins: '+ red,font=("Arial", 15, "bold"))

