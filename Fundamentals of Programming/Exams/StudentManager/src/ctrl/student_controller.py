'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.student import Student

class StudentController(object):
    '''
    classdocs
    '''


    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__repo = repository
    
    
    def save(self, studentId, studentName, studentGroup):
        self.__repo.save(Student(int(studentId), studentName, int(studentGroup)))
        
    
    def remove(self, studentId):
        self.__repo.remove(int(studentId))
        
    
    def getAll(self):
        return self.__repo.getAll()