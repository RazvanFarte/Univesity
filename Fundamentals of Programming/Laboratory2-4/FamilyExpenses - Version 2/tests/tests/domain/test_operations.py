'''
Created on 25 oct. 2016

@author: Dell
'''
from familyexpenses.domain.entities import create_expense
from familyexpenses.domain.operations import add_expense, sum_of_category, \
    sort_day, sort_category, filter_others
from familyexpenses.ui.console import init, ui_remove, ui_undo, ui_add,\
    ui_insert


def test_add_exepnse():
    l = init()
    lenght = len(l)
    
    obj = create_expense("30", 200, "drinks")
    add_expense(l, obj)
    assert (lenght + 1) == len(l)
    assert obj in l
    
    
    obj = create_expense("1", 300, "batteries")
    lenght = len(l)
    add_expense(l, obj)
    assert lenght + 1 == len(l)
    assert (obj in l)
    assert int(l[l.index(obj) + 1][0]) \
        > int(l[l.index(obj)][0])  # Obj should be affter last expense in day 1
     
def test_remove_expense():
    l = init()
    length = len(l)
    u = []
    
    ui_remove(l, u, "food")
    for x in l:
        assert "food" not in x
    assert length >= len(l)
    
    l = init()
    length = len(l)
    ui_remove(l, u,"3", "15")
    for x in l:
        assert int(x[0]) < 3 or int(x[0]) > 15
    assert length >= len(l)
    
    l = init()
    length = len(l)
    ui_remove(l, u, "2")
    for x in l:
        assert "2" not in x
    assert length >= len(l)
    
def test_sum_category():
    l = init()
    
    assert sum_of_category(l, "fun") == 0 # if there is no such category, the sum must be 0
    
def test_sort():
    l = init()
    
    d = sort_day(l)
    for i in range(len(d)-1):
        assert d[i][1] >= d[i+1][1]
        
    d = sort_category(l, "food")
    for i in range(len(d)-1):
        assert d[i][1] >= d[i+1][1]
    
def test_filter():
    l = init()
    le = len(l)
    
    filter_others(l, "food")
    assert len(l) <= le
    for x in l:
        assert "food" in x
        
def test_undo():
    l = init()
    u = []
    
    ui_insert(l, u, "2","300", "food")
    ui_undo(l, u)
    assert create_expense("2", "300", "food") not in l
    

def test_all_operations():
    test_add_exepnse()
    test_remove_expense()
    test_sum_category()
    test_sort()
    test_filter()
    
       
