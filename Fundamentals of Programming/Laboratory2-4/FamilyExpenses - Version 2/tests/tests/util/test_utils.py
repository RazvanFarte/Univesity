'''
Created on 25 oct. 2016

@author: Dell
'''
from familyexpenses.uitl.util import is_int

def test_is_int():
    assert (is_int(3) == True)
    assert (is_int(0) == True)
    assert (is_int(-3) == True)
    assert (is_int(2.0) == True)

def test_all_utils():
    test_is_int()