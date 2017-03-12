'''
Created on Feb 22, 2017

@author: Razvan
'''

class Validator(object):
    '''
    classdocs
    '''
    @staticmethod
    def validate(obj):
        if not isinstance(obj.id, int):
            raise Exception("Id must be an integer")
        
class TaximetristValidator(Validator):
    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        
class OrderValidator(Validator):
    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        
        if obj.distance < 1:
            raise Exception("Distance must be at least 1")