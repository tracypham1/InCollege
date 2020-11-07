import manage as m 
import check 
import csv
import os.path
from datetime import datetime
from datetime import timedelta

FILENAME_STD = "student_data.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_STG = "settings.csv"
FILENAME_POL = "policy.csv"
FILENAME_PRO = "profiles.csv"
FILENAME_FRI = "friends.csv"
FILENAME_REQ = "requests.csv"
FILENAME_APP = "applications.csv"
FILENAME_MES = "pending_messages.csv"
FILENAME_SAVE_MES = "messages.csv"
FILENAME_NEW_USER = "new_user.csv"
FILENAME_NEW_JOB = "new_jobs_notif.csv"
FILENAME_NEW_JOB = "new_jobs.csv"
FILENAME_DEL_JOB = "del_jobs_notif.csv"
STORY = "success_story.txt"
empty_string = " "

#The screen is at the begin of the program, or after its options finish (log-in, sign up)
def welcomeScreen():    
    #read the data from a text file
    with open(STORY) as file:
        for line in file:
            print(line, end="")
            print()
    if(not os.path.exists("requests.csv")):
        open("requests.csv", 'w').close()
    if(not os.path.exists("friends.csv")):
        open("friends.csv", 'w').close()
    if(not os.path.exists(FILENAME_MES)):
        open(FILENAME_MES, 'w').close()
    if(not os.path.exists(FILENAME_SAVE_MES)):
        open(FILENAME_SAVE_MES, 'w').close()
    if (not os.path.exists(FILENAME_NEW_USER)):
        open(FILENAME_NEW_USER, 'w').close()
    if(not os.path.exists(FILENAME_NEW_JOB)): 
        open(FILENAME_NEW_JOB, 'w').close()

    print()
    print("Select one of the below options:\n")
    print("(1) Log-in to an existing account") #log-in
    print("(2) Sign up a new InCollege account") # sign up
    print("(3) Find someone that you know")
    print("(4) Play the video")
    print("(5) Useful links")
    print("(6) Important links")
    print("(7) Exit the program")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,7)

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
    elif (choice == "5"):
        usefulLinks_Screen(0,empty_string)
    elif (choice == "6"):
        importantLinks_Screen(0, empty_string)
    elif (choice == "7"):
        return


def importantLinks_Screen(num, name):
    print()
    print("Important Links: Select one of the below options:")
    print("(1) A Copyright Notice")
    print("(2) About")
    print("(3) Accessibility")
    print("(4) User Agreement")
    print("(5) Privacy Policy")
    print("(6) Cookie Policy")
    print("(7) Copyright Policy")
    print("(8) Brand Policy")
    print("(9) Go back to previous screen")
    choice = input("Your selection: ")

    # check the right value of input from user
    choice = check.check_option(choice, 1, 9)

    if (choice == "1"):
        policy(num, name, choice)
    elif (choice == "2"):
        policy(num, name, choice)
    elif (choice == "3"):
        policy(num, name, choice)
    elif (choice == "4"):
        policy(num, name, choice)
    elif (choice == "5"):
        privacy_policy(num, name)
    elif (choice == "6"):
        policy(num, name, choice)
    elif (choice == "7"):
        policy(num, name, choice)
    elif (choice == "8"):
        policy(num, name, choice)
    elif (choice == "9"):
        if num == 0:
            welcomeScreen()
        elif num == 1:
            log_in_Screen(name)


def policy(num, name, selection):
    #helper variables
    lines = list()
    blank = []
    count = 0

    with open(FILENAME_POL, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (row != blank):
                lines.append(row)
                count = count + 1
            for field in row:
                if(field == selection):
                    pol = lines[count-1][1]
                    print()
                    print(pol)
    
    if(selection != "5"):
        #option to return to screen before
        print()
        print("Select one of the below options:")
        print("(1) Go back to previous screen: Important Links")
        choice = input("Your selection: ")

        # check the right value of input from user
        choice = check.check_option(choice, 1, 1)

        if (choice == "1"):
            importantLinks_Screen(num, name)
    



def privacy_policy(num, name):
    #display privacy policy 
    policy(num, name, "5")

    if num == 0:
        print("Sign in for Guest Controls and Language Features")
        print("(1) Go back to Important links")
        choice = input("Your selection: ")

        # check the right value of input from user
        choice = check.check_option(choice, 1, 1)

        if (choice == "1"):
            importantLinks_Screen(num, name)

    elif num == 1: #signed in user will be able to choose guest controls or change language
        print()
        print("Privacy Policy: Select one of the below options:")
        print("(1) Guest Controls")
        print("(2) Language")
        print("(3) Go back to previous screen: Important Links")
        choice = input("Your selection: ")

        # check the right value of input from user
        choice = check.check_option(choice, 1, 3)

        if (choice == "1"):
            guest_controls(num, name)
        elif (choice == "2"):
            language(num, name)
        elif (choice == "3"):
            importantLinks_Screen(num, name)


def guest_controls(num, name):

    #helper variables
    lines = list()
    entry = [" ", " ", " ", " ", " "]
    blank = []
    count = 0

    #read current language setting and fill 'lines' with info
    with open(FILENAME_STG, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank: #or else there will be stupid amount of white space
                lines.append(row)
                count = count + 1
            for field in row: 
                if (field == name):
                    entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                    lines.pop()
                    count = count - 1

    #display to user and allow to set
    print()
    print("Email Feature is currently", entry[1])    
    print("SMS Feature is currently", entry[2])
    print("Targeted Advertising Feature is currently", entry[3])
    print("Select one of the below options:")
    print("(1) Toggle Email Feature")
    print("(2) Toggle SMS Feature")
    print("(3) Toggle Targeted Advertising Feature")
    print("(4) Go back to previous screen: Privacy Policy")
    choice = input("Your selection: ")

    # check the right value of input from user
    choice = check.check_option(choice, 1, 4)

    if (choice == "1"):
        if (entry[1] == "on"):
            entry[1] = "off"
        else: 
            entry[1] = "on"
        lines.append(entry)
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        guest_controls(num, name)
    elif (choice == "2"):
        if (entry[2] == "on"):
            entry[2] = "off"
        else: 
            entry[2] = "on"
        lines.append(entry)
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        guest_controls(num, name)
    elif (choice == "3"):
        if (entry[3] == "on"):
            entry[3] = "off"
        else: 
            entry[3] = "on"
        lines.append(entry)
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        guest_controls(num, name)
    elif (choice == "4"):
        privacy_policy(num, name)


#name is the unique username of the user
#display language and allow to change
def language(num, name):

    #helper variables
    lines = list()
    entry = [" ", " ", " ", " ", " "]
    blank = []
    count = 0

    #read current language setting and fill 'lines' with info
    with open(FILENAME_STG, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank: #or else there will be stupid amount of white space
                lines.append(row)
                count = count + 1
            for field in row: 
                if (field == name):
                    entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                    lines.pop()
                    count = count - 1

    #display to user and allow to set
    print()
    print("Language is currently set to", entry[4])
    print("Select one of the below options:")
    print("(1) Set to English")
    print("(2) Set to Spanish")
    print("(3) Go back to previous screen: Privacy Policy")
    choice = input("Your selection: ")

    # check the right value of input from user
    choice = check.check_option(choice, 1, 3)

    if (choice == "1"):
        entry[4] = "English"
        lines.append(entry)
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        language(num, name)
    elif (choice == "2"):
        entry[4] = "Spanish"
        lines.append(entry)
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        language(num, name)
    elif (choice == "3"):
        lines.append(entry)
        #add entry back to list
        #overwrite
        with open(FILENAME_STG, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        privacy_policy(num, name)


def usefulLinks_Screen(num, name):
    print()
    print("Select one of the below options:")
    print("(1) General")
    print("(2) Browse InCollege")
    print("(3) Business solutions")
    print("(4) Directories")
    print("(5) Go back to previous screen")
    choice = input("Your selection: ")

    # check the right value of input from user
    choice = check.check_option(choice, 1, 5)

    if (choice == "1"):
        generalLinks_Screen(num,name)
    elif (choice == "2"):
        print("\nunder construction")
        usefulLinks_Screen(num, name)
    elif (choice == "3"):
        print("\nunder construction")
        usefulLinks_Screen(num, name)
    elif (choice == "4"):
        print("\nunder construction")
        usefulLinks_Screen(num,name)
    elif (choice == "5"):
        if num == 0:
            welcomeScreen()
        elif num == 1:
            log_in_Screen(name)


def generalLinks_Screen(num, name):
    print()
    print("Select one of the below options:")
    print("(1) Sign up")
    print("(2) Help Center")
    print("(3) About")
    print("(4) Press")
    print("(5) Blog")
    print("(6) Careers")
    print("(7) Developers")
    print("(8) Back to UsefulLinks screen")

    choice = input("Your selection: ")

    # check the right value of input from user
    choice = check.check_option(choice, 1, 8)

    if (choice == "1"):
        sign_up_Screen()
    elif (choice == "2"):
        print("\nWe're here to help")
        generalLinks_Screen(num,name)
    elif (choice == "3"):
        print("\nInCollege: Welcome to In College, \n the world's largest college student network \n with many users in many countries and territories world wide")
        generalLinks_Screen(num,name)
    elif (choice == "4"):
        print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports" )
        generalLinks_Screen(num,name)
    elif (choice == "5"):
        print("\nunder construction")
        generalLinks_Screen(num,name)
    elif (choice == "6"):
        print("\nunder construction")
        generalLinks_Screen(num,name)
    elif (choice == "7"):
        print("\nunder construction")
        generalLinks_Screen(num,name)
    elif (choice == "8"):
        usefulLinks_Screen(num, name)


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

    print("Enter 1 to see all notifications. Enter 0 to continue")
    pick = input("Your selection: ")
    pick = check.check_option(pick, 0, 1)
    if pick == "1":
        check_requests(name)
        check_application(name)
        check_application(name)
        check_messages(name)
        check_profile_creation(name)
        #check_new_user(name)
        check_applied_in_seven_days(name)
        check_new_job(name)
        check_del_job(name)

    check_new_user(name)

    print()
    print("Select one of the below options:")
    print("(1) Post Job")
    print("(2) Delete Job")
    print("(3) Search Jobs")
    print("(4) Create Profile")
    print("(5) View Profile")
    print("(6) Search for friends to connect with")
    print("(7) Show my network")
    print("(8) New Skill")
    print("(9) Useful links")
    print("(10) Important links")
    print("(11) Send Message")
    print("(12) Sign Out")
    choice = input("Your selection: ")

    #check the right value of input from user
    choice = check.check_option(choice,1,12)
    
    if(choice == "1"): 
        manage = m.Manage()
        manage.new_job(name)
        log_in_Screen(name)
    elif (choice == "2"):
        manage = m.Manage()
        list_title_job = [] # keep the titles of jobs that the user posted
        for element in manage.get_list_job():
            if element.get_post_name() == name:
                list_title_job.append(element.get_title())
        
        if len(list_title_job) != 0:
            print("\nThis is the list of jobs that you posted: ")
            count = 0
            for element in list_title_job:
                count +=1
                print(str(count) + ": " + element)
            
            for element in list_title_job:
                print()
                print("Do you want to delete the job with title: " + "\"" +element + "\"")
                print ("Select one of the below option:")
                print("(1) Yes")
                print("(2) No")
                choice = input("Your selection: ")
                #check the right value of input from user
                choice = check.check_option(choice,1,2)
                if choice == "1":
                    manage.delete_job(name, element)
                else:
                    pass
        else:
            print("\nYou didn't post any job in the system!")      
        log_in_Screen(name)
    elif(choice == "3"):
        job_Screen(name)
    elif(choice == "4"):
        manage = m.Manage()
        manage.createProfile(name)
        choice = input("\nEnter 1 to return to previous screen: ")
        #check that input has an acceptable value
        choice = check.check_option(choice,1,1)
        log_in_Screen(name)
    elif(choice == "5"):
        manage = m.Manage()
        manage.viewProfile(name)
        choice = input("\nEnter 1 to return to previous screen: ")
        #check that input has an acceptable value
        choice = check.check_option(choice,1,1)
        log_in_Screen(name)
    elif(choice == "6"):
        student_Search_Console(name)
        log_in_Screen(name)    
    elif (choice == "7"):
        show_Network(name)
    elif(choice == "8"):
        learnSkill_Screen(name)
    elif(choice == "9"):
        usefulLinks_Screen(1,name)
    elif(choice == "10"):
        importantLinks_Screen(1, name)
    elif(choice == "11"):
        send_message(name)
    elif(choice == "12"):
        welcomeScreen()

def sign_up_Screen():
    manage = m.Manage()
    name = manage.new_account()
    lines = list()
    if name != None: #sign up successfully
       with open(FILENAME_NEW_USER, "w") as file:
           writer_csv = csv.writer(file)
           lines.append(name)
           lines.append("first")
           writer_csv.writerow(lines)
       log_in_Screen(name)
       #add name to new_user file

    else: 
        print()
        print("Select one of the below options:")
        print("(1) Sign Up Again! ")
        print("(2) Do Not Sign Up. Come Back Home Screen!")
        choice = input("Your selection: ")

        #check that user input has an acceptable value
        choice = check.check_option(choice,1,2)

        if(choice == "1"):
            sign_up_Screen()
        elif (choice == "2"):
            welcomeScreen()
    
def join_Incollege_Screen():
    manage = m.Manage()
    #prompt the users for first and last name of their friend
    first = input("Enter first name of your friend: ")
    last = input("Enter last name of your friend: ")
    manage.find_people(first, last)
    print()
    print("Select one of the below options:")
    print("(1) Log in")
    print("(2) Sign up")
    print("(3) Go back to Home Screen")
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


def student_Search_Console(sign_name):
    manage = m.Manage()
    sent = 0
    choice = 0

    print()
    while sent == 0:
        results = list()
        entry = [" ", " ", " ", " "]
        print("Friend Search")
        print("Select one of the below options:")
        print("(1) Search by Last Name")
        print("(2) Search by University")
        print("(3) Search by Major")
        print("(4) Go back to previous screen: Log-in Screen")
        choice = input("Your selection: ")
        # check that user provided acceptable input
        choice = check.check_option(choice, 1, 4)

        if (choice == "1"):
            lname = input("Enter Last Name: ")
            print()
            names = list()
            names = manage.return_unames_from_last(lname)
            for uname in names:
                partialResults = list()
                partialResults = manage.return_students_from_uname(uname)
                for entry in partialResults:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sign_name, names)
        elif (choice == "2"):
            univ = input("Enter University: ")
            print()
            names = manage.return_unames_from_univ(univ)
            for uname in names:
                partialResults = list()
                partialResults = manage.return_students_from_uname(uname)
                for entry in partialResults:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sign_name, names)
        elif (choice == "3"):
            major = input("Enter Major: ")
            print()
            names = manage.return_unames_from_major(major)
            for uname in names:
                partialResults = list()
                partialResults = manage.return_students_from_uname(uname)
                for entry in partialResults:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sign_name, names)
        elif (choice == "4"):
            sent = 1

def check_requests(sign_name):
    manage = m.Manage()
    blank = []
    count = 0
    count2 = 0
    countReq = 0
    addUser1 = list()
    addUser2 = list()
    superLines = list()
    lines = list()
    lines2 = list()

    with open(FILENAME_REQ, 'r') as readFile:  
        reader2 = csv.reader(readFile)
        for row2 in reader2:
            if row2 != blank:
                lines2.append(row2)
                count2 = count2 + 1
                if lines2[count2-1][1] == sign_name:
                    countReq = countReq + 1
                
    if countReq > 0:
        
        print("You have one or more pending friend requests. Do you wish to review them?")
        print("Enter '1' if yes and '0' if no")
        choice = input("Your selection: ")
        # check that user provided acceptable input
        choice = check.check_option(choice, 0, 1)
        if choice == "1":
            with open(FILENAME_REQ, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        if(row[1] != sign_name):
                            superLines.append(row)

            with open(FILENAME_REQ, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        lines.append(row)
                        count = count + 1
                        if lines[count-1][1] == sign_name:
                            print()
                            print("You have a pending friend request from " + lines[count-1][0])
                            print("Do you accept it? Enter '1' for yes and '0' for no")
                            accept = input("Your selection: ")
                            accept = check.check_option(accept, 0, 1)
                            if accept == "1":
                                addUser1.append(sign_name)
                                addUser2.append(lines[count-1][0])

            i = 0
            while i < len(addUser1):
                manage.add_friend(addUser1[i], addUser2[i])
                i = i + 1
                
            with open(FILENAME_REQ, "w") as writeFile:
                writer = csv.writer(writeFile)
                for line in superLines:
                    writer.writerow(line)
                
############################## Show Network console ##################################

def show_Network(name):
    print()
    print("Select one of the below options:")
    print("(1) Check Friend Requests")
    print("(2) Show Friends List")
    print("(3) Display Friend Profile")
    print("(4) Remove Friend")
    print("(5) Return to Main Menu")
    choice = input("Your selection: ")
    print()

    if(choice == "1"):
        show_Requests(name)
    elif (choice == "2"):
        friend_List(name)
    elif (choice == "3"):
        display_Friend(name)
    elif (choice == "4"):
        remove_Friend(name)
    elif (choice == "5"):
        log_in_Screen(name)

def show_Requests(name):
    blank = []
    count2 = 0
    countReq = 0
    lines2 = list()

    with open(FILENAME_REQ, 'r') as readFile:  
        reader2 = csv.reader(readFile)
        for row2 in reader2:
            if row2 != blank:
                lines2.append(row2)
                count2 = count2 + 1
                if lines2[count2-1][1] == name:
                    countReq = countReq + 1
    print()
    if countReq == 0:
        print("No Pending Friend Requests")
    elif countReq > 0:
        print("Your pending friend requests are: ")
        with open('requests.csv', newline='') as f:
            reqReader = csv.reader(f)
            data = list(reqReader)
        with open('student_data.csv', newline='') as g:
            userReader = csv.reader(g)
            usernames = list(userReader)
        for request in data:    #checks all requests
            if name in request: #if user is found in a request
                index = request.index(name)    
                if index==0:
                    friend=1
                elif index==1:
                    friend=0
                uname=request[friend]
                num = -1
                for i in usernames:
                    num = num + 1
                    if(num%2==0):
                        if i[0]==uname:
                            print(i[2]+' '+i[3])
                            break
    show_Network(name)
    
    
def friend_List(name):
    with open(FILENAME_FRI, 'r') as my_file:
        is_blank = len(my_file.read().strip())
    if is_blank == 0:
        print("You currently do not have anyone added to your friends list.")
        log_in_Screen(name)
    else:
        with open('student_data.csv', newline='') as g:
            userReader = csv.reader(g)
            usernames = list(userReader)
        print("Your friends are: ")
        with open(FILENAME_FRI, newline='') as f:
            friReader = csv.reader(f)
            data = list(friReader)
        for user in data:    #checks all friends
            if name in user: #if user is found in a friend pairing
                index = user.index(name)    
                if index==0:
                    friend=1
                    uname=user[friend]
                    num = -1
                    for i in usernames: #searches through student data for first and last name
                        num = num + 1
                        if(num%2==0):
                            if i[0]==uname:
                                print(i[2]+' '+i[3])
                                break
        show_Network(name)


def remove_Friend(name):

    with open(FILENAME_FRI, 'r') as my_file:
        is_blank = len(my_file.read().strip())
    if is_blank == 0:
        print("You currently do not have anyone added to your friends list.")
        log_in_Screen(name)
    else:
        username=''
        with open(FILENAME_STD, newline='') as g:       #finds the username of the friend they want removed
            userReader = csv.reader(g)
            data = list(userReader)
        removeFirst = input("What is the first name of the person you would like to remove? ")
        removeLast = input("What is the last name? ")
        num = -1
        for user in data:
            num = num + 1
            if(num%2==0):
                if(user[2]==removeFirst and user[3]==removeLast):
                    username = user[0]                 #username of the student
        if(username==''):
            print("User not found. Try again. ")
            remove_Friend(name)
        with open(FILENAME_FRI, newline='') as f:
            friReader = csv.reader(f)
            friends = list(friReader)      

        with open(FILENAME_FRI,"w",newline="") as f:
            writer=csv.writer(f)
            num = -1    
            for pair in friends:
                num = num + 1
                if(num%2==0):
                    if (pair[0]==name and pair[1]==username) or (pair[0]==username and pair[1]==name):
                        continue
                    else:
                        writer.writerow((pair[0],pair[1]))
                        writer.writerow("")
        print("Removed Friend. ")
        show_Network(name)

def display_Friend(name):
    username=''
    
    with open(FILENAME_FRI, 'r') as my_file:
        is_blank = len(my_file.read().strip())
    if is_blank == 0:
        print("You currently do not have anyone added to your friends list.")
        log_in_Screen(name)
    else:
        with open('student_data.csv', newline='') as g:
            userReader = csv.reader(g)
            usernames = list(userReader)
        print("Your friends are: ")
        with open(FILENAME_FRI, newline='') as f:
            friReader = csv.reader(f)
            data = list(friReader)
        for user in data:    #checks all friends
            if name in user: #if user is found in a friend pairing
                index = user.index(name)    
                if index==0:
                    friend=1
                    uname=user[friend]
                    num = -1
                    for i in usernames: #searches through student data for first and last name
                        num = num + 1
                        if(num%2==0):
                            if i[0]==uname:
                                print(i[2]+' '+i[3])
                                break

                            
    print("Type in the first and last name of your friend to view their profile:")
    first_name_orig = input('Enter the first name: ')
    last_name_orig = input('Enter the last name: ')

    with open(FILENAME_STD, newline='') as g:       #finds the username of the friend 
        userReader = csv.reader(g)
        data = list(userReader)
    num = -1
    for user in data:
        num = num + 1
        if(num%2==0):
            if(user[2]==first_name_orig and user[3]==last_name_orig):
                username = user[0]                 
    if(username==''):
        print("User not found. Try again. ")
        display_Friend(name)

    manage = m.Manage()
    manage.viewProfile(username)  
    g.close()
    show_Network(name)





################## End of show network console ###################################








              
############################## Show and Apply for Jobs Console ##################################

def job_Screen(name):
    selection = 0
    while(selection != "5"):
        check_num_jobs_appliedto(name)
        print("Enter '1' to search all jobs in the system")
        print("Enter '2' to view jobs that you have applied for")
        print("Enter '3' to view jobs that you have not applied for")
        print("Enter '4' to view saved jobs.")
        print("Enter '5' to go back.")
        selection = input("Your selection: ")
        #check that acceptable input was provided by the user
        selection = check.check_option(selection,1,5)
        if(selection == "1"): #search all jobs
            manage = m.Manage()
            jobs = list()
            print("The following jobs are currently in the system:")
            with open(FILENAME_JOB,"r") as file:
                reader_csv = csv.reader(file)
                i = 0
                for row in reader_csv:
                    if row != [] and row != ["Title","Description","Employer","Location","Salary","Post_Name"]:
                        i = i + 1
                        jobs.append(row)
                        applied = 0
                        with open(FILENAME_APP,"r") as file:
                            reader_csv_B = csv.reader(file)
                            for entry in reader_csv_B:
                                if entry!= []:
                                    if (entry[0] == name) and (entry[1] == row[0]) and (entry[2] == row[2]):
                                        applied = applied + 1
                        if applied > 0:
                            print(str(i) + ": " + row[0] + " (Applied)")
                        else:
                            print(str(i) + ": " + row[0])
                job_num = len(jobs)
            choice = job_num + 1
            choice_B = 0
            while(choice != "0"):
                print("Enter the number of the job you would like to view (and if you wish, save or apply to), or enter '0' to go back")
                choice = input("Your selection: ")
                #check that acceptable input was provided by the user
                choice = check.check_option(choice,0,job_num)

                if(choice != "0"):
                    print(jobs[int(choice)-1][0])
                    print("Employer: " + jobs[int(choice)-1][2])
                    print("Location: " + jobs[int(choice)-1][3])
                    print("Salary: " + jobs[int(choice)-1][4])
                    print("Description: " + jobs[int(choice)-1][1])
                    print()
                    print("Enter '1' to apply for this job, '2' to save it, or '3' to go back")
                    choice_B = input("Your selection: ")
                    choice_B = check.check_option(choice_B,1,3)
                    if (choice_B == "1"): #Application
                        applied = 0
                        with open(FILENAME_APP,"r") as file:
                            reader_csv_C = csv.reader(file)
                            for entry in reader_csv_C:
                                if entry!= []:
                                    if (entry[0] == name) and (entry[1] == jobs[int(choice)-1][0]) and (entry[2] == jobs[int(choice)-1][2]):
                                        applied = applied + 1
                        if applied > 0:
                            print("You have already applied to that job")
                        else: 
                            manage.add_application(name, jobs[int(choice)-1][0], jobs[int(choice)-1][2])

                            #goes here if applied was successfull, so we record this date for the notification
                            manage.save_date_LastJobAppliedTo(name)
                    elif (choice_B == "2"): #Save
                        manage.add_save_job(name,jobs[int(choice)-1][0])
                        
        #View jobs applied to
        elif(selection == "2"): 
            print("You have applied to the following jobs:")
            with open(FILENAME_APP,"r") as file:
                reader_csv = csv.reader(file)
                i = 0
                for row in reader_csv:
                    if row != [] and row[0] == name:
                        print(row[1] + " at " + row[2])

        #Wiew jobs not applied to
        elif(selection == "3"): 
            list_application = [] #keep title of applications of the user
            with open (FILENAME_APP, "r") as file:
                reader_csv = csv.reader(file)
                for row in reader_csv:
                    if row != [] and row [0] == name:
                        list_application.append(row[1])

            list_job = [] # keep title of job in the system.
            with open (FILENAME_JOB, "r") as file:
                reader_csv = csv.reader(file)
                for row in reader_csv:
                    if row != [] and row != ["Title","Description","Employer","Location","Salary","Post_Name"]:
                        list_job.append(row[0])
            
            count = 0
            for element in list_job:
                if element not in list_application:
                    count +=1
                    print(str(count) + ": " + element)

        #View saved jobs
        elif(selection == "4"): 
            manage = m.Manage()
            list_save_job = manage.list_save_job(name)
            if len(list_save_job) != 0:               
                count = 0
                for element in list_save_job:
                    count +=1
                    print (str(count) + ": " + element)
            else:
                print("You don't have any saved jobs")
            
            if len(list_save_job) != 0:

                print("Do you want to unmark a job in saved jobs?")
                print("Select one of the below options:")
                print("(1) Unmark")
                print("(2) Keep saved jobs")
                choice = input("Your selection: ")
                #check the right value of input from user
                choice = check.check_option(choice,1,2)

                if (choice == "1"):
                    for element in list_save_job:
                        print()
                        print("Do you want to unmark the job that has the title " + "\"" + element + "\"")
                        print("Select one of the below options:")
                        print("(1) Yes")
                        print("(2) No")
                        choice = input("Your selection: ")
                        #check the right value of input from user
                        choice = check.check_option(choice,1,2)
                        if (choice == "1"):
                            manage.delete_save_job(name,element)
                        else:
                            pass

                elif (choice == "2"):
                    pass
        
        elif(selection == "5"): #return
            log_in_Screen(name)

############################## End of Show and Apply for Jobs Console ##################################

         
# if the job that the user applied is deleted, the user will have the notification about the job that is deleted
def check_application(name):
        list_application = [] #keep title of applications of the user
        with open (FILENAME_APP, "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != [] and row [0] == name:
                    list_application.append(row[1])
       
        
        list_job = [] # keep title of job in the system.
        with open (FILENAME_JOB, "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != [] and row != ["Title","Description","Employer","Location","Salary","Post_Name"]:
                    list_job.append(row[0])

     
        
        for element in list_application:
            if element not in list_job:
                print()
                print("The job with title " + "\"" + element + "\""+ " is removed")
                delete_application(name,element)


#delede all applications for the job which is deleted 
def delete_application(name, title):
    
    st = []
    with open(FILENAME_APP,"r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and (row[0] != name or row[1] != title):
                st.append(tuple(row))

    with open(FILENAME_APP,"w") as file:
        writer_csv = csv.writer(file)
        for element in st:
            writer_csv.writerow(element)

##########################################SENDING MESSAGE FEATURE#########################################
#same functionalitty as display_friends but that one had a view profile feature integrated in it, soooooo
#return a list of friends by username
def get_friends(name):
    friend_list = [] # keep username
   

    with open (FILENAME_FRI, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row [0] == name and (row[1] not in friend_list):
                friend_list.append(row[1])
            elif row != [] and row [1] == name and (row [0] not in friend_list):
                friend_list.append(row[0])
    
    return friend_list

#returns list of all usernames in system
def all_profiles(name):
    names = list()
    uname = list()
    blank = []
    valid_users = get_friends(name)
            
    with open(FILENAME_STD, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if (row != blank) and (row[0] != name) and (row[0] != "User_Name"): #or else there will be too much empty space
                uname.append(row[0])
                names.append(row[2]+" "+row[3])

    i = 0
    print("Users of InCollege: ")
    while i < len(names):
        if (uname[i] in valid_users):
            print(str(i+1)+". " + uname[i]+": "+names[i] + " - FRIEND")
        else :
            print(str(i+1)+". " + uname[i]+": "+names[i])
        i += 1
    return uname

def send_message(name):
    #get the tier account of the user. name == username
    with open(FILENAME_STD, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row != [] and (row[0] == name):
                tier = row[4]
    
    #display list of all people in system
    all_users = all_profiles(name)
    valid_users = get_friends(name)

    #prompt user to select
    choice = input("Select a friend to send a message to by the number: ")
    choice = check.check_option(choice,1,len(all_users))

    sendTo = all_users[int(choice)-1] #username looking to sendTo
    canSend = False

    #check if user is friend before they can send message
    if tier == "standard":
        for x in valid_users:
            if x == sendTo:
                canSend = True
    elif tier == "plus": #plus members able to send the message directly
        canSend = True


    #send the message or don't
    if canSend == True:
        manage = m.Manage()
        message = input("Message being sent to user "+sendTo+":\n")
        #sender = name
        #receiver = sendTo
        manage.add_pending_message(name, sendTo, message)
        print("Message sent!")
    else: 
        print("I'm sorry, you are not friends with that person")
    
    #menu options
    print("Select one of the below options:")
    print("(1) Send another message")
    print("(2) Return to Log In Screen")
    choice = input("Your selection: ")
    #check the right value of input from user
    choice = check.check_option(choice,1,2)

    if (choice == "1"):
        send_message(name)
    else:
        log_in_Screen(name)

def check_profile_creation(name):
    #Read profile name and if none match then send message
    send_message = 1
    with open(FILENAME_PRO, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row[0] == name:
                #if name found then don't send message.
                send_message = 0

    print_profile_notification(send_message)


def print_profile_notification(send_message):
    if send_message == 1:
        print("You have not created a profile yet! Please make a profile")

def check_new_user(name):
    #look at file named new_users if name on list then send notification
    #after send notification remove name from list

    lines = list()
    new_row = list()
    with open(FILENAME_NEW_USER, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            lines.append(row)
            if row != [] and row[0] == name:
                # if name found send message and remove name from file

                if row[1] == "first":
                    lines.remove(row)
                    new_row.append(name)
                    new_row.append("second")
                    lines.append(new_row)
                elif row[1] == "second":
                    #look in student.data and find last name and first name
                    with open(FILENAME_STD, "r") as file1:
                        reader_csv1 = csv.reader(file1)
                        for row1 in reader_csv1:
                            if row1 != [] and row1[0] == name:
                                first_name = row1[2]
                                last_name = row1[3]
                                print(first_name +" " +last_name + " has joined in college")
                        # if name found send message and remove name from file
                    lines.remove(row)
                    new_row.append(name)
                    new_row.append("third")
                    lines.append(new_row)
                elif row[1] == "third":
                    #print(" first name , last name has joined in college")
                    var = 1


                #remove name from list
    with open(FILENAME_NEW_USER, "w") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)




def check_messages(name):
    list_message = [] # keep a tupe (from, message)
    with open (FILENAME_MES, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row [1] == name:
                list_message.append((row[0],row[1], row[2]))
    
    if len(list_message) > 0:
        print ("You have some messages from some people!")
        for element in list_message:   
            From, To, Message = element

            print()
            print("This message " + "\"" + Message + "\"" + " from " + "\"" + From + "\"")
            print()
            print ("Do you want to save the message from " + "\"" + From + "\"" + " ?")
            print("Select one of the below options:")
            print("(1) Yes")
            print("(2) No")
            choice = input("Your selection: ")
            #check the right value of input from user
            choice = check.check_option(choice,1,2)

            if (choice == "1"):
                add_message(From,To,Message)
                delete_pending_message(From, To, Message)
            elif  choice == "2":
                delete_pending_message(From, To, Message)
            

            print()
            print("Do you want to respond the message from " + "\"" + From + "\"" + " ?")
            print("Select one of the below options:")
            print("(1) Yes")
            print("(2) No")
            choice = input("Your selection: ")
            #check the right value of input from user
            choice = check.check_option(choice,1,2)

            if choice == "1":
                mes = input ("Please type a message: ")
                with open(FILENAME_MES,"a") as file:
                    writer = csv.writer(file)
                    writer.writerow((To, From, mes))
                    print("The message was sent to " + "\"" + From + "\"")
            elif choice == "2":
                pass

def add_message(From, To, Message):
    with open(FILENAME_SAVE_MES, "a") as file:
        writer = csv.writer(file)
        writer.writerow((From, To, Message))

def delete_pending_message (From, To, Message):
    st = []
    with open(FILENAME_MES,"r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and (row[0] != From or row[1] != To or row[2] != Message):
                st.append(tuple(row))

    with open(FILENAME_MES,"w") as file:
        writer_csv = csv.writer(file)
        for element in st:
            writer_csv.writerow(element)

###############################JOB RELATED NOTIFICATIONS########################
def check_applied_in_seven_days(name):
    #checks if its been seven days since applying to a job
    with open(FILENAME_STD, "r") as file:
        reader = csv.reader(file)
        lines = list(reader)
        for row in lines:
            if (row != []) and (row[0] == name):
                lastApplied = row[5]
                _today =  datetime.today().strftime('%Y %m %d')
                today = datetime.strptime(_today, '%Y %m %d')
                sevenMinusToday = today+timedelta(days=-7)
                if(row[5] != "0"):
                    lastTime = datetime.strptime(lastApplied, '%Y-%m-%d %H:%M:%S')
                    if(lastTime <= sevenMinusToday):
                        #send job notification
                        print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

def check_num_jobs_appliedto(name):
    with open(FILENAME_APP,"r") as file:
                reader_csv = csv.reader(file)
                i = 0
                for row in reader_csv:
                    if row != [] and row[0] == name:
                        i += 1
    print("\nYou have currently applied for "+str(i)+" job(s).")

def check_new_job(name):
    overwrite = list()
    
    with open(FILENAME_NEW_JOB, "r") as file:
        reader = csv.reader(file)
        job = list(reader) 
        for row in job: #each row is a 'job title', 'list of users who have not seen'
            if(row == []):
                continue
            new_row = list()
            if(row != []) and (row[0] != "jobTitle"):
                for entry in row:
                    if entry == name:
                        print("A new job "+row[0]+" has been posted")
                    else:
                        new_row.append(entry)
            overwrite.append(new_row)
          
    with open(FILENAME_NEW_JOB, "w") as file:
        writer = csv.writer(file)
        writer.writerows(overwrite) 

def check_del_job(name):
    new_notif = list()

    with open(FILENAME_DEL_JOB, "r") as file:
        reader = csv.reader(file)
        notif = list(reader) 
        for row in notif:
            if (row != []) and (row[0] == name):
                print("The job \'"+row[1]+"\' you applied for has been deleted.")
            elif (row != []):
                new_notif.append(row)
            
    with open(FILENAME_DEL_JOB, "w") as file:
        writer = csv.writer(file)
        writer.writerows(new_notif) 
