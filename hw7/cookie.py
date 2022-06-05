''' CS5001
    Zachary Sylvane
    March 20, 2020
    HW7, 
'''
import os
from cookie_functions import *
    
class Cookie:
    ''' class: Cookie
        Attributes: score, achievements
        Methods: initialize_score, add_point
    '''
    def __init__(self, score = 0, achievements = {} ):
        '''
        Constructor -- creates an new instance of a cookie
        Parameters:
           self -- the current object
           score -- initial score for clicking cookie
           achievements -- initial achievements
        '''

        self.score = score
        self.achievements = achievements

    def initialize_score(self, SCOREFILE):
        '''
        Method -- updates score by reading SCOREFILE
        Parameters:
           self -- the current object
           score -- score txt file
        Returns nothing
        This method is called by the method game_score in Game class
        '''
        # calls read_file if score.txt exists, else score = 0
        if os.path.isfile(SCOREFILE):
            self.score = read_file(SCOREFILE)
        else:
            self.score = 0

    def add_point(self):
        '''
        Method -- adds point to current score
        Parameters:
           self -- the current object
        Returns nothing
        This method is called by the method game_score in Game class
        '''
        self.score+=1
        
