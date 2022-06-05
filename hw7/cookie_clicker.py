''' CS5001
    Zachary Sylvane
    March 24, 2020
    HW7, driver
'''
import turtle
from game import *
from cookie import *

IMAGE = 'cookieman.gif'
SCOREFILE = 'scores.txt'
ACHIEVEMENTS = 'achievements.txt'
        
def main():

    screen = turtle.Screen()
    screen.setup(800, 565)
    screen.bgcolor("light sky blue")
    turtle.setposition(0, 0)
    # turtle can draw cookieman.gif and starting position
    turtle.Screen().register_shape(IMAGE)
    turtle.shape(IMAGE)

    # writes SCORE on the turtle screen -- the score is displayed underneath on click
    # but SCORE is permanent and will not update on click/ clear()
    score = turtle.Turtle()
    score.hideturtle()
    score.penup()
    score.setposition(-300, 225)
    score.write('SCORE:', font = ("Arial", 20, "bold"))

    # creates a game object and calls methods game and read_achievements
    game = Game(SCOREFILE, ACHIEVEMENTS)
    # game score will initialize cookie score
    game.game_score()
    game.read_achievements()

    
main()
    
