'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.repo.repository import Repository
from src.domain.student_validator import StudentValidator
from src.domain.grade_validator import GradeValidator
from src.domain.student import Student
from src.domain.grade import Grade
from src.domain.assignment_validator import AssignmentValidator
from src.domain.assignment import Assignment

class FileRepository(Repository):
    '''
    classdocs
    '''


    def __init__(self, validatorClass, fileName):
        Repository.__init__(self, validatorClass)
        self.__fileName = fileName
        self.__loadFromFile()
    
    
    def findById(self, objID):
        for elem in super().getAll():
            if elem.id == objID:
                return True
        return False
    
    
    def save(self, obj):
        Repository.save(self, obj)
        
        self.__saveToFile()
        
        
    def remove(self, objId):
        Repository.remove(self, objId)
        
        self.__saveToFile()
        
        
    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            for elem in self.getAll():
                
                if elem.validator == StudentValidator:
                    f.write(str(elem.id) + ";" + elem.name + ";" + str(elem.group) + "\n")
                
                if elem.validator == GradeValidator:
                    f.write(str(elem.id) + ";" + str(elem.studentId) + ";" + 
                            str(elem.lab) + ";" + str(elem.problem) + ";" +
                            str(elem.grade) + "\n")
                    
                if elem.validator == AssignmentValidator:
                    f.write(str(elem.id) + ";" + str(elem.lab) + ";" + str(elem.problem) +
                            ";" + str(elem.studID))
                    
        
    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            for line in f:
                
                if self._Repository__validator == StudentValidator:
                    line = line.strip()
                    line = line.split(";")
                    super().save(Student(int(line[0]), line[1], int(line[2])))
                
                
                if self._Repository__validator == GradeValidator:
                    line = line.strip()
                    line = line.split(";")
                    super().save(Grade(int(line[0]), int(line[1]), int(line[2]),
                                       int(line[3]), int(line[4])))
                    
                if self._Repository__validator == AssignmentValidator:
                    line = line.strip()
                    line = line.split(";")
                    super().save(Assignment(int(line[0]), int(line[1]), int(line[2]),
                                       int(line[3])))