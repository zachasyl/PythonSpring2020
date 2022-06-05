''' CS5001
    Zachary Sylvane
    February 25, 2020
    HW6
'''
import random
import os.path
import sys

def read_file(filename):
    ''' Function read_file
        Parameters: filename,a string
        Returns: wins contained in file, a string
    '''
    try:
        with open(filename, 'r') as infile:
            read_wins = []
            lines = infile.readlines()
            for line in lines:
                read_wins.append(line)
                wins = int(read_wins[0])
                return wins
        
    except OSError:
        print('Error. sorry for the inconvinience')

def random_sentence(filename):
    ''' Function random_sentence
        Parameters: filename, a string
        Returns: chosen_sentence, a list
        Does: takes random chosen_sentence from file
              prints the category of chosen_sentence
    '''
    try:
        with open('wof.txt', 'r') as infile:
            sentences = []
            phrase = []
            categories = []
            
            lines = infile.readlines()
            
            for line in lines:
                start = line.index(":")
                question = line[start + 1:].upper()
                category_excised = line[:start].upper()
                sentences.append(question.split())
                categories.append(category_excised)
                
    except OSError:
        print('Error. Sorry for the inconvinience')
        sys.exit()
    num = random.randint(0, len(sentences) - 1)
    chosen_sentence = sentences[num]
    chosen_category = categories[num]
    print('the category is ' + chosen_category + '. You get 5 guesses.')
    return chosen_sentence

def sentence_to_blanks(chosen_sentence, filename):
    ''' Function sentence_to_blanks
        Parameters: chosen_sentence -list, filename - string
        Returns: a tuple containing two lists
        Does: Creates a list in which each element is
              one letter of the chosen_sentence.
              Creates a list of '_' that will be updated
              when the player guesses a letter
    '''
    blanks = []
    blanks_compare = []
    for i in range(len(chosen_sentence)):
        if i > 0:
            blanks_compare.append(' ')
            blanks.append(' ')
        for j in range(len(chosen_sentence[i])):
            blanks_compare.append(chosen_sentence[i][j])
            # characters that arent in the alphabet are appended
            # https://www.geeksforgeeks.org/python-string-isalpha-application/
            if chosen_sentence[i][j].isalpha():
                blanks.append('_')
            else:
                blanks.append(chosen_sentence[i][j])
    # calls show_the_board to print blanks
    show_the_board(blanks)
    return blanks, blanks_compare
        
def guess_please(filename, blanks, blanks_compare, chosen_sentence, \
                 guesses_left):
    ''' Function guess_please
        Parameters: filename str, blanks lst, blanks_compare lst,
                    chosen_sentence lst, guesses_left int.
        Returns: nothing
        Does: takes players guess and calls show_the_board to output
              an updated blanks w/ correct letters. Forces player
              to solve if out of guesses
    '''
    guess = input('what is your guess?\n').upper()
    for i in range(len(blanks)):
        if guess == blanks_compare[i]:
            blanks[i] = guess

    show_the_board(blanks)
    guesses_left-=1
    
    print('you have', guesses_left, 'guesses')
    if guesses_left == 0:
        solve_puzzle(chosen_sentence, filename)

def show_the_board(blanks):
    ''' Function show_the_board
        Parameters: blanks, a list
        Returns: nothing
        Does: updates/displays guessed letters and blanks
    '''
    print('\n')
    for i in range(len(blanks)):
        print(blanks[i], end = ' ')
    print('\n')

def solve_puzzle(chosen_sentence, filename):
    ''' Function solve_puzzle
        Parameters: chosen_sentence, filename, 
        Returns: nothing
        Does: compares players solve input with actual solution
    '''
    if os.path.isfile(filename):
        wins = read_file(filename)
    else:
        wins = 0

    solution = ''
    # creates a string, solution, from chosen sentence to compare with
    # player input for exact match
    for i in range(len(chosen_sentence)):
        # if/else avoids a space at the END of solution
        if i < len(chosen_sentence)-1:
            solution = solution + chosen_sentence[i] + ' '
        else:
            solution = solution + chosen_sentence[i]

    solve = input('SOLVE THE PUZZLE!\n').upper()
    
    if solve == solution:
        print('CORRECT! CONGRATULATIONS! ')
        wins += 1
        try:
            with open(filename, 'w') as outfile:
                b = []
                outfile.write(str(wins))
        except OSError:
            print('Error. Sorry for the inconvinience')
    else:
        print('Incorrect...You lose.', solution, 'was the correct answer.')
        
