from functions import read_file_red
from class_player import Player
import unittest


# testing red since Player() defaults objects to red
def test_read_file_red(filename, player, expected):
    ''' Function: test_read_file_black
        Parameters: file name txt str, player object
        returns: score of player object, string
    '''
    
    actual = read_file_red(filename, player)
    print("Testing score with", filename, "and", player, "\n"
          "\t...Expected:", expected, "\n"
          "\t...Actual:", actual)

player_1 = Player()

try:
    with open('score_file_red.txt', 'r') as infile:
        read_score = []
        lines = infile.readlines()
        for line in lines:
            read_score.append(line)
            red = read_score[0]
            print(red)
except:
    ('error')

# note that the expected will be one less than the actual
# because the actual function will add one before writing
# since it is prompted upon winning. I dont want to alter the
# value / change its type im just trying to test reading here.

# the actual function returns an INTEGER. The test returns
# a string. The function takes the string (expected) makes it
# an int and adds one

test_read_file_red('score_file_red.txt', player_1, red)

