'''
Created on Feb 17, 2017

@author: Razvan
'''
from src.domain import Person

class Repository(object):
    '''
    classdocs
    '''


    def __init__(self, validatorClass):
        '''
        Constructor
        '''
        self.__validator = validatorClass
        self.__objects = []

    def get_validator(self):
        return self.__validator


    def get_objects(self):
        return self.__objects

        
    def save(self, obj):
        if obj in self.objects:
            raise Exception("Duplicated id for object \"{}\"".format(obj))

        self.objects.append(obj)
        
    def findById(self, id):
        for elem in self.objects:
            if id == elem.id:
                return elem
        return None
    
    def remove(self, obj):
        if obj in self.objects:
            return self.objects.remove(obj)
        return None
        
    validator = property(get_validator, None, None, "validator's docstring")
    objects = property(get_objects, None, None, "objects's docstring")
    
    
class FileRepository(Repository):
    def __init__(self, validatorClass, fileName):
        Repository.__init__(self, validatorClass)
        self.__fileName = fileName
        self.__loadFromFile()

    def get_file_name(self):
        return self.__fileName


    def set_file_name(self, value):
        self.__fileName = value


    def del_file_name(self):
        del self.__fileName

    fileName = property(get_file_name, set_file_name, del_file_name, "fileName's docstring")
    
    def save(self, obj):
        Repository.save(self, obj)
        
        self.__saveToFile()
        
    def __loadFromFile(self):
        with open(self.fileName, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(" ")
                
                super().save(Person(int(line[0]), line[1], line[2], line[3]))
                
                
    def __saveToFile(self):
        with open(self.fileName, "w") as f:
            for elem in super().objects:
                f.write(str(elem) + "\n")