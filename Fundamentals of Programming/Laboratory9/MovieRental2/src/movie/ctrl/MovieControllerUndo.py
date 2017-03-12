'''
Created on 13 dec. 2016

@author: Dell
'''
from movie.ctrl.MovieControler import MovieControler
from movie.ctrl.UndoController import FunctionCall, Operation

class MovieControllerUndo(MovieControler):
    '''
    classdocs
    '''
    
    def __init__(self, movieRepository, undoController):
        MovieControler.__init__(self, movieRepository)
        self.__undoController = undoController
        
    def add(self, movieId, movieTitle, movieDescription, movieGenre):
        MovieControler.add(self, movieId, movieTitle, movieDescription, movieGenre)
        
        #We make a new operation
        if self.__undoController.newOperation() == False:
            return
        
        #We define undo and redo
        redo = FunctionCall(self.add, movieId, movieTitle, movieDescription, movieGenre)
        undo = FunctionCall(self.remove, movieId)
        
        #We put them together
        operation = Operation(undo, redo)
        
        #Add operation object to undoController
        self.__undoController.addOperation(operation)
        
    def remove(self, movieId):
        movie = MovieControler.remove(self, movieId)
        
        if self.__undoController.newOperation() == False:
            return
        
        redo = FunctionCall(self.remove, movieId)
        undo = FunctionCall(self.add, movie.entityId, movie.entityName, movie.entityDescription, 
                            movie.entityGenre)
        
        self.__undoController.addOperation(Operation(undo, redo))
        
    def update(self, movieId, tag, valueUpdate):
        movie = self.get_repository().find_by_id(movieId)
        
        movieName = movie.entityName
        movieDescription = movie.entityDescription
        movieGenre = movie.entityGenre

        MovieControler.update(self, movieId, tag, valueUpdate)
        
        if self.__undoController.newOperation() == False:
            return
        
        self.__undoController.newOperation()
        
        redo = FunctionCall(self.update, movieId, tag, valueUpdate)
        undo = FunctionCall(self.update, movieId, tag, (lambda x: movieName if tag == "movieTitle" else
                            movieDescription if tag == "movieDescription" else movieGenre)(movie))
        
        self.__undoController.addOperation(Operation(undo, redo))