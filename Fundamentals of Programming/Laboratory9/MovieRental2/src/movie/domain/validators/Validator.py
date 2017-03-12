'''
Created on 7 nov. 2016

@author: Dell
'''
from movie.domain.exceptions.ValidatorException import ValidatorException

class Validator(object):
    '''
    classdocs
    '''
    @staticmethod
    def validate(entity):
        
        if not isinstance(entity.entityId, int):
            raise ValidatorException("Id must be an integer!")