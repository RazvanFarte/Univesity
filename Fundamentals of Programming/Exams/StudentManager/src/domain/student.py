'''
Created on Feb 14, 2017

@author: Razvan
'''
from src.domain.student_validator import StudentValidator

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, studentId, studentName, groupNumber, validator = StudentValidator):
        '''
        studentId - int
        studentName - string
        groupNumber - int
        '''
        
        self.__id = studentId
        self.__name = studentName
        self.__group = groupNumber
        self.__validator = StudentValidator

    def get_validator(self):
        return self.__validator


    def del_validator(self):
        del self.__validator


    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def get_group(self):
        return self.__group


    def set_name(self, value):
        self.__name = value


    def set_group(self, value):
        self.__group = value


    def del_id(self):
        del self.__id


    def del_name(self):
        del self.__name


    def del_group(self):
        del self.__group

    id = property(get_id, None, del_id, "id's docstring")
    name = property(get_name, set_name, del_name, "name's docstring")
    group = property(get_group, set_group, del_group, "group's docstring")
    validator = property(get_validator, None, del_validator, "validator's docstring")
    
    
    def __str__(self, *args, **kwargs):
        return "Student id: {0}\nStudent name: {1}\nGroup: {2}\n".format(self.id, self.name,
                                                                        self.group)
        
    