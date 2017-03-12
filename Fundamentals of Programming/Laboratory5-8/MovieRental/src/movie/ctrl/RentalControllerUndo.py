'''
Created on 13 dec. 2016

@author: Dell
'''
from movie.ctrl.RentalControler import RentalControler
from movie.ctrl.UndoController import FunctionCall, Operation
from movie.domain.entities.Rental import Rental

class RentalControllerUndo(RentalControler):
    '''
    classdocs
    '''
    
    def __init__(self, rentalRepository, movieRepository, clientRepository, undoController):
        RentalControler.__init__(self, rentalRepository, movieRepository, clientRepository)
        self.__undoController = undoController
        
    def add(self, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
        rent = RentalControler.add(self, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        
        if self.__undoController.newOperation() == False:
            return
        
        undo = FunctionCall(self.remove, rent.entityId)
        redo = FunctionCall(self.add, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        
        operation = Operation(undo, redo)
        
        self.__undoController.addOperation(operation)
        
    def remove(self, rentalId):
        rent = RentalControler.remove(self, rentalId)
        Rental.rentalCounter -= 1
        
        #Don't put that "if self.__undoController.newOperation() == False:" here!!!
        
        undo = FunctionCall(self.add, rent.entityId, rent.movieId, rent.clientId, rent.rentedDate, rent.dueDate, rent.returnedDate)
        redo = FunctionCall(self.remove, rentalId)
        
        operation = Operation(undo, redo)
        
        self.__undoController.addOperation(operation)
         
    def returnMovie(self, movieId):
        rent = RentalControler.returnMovie(self, movieId)
        
        if self.__undoController.newOperation() == False:
            return
        
        undo = FunctionCall(rent.set_returned_date, None)
        redo = FunctionCall(rent.set_returned_date, rent.returnedDate)
        
        operation = Operation(undo,redo)
        
        self.__undoController.addOperation(operation)
    
        
    