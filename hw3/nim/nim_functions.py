''' CS5001
    Zachary Sylvane
    January 25, 2020
    HW2 3, Programming #3
'''
import random


def ai(bean_count):
    ''' Function AI
        Parameters: bean_count, 1 integer, amount of beans
        Returns: the amount of beans AI will take, an integer 1-3
    '''
    AI_choice = 9
       # the AI will force the player to take the last bean when there are 3 or 2 beans left during its turn
       # otherwise, during the earlier parts of the game, the AI will select a choice randomly but legally
    if bean_count == 2:
        AI_choice = 1
        return AI_choice
    elif bean_count == 3:
        AI_choice = 2
        return AI_choice
    elif bean_count == 4:
        AI_choice = 3
        return AI_choice
    else:
        while AI_choice > bean_count:
            AI_choice = random.randint(1, 3)
            return AI_choice

def is_over(bean_count):
    ''' Function is_over
        Parameters: bean_count, 1 integer, amount of beans
        Returns: boolean, whether the game is over or not
    '''
    while bean_count > 0:
            game_over = False
            return game_over
    else:
        game_over = True
        return game_over


def coin_flip(integer):
    ''' Function coin_flip
        Parameters: any integer
        Returns: returns the string T or H
        Does: determines if integer is odd or even and returns T or H
    '''
    # even
    if integer % 2 == 0:
        return 'H'
    
    # odd
    else:
        return 'T'



def heads_or_tails(coin_guess):
    ''' Function heads_or_tails
        Parameters: coin_guess, a string 'h' or 't'
        Returns: boolean
        Does: determines if user(player_1) goes first or not
              by comparing the player's coin_guess with the actual result
              actual result is found by calling coin_flip.
    '''
    # can change to 1-100 or whatever since coin_clip is odd/even based
    # as long as same amt even and odd numbers

    result = coin_flip(random.randint(1, 2))

    # convert the string to boolean and print
    if result == 'H':
            heads = True
            tails = False
            print('its heads')
    else:
        heads = False
        tails = True
        print('its tails')


    if coin_guess == 'h' and heads == True:
        print('you go first. There are 8 beans')
        player_1 = True
        player_2 = False
        return player_1
            
            
    elif coin_guess == 't' and tails == True:
        print('you go first. There are 8 beans.')
        player_1 = True
        return player_1
    else:
        print('I am first. There are 8 beans.')
        player_1 = False
        player_2 = True
        return player_1
