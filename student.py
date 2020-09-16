""" 
student.py file has:
class Student: store information of a student such as name, password, ....
"""
class Student:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
    
    def get_name(self):
        return self.__name
    def get_password(self):
        return self.__password

    def __str__(self):
        return self.__name

