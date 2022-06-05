MINUTESPERYEAR = 525600
MINUTESPERDAY = 1440
MINUTESPERHOUR = 60
MINUTESPERMINUTE = 1
# As in there is 1/60th of a minute per 1 second
MINUTESPERSECOND = 1/60

'''
    Zachary Sylvane
    CS5001
    HW1 Programming #3
    1/13/2020

    Test case #1:
    Input: 1.5 minutes
    Output: 1 minute and 30 seconds.

    Test case #2:
    Input: 525665 minutes
    Output: 1 year, 1 hour, 5 minutes

    Test case #3:
    Input: 2040 minutes
    Output: 1 day,10 hours

    
'''

def main():

    # User is asked to input an amout of minutes, decimals allowed,
    # treated as float
    minutes_to_measure = float(input("How many "
                                     "minutes?\n"))

    # User's minutes are divided // by the amount of minutes in a year,
    # minutes in a day, and so on.
    # The program then stores the REMAINING, leftover minutes.
    # For instance, if user inputs 525600 there will be 0 leftover minutes for
    # further calculations
    y_leftover = minutes_to_measure % MINUTESPERYEAR
    d_leftover = y_leftover % MINUTESPERDAY
    h_leftover = d_leftover % MINUTESPERHOUR
    m_leftover = h_leftover % MINUTESPERMINUTE
    
    # After printing the amount of minutes divided by the minutes in a year,
    # the program prints the leftover minutes divided by the next largest
    # category, so on and so forth.
    # Dividing hleftover by MINUTESPERMINUTE will always result in hleftover so
    # I leave out the extra calculation
    print("That is: \n", int(minutes_to_measure / MINUTESPERYEAR),"Years\n",\
                         int(y_leftover / MINUTESPERDAY), "Days\n",\
                         int(d_leftover / MINUTESPERHOUR),"Hours\n", \
                         int(h_leftover),"Minutes\n", \
    # Rounding seconds so we dont drop off the decimal points
    # for a case like 4.98 seconds.
                         round(m_leftover / MINUTESPERSECOND), "Seconds")


main()

