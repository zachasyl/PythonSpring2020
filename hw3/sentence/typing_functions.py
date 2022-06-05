''' CS5001
    Zachary Sylvane
    January 25, 2020
    HW 3, Programming #3 functions
'''


def calculate_wpm(num_words, time):
        ''' Function: Calculate_wpm
            Parameters: num_words, time -- num_words is an int,
                        and time is a float
            Returns: WPM, an int.
            Does:    Prints the time to the hundreths place
                     and prints num_words as an int
        '''

        wpm = int((num_words / time) * 60)
        
        print('you typed', num_words, 'words in', '{:.2f}'.format(time), \
              'seconds')
        return wpm

def calculate_adjusted(num_words, num_mistakes, time):
        ''' Function: Calculate_adjusted
            Parameters: num_words, num_mistakes, time -- num_words is an int,
                        num_mistakes is an int, time is a float
            Returns: adjusted WPM, an int, or 0
            Does:    calculates adjusted WPM taking mistakes into account
        '''
        
        adjusted = int(((num_words - num_mistakes) /time) * 60)
        print('you made', num_mistakes, ' mistakes. Your adjusted wpm is: \n')
        # prevents adjusted from being negative
        if adjusted >0:
                return adjusted
        else:
                return 0
        
