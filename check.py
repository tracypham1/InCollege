"""  
Check.py file include classes to check and test input value from users
"""

import student as s
import manage as m

class Password_account:

    #at least 8 characters
    def min_character(self, password):
        if len(password) < 8:
            print("The password needs at least 8 characters")
            return False
        else:
            return True

    #at most 12 characters
    def max_character(self, password):
        if len(password) > 12:
            print("The password needs at most 12 characters")
            return False
        else:
            return True

    #at least one capital letter
    def capital_letter(self, password): 
        if not any(character.isupper() for character in password):
            print("The password needs at least one capital")
            return False
        else:
            return True

    #at least one digit 
    def digit(self, password):
        if not any(character.isdigit() for character in password):
            print("The password needs at least one digit")
            return False
        else:
            return True

    #at least one non_alpha
    def non_alpha(self,password):
        if password.isalnum():
            print("The password needs at least one non-alpha character")
            return False
        else: 
            return True


class name_Password:

    def name_check(self, name):
        manage = m.Manage()
        
        for element in manage.get_list():
            if element.get_name() == name:
                
                return True

        print("Don't have any account with name:", name)
        return False

    def password_check(self, name, password):
        manage = m.Manage()

        for element in manage.get_list():
            if element.get_name() == name and element.get_password() == password:
                return True

        return False

    




        



        
