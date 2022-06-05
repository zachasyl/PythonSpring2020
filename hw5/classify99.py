''' CS5001
    Zachary Sylvane
    February 9, 2020
    HW5, Programming #1
'''
from classify_functions import *
def main():


    # this will most_frequent will return word list for each character
    # that return is used as a paramater for count_words
    jake_word_list = (only_words(JAKE))
    jake_favs = count_words(jake_word_list, 'JAKE')

    rosa_word_list = (only_words(ROSA))
    rosa_favs = count_words(rosa_word_list, 'ROSA')

    holt_word_list = (only_words(HOLT))
    holt_favs = count_words(holt_word_list, 'HOLT')

    gina_word_list = (only_words(GINA))
    gina_favs = count_words(gina_word_list, 'GINA')

    question = ''
    

    while question != '1' and question != '2' and question != '3':
        question = input('Choose from the following options...\n'
                             '1. Choose a test quote at random\n'
                              '2. Type a quote in yourself.\n'
                               '3. Quit\n' )
    
    if question == '1':
        chosen_saying_split= []
        chosen_saying = random_saying()
        print('\n')
        print('\n')
        print(chosen_saying)


        chosen_saying_list = []
        chosen_saying_list.append(chosen_saying)
        chosen_split = []
        exact_match = False

        #tests for exact match
        for i in range(0, len(JAKE)):              
            if chosen_saying == JAKE[i]:
                print('JAKE SAID IT!')
                exact_match = True
        for i in range(0, len(ROSA)):              
            if chosen_saying == ROSA[i]:
                print('ROSA SAID IT!')
                exact_match = True
        for i in range(0, len(HOLT)):              
            if chosen_saying == HOLT[i]:
                print('HOLT SAID IT!')
                exact_match = True
        for i in range(0, len(GINA)):              
            if chosen_saying == GINA[i]:
                exact_match = True
                print('GINA SAID IT!')

        # if not exact match, will test who is most likely to have said it
        if exact_match == False:

            for i in range(0, len(chosen_saying_list)):
                chosen_saying_split = chosen_saying_list[i].split(' ')
                chosen_split.append(chosen_saying_split)


            score_list = []
            
            jake_score = comparison(jake_favs, chosen_saying_split)
            rosa_score = comparison(rosa_favs, chosen_saying_split) 
            holt_score = comparison(holt_favs, chosen_saying_split) 
            gina_score = comparison(gina_favs, chosen_saying_split) 
            
            score_list.append(jake_score)
            score_list.append(rosa_score)
            score_list.append(holt_score)
            score_list.append(gina_score)

            highest_score = max(score_list)

            # pairs highest score with order each person
            # was appended to score_list
            if highest_score == score_list[0]:
                most_likely_said_by = 'Jake'
            elif highest_score == score_list[1]: 
                most_likely_said_by = 'Rosa'
            elif highest_score == score_list[2]: 
                most_likely_said_by = 'Holt'
            elif highest_score == score_list[3]: 
                most_likely_said_by = 'Gina'

            print(highest_score)
            print(most_likely_said_by)


    if question == '2':

        score_list = []

        your_quote = input()
        your_quote_list = []
        your_quote_list.append(your_quote)
        your_quote_elements = only_words(your_quote_list)

        exact_match = False

        #tests for exact match
        for i in range(0, len(JAKE)):              
            if your_quote == JAKE[i]:
                print('JAKE SAID IT!')
                exact_match = True
        for i in range(0, len(ROSA)):              
            if your_quote == ROSA[i]:
                print('ROSA SAID IT!')
                exact_match = True
        for i in range(0, len(HOLT)):              
            if your_quote == HOLT[i]:
                print('HOLT SAID IT!')
                exact_match = True
        for i in range(0, len(GINA)):              
            if your_quote == GINA[i]:
                exact_match = True
                print('GINA SAID IT!')

        # if not exact match, will test who is most likely to have said it
        if exact_match == False:

            jake_score = comparison(jake_favs, your_quote_elements)
            rosa_score = comparison(rosa_favs, your_quote_elements) 
            holt_score = comparison(holt_favs, your_quote_elements) 
            gina_score = comparison(gina_favs, your_quote_elements)

            score_list.append(jake_score)
            score_list.append(rosa_score)
            score_list.append(holt_score)
            score_list.append(gina_score)

            highest_score = max(score_list)

            if highest_score == score_list[0]:
                most_likely_said_by = 'Jake'
            elif highest_score == score_list[1]: 
                most_likely_said_by = 'Rosa'
            elif highest_score == score_list[2]: 
                most_likely_said_by = 'Holt'
            elif highest_score == score_list[3]: 
                most_likely_said_by = 'Gina'

            print(highest_score)
            print(most_likely_said_by)

main()
