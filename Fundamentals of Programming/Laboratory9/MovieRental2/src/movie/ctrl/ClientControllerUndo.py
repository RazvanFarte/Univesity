'''
Created on 13 dec. 2016

@author: Dell
'''
from movie.ctrl.ClientControler import ClientControler
from movie.ctrl.UndoController import FunctionCall, Operation

class ClientControllerUndo(ClientControler):
    '''
    classdocs
    '''

    def __init__(self, clientRepository, undoController):
        '''
        Constructor
        '''
        
        #TODO What happens with private variables from superclass?
        ClientControler.__init__(self, clientRepository)
#         self.__clientRepository = undoController
        self.__undoController = undoController
        
    def add(self, clientId, clientName):
        ClientControler.add(self, clientId, clientName)
        
        #We make a new operation
        if self.__undoController.newOperation() == False:
            return
        
        #We define undo and redo
        redo = FunctionCall(self.add, clientId, clientName)
        undo = FunctionCall(self.remove, clientId)
        
        #We put them together
        operation = Operation(undo, redo)
        
        #Add operation object to undoController
        self.__undoController.addOperation(operation)
    
    def get_repository(self):
        return ClientControler.get_repository(self)
        
    def remove(self, clientId):
        client = ClientControler.remove(self, clientId)
        clientName = client.entityName
        
        if self.__undoController.newOperation() == False:
            return
        
        redo = FunctionCall(self.remove, clientId)
        undo = FunctionCall(self.add, client.entityId, clientName)
        
        self.__undoController.addOperation(Operation(undo, redo))
        
    def update(self, clientId, clientName):
        client = self.get_repository().find_by_id(int(clientId))
        
        ClientControler.update(self, clientId, clientName)
        
        self.__undoController.newOperation()
        
        redo = FunctionCall(self.update, clientId, clientName)
        undo = FunctionCall(self.update, clientId, client.entityName)
        
        self.__undoController.addOperation(Operation(undo, redo))