


'''
    Zachary Sylvane
    CS5001
    HW1 Programming #1
    1/13/2020
'''

def main():

    # The user is prompted for input information, which is then stored.
    firstname = input("Enter your first name\n")
    lastname = input("Enter your last name\n")
    age = input("Enter your age\n")
    income = input("Enter your average annual income\n")
    doggos = input("Enter the number of dogs in your family\n")
    jacoboredward = input("Team Jacob ot Team Edward?\n")

    # And the program prints out the stored information
    # as well as a description of the initial prompt
    print("Thank you for your profile information! "
          "Here is what we stored for you:")
    print("Name:", firstname, lastname)
    print("Age:", age)
    print("Income:", income)
    print("You have", doggos, "dogs")
    print("You are on team", jacoboredward)
    
main()
