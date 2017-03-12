'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.entities import Question

class Repository:
    def __init__(self, validator):
        
        self.__validator = validator
        self.__objects = {}
        
    def get_objects(self):
        return self.__objects


    def get_validator(self):
        return self.__validator


    validator = property(get_validator, None, None, "validator's docstring")
    objects = property(get_objects, None, None, "objects's docstring")
    
    
    def save(self, obj):
        if not self.validator == obj.validator:
            raise TypeError("Can't add object {0}\t to current repo {1}".format(obj, self))
        
        if not self.findById(obj.id) is None:
            raise Exception("Duplicated id") 
        
        try:
            self.validator.validate(obj)
        except Exception as ex:
            raise Exception("Object {0} is not valid.".format(obj) + str(ex))
        
        self.objects[obj.id] = obj
        
    
    def findById(self, objID):
        if not objID in self.objects.keys():
            return None
        
        return self.objects[objID]
    
    
    def getObjects(self):
        return self.objects.values()
    
    
class FileRepository(Repository):
    
    def __init__(self, validator, fileName):
        Repository.__init__(self, validator)
        self.__fileName = fileName
        self.__readFromFile()

    def set_file_name(self, value):
        self.__fileName = value

    def get_file_name(self):
        return self.__fileName


    fileName = property(get_file_name, set_file_name, None, "fileName's docstring")
    
    
    def save(self, obj):
        super().save(obj)
        
        self.__writeToFile()
        
    
    def __readFromFile(self):
        with open(self.fileName, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(";")
                
                super().save(Question(int(line[0]), line[1], line[2], line[3], line[4],
                                      line[5], line[6]))
    
    
    def __writeToFile(self):
        with open(self.fileName, "w") as f:
            for element in super().getObjects():
                f.write(str(element) + '\n')
