import manage as m 
import check 

STORY = "success_story.txt"

#The screen is at the begin of the program, or after its options finish (log-in, sign up)
def welcomeScreen():
    #read the data from a text file
    with open(STORY) as file:
        for line in file:
            print(line, end="")
            print()
    print()
    print("Select one of the below options:\n")
    print("(1) Log-in to an existing account") #log-in
    print("(2) Sign up a new InCollege account") # sign up
    print("(3) Find someone that you know")
    print("(4) Play the video")
    print("(5) Exit the program")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,5)

    if(choice == "1"):
        manage = m.Manage() #create a new object Manage
        name = manage.log_in() #get user's name after loging in successful
        if name == None: #if the user fails when loging in the account
            welcomeScreen()
        else:
            log_in_Screen(name)
    elif(choice == "2"):
        sign_up_Screen()
    elif (choice == "3"):
        join_Incollege_Screen()
    elif (choice == "4"):
        print("\nVideo is now playing!\n")
        welcomeScreen()
    elif(choice == "5"):
        return
    

#Displays 5 skills that the user can learn (all of which return "under construction"). The user is also allowed to not choose a skill, which will bring the user back to the welcome screen by calling welcomeScreen.
def learnSkill_Screen(name):
    print()
    print("Select one of the below options:")
    print("(1) Learn resume-building")
    print("(2) Learn interview tips")
    print("(3) Learn dress code")
    print("(4) Learn writing etiquette")
    print("(5) Learn suggested technology")
    print("(6) Come Back Log in Screen!")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,6)

    if(choice == "1"):
        print("under construction")
        learnSkill_Screen(name)
    elif(choice == "2"):
        print("under construction")
        learnSkill_Screen(name)
    elif(choice == "3"):
        print("under construction")
        learnSkill_Screen(name)
    elif(choice == "4"):
        print("under construction")
        learnSkill_Screen(name)
    elif(choice == "5"):
        print("under construction")
        learnSkill_Screen(name)
    elif(choice == "6"):
        log_in_Screen(name)
        

#The screen after the user log in successfully
def log_in_Screen(name):
    print()
    print("Select one of the below options:")
    print("(1) Post Job")
    #print("(2) Apply Job")
    print("(2) Search Job")
    print("(3) Join Friend")
    print("(4) New Skill")
    print("(5) Sign Out")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,5)
    
    if(choice == "1"): 
        manage = m.Manage()
        manage.new_job(name)
        log_in_Screen(name)
    elif(choice == "2"):
        print("\nUnder Construction")
        log_in_Screen(name)
    elif(choice == "3"):
        print("\nunder Construction")
        log_in_Screen(name)
    elif(choice == "4"):
        learnSkill_Screen(name)
    elif(choice == "5"):
        welcomeScreen()


def sign_up_Screen():
    manage = m.Manage()
    name = manage.new_account()
    if name != None: #sign up successfully
       log_in_Screen(name)
    else: 
        print()
        print("Select one of the below options:")
        print("(1) Sign Up Again! ")
        print("(2) Do Not Sign Up. Come Back Home Screen!")
        choice = input("Your selection: ")

        #check the right value of input from user
        choice = check.check_option(choice,1,2)

        if(choice == "1"):
            sign_up_Screen()
        elif (choice == "2"):
            welcomeScreen()
    
#The screen after choose find a friend from home screen
def join_Incollege_Screen():
    manage = m.Manage()
    #promp from the users for first and last name of their friend
    first = input("Enter first name of your friend: ")
    last = input("Enter last name of your friend: ")
    manage.find_people(first, last)
    print()
    print("Select one of the below options:")
    print("(1) Log in")
    print("(2) Sign up")
    print("(3) Come Back Home Screen!")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,3)
    
    if(choice == "1"):
        manage = m.Manage()
        name = manage.log_in() 
        if name == None: #if the user fails when loging in the account
            welcomeScreen()
        else: #log in successfully
            log_in_Screen(name)
    elif(choice == "2"):
        sign_up_Screen()
    elif (choice == "3"):
        welcomeScreen()





