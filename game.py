#Author Johnathan Lee
#Year 9 Design C2 
#Jabari Jumps game
#Functions read from the bottom up to ensure all are properly defined before they are called
#Each function is called by the previous one which is why the layout is the same

import time #This is the libray that stores functions realted to time like time.sleep()
from playsound import playsound#funcion for playing sounds, you need to install it via terminal

 #These are the colours I use labeled under the class bcolours        
class bcolours:
    questions = '\u001b[35m'#ANCI colour codes
    comments = '\u001b[36m'
    header = '\u001b[33m'
    options = '\u001b[34m'
    correct = '\u001b[32m'
    wrong = '\u001b[31m'
    ENDC = '\u001b[37m'
#divider for each question
split = "<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>"


def adventure():#Adventure mode choice based story 
    print(bcolours.header + "Welcome to adventure"+bcolours.ENDC)
    name = input(bcolours.questions+"What is your name?"+bcolours.ENDC)
    print("Hello", name, "welcome to adventure")
    print(bcolours.header +"Create your own story!"+bcolours.ENDC)
    
    def choice3b():
        print(bcolours.comments+"Since you lost your friend challenges you to dive from the board")
        print("I hope you've dived before!")
        print("(well if you don't i can help you)")
        print("here are some diving instructions"+bcolours.ENDC)
        print(bcolours.options+"1. bend knees")
        print("2. point arms")
        print("3. look down")
        print("4. Jump"+bcolours.ENDC)
        print(bcolours.comments+"Make sure you do these in order"+bcolours.ENDC)
        print("""

















            """)
        print(bcolours.comments+"Are your ready to jump?"+bcolours.ENDC)
        print(bcolours.questions+"What do you do first?"+bcolours.ENDC)
        print(bcolours.options+"1. Jump")
        print("2. bend knees, point arms, look down"+bcolours.ENDC)
        dive = input("Enter here")
        if dive == "1":
            print(bcolours.comments+'Without preparing you jump on the board')
            print("You fall")
            time.sleep(1)
            print("down")
            time.sleep(1)
            print("down")
            time.sleep(1)
            print("down")
            print("You land with a huge splash")
            print("That's not a dive your friend says")
            print("You both head home together")
            print("I hope you had a fun day!"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            title()
        elif dive == "2":
            print(bcolours.comments+'with the proper preparation you jump off the board')
            print("you fall fast through the air")
            print("You enter the water with no splash")
            print("PERFECT DIVE!!!")
            print('Your friend congradulates you on your amazing dive')
            ("What a fun day with your friend")
            ("You walk home with your friend and get icecream on the way"+bcolours.ENDC)
            flavour = input(bcolours.questions+"What flavour did you get?"+bcolours.ENDC)
            print(flavour,bcolours.comments+"! That's my favourite to!")
            print("I hope you had a great day!"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            title()
    def choice3a():
        print(bcolours.comments+"Since you won you get to make your friend do somthing")
        print("what do you want him to do?")
        print("After some thought you tell him to do a huge cannonball off the diving board")
        print("Your friend runs up the ladder and does a huge belly flop"+bcolours.ENDC)
        time.sleep(3)#3sec delay 
        print(bcolours.comments+"""
             _______  _______  _        _______  _______          
            (  ____ \(  ____ )( \      (  ___  )(  ____ \|\     /|
            | (    \/| (    )|| (      | (   ) || (    \/| )   ( |
            | (_____ | (____)|| |      | (___) || (_____ | (___) |
            (_____  )|  _____)| |      |  ___  |(_____  )|  ___  |
                  ) || (      | |      | (   ) |      ) || (   ) |
            /\____) || )      | (____/\| )   ( |/\____) || )   ( |
            \_______)|/       (_______/|/     \|\_______)|/     \|
                                                      
         """+bcolours.ENDC)
        playsound('splash.wav')
        ("What a fun day with your friend")
        ("You walk home with your friend and get icecream on the way")
        flavour = input(bcolours.questions+"What flavour did you get?"+bcolours.ENDC)
        print(flavour,bcolours.comments+"! That's my favourite to!")
        print("I hope you had a great day!"+bcolours.ENDC)
        print(bcolours.header+split+bcolours.ENDC)
        title()

    def choice2():
        print(bcolours.comments+"I like the pool to its very cool")
        print("Funny right?")
        print("Nevermind")
        print("You arrive at the pool and step inside"+bcolours.ENDC)
        print(bcolours.questions+"Your friend is their to")
        friend = input("What's your friends name?"+bcolours.ENDC)
        print(friend,bcolours.comments+"challenges you to a game of rock, paper, scissors"+bcolours.ENDC)
        print(bcolours.questions+"What do you choose?"+bcolours.ENDC)
        print(bcolours.options+"Enter 1 for rock")
        print("2 for paper")
        print("3 for scissors"+bcolours.ENDC)
        gamechoice = input("You chose")
        if gamechoice == "1":
            print(bcolours.comments+"You both put out rock its a tie, try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            choice2()
        elif gamechoice == "2":
            print(bcolours.correct+"You put out paper, your friend put out rock")
            print("You win!"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            choice3a()
        elif gamechoice == "3":
            print(bcolours.wrong+"You put out sicssors")
            time.sleep(2)
            print("tough luck your friend put out rock you lost"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            choice3b()
        else:
            print("please try again")
            print(bcolours.header+split+bcolours.ENDC)
            choice2()

    def choice1():
        print(bcolours.questions+"What do you want to do today?"+bcolours.ENDC)
        print(bcolours.options+"1. Go to the pool")
        print("2. Go to the park")
        print("3. Play video games "+bcolours.ENDC)
        answer = input("Input here")
        if answer == "1":
             print(bcolours.comments+"Ok sure lets go"+bcolours.ENDC)
             print(bcolours.header+split+bcolours.ENDC)
             choice2()
            
        elif answer == "2":
             print (bcolours.comments+"Sure lets go"+bcolours.ENDC)
             print("")
             print(bcolours.wrong+"Wait..the park's overun with giraffes, How'd that happen"+bcolours.ENDC)
             print(bcolours.comments+"sorry we have to do somthing else"+bcolours.ENDC)
             
             choice1()

        elif answer == "3":
             print (bcolours.comments+"Well your already playing one so... Have fun")
             print("But here's a puzzle to keep you busy"+bcolours.ENDC)
             print(bcolours.options+"Playing On Two Apple Tablets Obviously"+bcolours.ENDC)
             potato = input("Enter the capiltaization of each word and press enter")
             if potato == "potato" or potato =="POTATO":
                 print(bcolours.comments+"Haha you said potato, I like potatos. :)")
                 print("Here's your prize....")
                 time.sleep(5)
                 print("ABSOLUTLY NOTHING")
                 print("What did you expect")
                 print("Now go do somthing else"+bcolours.ENDC)
                 print(bcolours.header+split+bcolours.ENDC)
                 choice1()

             else: 
                 print(bcolours.wrong+"Invalid please try again"+bcolours.ENDC)
                 print(bcolours.header+split+bcolours.ENDC)
                 choice1()
        else:
            print(bcolours.wrong+"please try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            choice1()
    
    choice1()

def game():
    score = 0 
    print(bcolours.header +"Well you know how to play the game now..."+bcolours.ENDC)
    print(bcolours.header +"WELCOME TO THE QUIZ"+bcolours.ENDC)
    print(bcolours.comments+"you will be scored on this quiz whats the highest you can get"+bcolours.ENDC)
    print(bcolours.comments+"be in the shoes of jabari and relieve his day"+bcolours.ENDC)
    print(bcolours.questions+"Here is the first question"+bcolours.ENDC)
    def endgame():
        nonlocal score
        print("Your score was", score,".")
        playsound('clapping.mp3')
        print("With your help")
        print("Jabari took a deep breath and spread")
        print("his arms and bent his knees.")
        print("")
        print("Then he sprang up!")
        print("")
        print("Up off the board!")
        print("Flying!")
        print("And he came down with a huge")
        splash = """
             _______  _______  _        _______  _______          
            (  ____ \(  ____ )( \      (  ___  )(  ____ \|\     /|
            | (    \/| (    )|| (      | (   ) || (    \/| )   ( |
            | (_____ | (____)|| |      | (___) || (_____ | (___) |
            (_____  )|  _____)| |      |  ___  |(_____  )|  ___  |
                  ) || (      | |      | (   ) |      ) || (   ) |
            /\____) || )      | (____/\| )   ( |/\____) || )   ( |
            \_______)|/       (_______/|/     \|\_______)|/     \|
                                                      
         """
        print(bcolours.comments+splash+bcolours.ENDC)
        playsound('splash.wav')
        print(bcolours.header+"Thanks for Playing!!!!"+bcolours.ENDC)
        playsound('clapping.mp3')
        print(bcolours.header+split+bcolours.ENDC)
        title()

    def quiz6():
        nonlocal score
        print(bcolours.questions+"Last question: What does Jabari say when he gets to the end of the board?"+bcolours.ENDC)
        print(bcolours.options+"1. I love hippos")
        print("2. I'm tired")
        print("3. I love suprises")
        print("4. I can do this"+bcolours.ENDC)
        answer = input("Enter answer here")
        if answer == "1":
             print("Not hippos...")
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz6()
            
        elif answer == "2":
             print (bcolours.wrong+"No, he's not feeling tired ")
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz6()

        elif answer == "3":
             print (bcolours.correct+"Who doesn't love suprises?"+bcolours.ENDC)
             playsound('clapping.mp3')
             print(bcolours.header+split+bcolours.ENDC)
             score += 1
           
             endgame()
        elif question == "4":
             print (bcolours.wrong+"He can do this but that's not what he says")
             print("please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz6()
        else: 
            print("Invalid please try again")
            playsound('wrong.wav')
            print(bcolours.header+split+bcolours.ENDC)
            quiz6()
    def quiz5():
        nonlocal score
        print(bcolours.questions+"How is Jabari feeling at the top of the diving board"+bcolours.ENDC)
        print(bcolours.options+"1. Happy")
        print("2. Sad")
        print("3. Angry")
        print("4. Scared"+bcolours.ENDC)
        answer = input("Enter answer here")
        if answer == 1:
             print(bcolours.wrong+"Maybe a little happy, try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz5()
            
        elif answer == "2":
             print (bcolours.wrong+"No he's not sad, he's about to jump!")
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz5()

        elif answer == "3":
             print (bcolours.wrong+"Angry? at what")
             print("please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
           
             quiz5()
        elif answer == "4":
             print (bcolours.correct+"Yes, Jabari feels a little scared but everyone does to sometimes")
             playsound('clapping.mp3')
             print("Jabari stands atop the diving board"+bcolours.ENDC)
             print(bcolours.header+split+bcolours.ENDC)
             score += 1
             quiz6()
        else: 
            print("Invalid please try again")
            playsound('wrong.wav')
            print(bcolours.header+split+bcolours.ENDC)
            quiz5()

    def quiz4():
        nonlocal score
        print(bcolours.questions+"Jabari walks up to the diving board, what does he do?")
        print("What is the order of things jabari does when he gets to the ladder"+bcolours.ENDC)
        print(bcolours.options+"1. Wait and let others go infront of him")
        print("2. Do streches")
        print("3. Start climbing the ladder")
        print("4. Talk to his dad and take a rest"+bcolours.ENDC)

        answer = input("Enter the order of events here, make sure its in a row like 1234")
        if answer == "1342":
            print(bcolours.comments+"Nice job, After streches Jabari climbs up the ladder and reaches the top"+bcolours.ENDC)
            playsound('clapping.mp3')
            print(bcolours.header+split+bcolours.ENDC)
            quiz5()
        else:
            print("Please try again")
            playsound('wrong.wav')
            print(bcolours.header+split+bcolours.ENDC)
            quiz4()


    def quiz3():
        nonlocal score
        print(bcolours.header+"Alright you made it to the pool!")
        print("Jabari looks around"+bcolours.ENDC)
        print(bcolours.questions+"What does he want to do?"+bcolours.ENDC)
        print(bcolours.options+"1. Jump off the diving board")
        print("2. Race his friends")
        print("3. Do a flip underwater")
        print("4. Swim laps around the pool"+bcolours.ENDC)
        answer = input("Enter here")
        if answer == "1":
             print(bcolours.correct+"Of Course! The diving board looks so fun and Jabari wants to jump!"+bcolours.ENDC)
             playsound('clapping.mp3')
             print(bcolours.header+split+bcolours.ENDC)
             score += 1
             quiz4()
            
        elif answer == "2":
             print (bcolours.wrong+"Hmm maybe he might want to later")
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz3()

        elif answer == "3":
             print (bcolours.wrong+"Do a flip, pretty hard and i don't know if Jabari can do one?")
             print("please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
           
             quiz3()
        elif question == "4":
             print (bcolours.wrong+"But that's boring...")
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz3()
        else: 
             print("Invalid please try again")
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             quiz3()
    

    def quiz2():
        nonlocal score
        print(bcolours.comments+"Nice, Here is the next question"+bcolours.ENDC)
        print(bcolours.questions+"Jabari arrives at the pool, but the door is locked with a passcode"+bcolours.ENDC)
        print(bcolours.comments+"Jabari looks around and sees a sign, it says"+bcolours.ENDC)
        print(bcolours.comments+"The pool passcode is: 0922")
        print("remember it?"+bcolours.ENDC)
        time.sleep(5)
        #space to clear the screen so the player cannot see the code
        print("""








            












            


















           













            









            """)
        answer = input("Enter in the passcode here")
        if answer == "0922":
            print(bcolours.correct+"Nice job you can now go swimming"+bcolours.ENDC)
            playsound('clapping.mp3')
            print(bcolours.header+split+bcolours.ENDC)
            score += 1
            quiz3()
        else:
            print(bcolours.wrong+"Please try again"+bcolours.ENDC)
            playsound('wrong.wav')
            print(bcolours.header+split+bcolours.ENDC)
            score -= 1
            quiz2()
    def quiz1():
         nonlocal score
         print(bcolours.questions+"First question: What does Jabari want to do?"+bcolours.ENDC)
         print(bcolours.options+"1. Get icecream")
         print("2. Go for a bike ride")
         print("3. Go swimming")
         print("4. Do nothing"+bcolours.ENDC)
         answer = input("please inert your answer here")
         if answer == "1":
             print(bcolours.wrong+"Not quite but he proably likes ice cream"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz1()
            
         elif answer == "2":
             print (bcolours.wrong+"Hmm maybe he might want to later")
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             score -= 1
             quiz1()

         elif answer == "3":
             print (bcolours.correct+"Good Job, Jabari loves swimming"+bcolours.ENDC)
             playsound('clapping.mp3')
             print(bcolours.header+split+bcolours.ENDC)
             score += 1
             quiz2()
         elif answer == "4":
             print (bcolours.wrong+"But that's boring...")
             score -= 1
             print("Please try again"+bcolours.ENDC)
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             quiz1()
         else: 
             print("Invalid please try again")
             playsound('wrong.wav')
             print(bcolours.header+split+bcolours.ENDC)
             quiz1()
    quiz1()



    
    #indepth tutorial that will let the user learn how to play the game and adventure modes
def tutorial():
    print(bcolours.comments+"You will see a few types of questions playing this game this tutorial will teach you how to play."+bcolours.ENDC)
    print(bcolours.header+"first question: Multiple choice")
    print("choose the choice that is correct"+bcolours.ENDC)
    def question3():
         print(bcolours.comments+"okay good job finally making it here")
         print("last question: A puzzle")
         print("you will be given a piece of text and you need to find the code"+bcolours.ENDC)
         print(bcolours.questions+"here it is:"+bcolours.ENDC)
         print(bcolours.comments+"(the code is answer)"+bcolours.ENDC)
         code = input("Enter the code here or press 1 for a hint")
         if code == "1":
             print(bcolours.comments+"look at the last word"+bcolours.ENDC)
             print(bcolours.header+split+bcolours.ENDC)
             question3()
         elif code == "answer":
             print(bcolours.correct+"Nice that was hard, but now your ready to play the game"+bcolours.ENDC)
             print(bcolours.header+split+bcolours.ENDC)
             title()
    def question2():#second type of question ordering 
         print("""








            """)
         print(bcolours.comments+"Huh.. so i guess your pretty smart you know what 1+1 is. Trust me this next one will be much harder")
         print("jk its still easy"+bcolours.ENDC)
         print(bcolours.questions+"Here is a different type of question: Ordering")
         print("You will see a number every line put them in the order you see them to get the question right"+bcolours.ENDC)
         print(bcolours.options+"1")
         print("2")
         print("3")
         print("4")
         print("5"+bcolours.ENDC)
         order = input("Print the answer here")#input is taken as a set of strings which is the order of the numebers
         if order == "12345":#check if its true
            print(bcolours.correct+"correct"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question3()#calls next question 
         else:#recalls the question if wrong or invalid
            print(bcolours.wrong+"Please try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question2()
    #example layout of a question found in game
    def question1(): 
        print("""








            """)
        
        print(bcolours.questions+"What is 1 + 1? (pretty simple right?)"+bcolours.ENDC)#question is asked
        print(bcolours.options+"1. 2")#options are given and player inputs answer as a number
        print("2. 4")
        print("3. 5")
        print("4. Window"+bcolours.ENDC)
        question = input("Enter your answer here")#Input is taken in assigned to a variable as a string
        if question == "1": #this uses selection to determine which input is the write answer
            print(bcolours.correct+"Nice good job: Moving on"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question2()
            
        elif question == "2":
            print (bcolours.wrong+"4? I asked 1 + 1")
            print("Please try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question1()

        elif question == "3":
            print (bcolours.wrong+"The most obvious choice definenly the correct answer....not")
            print("Please try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question1()
        elif question == "4":
            print (bcolours.comments+"Window |+|? LOL WRONG")
            print("Please try again"+bcolours.ENDC)
            print(bcolours.header+split+bcolours.ENDC)
            question1()
         
            
        else:#failsafe incase the player enters in the wrong number
            print ("Invalid:Please choose a number")
            print("Please try again")
            print(bcolours.header+split+bcolours.ENDC)
            question1()
    question1() 
#title page: This is where the player will land and the different fuctions above will be called
def title():
#splash of ascii art
    mySplash = """
       ___       _                _                
      |_  |     | |              (_)               
        | | __ _| |__   __ _ _ __ _                
        | |/ _` | '_ \ / _` | '__| |               
    /\__/ / (_| | |_) | (_| | |  | |               
    \____/ \__,_|_.__/ \__,_|_|  |_|               
                                                 
                                                 
       ___                                         
      |_  |                                     
        | |_   _ _ __ ___  _ __  ___               
        | | | | | '_ ` _ \| '_ \/ __|              
    /\__/ / |_| | | | | | | |_) \__ \              
    \____/ \__,_|_| |_| |_| .__/|___/              
                        | |                      
                        |_|                      
    _____ _            _____                      
    |_   _| |          |  __ \                     
      | | | |__   ___  | |  \/ __ _ _ __ ___   ___ 
      | | | '_ \ / _ \ | | __ / _` | '_ ` _ \ / _ \

      | | | | | |  __/ | |_\ \ (_| | | | | | |  __/
      \_/ |_| |_|\___|  \____/\__,_|_| |_| |_|\___|
    """

    print(bcolours.header +mySplash + bcolours.ENDC)
    print(bcolours.header +"Press 1 for Jabari Quiz"+bcolours.ENDC)
    print(bcolours.header +"Press 2 for Choose your own Adventure"+bcolours.ENDC)
    print(bcolours.header +"Press 3 For Tutorial"+bcolours.ENDC)
    print(bcolours.comments+"Press Enter to close"+bcolours.ENDC)
    category = input()#selection
    if category == "1":
     print(bcolours.header +"Welcome to the quiz!" + bcolours.ENDC)
     game()#Calls quiz or "game" function
     
        
    elif category == "2":
     print (bcolours.header +"Welcome to Choose your own adventure" + bcolours.ENDC)
     
     adventure()#Calls choose your own adventure

    elif category == "3":
     print (bcolours.header + "Here's the tutorial!" + bcolours.ENDC)
     
     tutorial()#tutorial is here
        
    else:
      return 
     
     

title()#Small but this starts the code