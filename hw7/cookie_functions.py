''' CS5001
    Zachary Sylvane
    March 20, 2020
    HW7, 
'''

def read_file(filename):
    ''' Function read_file
        Parameters: filename,a string
        Returns: points contained in file, an int
    '''
    try:
        # will read file and append number within to list score
        with open(filename, 'r') as infile:
            read_score = []
            lines = infile.readlines()
            for line in lines:
                read_score.append(line)
                score = int(read_score[0])
                return score
    # if the file exists but there is an error ensures score will be 0
    # and program will keep running
    except OSError:
        # score will default to 0 as per attribute and game can continue
        # with corrupt file score will = 0
        print('sorry for the inconvinience. File cannot be read')
        # score = 0
        # return score
    
