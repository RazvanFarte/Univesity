'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.validator import Validator
from src.domain.assignment_validator import AssignmentValidator

class Assignment(object):
    '''
    classdocs
    '''
    
    counter = 0

    def __init__(self, assignmentID=None, labNumber=None, labProblem=None, studentID=None,
                 validator = AssignmentValidator):
        '''
        Constructor
        '''
        Assignment.counter += 1
        if assignmentID == None:
            self.__id = Assignment.counter
        else:
            self.__id = assignmentID
            if self.__id > Assignment.counter:
                Assignment.counter = self.__id
            
        self.__lab = labNumber
        self.__problem = labProblem
        self.__studID = studentID
        self.__validator = validator 

    def get_validator(self):
        return self.__validator


    def del_validator(self):
        del self.__validator


    def get_id(self):
        return self.__id


    def del_id(self):
        del self.__id



    def get_lab(self):
        return self.__lab


    def get_problem(self):
        return self.__problem


    def get_stud_id(self):
        return self.__studID


    def set_lab(self, value):
        self.__lab = value


    def set_problem(self, value):
        self.__problem = value


    def set_stud_id(self, value):
        self.__studID = value


    def del_lab(self):
        del self.__lab


    def del_problem(self):
        del self.__problem


    def del_stud_id(self):
        del self.__studID

    lab = property(get_lab, set_lab, del_lab, "lab's docstring")
    problem = property(get_problem, set_problem, del_problem, "problem's docstring")
    studID = property(get_stud_id, set_stud_id, del_stud_id, "studID's docstring")
    id = property(get_id, None, del_id, "id's docstring")
    validator = property(get_validator, None, del_validator, "validator's docstring")
        