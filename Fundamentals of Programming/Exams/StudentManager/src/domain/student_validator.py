'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.validator import Validator


class StudentValidator(Validator):
    
    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        
        if obj.name == "":
            raise Exception("Student must have a name")
        
        if obj.group == None:
            raise Exception("Student must have a group")
        