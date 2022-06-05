''' CS5001
    Zachary Sylvane
    March 25, 2020
    HW7
'''

import turtle
from cookie import *

SCOREFILE = 'scores.txt'

class Game:
    ''' Class: Game
        Attributes: cookie, score_file, achievefile, cookie_clicked
        Methods: game, click, read_achievements
    '''
    def __init__(self, scorefile, achievefile):
        '''
        Constructor -- creates an new instance of a game
        Parameters:
           self -- the current object
           scorefile -- txt file with score
           achievefile -- txt file with achievements
        '''
        # creates a cookie object 
        self.cookie = Cookie()
        self.scorefile = scorefile
        self.achievefile = achievefile
        # turtle.onclick is called with the Game click method as a parameter.
        # turtle.onclick will pass x and y coordinates to click method.
        self.cookie_click =  turtle.onclick(self.click)
        # ensures cookie object has a default dictionary that can pass as a parameter
        # without this line if there is no achivement file, the program will not
        # be able to keep track of the score once program is exited.
        self.cookie.achievements[0] = 0 

    def game_score(self):
        '''
        Method -- initializes score for cookie object
        Parameters:
           self -- the current object
        Returns nothing
        '''
        self.cookie.initialize_score(self.scorefile)
        
    def click(self, x, y):
       '''
       Method -- if click is over cookie, adds points/achievements and prints
                  if click is over exit, exits
       Parameters:
           self -- the current object
           x -- x coordinate of click given by turtle.onclick
           y -- y coordinate of click given by turtle.onclick
       Returns nothing
       '''
       # clears old score before each click
       turtle.clear()
       turtle.tracer(0)
       if x <= 5:

            self.cookie.add_point()
            
            print(self.cookie.score)

            for key in self.cookie.achievements:
                if key == str(self.cookie.score):
                    # if key in dictionary is == to score, prints name of achievement
                    print(self.cookie.achievements[key][0])
                    turtle.setposition(-300,170)
                    turtle.write(self.cookie.achievements[key][0], font = ("Arial", 15, "normal"))
                    # if key in dictionary is == to score, score += value in key.
                    # bonus achievement points.
                    self.cookie.score += int(self.cookie.achievements[key][1])
                    print(self.cookie.score)

                try:
                    with open(SCOREFILE, 'w') as outfile:
                        outfile.write(str(self.cookie.score))
                except OSError:
                    print('Sorry for the inconvinience. score cannot be written')
            # score written on turtle window
            turtle.setposition(-300,200)
            turtle.write(self.cookie.score, font = ("Arial", 15, "normal"))
       # exits if click is on the exit area   
       if x > 5:
           os._exit(0)
          
    def read_achievements(self):
        '''
        Method -- read achievement file, makes a list, then makes a dictionary
                  in which each key has as a value a list containing two elements 
        Parameters:
           self -- the current object
        Returns achievements_list, a list
        '''
        try:
            with open(self.achievefile, 'r') as infile:
                achievements_list = []
                lines = infile.readlines()
                for line in lines:
                    # creates list which will be used for dictionary
                    achievements_list.append(line.split())
                print(achievements_list)
                
                for i in range(len(achievements_list)):
                    # makes the [1] element of each sublist (dough, bake, affluent, etc) into the key of a dictionary.
                    # takes the [0] and [2] element of each sublist in list and makes them into the value of each dictionary key
                    # as a list
                    self.cookie.achievements[ achievements_list[i][1] ] = achievements_list[i][:1] + achievements_list[i][2:]

                print(self.cookie.achievements)
            
        except OSError:
            print('sorry for the inconvinience achievements are down.')
            # note that if there is no achievement file, 
            # self.cookie.achievements[0] = 0 in the Game constructor allows game to continue
            # I decided the code was more appropriate there than in this exception
        
