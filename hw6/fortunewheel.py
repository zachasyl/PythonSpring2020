''' CS5001
    Zachary Sylvane
    February 25, 2020
    HW6
'''
from fwfunctions import *
import os.path

def main():
    username = input('Enter your username to login\n')
    filename = username + '.txt'
    # if filename exists, wins is equal to the number preserved
    # in filename.txt. if file doesnt exist, player has never won
    if os.path.isfile(filename):
        wins = read_file(filename)
        print('you have', wins, 'wins')
    else:
        wins = 0
        print('you have 0 wins\n')
    # chooses the wof sentence and prints its category
    chosen_sentence = random_sentence(filename)
    blanks_tuple = sentence_to_blanks(chosen_sentence, filename)
    # this list contains every character  as an element
    # used to see if players guesses should be updated to blanks
    blanks_compare = blanks_tuple[1] 
    # this list will display blanks that are updated as the player guesses
    blanks = blanks_tuple[0]
    guesses_left = 5   
    # menu screen loop
    while guesses_left > 0:
        choice = input('what would you like to do? '\
                       'G -- Guess letter or S-- Solve \n').upper()
        if choice == 'G':
            guess_please(filename, blanks, blanks_compare, \
            chosen_sentence, guesses_left)
            guesses_left -=1
        if choice == 'S':
            solve_puzzle(chosen_sentence, filename)
            break
main()
