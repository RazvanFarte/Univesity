'''
Created on Feb 22, 2017

@author: Razvan
'''
from src.validators import TaximetristValidator, OrderValidator
from src.domain import Taximestrist, Order

class Repository(object):
    '''
    classdocs
    '''


    def __init__(self, validator):
        '''
        Constructor
        '''
        self.__validator = validator
        self.__objects = []

    def get_validator(self):
        return self.__validator


    def get_objects(self):
        return self.__objects


    def set_validator(self, value):
        self.__validator = value


    def set_objects(self, value):
        self.__objects = value


    def del_validator(self):
        del self.__validator


    def del_objects(self):
        del self.__objects

    validator = property(get_validator, set_validator, del_validator, "validator's docstring")
    objects = property(get_objects, set_objects, del_objects, "objects's docstring")
        
        
    def save(self, obj):
        if self.validator != obj.validator:
            raise Exception("Not good object for current repository")
        
        if obj in self.objects:
            raise Exception("Duplicate id")
        
        try:
            self.validator.validate(obj)
        except Exception as ex:
            raise Exception("Error while validating: " + str(ex))
        
        self.objects.append(obj)
        
    def findById(self, objId):
        for elem in self.objects:
            if objId == elem.id:
                return elem
        return None
    
class FileRepository(Repository):
    def __init__(self, validator, fileName):
        Repository.__init__(self, validator)
        
        self.__fileName = fileName
        self.__loadFromFile()

    def get_file_name(self):
        return self.__fileName


    def set_file_name(self, value):
        self.__fileName = value


    def del_file_name(self):
        del self.__fileName

        
    def __loadFromFile(self):
        with open(self.fileName, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(",")
                if super().validator == TaximetristValidator:
                    super().save(Taximestrist(int(line[0]), line[1]))
                    
                if super().validator == OrderValidator:
                    super().save(Order(int(line[0]), int(line[1])))
                    
                    
    def __saveToFile(self):
        with open(self.fileName, "w") as f:
            for elem in super().get_objects():
                f.write(str(elem) + "\n")
                
    def save(self, obj):
        Repository.save(self, obj)
        
        self.__saveToFile()
        
    
    fileName = property(get_file_name, set_file_name, del_file_name, "fileName's docstring")
    
    