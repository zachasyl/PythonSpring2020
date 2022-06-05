# charge for converting $350 = .03 * 350 + fee = $15.00
# fee calculated by: .03 * 350 = 10.5.
# 15 - 10.5 = 4.50
FLAT_FEE = 4.50

THREE_PERCENT = .03

'''

    Zachary Sylvane
    CS5001
    HW1 Programming #2
    1/13/2020



    Test case #1:
    Input: $351
    Total fee: $15.03

    Test case #2:
    Input: $30
    Total fee: $5.40

    Test case #3:
    Input: $500.25
    Total fee: $19.5075 (program should round to 19.51)

        
'''

def main():
    
    # User is prompted to enter a $ amount to convert.
    amount = float(input("Please enter an amount of money to convert \n$"))
    # Amount is multiplied by three percent and flat fee is added.
    # The charge is printed with 2 numbers after the decimal point, rounded.
    joes_charge = amount * THREE_PERCENT + FLAT_FEE
    print("Total fee: \n${:.2f}".format(joes_charge))
                       
main()
