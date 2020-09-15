#
#Team Michigan Requirement Epic #1 File
#This program is an early model of the InCollege application.
#Presents user with an initial screen and provides five different options.
#5 unique student accounts can be saved and accessed by the application.
#Job/Internship and "someone you know" options both return "under construction".
#"Learn a new skill" presents a list of made-up skils that also return "under construction",
#

#function learnSkill
#no inputs
#Displays 5 skills that the user can learn (all of which return "under construction"). The user is also allowed to not choose a skill, which will bring the user back to the welcome screen by calling welcomeScreen.
def learnSkill():
    print()
    print("Select one of the below options:")
    print("(1) Learn resume-building")
    print("(2) Learn interview tips")
    print("(3) Learn dress code")
    print("(4) Learn writing etiquette")
    print("(5) Learn suggested technology")
    print("(6) Return")
    choice = input("Your selection: ")
    if(choice == "1"):
        print("under construction")
    elif(choice == "2"):
        print("under construction")
    elif(choice == "3"):
        print("under construction")
    elif(choice == "4"):
        print("under construction")
    elif(choice == "5"):
        print("under construction")
    elif(choice == "6"):
        print()
        welcomeScreen()

#function topLevel
#no inputs
#Displays the options available at the top level, asks the user to select one, and performs the corresponding action. At the moment, only the "Learn a new skill" option returns something other than "under construction" by running the learnSkill function.
def welcomeScreen():
    print("Select one of the below options:")
    print("(1) Log-in to an existing account")
    print("(2) Create a new InCollege account")
    print("(3) Search for a job or internship")
    print("(4) Find someone that you know")
    print("(5) Learn a new skill")
    choice = input("Your selection: ")
    if(choice == "1"):
        print("under construction")
    elif(choice == "2"):
        print("under construction")
    elif(choice == "3"):
        print("under construction")
    elif(choice == "4"):
        print("under construction")
    elif(choice == "5"):
        learnSkill()


print("Welcome to InCollege.")
welcomeScreen()
