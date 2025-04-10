from lib.make_snippet import *

def test_return_empty_string():
    string = make_snippet("")
    assert string == ""

def test_return_one_word_string():
    string = make_snippet('Hello')
    assert string == "Hello"

def test_six_words():
    string = make_snippet("this is a really long sentence to test this code")
    assert string == "this is a really long..."

def test_four_words():
    string = make_snippet("hello there strange one")
    assert string == "hello there strange one"