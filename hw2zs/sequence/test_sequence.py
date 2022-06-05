''' CS5001
    Zachary Sylvane
    Spring 2020
    HW2 Programming #1 Test Sequence
    January 21, 2020
    
    (1) two test functions print test values and expected result
    (2) main calls calls test functions, giving them the test parameters
'''
from sequence import kth_term
from sequence import arith_sum

def kth_test(initial, diff, k, expected):
    '''Function: kth_test
       Parameters: initial value, common difference, k, expected -- all integers
       Returns: Nothing
       Does: Prints initial, diff, k, and expected result. Also
             calls kth_term for actual result, which is printed,
    '''

    print('Testing inputs: ', initial, ' ', diff, ' ',k , 'expecting result: ', expected  , '\n')
    kth_term_result = kth_term(initial, diff,  k)
    print('...actual result:', kth_term_result,  '\n')



def arith_test(initial, diff, n, expected):
    '''Function: arith_test
        Parameters: initial value, common difference, n, expected -- all integers
        Returns: Nothing
        Does: Prints initial, diff, n, and expected result. Also
              calls arith_sum for actual result, which is printed,
    '''
    print('Testing inputs: ', initial, ' ', diff, ' ',n , 'expecting result: ', expected  , '\n')

    # we do not want arith_sum to output a float because of integer division
    # arith_sum_result = int(arith_sum(initial, diff,  n)) this should be
    # changed in the actual function though.
    arith_sum_result = (arith_sum(initial, diff,  n)) 
    print('...actual result:', arith_sum_result,  '\n')
    '\n'
    ' \n'

def main():

    '''Function: main
       Parameters: none
       Returns: Nothing
       Does: calls kth_ test and arith_sum with test values and expected as parameters
    '''
    print('Kth term  test beginning...\n')

    # Test one: initial, diff, k, expected
    kth_test(1,1,10, 10)

    # Test two:
    kth_test(-10,1,10, -1)

    #Test three:
    kth_test(-10,2,-10, -32)

    #test four:
    kth_test(0,0, 0, 0)

    #Test five: 
    kth_test(3 ,-55,-33, 1873)

    print('\n \n \nArithsum test beginning...\n')

    # NOTE THAT THE EXPECTED AND ACTUAL WILL DIFFER
    # THE EXPECTED WILL BE AN INTEGER AND THE ACTUAL WILL BE A FLOAT
    # I PUT THE EXPECTED AS AN INTEGER BECAUSE THE COMMENTS IN
    # SEQUENCE.PY SAY SEQUENCE.PY SHOULD RETURN AN INTEGER BUT SEQUENCE.PY ACTUALLY RETURNS A FLOAT
    # BECAUSE OF DIVISION /
    
    # Test one initial, diff, n, expected: 
    arith_test(1,1,10, 55)

    # Test two:
    arith_test(-10,1,10, -55)

    #Test three:
    arith_test(-10,2,-10, 210)

    #test four:
    arith_test(0,0, 0, 0)

    #Test five: 
    arith_test(3,-55,-33, -30954)


main()

