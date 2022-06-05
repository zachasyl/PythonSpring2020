''' CS5001
    Zachary Sylvane
    January 21, 2020
    HW2 2, Programming #2
'''

def get_digit(number, power):
    ''' Function: get_digit
        Parameters: number and power -- int
        Return: a single digit of any number, integer
        Does: excises a single digit of any number utilizing 10^
    '''
    # If the number is negative, it does not matter in
    # regards to excising a single digit so we can treat as positive
    if number < 0:
       number = number * -1
       
    place = 10 ** power
    one_place_higher = place * 10

    remainder = number % one_place_higher

    if  power < 0:
        # not calculating for non integers
        return('none')
    
    else:
        # the remainder of number is divided by 10**power
        digit = ((number % one_place_higher) / place )
        return int(digit)
    
