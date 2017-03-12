'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.grade_validator import GradeValidator

class Grade(object):
    '''
    classdocs
    '''
    
    gradeCounter = 0

    def __init__(self, gradeId, studentId, labNumber, labProblem, grade, validator = GradeValidator):
        '''
        studentId - int
        labNumber - int
        labProlem - int
        grade - int
        '''
        Grade.gradeCounter += 1
        if gradeId == None:
            self.__gradeId = Grade.gradeCounter
        else:
            self.__gradeId = gradeId
            if self.__gradeId > Grade.gradeCounter:
                Grade.gradeCounter = self.__gradeId
        self.__id = studentId
        self.__lab = labNumber
        self.__problem = labProblem
        self.__grade = grade
        self.__validator = validator

    def get_grade_id(self):
        return self.__gradeId


    def del_grade_id(self):
        del self.__gradeId


    def get_validator(self):
        return self.__validator


    def del_validator(self):
        del self.__validator

        
    def get_id(self):
        return self.__id


    def get_lab(self):
        return self.__lab


    def get_problem(self):
        return self.__problem


    def get_grade(self):
        return self.__grade


    def set_lab(self, value):
        self.__lab = value


    def set_problem(self, value):
        self.__problem = value


    def set_grade(self, value):
        self.__grade = value


    def del_id(self):
        del self.__id


    def del_lab(self):
        del self.__lab


    def del_problem(self):
        del self.__problem


    def del_grade(self):
        del self.__grade

    studentId = property(get_id, None, del_id, "id's docstring")
    lab = property(get_lab, set_lab, del_lab, "lab's docstring")
    problem = property(get_problem, set_problem, del_problem, "problem's docstring")
    grade = property(get_grade, set_grade, del_grade, "grade's docstring")
    validator = property(get_validator, None, del_validator, "validator's docstring")
    id = property(get_grade_id, None, del_grade_id, "gradeId's docstring")
    
    
    def __str__(self, *args, **kwargs):
        return "Grade id: {0}\nStudent id: {4}\nLab number: {1}\nProblem num: {2}\nGrade: {3}\n".format(
            self.id, self.lab, self.problem, self.grade, self.studentId)
