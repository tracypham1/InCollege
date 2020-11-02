import pytest
import main
import check as ch
import console as cs
import manage as ma
import string
import csv

#search functionality
manage = ma.Manage()
FILENAME_STD = "student_data.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_STG = "settings.csv"
FILENAME_POL = "policy.csv"
FILENAME_PRO = "profiles.csv"
FILENAME_FRI = "friends.csv"
FILENAME_REQ = "requests.csv"
FILENAME_APP = "applications.csv"
FILENAME_MES = "pending_messages.csv"
FILE_SAVE_MES = "messages.csv"
STORY = "success_story.txt"
empty_string = " "


def test_add__pending_message():
    user1 = "DP";
    user2 = "TP1";
    message = "Pending Message, Test";
    checker = 0;
    blank = [];
    manage = ma.Manage()
    manage.add_pending_message(user1, user2, message)
    with open(FILENAME_MES, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank:
                print(row[0]);
                print(row[1]);
                print(row[2]);
                if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                    checker = 1;
                    
    assert checker == 1;


def test_delete_pending_message():
    user1 = "DP";
    user2 = "TP1";
    message = "Pending Message, Test";
    checker = 0;
    blank = [];
    
    with open(FILENAME_MES, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank:
                print(row[0]);
                print(row[1]);
                print(row[2]);
                if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                    checker = 1;
                    
    assert checker == 1;
    checker = 0;
    
    cs.delete_pending_message(user1, user2, message)
    with open(FILENAME_MES, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row != blank:
                print(row[0]);
                print(row[1]);
                print(row[2]);
                if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                    checker = 1;
    
    assert checker == 0;
