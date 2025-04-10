from lib.check_grammar import *

def test_check_all_lowercase():
    string = check_grammar('hello')
    assert string == False

def test_check_first_letter_upper_no_punc():
    string = check_grammar("Hello")
    assert string == False

def test_check_for_upper_and_full_stop():
    string = check_grammar("Hello.")
    assert string == True

def test_check_for_upper_and_exclimation():
    string = check_grammar("Hello!")
    assert string == True

def test_check_for_upper_and_question_mark():
    string = check_grammar("Hello?")
    assert string == True

def test_for_numbers():
    string = check_grammar('01234')
    assert string == False

def test_for_lower_and_punc():
    string = check_grammar("hello!")
    assert string == False
