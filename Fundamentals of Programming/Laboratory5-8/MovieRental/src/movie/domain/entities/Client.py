'''
Created on 7 nov. 2016

@author: Dell
'''
from movie.domain.exceptions.MovieException import MovieException
from movie.domain.validators.ClientValidator import ClientValidator


class Client(object):
    '''
    classdocs
    '''


    def __init__(self, clientId, clientName):
        self.__clientId = clientId
        self.__clientName = clientName

    def get_entity_id(self):
        return self.__clientId


    def get_entity_name(self):
        return self.__clientName


    def set_entity_name(self, value):
        self.__clientName = value


    def del_entity_id(self):
        del self.__clientId


    def del_entity_name(self):
        del self.__clientName

    entityId = property(get_entity_id, None, del_entity_id, "clientId's docstring")
    entityName = property(get_entity_name, None, del_entity_name, "clientName's docstring")
    
    def __str__(self):
        return "Client id: {x1}, client name: {x2}".format(x1 = self.entityId, x2 = self.entityName)
    
    def __eq__(self, other):
        '''
        Short Description:
            Compares two object, and if they are both Client objects and have the same id,
            return True
            
        Type of parameters:
            self - Client
            other - Client
            
        Preconditions:
            other - must be a Client object. Otherwise it will raise a TypeError
            
        Returns a boolean object:
            True - if their id are equal
            False - otherwise
            
        Postconditions:
            None
            
        Exceptions:
            TypeError - if other is not a Client object
        
        '''
        if not isinstance(other, Client):
            raise TypeError("Second argument is not a Client")
        return self.entityId == other.entityId
    
    def __ne__(self, other):
        return not self.__eq__(other)
    