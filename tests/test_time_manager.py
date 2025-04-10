from lib.time_manager import *

def test_time_for_no_words():
    time = time_manager(0)
    assert time == 0

def test_time_for_200_words():
    time = time_manager(200)
    assert time == 1

def test_time_for_over_600_words():
    time = time_manager(600)
    assert time == 3

def test_uneven_number():
    time = time_manager(363)
    assert time == 1.815

def test_random_numnber(): 
    time = time_manager(3636)
    assert time == 18.18