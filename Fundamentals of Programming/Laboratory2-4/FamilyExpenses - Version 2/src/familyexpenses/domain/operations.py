'''
Created on 25 oct. 2016

@author: Dell
'''
import operator

from familyexpenses.domain.entities import get_amount, get_day

def add_expense(month, expense):
    '''Adds an expense in list.
    Input:
        month - the list of expenses
        expense - the expense,containing [day,amount,category]
    Output:
        month - will contain also the expense
    '''
    k = False
    
    for i in range(len(month)):
        if int(expense[0]) < int(month[i][0]):
            month.insert(i, expense)
            k = True
            break
        
    if not k:
        month.append(expense)




def list_expense(month):
    '''Lists the expenses of this month
    '''
    for expense in month:
        print("Day " + expense[0] + ": spent " + str(expense[1])
              + " for " + expense[2])
 
def list_category(month, category):
    '''Lists the expenses of given category in this month
    '''
    print("For category " + category + " your expenses are:")
    for expense in month:
        if category in expense:
            print("Day " + expense[0] + ": spent " + str(expense[1]))

def list_conditional(month, category, operator, value):
    #TODO: Make it better. Too nested
    print("For category",category,"your expenses are:")
    for expense in month:
        if category in expense:
            if operator == ">":
                if expense[1] > value:
                    print("Day", expense[0] + ": spent", str(expense[1]))
            elif operator == "=":
                if expense[1] == value:
                    print("Day", expense[0] + ": spent", str(expense[1]))
            else:
                if expense[1] < value:
                    print("Day", expense[0] + ": spent", str(expense[1]))

def remove_between(month, initial_day, final_day):
    '''Removes all records in month between initial and final days
    Input
        month - list of expenses
        initial_day - integer
        final_day - integer
    Output
        -
    '''
    index = 0
    while index < len(month):
        if (initial_day <= int(month[index][0]) and final_day >= int(month[index][0])):
            del month[index]
        else:
            index += 1

def remove_day(month, day):
    '''Removes the expenses in day "day"
    Input:
        month - list of expenses
        day - day in which expenses are removed
    '''
    remove_between(month, day, day)

def filter_others(month, category, operator = None, value = None):
    '''Remove all categories but category
    '''
    if operator is None:
        index = 0
        while index < len(month):
            if category not in month[index]:
                del month[index]
            else:
                index += 1
    else:
        index = 0
        while index < len(month):
            if category not in month[index]:
                del month[index]
            else:
                if operator == ">":
                    if month[index][1] <= int(value):
                        del month[index]
                    else:
                        index += 1
                elif operator == "=":
                    if month[index][1] != int(value):
                        del month[index]
                    else: 
                        index += 1
                elif operator == "<":
                    if month[index][1] >= int(value):
                        del month[index]
                    else:
                        index += 1
                else:
                    index += 1

def remove_category(month, category):
    '''Remove all apparitions of category in this month
    '''
    index = 0
    while index < len(month):
        if category in month[index]:
            del month[index]
        else:
            index += 1
            
def sum_of_category(month, category):
    '''Calculates the sum of all expenses of type category in month
    Input:
        month - list of expenses
        category - string; category of expense
    '''
    s = 0
    for expense in month:
        if category in expense:
            s += get_amount(expense)
            
    return s

def sum_of_day(month, day):
    '''Calculates the sum of all expenses of the given day category in month
    Input:
        month - list of expenses
        day - string; day of expense
    '''
    s = 0
    for expense in month:
        if day in expense:
            s += get_amount(expense)
            
    return s

def max_day(month):
    '''Computes the day with maximum expenses and returns a tuple (day,expense)
    Input:
        month - list of expense
    Output:
        The day of maximum expenses as a string
    '''
    maxi = -1
    day = -1
    for i in range(31):
        x = sum_of_day(month, str(i))
        if maxi < x:
            maxi = x
            day = i
    
    return (str(day),maxi)

def expense_days(month):
    '''Returns a dictionary with total daily expenses
    '''
    dicti = {}
    for expense in month:
        day = get_day(expense)
        if day not in dicti:
            dicti[day] = get_amount(expense)
        else:
            dicti[day] += get_amount(expense)
    
    return dicti

def sort_day(month):
    '''Gives a sorted tuple by amount of money spent in days
    '''
    daily_expenses = expense_days(month)
    daily_expenses = sorted(daily_expenses.items(), key=operator.itemgetter(1), reverse=True)
    
    return daily_expenses

def sort_category(month, category):
    '''Gives a sorted tuple with expenses having category, sorted descending 
    by amount
    '''
#     d = tuple(tuple(x) for x in month if category in x)
#     d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    days = [x for x in month if category in x]
    
    for i in range (0,len(days) - 1):
        for j in range(i+1,len(days)):
            if days[i][1] < days[j][1]:
                days[i],days[j] = days[j], days[i]
#     ord_days = []
#     for day in days:
#         add_expense(ord_days, day)
    
    return days
    