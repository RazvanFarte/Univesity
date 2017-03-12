'''
Created on Feb 23, 2017

@author: Razvan
'''
from pip._vendor.colorama.win32 import COORD

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, gameController):
        '''
        Constructor
        '''
        self.__controller = gameController
        
    def get_controller(self):
        return self.__controller


    def set_controller(self, value):
        self.__controller = value


    def del_controller(self):
        del self.__controller

    controller = property(get_controller, set_controller, del_controller, "controller's docstring")

    def __readLine(self):
        line = input("Command: ")
        line = line.strip()
        
        line = line.split(" ", 1)
        
        return line[0], line[1:] if len(line) > 1 else []
    
    
    def __start(self):
        self.controller.start()
    
    def __cheats(self):
        pass
    
    def __getCoordinatesFromString(self, st):
        """Get from as string C1L1C2L2C3L3 values in two lists collums(as letters "A" "B"..) and rows
        
        Output
            returns list of stirngs
        """
        li = list(st)
        
        return [li[x] for x in range(len(li)) if x % 2 == 0],[li[x] for x in range(len(li)) if x % 2 == 1]
        
    
    def __addShip(self, coordinates):
        collums, rows = self.__getCoordinatesFromString(coordinates)
        self.controller.addShip(collums, rows)
    
    
    def run(self):
        
        commands = {"ship": self.__addShip, "cheats": self.__cheats, "start":self.__start}
        
        while True:
            comm, args = self.__readLine()
            
            if comm == "exit":
                break
            
            try:
                commands[comm](*args)
            except Exception as ex:
                print(ex)
            
    
            