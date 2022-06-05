''' CS5001
    Zachary Sylvane
    January 25, 2020
    HW 3, Programming #1
'''
import turtle

def main():
    screen = turtle.Screen()
    screen.setup(800,565)
    screen.bgcolor("light sky blue")

    moon = turtle.Turtle()
    moon.hideturtle()
    moon.penup()
    moon.setx(-400)
    moon.sety(200)
    moon_current_x = -400
    moon_current_y = 200

    sun = turtle.Turtle()
    sun.hideturtle()
    sun.penup()
    sun.setx(0)
    sun.sety(200)
    sun.dot(60, "yellow")
    sun_current_x = 0
    sun_current_y = 200

    speed = 1
    moon_moving = True

    # while the moon is moving, its X pos is updated so it can be used to
    # see if the moon touches the sun or edge of screen.
    # each time the moon moves according to its speed of 1, it is cleared
    # and redrawn as the loop repeats
    while moon_moving == True:
        moon_current_x += speed
        screen.tracer(10)
        moon.clear()
        moon.fd(speed);moon.dot(80, "gray")
        
        # if right side of moon touches left side of sun, night is black. once left side of moon
        # leaves right side of sun, sky is blue. can adjust numbers to make look more realistic.
        if moon_current_x +80 > sun_current_x and moon_current_x <sun_current_x + 60 :
            screen.bgcolor("black")
        else:
            screen.bgcolor("light sky blue")

        # loop will end when turtle reaches end of screen
        # note full screen width would be 565 
        if moon_current_x > 400:
            break
    
main()
