'''
Created on Feb 16, 2017

@author: Razvan
'''
from src.entities import Sentence, SentenceValidator
from unittest.case import TestCase

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

        
    def save(self, obj):
        """
        Input
            obj - object to be saved in repository (Sentence)
        """
        if obj in self.objects:
            raise Exception("Duplicate sentences")
        
        try:
            self.validator.validate(obj)
        except Exception as ex:
            raise Exception("Error durring validate sentence. " + str(ex))
        
        self.objects.append(obj)
        
    validator = property(get_validator, None, None, "validator's docstring")
    objects = property(get_objects, None, None, "objects's docstring")
    

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

    fileName = property(get_file_name, set_file_name, del_file_name, "fileName's docstring")
    
    def save(self, obj):
        Repository.save(self, obj)
        
        self.__saveToFile()
        
    def __saveToFile(self):
        with open(self.fileName, "w") as f:
            for object in self.objects:
                f.write(str(object) + "\n")
    
    def __loadFromFile(self):
        with open(self.fileName, "r") as f:
            for line in f:
                line = line.strip()
                words = line.split(" ")
                
                super().save(Sentence(words))
                
                
class TestRepository(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.sentenceRepo = FileRepository(SentenceValidator, "testFile")
        
    def testSave(self):
        l = ["ana","are","mere"]
        self.sentenceRepo.save(Sentence(l))
        
        self.assertRaisesRegex(Exception, self.sentenceRepo.save(Sentence(l)))
        l.append("pere")
        
        self.sentenceRepo.save(Sentence(l))
