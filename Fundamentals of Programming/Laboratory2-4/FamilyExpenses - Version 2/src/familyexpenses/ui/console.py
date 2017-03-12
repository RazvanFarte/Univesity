'''
Created on 25 oct. 2016

@author: Dell
'''
from _datetime import datetime

from familyexpenses.domain.entities import create_expense
from familyexpenses.domain.operations import add_expense, list_expense, \
    list_category, list_conditional, remove_between, remove_day, remove_category, \
    sum_of_category, max_day, sort_day, sort_category, filter_others
from familyexpenses.uitl.util import is_int
import copy
from copy import deepcopy


def init():
    # TODO- delete after release phase
    return [create_expense("1", 100, "food"),
            create_expense("3", 145, "water"),
            create_expense("5", 400, "clothes"),
            create_expense("5", 300, "soap"),
            create_expense("7", 200, "food"),
            create_expense("7", 200, "bed"),
            create_expense("7", 375, "books"),
            create_expense("18", 40, "keyboard"),
            create_expense("19", 100, "shoes"),
            create_expense("24", 15, "food"),
            ]
    

def ui_add(month, undo_list, amount, category):
    '''
    Adds to the current day the amount of money and in category tag
    
    Input:
    month - a dictionary that consists in a dictionary of "days" and a dictionary of "categories"
    day - day when amount was spent
    amount - sum that was spent
    category - type of amount spent
    '''
    undo_list.append(copy.deepcopy(month))
    add_expense(month, create_expense(str(datetime.now().day), amount, category))

def ui_insert(month, undo_list, day, amount, category):
    '''
    Adds to day the amount of money and in category tag
    
    Input:
        month - a dictionary that consists in a dictionary of "days" and a dictionary of "categories"
        day - day when amount was spent
        amount - sum that was spent
        category - type of amount spent
    '''
    undo_list.append(copy.deepcopy(month))
    add_expense(month, create_expense(day, amount, category))
    
def ui_list(month, undo_list, arg1=None, arg2=None, arg3=None):
    '''Prints the list of expenses
    
    Input:
        month - list of expenses
    '''
    if not month:
        print("There are no expenses this month")
        return
    if arg1 is None:
        list_expense(month)
    elif arg2 == None:
        list_category(month, arg1)
    else:
        list_conditional(month, arg1, arg2, int(arg3))
    
def read_line():
    '''Reads a line and returns separately command and arguments (if exists)
    Input
        -
    Output 
        command - a string
        arguments - a list of strings
    '''   
    line = input("Command: ").lower()
    # We get the command
    index = line.find(" ")
    if index is not -1:
        command = line[:index]
    
        # We get the arguments    
        arguments = line[index + 1:].split(" ")
        
        return command.lower(), arguments
    else:
        return line.lower(), ""

def ui_remove(month, undo_list, obj, day2=None):
    '''
    Input:
        month - list of expenses
        obj - string
        day2 - string
    '''
    undo_list.append(copy.deepcopy(month))
    if day2 is not None:
        remove_between(month, int(obj), int(day2))
    else:
        if is_int(obj):
            remove_day(month, int(obj))
        else:
            remove_category(month, obj)

def ui_sum(month, undo_list, category):
    '''Prints the sum of expenses in this category
    '''
    print("The total for", category, "this month is ", 
          sum_of_category(month, category))

def ui_max(month, undo_list, day):
    '''Prints day with greatest expenses
    '''
    max_expense = max_day(month)
    print("The highest rate this month was in day", 
          max_expense[0], ":", max_expense[1])
    
def ui_filter(month, undo_list, category, operator = None, value = None):
        undo_list.append(copy.deepcopy(month))
        filter_others(month, category, operator, value)
        
    
def ui_sort(month, undo_list, arg):
    if "day" == arg.lower().strip():
        m = sort_day(month)
    else:
        m = sort_category(month,arg)
        
    for day in m:
        print("Day", day[0], "spent", day[1])

def ui_undo(month,undo_list):
#     month = copy.deepcopy(undo_list.pop())
    if undo_list == []:
        return
    del month[:]
    month += undo_list.pop()
    

def run():
    '''Main body of app
    '''
    month = init()
    undo_list = []
    commands = {"add":ui_add, "insert":ui_insert, "list":ui_list, "remove":ui_remove,
                 "help":ui_help, "sum":ui_sum, "max":ui_max, "sort":ui_sort, 
                 "filter":ui_filter, "undo":ui_undo}
    while True:
        comm, arguments = read_line()
        
        if comm == "exit":
            break
        
        try:
            commands[comm](month, undo_list, *arguments)
        except KeyError as kerr:
            print("Inexistent command.", kerr)
#            print_help()
        except Exception as exc:
            print("Error", exc)
#            print_help()

def ui_help(month, undo_list):
    print("Operations\n" 
           + "add <amount> <category>(Adds an expense for today)\n"
           + "insert <day> <amount> <category>(Adds an expense to <day>)\n"
           + "remove <day> (Removes the expenses for <day>)\n"
           + "remove <day1> <day2> (Removes the expenses between <day1> and <day2>)\n"
           + "remove <category> (Removes <category> from expenses)\n"
           + "list (Prints this month's expenses)\n"
           + "list <category> (Prints all expenses for <category>)\n"
           + "list <category> [< | = | >] <value> (Prints all expenses for <category>"
           + "greater, equal or less than <value>)\n"
           + "sum <category> (Prints the total expense for <category>)\n"
           + "max day (Prints the day with maximum expenses)\n"
           + "sort day (Prints the expenses in descending order by amount of money)\n"
           + "sort <category> (Prints the expenses for <category> in descending order>)\n"
           + "filter <category> (Keep ony expenses in <category>)\n"
           + "flter <category> [ < | = | > ] <value> (Keep only expenses in <category)"
           + "with amount <, =, or > than <value>)\n"
           + "undo (Undo the last operation)")
