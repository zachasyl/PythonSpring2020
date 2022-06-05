''' CS5001
    Zachary Sylvane
    February 12, 2020
    HW5, Programming #2
    Test Suite
'''
'''
    (1) one test function prints test values and expected result
    (2) main calls calls test functions, giving them the test parameters
'''

from classify_functions import comparison

# new set of data for testing 
a = [['3', 'apples'], ['1', 'oranges'], ['1', 'mangos']]

b = [[ '1','cake'], ['1', 'cookies'], ['1', 'brownies']] 

c = [[ '1', 'carrots'], ['1', 'lettuce'], ['1', 'asparagus']]

x = ['i', 'like', 'eating', 'apples', 'and', 'mangos'] #4

y = ['i', 'like', 'cake', 'and', 'cookies', 'and', 'icecream'] #2

z = ['carrots', 'lettuce', 'and', 'asparagus', 'are', 'bad'] #3
    

def comparison_test(favorites, sentence, expected):
    '''Function: comparison_test
       Parameters: favorites: a list of favorite words and occurences of each word
                              (together, one element), strings;
                   x: sentences, each element is a word. string.
       Returns: matches between words in each list, a score.
     
    '''

    print('Testing inputs: ', favorites, ' ', sentence, ' ',  'expecting result: ', expected  , '\n')
    comparison_result = comparison(favorites, sentence)
    print('...actual result:', comparison_result,  '\n')

def main():

    '''Function: main
       Parameters: none
       Returns: Nothing
       Does: calls most_frequent_test with test values and expected as parameters
    '''
    print('most_frequent test starting...\n')

    # Test one: character, expected
    comparison_test(a,x, 4)
    # Test two:
    comparison_test(b,y, 2)
    #Test three:
    comparison_test(c,z, 3)

main()


