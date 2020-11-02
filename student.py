""" 
student.py file has:
class Student: store information of a student such as first name, last name, password, ....
"""
class Student:
    def __init__(self, user_name, password, first, last, tier = 'standard'):
        self.__user_name = user_name
        self.__password = password
        self.__first = first
        self.__last = last
        self.__name = first + " " + last
        self.__tier = tier
        

    def get_user_name(self):
        return self.__user_name

    def get_first(self):
        return self.__first

    def get_last(self):
        return self.__last

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    #will be either 'standard' or 'plus'
    def get_tier(self):
        return self.__tier

    def __str__(self):
        return self.__name

