''' CS5001
    Zachary Sylvane
    January 27, 2020
    HW2= 3, Programming #3

'''
from sentence import select_sentence
from sentence import count_mismatches
from sentence import count_words
from typing_functions import calculate_wpm
from typing_functions import calculate_adjusted

import time


def main():
        time.perf_counter()
        # initializing now in case user types done immediately to end program, for instance
        wrong = 0
        ready = ''
        total_words = 0
        your_try = ''
        
        while ready != 'Y':
                ready = input('are you ready? Y/N \n').upper()

        while your_try != 'DONE':
                the_sentence = select_sentence()
                your_try = input(the_sentence + '\n')
                # need to exist loop early so that the amount
                # of mismatches is not measured when the user enters 'done'
                # midloop
                if your_try == 'DONE':
                        break
                total_words = int(total_words + count_words(your_try))
                wrong = int(count_mismatches(the_sentence, your_try))


        print(calculate_wpm(total_words, time.perf_counter()), 'words per minute')
        print(calculate_adjusted(total_words, wrong, time.perf_counter()))

                
main()
