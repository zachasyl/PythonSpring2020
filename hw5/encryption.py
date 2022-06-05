''' CS5001
    Zachary Sylvane
    February 12, 2020
    HW5, Programming #2
'''
'''
the man who passes the sentence should swing the sword

everyone is mine to torment

you know nothing jon snow

that's what i do i drink and i know things

'''


'''
my encrypted sentence:
dibpt jt b mbeefs
'''

def main():
    # user interface, just made so I can test program
    crypt_decrypt = input('do you want to encrypt (press 1) or decrypt (press 2)')

    if crypt_decrypt == '1':
        # input message is forced to lowercase
        message = str(input('what is your message?').lower())
        shift = int(input('what is your shift?'))
        # cant go past the alphabet max
        if shift > 25:
            shift = 1
        encrypt(message, shift)

    elif crypt_decrypt == '2':
         message = str(input('what is your message?').lower())
         shift = int(input('what is your deshift?'))
         if shift > 25:
             shift = 1
         decrypt(message, shift)


def encrypt(message, shift):
    '''Function encryprt
        Parameters: message, a string; shift amount, an int
        Returns: encrypted message, a string
    '''
    ord_list = []
    char_list = []

    # converts to number and adds shift
    for i in range(len(message)):
        if ord(message[i]) + shift < 122:
            ord_list.append(ord(message[i]) +shift)
        elif ord(message[i])  + shift > 122:
            list_modulo = ord(message[i])
            
            ord_list.append((list_modulo + shift) % 122 + 96)

    # converts to characters now that number is shifted
    for i in range(len(ord_list)):
        char_list.append(chr(ord_list[i]))


    string_char_list = ''
    for i in range (len(char_list)):
        string_char_list += str(char_list[i]) 

    print(string_char_list)
    return string_char_list
    
def decrypt(message, deshift):
    ''' Function decrypt
        Parameters: message, a string; shift amount, an int
        Returns: decryped message, a string
    '''
    ord_list = []
    char_list = []
    for i in range(len(message)):

            if  ord(message[i]) - deshift >= 97:
                ord_list.append(ord(message[i]) - deshift)
                                
            elif ord(message[i]) - deshift < 97:
                #using modulo to wrap around alphabet
                modulo = 122 % ord(message[i])
                ord_list.append(ord(message[i]) + modulo - deshift +1)

    
    for i in range(len(ord_list)):
         #ensures spaces between words
        if ord_list[i] == 58:
            ord_list[i] = 32
        # converts to alphabet character
        char_list.append(chr(ord_list[i]))


    print(ord_list)
    print(char_list)

    string_char_list = ''
    for i in range (len(char_list)):
        string_char_list += str(char_list[i]) 

    print(string_char_list)
    return string_char_list


'''
    How I solved decryption samples:
'''

'''
a_list = ''
list1 = ['xli', 'qer', 'als', 'tewwiw', 'xli', 'wirxirgi', 'wlsyph', 'wamrk', 'xli', 'wasvh']
list2_bad = ['lclyfvul pz tpul av avytlua']
list2 =['lclyfvul', 'pz', 'tpul', 'av', 'avytlua']
# eh there arent that many commas, im gonna do the rest manually >_<
##for i in range(0, len(list2_bad)):
##        z = list2_bad[i].split(' ')
##        list2.append(z)


list3 = ['zpv', 'lopx', 'opuijoh,', 'kpo' 'topx']
        
list4 = ["xlex'w", 'alex', 'm', 'hs:', 'm', 'hvmro', 'erh', 'm', 'orsa', 'xlmrkw']

g = 0
a_list = list1
while g <= 3:
    shift_loop = 0
    for i in range(0, len(a_list)):
        shift_loop = 1
        for j in range(1, 8):
            decrypt(a_list[i].lower(), shift_loop)
            
            shift_loop+=1
        print('NEXT STRING! \n')

    g+=1
    if g ==1:
        a_list = list2
    elif g ==2:
        a_list = list3
    elif g ==3:
        a_list = list4
    
    print('NEXT LIST! \n')
'''


main()










