'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.validator import Validator

class GradeValidator(Validator):
    '''
    classdocs
    '''
    
    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        
        if not isinstance(obj.grade, int):
            raise TypeError("Grade must be an integer")
        
        if not isinstance(obj.lab, int):
            raise TypeError("Lab number must be an integer")
        
        if not isinstance(obj.problem, int):
            raise TypeError("Problem number must be an integer")
        
        if obj.grade < 0 or obj.grade > 10:
            raise ValueError("Grade must have a value between 0 and 10")
        
        if obj.lab < 0:
            raise ValueError("Laboratory number must be greater than 0")
        
        if obj.problem < 1 or obj.problem > 20:
            raise ValueError("Laboratory problem must be between 1 and 20")
        