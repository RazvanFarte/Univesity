'''
Created on Feb 14, 2017

@author: Razvan
'''

class Validator(object):
    '''
    Validates an IDObject
    '''
    
    @staticmethod
    def validate(obj):
        if not isinstance(obj.id, int):
            raise TypeError("Id must be an integer")
        if obj.id <= 0:
            raise ValueError("Id must be positive")
        