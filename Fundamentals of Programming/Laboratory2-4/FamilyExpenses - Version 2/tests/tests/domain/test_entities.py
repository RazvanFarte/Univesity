'''
Created on 25 oct. 2016

@author: Dell
'''
from familyexpenses.domain.entities import create_expense, get_day, get_amount,\
    get_category, set_amount

def test_create_expense():
    exp = create_expense("30", 200, "water")
    assert len(exp) == 3
    assert type(exp) == type([])
    assert type(exp[0]) == type("")
    assert type(exp[1]) == type(300)
    assert type(exp[2]) == type("")
    
def test_getters_setters():
    exp = create_expense("14", 300, "electricity")
    assert type(get_day(exp)) == type("")
    assert type(get_amount(exp)) == type(300)
    assert type(get_category(exp)) == type("")
    
    exp1 = create_expense("20", 500, "electricity")
    set_amount(exp,50)
    set_amount(exp1,"50")
    assert (get_amount(exp) == get_amount(exp1))
    
def test_all_entities():
    test_create_expense()
    test_getters_setters()
    