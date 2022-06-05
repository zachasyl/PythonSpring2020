''' Zachary Sylvane
    CS5001
    Homework 2 Programming 3
    January 20, 2020
'''
import math
from boston import x_conversion
from boston import y_conversion
from boston import distance
import turtle

# the lat long at 0,0, wvh, the center of the image background
LAT_0 = 42.338574
LONG_0 = -71.0945489

def main():
    '''asks user to input name, latitude, and longitude of location.
       calculates latitude, longitude and distance by calling functions.
       prints distance, x and y coordinate
    '''
    # Sets background image, calls turtle functions, hides turtle arrow
    # sets turtle position, draws blue dot at WVH 0,0
    screen = turtle.Screen()
    screen.setup(800,565)
    screen.bgpic('boston_map.png')
    screen.title("Boston")
    turtle.hideturtle()
    turtle.position()
    (0.00,0.00)
    turtle.dot(10, "blue")

    # gets location, lat and long from user 
    favorite_place = str(input("What is the name of your favorite boston location?  "))
    lat = float(input("What is the latitude of your favorite boston location?  "))
    long = float(input("What is the longitude of your favorite boston location?  "))

    # calls functions to convert lat/long to coordinates
    x_coordinate = x_conversion(lat, LAT_0, long, LONG_0)
    y_coordinate = y_conversion(lat, LAT_0, long, LONG_0)

    #calls distance function to convert lat/long to mile distance from wvh
    dist = distance(lat, LAT_0, long, LONG_0)

    print('x coordinate: ', x_coordinate)
    print('y coordinate: ',y_coordinate)
    # stops turtle from drawing a line and draws red dot
    # at the x,y converted points
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate )
    turtle.dot(10, "red")
    turtle.write(favorite_place + "\n" + "~" +  dist + " miles", \
                 align = "left",font = ("Arial", 10, "bold"))

main()


   
