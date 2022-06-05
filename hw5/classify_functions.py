''' CS5001
    Zachary Sylvane
    February 9, 2020
    HW5, Programming #1
'''

import random
from classify_data import *

def random_saying():
    '''Function random_saying
        Parameters: none
        Returns: a random sentence from TESTING list, str
    '''
    rand_num= 0
    rand_num = random.randrange(0, len(TESTING))
    random_saying  = TESTING[rand_num]

    return random_saying

def only_words (character):
    ''' Function only_words
        Parameters: character, a list in which elements are full
                    sentences
        Returns: words_only, a list where each element is one word
    '''
    character_appended = []
    jake_final = []
    worlds_only_final = []

    words_only = []
    decrease_increment = 1

    worlds_only_final = []
    
    for i in range(0, len(character)):
        x = character[i].split(' ')
        character_appended.append(x)

    for i in range(0, len(character_appended)):
        for j in range(0, len(character_appended[i])):
            words_only.append(character_appended[i][j])
    
    counter_list = []
    stopword_exists = False
    return words_only

def count_words(words_only, character_name):
    ''' Function count_words
        Parameters: words_only, each word is an element str
                    character_name, a string that is the name of character saying a quote
        Returns: a list of favorite words of each character
        Does:    looks through words_only to find the favorite words of each character
                 uses character_name str to associate words with each char.
    '''
    counter_list = []
    increase_increment = 1
    counter = 0
    start = 0
    stop_range = len(words_only)

    # this part of code removes the stopwords for words_only so words like 'if' arent
    # used as favorite words
    for exclude in range (0, len(STOPWORDS)):
        for j in range (0, stop_range):
            if j < stop_range and STOPWORDS[exclude].upper() == words_only[j].upper():
                words_only.remove(words_only[j])
                # must decrease range after removal of element to prevent index error
                stop_range = stop_range - 1
    stop_range = len(words_only)     
    duplicates = ''

    # now the stopwords have been removed from words_only.
    # commonality of words are counted and common words are put into words_only_variable
    # the counter and words_only_variable are appended to counter_list

    for i in range (0, stop_range):
        increase_increment = 0
        # this prevents [0] from being 0 due to counter's initialization
        if counter > 0:
            counter_list.append(str(counter) + ' ' + words_only_variable)
        counter = 0
        words_only_variable = ''
        
        for j in range(0, stop_range):
           increase_increment  +=1
           if i < stop_range and words_only[i] == words_only[i-increase_increment]:
              
              counter+=1
              words_only_variable = words_only[i]
    stop_range = len(counter_list)
           
    x = 0
    final_list = []
    # counters are appended to final_list
    for num in counter_list: 
        if num not in final_list: 
            final_list.append(num) 

    count_list_final = []

    for i in range (0, len(final_list)):
         separate = final_list[i].split(' ')
         count_list_final.append(separate)
    higher_numer = 0

    max_list = []
    jake_list = []
    gina_list = []
    holt_list = []
    rosa_list = []

    # max_list takes the 5 most common words:
    max_list.append(max(count_list_final))
    count_list_final.remove(max(count_list_final))
    max_list.append(max(count_list_final))
    count_list_final.remove(max(count_list_final))
    max_list.append(max(count_list_final))
    count_list_final.remove(max(count_list_final))
    max_list.append(max(count_list_final))
    count_list_final.remove(max(count_list_final))
    max_list.append(max(count_list_final))
    print('\n')

    # returns max_list for appropriate character
    if character_name == 'JAKE':
        jake_list = max_list
        return jake_list
    elif character_name == 'ROSA':
        rosa_list = max_list
        return rosa_list
    elif character_name == 'HOLT':
        holt_list = max_list
        return holt_list
    elif character_name == 'GINA':
        gina_list = max_list
        return gina_list

def comparison(favorites, sentence):
    ''' Function comparison
        Parameters: favorites: a list of favorite words and occurences of each word
                    (together, one element), strings;
                    sentences, each element is a word. string.
        Returns:    matches between words in each list, a score.
       
    '''
# x is the random quote if you press 1 or your input quote, each word separated
# favorites is character favorites words and how much ccurs
# will return score for each characters favorites
    the_range = len(favorites)
    score = 0
    for i in range(0, len(sentence)):
        for j in range(0, the_range):
             
            if j < the_range and sentence[i] == favorites[j][1]:
                 # rather than adding 1 to the score, i add how many times that top word appeared to give
                 # individual weight to each of the top five words
                score += int(favorites[j][0])
                # must decrease range after removal of element to prevent index error!
    return score

