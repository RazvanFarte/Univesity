'''
Created on Feb 22, 2017

@author: Razvan
'''
from src.validators import TaximetristValidator, OrderValidator
from unittest.test.test_result import __init__

class Taximestrist(object):
    '''
    classdocs
    '''


    def __init__(self, id, name, validator=TaximetristValidator):
        '''
        Constructor
        '''
        self.__id = id
        self.__name = name
        self.__validator = validator

    def get_validator(self):
        return self.__validator


    def set_validator(self, value):
        self.__validator = value


    def del_validator(self):
        del self.__validator

        
    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value


    def del_name(self):
        del self.__name

    id = property(get_id, None, None, "id's docstring")
    name = property(get_name, set_name, del_name, "name's docstring")


    def __str__(self):
        return "{},{}".format(self.id, self.name)
    
    def __eq__(self, other):
        if not isinstance(other, Taximestrist):
            return False
        
        return self.id == other.id
    validator = property(get_validator, set_validator, del_validator, "validator's docstring")
    
    
class Order(object):
    
    def __init__(self, id, distance, validator=OrderValidator):
        self.__id = id
        self.__distance = distance
        self.__validator = validator

    def get_validator(self):
        return self.__validator


    def set_validator(self, value):
        self.__validator = value


    def del_validator(self):
        del self.__validator


    def get_id(self):
        return self.__id


    def get_distance(self):
        return self.__distance


    def set_distance(self, value):
        self.__distance = value


    def del_distance(self):
        del self.__distance

        
    id = property(get_id, None, None, "id's docstring")
    distance = property(get_distance, set_distance, del_distance, "distance's docstring")
    
    def __str__(self):
        return "{},{}".format(self.id, self.distance)    
    
    validator = property(get_validator, set_validator, del_validator, "validator's docstring")


class IncomeDTO(object):
    def __init__(self, id, name, income):
        self.__id = id
        self.__name = name
        self.__income = income
        
    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def get_income(self):
        return self.__income


    def set_name(self, value):
        self.__name = value


    def set_income(self, value):
        self.__income = value


    def del_name(self):
        del self.__name


    def del_income(self):
        del self.__income

    id = property(get_id, None, None, "id's docstring")
    name = property(get_name, set_name, del_name, "name's docstring")
    income = property(get_income, set_income, del_income, "income's docstring")

    def __lt__(self, other):
        return self.income < other.income
    
    def __gt__(self,other):
        return self.income > other.income
    
    def __ge__(self, other):
        return not (self < other)
     
    def __le__(self, other):
        return not (self > other)
    
    def __str__(self, *args, **kwargs):
        return "{},{},{}".format(self.id, self.name, self.income)