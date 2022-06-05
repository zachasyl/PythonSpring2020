''' Zachary Sylvane
    CS5001
    Homework 2 Programming 3
    Test Suite
    January 20, 2020
'''
LAT_0 = 42.338574
LONG_0 = -71.0945489

from boston import x_conversion
from boston import y_conversion
from boston import distance

def test_coordinate_conversion(latitude, longitude, expected_x, expected_y):
    ''' Function: test_coordinate_conversion
        Parameters: latitude, longitude, floats
                    expected_x, expected_y, integers
        Returns: Nothing
        Does:  calls x and y_conversion functions to get the actual
               x and y coordinate, prints input lat/long as well as
               expected x/y and actual x/y
    '''
    
    actual_x = x_conversion(latitude, LAT_0, longitude, LONG_0)
    actual_y = y_conversion(latitude, LAT_0, longitude, LONG_0)

    print(  "\n"
            "Testing coordinate conversion...\n"
            "latitude =", latitude,  "...\n"
            "longitude =", longitude,  "...\n\n"
            "\tExpected x:", expected_x, "\n"
            "\tExpected y:", expected_y, "\n"
            "\tActual x:",  actual_x,
            "\tActual y:", actual_y,
            "\n")
    
def test_distance(latitude, longitude, expected_distance):
    ''' Function: test_distance
        Parameters: latitude, longitude, expected_distance, all floats.
        Returns: Nothing
        Does:  calls actual_distancefunctions to get the actual
               distance, prints input lat/long as well as
               expected distance and actual distance
    '''
    actual_distance = distance(latitude, LAT_0, longitude, LONG_0)

    print(  "\n"
            "Testing distance calculation...\n"
            "latitude =", latitude,  "...\n"
            "longitude =", longitude,  "...\n\n"
            "\tExpected distance =", expected_distance,  "...\n"
            "\tActual distance =", actual_distance,  "...\n")
     
def main():
    ''' For tester to input coordinates for coordinate or
        distance calculations
    '''
    # coordinate conversion tests.
    # latitude, longitude, expected x,expected y
    test_coordinate_conversion(42.3466803, -71.0994118, -39, 90)
    test_coordinate_conversion(42.338574, -71.0945489, 0, 0)
    test_coordinate_conversion(42.3555, -71.0639, 251, 188)

    # distance tests. latitude, longitude, expected distance
    test_distance(42.3466803, -71.0994118, 0.89)
    test_distance(42.338574,-71.0945489, 0.00)
    #boston commons is big so this may be off a bit
    test_distance(42.3555,-71.0639, 2.00)
    
main()
