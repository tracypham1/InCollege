import pytest
import main
import check as ch
import manage as ma
import student as st
import job as jo
import random
from random import choice
import string
import csv


class TestClass:
    def test_importantLinks(self):             #adds students to test the creation of default setting values
        filename = "settings.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        #########################################

        stud1 = st.Student("TP1", "P@ssword123", "Tracy", "Pham")
        assert manage.add_student(stud1) == stud1.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "TP1"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud1.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.add_student(stud2) == stud2.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "TP2"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud2.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.add_student(stud3) == stud3.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "DP"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud3.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################

        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.add_student(stud4) == stud4.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "KP"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud4.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.add_student(stud5) == stud5.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "YQ"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud5.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])
