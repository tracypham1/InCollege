import pytest
import main
import check as ch
import manage as ma
import student as st
import random
from random import choice
import string


class TestClass:

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

    def test_maxAcc(self):  # test uniqueness and number of attempts
        manage = ma.Manage()
        stud1 = st.Student("Tracy", "P@ssword123")
        assert manage.add_student(stud1) == True
        stud2 = st.Student("Thinh", "P@ssword123")
        assert manage.add_student(stud2) == True
        stud3 = st.Student("Daniel", "P@ssword123")
        assert manage.add_student(stud3) == True
        stud4 = st.Student("Kelvin", "P@ssword123")
        assert manage.add_student(stud4) == True
        stud5 = st.Student("Kelvin", "P@ssword123")
        assert manage.add_student(stud5) == False
        stud6 = st.Student("Yakira", "P@ssword123")
        assert manage.add_student(stud6) == True
        stud7 = st.Student("James", "P@ssword123")
        assert manage.add_student(stud7) == False


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


def test_name_Password():
    chk = ch.name_Password()
    #this test is to check if the username Bob or william were created.
    # assuming this is before any names are entered it should be false
    # Also checks if the user Yakira's correct password is password which it is not so it returns false
    assert chk.name_check("Bob") == False
    assert chk.name_check("william") == False
    assert chk.password_check("Yakira","password") == False


