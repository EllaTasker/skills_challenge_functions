from lib.count_words import *

def test_empty_string():
    string = count_words("")
    assert string == 0

def test_string_of_1():
    string = count_words("hello")
    assert string == 1

def test_for_multiple_words():
    string = count_words('This is a long sentence to test code')
    assert string == 8

    
def string_with_punctuation():
    string = count_words('hello, there little thing')
    assert string == 4