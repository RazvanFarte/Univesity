'''
Created on 25 oct. 2016

@author: Dell
'''

def create_expense(day, amount, category):
    '''Creates a expense, as a list with these 3 params
    Input:
    day - string representing a day of month between 1 and 30
    amount - string, representing the sum spent on category in this day
    category - string, representing a category of expense
    Output:
    list [day, int(amount), category]
    '''
    return [day, int(amount), category]

def get_day(expense):
    return expense[0]

def get_amount(expense):
    return expense[1]

def get_category(expense):
    return expense[2]

def set_day(expense,day):
    expense[0] = day

def set_amount(expense,amount):
    if type(amount) == type(10):
        expense[1] = amount
    else:
        expense[1] = int(amount)
    
def set_category(expense, category):
    expense[2] = category
