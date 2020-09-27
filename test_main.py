import pytest
import main
import check as ch
import manage as ma
import student as st
import job as jo
import random
from random import choice
import string


class TestClass:
    def test_maxAcc(self):             #adds accounts so I can test the connection
        filename = "student_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()
        stud1 = st.Student("TP1", "P@ssword123", "Tracy", "Pham")
        assert manage.add_student(stud1) == stud1.get_user_name()
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.add_student(stud2) == stud2.get_user_name()
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.add_student(stud3) == stud3.get_user_name()
        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.add_student(stud4) == stud4.get_user_name()
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.add_student(stud5) == stud5.get_user_name()

    def test_Connection(self):
        manage = ma.Manage()
        student = st.Student("TP1", "P@ssword123", "Tracy", "Pham")         #tests cases where there is a match
        assert manage.find_people("Tracy", "Pham") == student.get_user_name()
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.find_people("Thinh", "Phung") == stud2.get_user_name()
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.find_people("Daniel", "Polt") == stud3.get_user_name()
        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.find_people("Kelvin", "Pun") == stud4.get_user_name()
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.find_people("Yakira", "Quemba") == stud5.get_user_name()

        assert manage.find_people("Random", "Random") == None           #tests case where theres no match

    def test_Jobs(self):             #adds jobs so I can test the addition
        filename = "job_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()
        job1 = jo.Job("Porter", "TransportsItems", "Bridges", "UCA", "10", "TP1")
        assert manage.add_job(job1, "TP1") == job1.get_post_name()
        job2 = jo.Job("Developer", "WritesCode", "USF", "FL", "20", "TP2")
        assert manage.add_job(job2, "TP2") == job2.get_post_name()
        job3 = jo.Job("Tester1", "Tests", "USF", "FL", "20", "DP")
        assert manage.add_job(job3, "DP") == job3.get_post_name()
        job4 = jo.Job("Tester2", "Tests", "USF", "FL", "20", "KP")
        assert manage.add_job(job4, "KP") == job4.get_post_name()
        job5 = jo.Job("SCRUMMaster", "ManagesSCRUM", "USF", "FL", "30", "YQ")
        assert manage.add_job(job5, "YQ") == job5.get_post_name()

    def test_passwordLength(self):
        correct = random.randint(8, 12)
        less = random.randint(0, 7)
        more = random.randint(13, 40)
        stringC = "x" * correct
        assert ch.Password_account.max_character(self, stringC) == True and ch.Password_account.min_character(self,
                                                                                                              stringC) == True
        stringL = "x" * less
        assert ch.Password_account.max_character(self, stringL) == False or ch.Password_account.min_character(self,
                                                                                                              stringL) == False
        stringM = "x" * more
        assert ch.Password_account.max_character(self, stringM) == False or ch.Password_account.min_character(self,
                                                                                                              stringM) == False

    def test_capitalLetter(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        assert ch.Password_account.capital_letter(self, password) == False
        password2 = ''.join(choice((str.upper, str.lower))(c) for c in password)
        assert ch.Password_account.capital_letter(self, password2) == True

    def test_oneDigit(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        numpass = list(password)
        randint = random.randint(0, length - 1)
        numpass[randint] = str(random.randint(0, 9))
        password = ''.join(numpass)
        assert ch.Password_account.digit(self, password) == True

    def test_nonAlpha(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        alphapass = list(password)
        nonAlpha = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "*", "=", "/"]
        randint = random.randint(0, length - 2)
        alphapass[randint] = str(random.choice(nonAlpha))
        alphapass[randint + 1] = str(random.randint(0, 9))
        password = ''.join(alphapass)
        assert ch.Password_account.digit(self, password) == True


def get_random_lowercase_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))




#This test checks that all the requirements for a valid password are being met
def test_password():
    chk = ch.Password_account()
    assert chk.min_character("onetwoth") == True
    assert chk.min_character("one") == False
    assert chk.max_character("abcedfghjklm") == True
    assert chk.max_character("abcdefghjkrty") == False
    assert chk.capital_letter("Thinh") == True
    assert chk.capital_letter("thinh") == False
    assert chk.digit("hello1") == True
    assert chk.digit("hello") == False
    assert chk.non_alpha("no@") == True
    assert chk.non_alpha("no") == False






