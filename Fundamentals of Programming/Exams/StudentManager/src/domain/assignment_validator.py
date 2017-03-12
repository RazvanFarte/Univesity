'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.domain.validator import Validator

class AssignmentValidator(Validator):
    '''
    classdocs
    '''

    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        