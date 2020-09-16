
"""
manage.py file has:
class Manage: manages I/O file 
"""

import student as s
import csv
import os.path

FILENAME = "student_data.csv"

class Manage:
    def __init__(self):
        
        #create a list of student Object
        #selft__list_student will store object of Student class
        self.__list_student = []

        #add title for the student_data.csv
        if not os.path.isfile(FILENAME):
            with open(FILENAME,"w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("name","password"))

        #add data from student_data.csv to __self.__list_student
        with open(FILENAME,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                self.__list_student.append(s.Student(row[0], row[1]))
                
    
    def get_list(self):
        return self.__list_student
            

    def add_student(self, student):
        for element in self.__list_student:
            if element.get_name() == student.get_name():
                print("There is an account with the same name")
                return
        if len(self.__list_student) < 6:
            self.__list_student.append(student)
            print("The account of",student.get_name(), "is created!")

            #need to add a new student to student_data.csv
            with open(FILENAME,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow((student.get_name(),student.get_password()))   
            
        else:
            print("All permitted accounts have been created, please come back later")
    

                    




   

    

        
