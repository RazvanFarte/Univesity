'''
Created on 8 nov. 2016

@author: Dell
'''

from movie.domain.validators.Validator import Validator 
from movie.domain.validators.Validator import ValidatorException


class RentalValidator(Validator):
    '''
    classdocs
    '''
    @staticmethod
    def validate(entity):
        Validator.validate(entity)
        
        if not isinstance(entity.movieId, int) or not isinstance(entity.clientId, int):
            raise ValidatorException("Id must be an integer!")
        
    
    
