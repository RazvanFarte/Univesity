'''
Created on Feb 14, 2017

@author: Razvan
'''
from builtins import Exception

class Repository(object):
    
    def __init__(self, validatorClass):
        '''
        validatorClass - class name with static methdo validate, which will validate the entities
            from repository
        '''
        self.__validator = validatorClass
        self.__objects = {}
    
    def save(self, obj):
        """Saves the object in repository. If the object's id is already in repo, it will raise
        duplicate id. If objects validator and repository validator don't match, it will raise
        an exception
        
        Input:
            -object - an object
        Output:
            -None
        
        Raises:
            - Exception -  if the object is already saved in repository
            - TypeError - if the object is not matching the repository
        """
        if not obj.validator == self.__validator:
            raise TypeError("Object not matching the repository")
        
        try:
            self.__validator.validate(obj)
        except Exception as ex:
            raise Exception("Not a valid object" + str(ex))

        if obj.id in self.__objects.keys():
            raise Exception("Duplicated ID")
        
        self.__objects[obj.id] = obj
        
    
    def remove(self, objId):
        """Removes the object with id objId from repository and returns it. If
        repository does not contain this object, it will raise repository Exception
        """
        if objId not in self.__objects.keys():
            raise Exception("Object not in repository")
        
        del self.__objects[objId]
        
    
    def getAll(self):
        return self.__objects.values()