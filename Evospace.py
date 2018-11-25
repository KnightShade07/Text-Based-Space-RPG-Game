##Program Author: Ethen Oliva
##Text Based Space Adventure Game

import random
import time

def main():
    game_intro()
    choose_job_class()

 





##This class is where you'll handle adding or subtracting credits from the player
##When they do something like complete a mission or buy something from a shop
class Credits:
    def __init__(self):
        self.player_credits = 0
    
    def credit_add(self, credits):
        self.player_credits+=credits
   
myClass = Credits()
    



def game_intro():
    ##Story Introduction
    print('You are a pilot traveling the Milky Way galaxy, looking for')
    print('the next new, threatening, and dangerous adventure!')
    print('you do not have very many credits to your name at the moment,')
    print('but that will come with time, do not worry!')
    print('Alrighty then, let us get started!')
    ##Player inputs their name, and then the class Player will store that information for them, so
    ##When the player wants to look at their stats in a menu, it will always
    ##be there for them.

##This class is where you'll store all the information about your player,
 ##Like EXP,Rank, Ship, Name
    class Player():
        def __init__(self):
            self.dict ={}
            self.player_name = input(str('Enter your name!:'))
            self.experience_points = 0
            self.current_ship = ''
            self.rank =''        

    player = Player()

    player.player_name
    ##Transition to next function, the function that will let the player pick their job!


  
    
        
def choose_job_class():
    select_job_class =str(input("Choose your class! Type 'Options to see the availible job classes!'"))
    ##List of job classes that the player can choose from!
    print('(1) is the Bounty Hunter job class, who primarily specializes in combat against pirates.')
    print('(2) is the Trader Job class, who trades goods between space stations.')
    print('(3) is the Explorer Job class, who explores the galaxy for new and exciting things.')
    select_job_class = str(input('Which job class will you choose?(1,2, or 3):'))
    if select_job_class == '1':
        print('Great Choice! Who wouldn''t like blasting space pirates?')
        print('For starters, lets get you some money, eh?')
         ##Give the player their starting amount of credits!
        print('Here is {} credits for you to get started'.format(int(myClass.player_credits + 10000)))
        ##Display how many credits the player now has!
        myClass.credit_add(10000)
        print('Congrats! You now have' ' ' +  str(myClass.player_credits) + ' ' 'credits!')
    elif select_job_class =='2':
        print('Great Choice! Who wouldn''t like blasting space pirates?')
        print('For starters, lets get you some money, eh?')
         ##Give the player their starting amount of credits!
        print('Here is {} credits for you to get started'.format(int(myClass.player_credits + 10000)))
        ##Display how many credits the player now has!
        myClass.credit_add(10000)
        print('Congrats! You now have' ' ' +  str(myClass.player_credits) + ' ' 'credits!')
       
    elif select_job_class =='3':
        print('Great Choice! Who wouldn''t like blasting space pirates?')
        print('For starters, lets get you some money, eh?')
         ##Give the player their starting amount of credits!
        print('Here is {} credits for you to get started'.format(int(myClass.player_credits + 10000)))
        ##Display how many credits the player now has!
        myClass.credit_add(10000)
        print('Congrats! You now have' ' ' +  str(myClass.player_credits) + ' ' 'credits!')
def continue_story():
        
    return()

main()



