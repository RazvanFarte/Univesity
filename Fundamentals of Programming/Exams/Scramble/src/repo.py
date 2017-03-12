'''
Created on Feb 22, 2017

@author: Razvan
'''
import random

from src.Sentence import SentenceValidator, Sentence


class FileRepository(object):
    '''
    classdocs
    '''


    def __init__(self, validator, fileName):
        '''
        Constructor
        '''
        self.__validator = validator
        self.__objects = []
        self.__fileName = fileName
        
        self.__loadFromFile(self.fileName)

    def get_objects(self):
        return self.__objects


    def set_objects(self, value):
        self.__objects = value


    def del_objects(self):
        del self.__objects

        
    def get_validator(self):
        return self.__validator


    def get_file_name(self):
        return self.__fileName


    def set_validator(self, value):
        self.__validator = value


    def set_file_name(self, value):
        self.__fileName = value


    def del_validator(self):
        del self.__validator


    def del_file_name(self):
        del self.__fileName

    validator = property(get_validator, set_validator, del_validator, "validator's docstring")
    fileName = property(get_file_name, set_file_name, del_file_name, "fileName's docstring")
    objects = property(get_objects, set_objects, del_objects, "objects's docstring")

    def chooseObject(self):
        """Returns a random object from repository"""
        return random.choice(self.objects)
    
    def __str__(self):
        return "{} repository".format(self.validator)
    
    def save(self, obj):
        """Saves the object into repository
        
        Input:
            obj - object to be saved. It must have a "validator" public field which match to repo 
                validator
        Output:
            None
            
        Raises:
            DuplicateObjectError - if the same instance is added again(case sensitive)
            MismatchError - if the given object is of other type than repository
            ValidationError - if obj is not valid
        """
        
        if obj.validator != self.validator:
            raise Exception("Object {} is not fit for {}".format(obj, self))
        
        if obj in self.objects:
            raise Exception("Duplicate object {} for {}".format(obj, self))
        
        try:
            self.validator.validate(obj)
        except Exception as ex:
            raise Exception("Error during validation:", ex)
        
        self.objects.append(obj)
        
    def __loadFromFile(self, fileName):
        """Loads from file "fileName" each element"""
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()
                listOfWords = line.split(" ")
                
                if self.validator == SentenceValidator:
                    self.save(Sentence(listOfWords))
                    
                    


        