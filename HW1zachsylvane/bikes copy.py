WHEELSPERBIKE = 2
FRAMESPERBIKE = 1
LINKSPERBIKE = 50


'''
    Zachary Sylvane
    CS5001
    HW1 Programming #4
    1/13/2020

    Test case #1:
    Input: 8 wheels, 8 frames, 8 links
    Bikes: 0 bikes.
    Leftovers: 8w, 8f, 8l
    

    Test case #2:
    Input: 9 wheels, 10 frames, 151 links
    Bikes: 3 bikes
    Leftovers: 3 wheels, 7 frames, 1 link

    Test case #3:
    Input: 10 wheels, 11 frames, 300 links
    Bikes: 5 bikes
    Leftovers: 0w, 6 frame, 50 links



'''

def main():

    # Asks user to input wheels frame, and link amount to make bikes.
    # Input is expected to be a whole number
    user_wheels = int(input("how many wheels do you have?\n"))
    user_frames = int(input("how many frames do you have?\n"))
    user_links = int(input("how many links do you have?\n"))

    # The user amount is divided // by the amount of each part
    # needed to complete one bike so we dont get floats.
    wheels =  user_wheels //WHEELSPERBIKE   
    frames = user_frames //FRAMESPERBIKE   
    links = user_links //LINKSPERBIKE  

    # this function stores the lowest number as the label's value
    # we are limited to how many bikes we can build by what we
    # have the least of
    bikes_possible = min(wheels, frames, links)

    # now that we know how many bikes we can make, we can multiply
    # that amount by how many of each part is required.
    # we do not need to worry that there wont be enough parts
    # since we already know and are using the least amount of bikes possible.
    # these stored values will be used to calculate remaining parts
    wheels_possible = bikes_possible * WHEELSPERBIKE
    frames_possible = bikes_possible * FRAMESPERBIKE
    links_possible = bikes_possible * LINKSPERBIKE

    # by subtracting the parts possible from the user's input
    # the leftover parts from the user's input remain to be kept
    leftover_wheels = user_wheels - wheels_possible
    leftover_frames = user_frames - frames_possible
    leftover_links = user_links - links_possible
    
    # prints how many bikes can be made and how many
    # parts are leftover but cannot be made into a bike
    print("We will make you" ,bikes_possible, "bikes\n" \
          "We will keep the leftovers\n", leftover_wheels, "wheels\n",\
           leftover_frames, "frames\n",leftover_links, "links")

   

    
main()

