'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.domain.assignment import Assignment
from src.domain.grade import Grade

class AssignmentCotroller(object):
    '''
    classdocs
    '''


    def __init__(self, assignmentRepository, gradeRepository, studentRepository):
        '''
        Constructor
        '''
        self.__assignmentRepository = assignmentRepository
        self.__gradeRepository = gradeRepository
        self.__studentRepository = studentRepository
        
        
    def assignToStudent(self, labNumber, problemNumber, studentId):
        if self.__hasAssigned(labNumber, studentId):
            raise Exception("Homework already assigned")
        
        assignment = Assignment(None, labNumber, problemNumber, studentId)
        
        self.__assignmentRepository.save(assignment)
        
    
    def assignToGroup(self, labNumber, groupNumber):
        indexAssignment = 1
        for elem in self.__studentRepository.getAll():
            if elem.group == groupNumber:
                try:
                    self.assignToStudent(labNumber, indexAssignment, elem.id)
                    indexAssignment += 1
                except Exception:
                    pass
                
    def gradeStudent(self, studentId, labNumber, gradeValue):
        """Grade a student for a laboratory
        """
        if not self.__studentRepository.findById(studentId):
            raise Exception("Student does not exist")
        
        if not self.__hasAssigned(labNumber, studentId):
            raise Exception("Student is not assigned a laboratory")
        
        self.__gradeRepository.save(Grade(None, studentId, labNumber, 0, gradeValue))
    
                
    def __hasAssigned(self, labNumber, studentId):
        for elem in self.__assignmentRepository.getAll():
            if elem.lab == labNumber and elem.studID == studentId:
                return True
        return False