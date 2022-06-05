''' CS5001
    Zachary Sylvane
    January 25, 2020
    HW 3, Programming #2
'''
from nim_functions import ai
from nim_functions import is_over
from nim_functions import coin_flip
from nim_functions import heads_or_tails


heads = ''
tails = ''

def main():
       
        coin_guess = ''
        while coin_guess != "h" and coin_guess != "t":
            coin_guess = str(input('Heads or tails? h for heads, t for tails \n'))
        # heads_or_tails returns either true of false, if it returns false, the human will be player_2
        player_1 = heads_or_tails(coin_guess)
        player_2 = ''
        
        if player_1 == True:
            player_2 = False
        elif player_1 == False:
            player_2 = True
            
        bean_count = 8
     
        while is_over(bean_count) == False:
            if player_1 == True:
                # setting my_beans higher than bean_count so it triggers at least once
                # the amount input will replace 9 after.
                my_beans = 9
                # inner loop will continue if amount selected is impossible. otherwise,
                # the selected amount will be subtracted from bean_count. also ensures
                # beancount cant go below 0
                while my_beans > bean_count or my_beans > 3:
                        my_beans = int(input('how many beans do you take? (1, 2, 3)\n'))
                bean_count = bean_count - my_beans
                print('there are now', bean_count, 'beans left')
                # changes the player turn
                player_1 = False
                player_2 = True

            elif player_2 == True:
                # the bean count will be used as a parameter for the AI_choice function
                # to determine a legal amount of beans to take
                AI_choice = ai(bean_count)
                print('I take', AI_choice, 'beans!')
                bean_count = bean_count - AI_choice
                print('there are now', bean_count, 'beans left')
                player_2 = False
                player_1 = True

        
        # the loop above  breaks when bean_count == True. the player who did not make the count == True
        # (the next player) is announced as the winner
        if  player_1 == True:
                print('I took the last bean. I lose. You win')
        elif player_2 == True:
                print('You took the last bean. I win. You lose')
  
main()

 






