'''
Created on Feb 22, 2017

@author: Razvan
'''

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, controller):
        '''
        Constructor
        '''
        self.__controller = controller
        
    def __readLine(self):
        line = input("Command: ")
        
        line = line.strip()
        line = line.split(" ")
        
        return line[0], line[1:] if len(line) > 1 else []
    
    def __addOrder(self, id, distance):
        self.__controller.save(int(id), int(distance))
        
    def __income(self, id):
        print(self.__controller.getIncome(int(id)))
        
    def __display(self):
        taximetrists = self.__controller.getBestTaxi()
        
        for elem in taximetrists:
            print(elem)
    
    def run(self):
        
        while True:
            comm, args = self.__readLine()
            
            if comm == "exit":
                break
            
            try:
                if comm == "add":
                    self.__addOrder(*args)
                    
                if comm == "income":
                    self.__income(*args)
                    
                if comm == "display":
                    self.__display(*args)
            except Exception as ex:
                print(ex)
            