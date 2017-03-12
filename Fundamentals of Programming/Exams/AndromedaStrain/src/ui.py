'''
Created on Feb 17, 2017

@author: Razvan
'''
from src.domain import Person

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, personController, infectionController):
        '''
        Constructor
        '''
        self.__personController = personController
        self.__infectionController = infectionController

    def get_person_controller(self):
        return self.__personController

    personController = property(get_person_controller, None, None, "personController's docstring")
    
    def __readLine(self):
        line = input("Command: ")
        line = line.strip()
        line = line.split(" ")
        
        return line[0], line[1:] if len(line) > 1 else []
    
    def run(self):
        
        while True:
            command, args = self.__readLine()
            
            if command == "exit":
                break
            
            try:
                if command == "add":
                    self.__uiAddPerson(*args)
                    
                if command == "newDay":
                    self.__uiStartNewDay(*args)
                    
                if command == "vaccinate":
                    self.__uiVaccinatePerson(*args)
                    
            except Exception as ex:
                print(ex)
                
            
    def __uiAddPerson(self, id):
        self.personController.save(int(id), Person.NONVACCINATED, Person.HEALTHY, 0)
        
    def __uiStartNewDay(self):
        self.__infectionController.newDay()
        
    def __uiVaccinatePerson(self, id):
        self.__infectionController.vaccinatePerson(int(id))