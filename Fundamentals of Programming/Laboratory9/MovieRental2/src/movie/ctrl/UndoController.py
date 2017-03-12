'''
Created on 12 dec. 2016

@author: Dell
'''

class UndoController(object):
    
    def __init__(self):
        self.__operations = []
        self.__index = -1
        self.__canRecord = True
        
    def addOperation(self, operation):
        if self.__canRecord == True:
            self.__operations[-1].append(operation)
            
    def newOperation(self):
        if self.__canRecord == False:
            return False
        
        self.__operations = self.__operations[0:self.__index + 1]
        self.__operations.append([])
        self.__index += 1
        
    def undo(self):
        if self.__index < 0:
            raise Exception("Things cannot be undone anymore!")
        
        self.__canRecord = False
        
        for oper in self.__operations[self.__index]:
            oper.undo()
        
        self.__canRecord = True
    
        self.__index -= 1
        return True
    
    def redo(self):
        if self.__index >= len(self.__operations) - 1:
            raise Exception("That's all")
        
        self.__index += 1
        self.__canRecord = False
        
        #TODO How will loop. From right to left or viceversa. Set direction
#         for oper in self.__operations[self.__index]:
#             oper.redo()
#         
        operations = self.__operations[self.__index]
        for i in range(len(operations) - 1, -1, -1):
            operations[i].redo()
            
        self.__canRecord = True
        
        return True
    
class FunctionCall(object):
    '''
    Is responsible with holding a function pointer and its params
    and with calling properly a function
    '''

    def __init__(self, functionName, *params):
        '''
        Constructor
        '''
        self.__functionName = functionName
        self.__params = params
        
    def callFunction(self):
        '''Cals the holded function'''
        self.__functionName(*self.__params)
        
        
class Operation():
    '''
    This class holds together undo and redo methods and call them
    '''
    
    def __init__(self, functionUndo, functionRedo):
        self.__functionUndo = functionUndo
        self.__functionRedo = functionRedo
        
    def undo(self):
        self.__functionUndo.callFunction()
        
    def redo(self):
        self.__functionRedo.callFunction()
        
