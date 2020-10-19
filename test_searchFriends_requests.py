import pytest
import main
import check as ch
import manage as ma
import string
import csv

#search functionality
manage = ma.Manage()
FILENAME_PRO = "profiles.csv"
FILENAME_STD = "student_data.csv"


def test_returnUserByLast():
    lname = "Pun"
    blank = []
    count = 0
    lines = list()
    expected = list()
    #read current students and fill 'lines' with relevant students
    with open(FILENAME_STD, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank: #or else there will be too much empty space
                lines.append(row)
                count = count + 1
                if lines[count-1][3] == lname:
                    expected.append(lines[count-1][0])
        return expected

        
    actual = manage.return_unames_from_last(lname)
    
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_returnUserByUniv():
    univ = "University Of South Florida"
    expected = list()
    blank = []
    count = 0
    lines = list()
    #read current students and fill 'lines' with relevant students
    with open(FILENAME_PRO, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank: #or else there will be too much empty space
                lines.append(row)
                count = count + 1
                if lines[count-1][3] == univ:
                    expected.append(lines[count-1][0])

    actual = manage.return_unames_from_univ(univ)
    
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_returnUserByMajor():
    major = "Computer Science"
    blank = []
    count = 0
    lines = list()
    expected = list()
    #read current students and fill 'lines' with relevant students
    with open(FILENAME_PRO, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank: #or else there will be too much empty space
                lines.append(row)
                count = count + 1
                if lines[count-1][2] == major:
                    expected.append(lines[count-1][0])
        return expected


    actual = manage.return_unames_from_major(major)
    
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])