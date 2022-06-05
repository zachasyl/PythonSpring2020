''' CS5001
    Zachary Sylvane
    Spring 2020
    HW3 Programming #2 Test Sequence
    January 28, 2020
    
    (1) test functions print test values and expected result
    (2) main calls calls test functions, giving them the test parameters
'''
from nim_functions import coin_flip
from nim_functions import is_over

def coin_flip_test(integer, expected):
    '''Function: coin_flip)test
       Parameters: integer, expected -- all integers
       Returns: Nothing
       Does: integer and expected result. Also calls coin_flip
             for actual result, which is printed
    '''

    print('Testing inputs: ', integer,  'expecting result: ', expected  , '\n')
    coin_flip_test_result = coin_flip(integer)
    print('...actual result:', coin_flip_test_result,  '\n')



def is_over_test(bean_count, expected):
    ''' Function: is_over_test
        Parameters: bean_count and expected both integers
        Returns: Nothing
        Does: Prints bean_count expected result. Also
              is_over for actual result, which is printed,
    '''
    print('Testing inputs: ', bean_count, ' ', 'expecting result: ', expected  , '\n')

   
    is_over_test_result = is_over(bean_count)
    print('...actual result:', is_over_test_result,  '\n')
    '\n'
    ' \n'

def main():

    '''Function: main
       Parameters: none
       Returns: Nothing
       Does: calls coinfliptest and isovertest with test values and expected as parameters
    '''
    print('coin flip test beginning...\n')

    # Test one Coin Flip: integer, expected
    coin_flip_test(9, 'T')

    # Test two:
    coin_flip_test(0, 'H')

    #Test three:
    coin_flip_test(105, 'T')

    #test four:
    coin_flip_test(-500, 'H')

  

    print('\n \n \nis_over test beginning...\n')

  
    
    # Test one: bean_count and expected
    is_over_test(2, False)

    # Test two:
    is_over_test(50, False)

    #Test three:
    is_over_test(-1, True)

    #test four:
    is_over_test(0, True)

    


main()
