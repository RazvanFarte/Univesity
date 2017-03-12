'''
Created on Feb 14, 2017

@author: Razvan
'''

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, studentController, gradeController, assignmentController):
        '''
        Constructor
        '''
        self.__studContr = studentController
        self.__grContr = gradeController
        self.__assContr = assignmentController
        
    
    def __addStudent(self, studentId, studentName, studentGroup):    
        self.__studContr.save(int(studentId), studentName, int(studentGroup))
        
    
    def __removeStudent(self, studentId):
        if not self.__grContr.hasGrades(int(studentId)):
            return self.__studContr.remove(int(studentId))
        raise Exception("Student has grades!")
    
    
    def __printStudents(self):
        for elem in self.__studContr.getAll():
            print(elem)
            
    
    def __readLine(self):
        line = input("Command: ")
        
        line = line.strip()
        line = line.split(" ")
        
        return line[0], [] if line[1:] is None else line[1:]
    
    
    def __addGrade(self, gradeId, studentId, labNumber, labProblem, gradeValue):
        self.__grContr.save(int(gradeId), int(studentId), int(labNumber), 
                            int(labProblem), int(gradeValue))
        
    
    def __removeGrade(self, gradeId):
        self.__grId(int(gradeId))
        
    
    def __printGrades(self):
        for elem in self.__grContr.getAll():
            print(elem)
    
    
    def __assignStudent(self, studentId, problemNumber, labNumber):
        self.__assContr.assignToStudent(int(labNumber), int(problemNumber), int(studentId))
        
    
    def __assignGroup(self, labNumber, groupNumber):
        self.__assContr.assignToGroup(int(labNumber), int(groupNumber))
    
    
    def run(self):
        
        commands = {"addStudent": self.__addStudent,"printStudents": self.__printStudents,
                    "removeStudent": self.__removeStudent, "addGrade": self.__addGrade,
                    "printGrades": self.__printGrades, "removeGrades": self.__removeGrade,
                    "assignStudent": self.__assignStudent, "assignGroup": self.__assignGroup}
        
        while True:
            comm, args = self.__readLine()
            
            if comm == "exit":
                break
            
            try:
                commands[comm](*args)
            except TypeError as ex:
                print("TypeError " + str(ex))
            except ValueError as ex:
                print("ValueError " + str(ex))
            except Exception as ex:
                print(str(ex))