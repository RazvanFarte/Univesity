'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.student import Student
from src.domain.grade import Grade

class GradeController(object):
    '''
    classdocs
    '''


    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__repo = repository
    
    
    def save(self, gradeId, studentId, labNumber, labProblem, gradeValue):
        self.__repo.save(Grade(int(gradeId), int(studentId), int(labNumber), int(labProblem), int(gradeValue)))
        
    
    def remove(self, gradeId):
        self.__repo.remove(int(gradeId))
        
    
    def getAll(self):
        return self.__repo.getAll()
    
    
    def hasGrades(self, studentId):
        for elem in self.__repo.getAll():
            if elem.studentId == studentId:
                return True
            
        return False