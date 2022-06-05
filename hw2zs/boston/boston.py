
''' Zachary Sylvane
    CS5001
    Homework 2 Programming 3
    Functions
    January 20, 2020
'''
import math

def x_conversion(lat,LAT_0, long, LONG_0):
    '''Function: x_conversion
       Parameters: lat, LAT_0, long, LONG_0. floats.
       return: x coordinate as an integer
    '''
    #formula for x conversion
    x = int(((long - LONG_0) * 4000000 * math.cos((lat + LAT_0) * 3.14/360)/360))
    return x

def y_conversion(lat,LAT_0, long, LONG_0):
    '''Function: y_conversion
       Parameters: lat, LAT_0, long, LONG_0. floats.
       return: y coordinate as an integer
    '''
    #formula for y conversion
    y = int((lat - LAT_0) * 4000000 / 360)
    return y


def distance(lat, LAT_0, long, LONG_0):
    
    '''Function: distance
       Parameters: lat, LAT_0, long, LONG_0. floats.
       return: distance between lat_0+long_0 and new coordinates.
               returns with 2 decimal places, mile approximate
               doesn't need to be more specific.
    '''
    #formula for distance.
    d = "{:.2f}".format(110.25 * (math.sqrt((lat - LAT_0)**2 + ((long - LONG_0) * math.cos(LAT_0))**2)))
    return d



