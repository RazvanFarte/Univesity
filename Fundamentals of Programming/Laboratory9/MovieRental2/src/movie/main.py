'''
Created on 8 nov. 2016

@author: f
'''
from movie.ctrl.ClientControler import ClientControler
from movie.ctrl.ClientControllerUndo import ClientControllerUndo
from movie.ctrl.MovieControler import MovieControler
from movie.ctrl.RentalControler import RentalControler
from movie.ctrl.RentalControllerUndo import RentalControllerUndo
from movie.ctrl.StatisticsControler import StatisticsControler
from movie.ctrl.UndoController import UndoController
from movie.domain.exceptions.MovieException import MovieException
from movie.domain.validators.ClientValidator import ClientValidator
from movie.domain.validators.MovieValidator import MovieValidator
from movie.domain.validators.RentalValidator import RentalValidator
from movie.repo.Repository import Repository, FileRepository
from movie.ui.Console import Console
from movie.ctrl.MovieControllerUndo import MovieControllerUndo
from util.Utils import PropertiesHandler
from movie.repo.Repository import BinaryRepository


if __name__ == '__main__':
    
    fileName = "settings.properties"
    propertiesHandler = PropertiesHandler(fileName)
    
    repositoryChose = propertiesHandler.getRepository()

    if repositoryChose == PropertiesHandler.MEMORYREPOSITORY:
        clientRepository = Repository(ClientValidator)        
        movieRepository = Repository(MovieValidator)
        rentalRepository = Repository(RentalValidator)
    else:
        clientsFile = propertiesHandler.getClientFile()
        moviesFile = propertiesHandler.getMovieFile()
        rentalsFile = propertiesHandler.getRentalsFile()            
        
        if repositoryChose == PropertiesHandler.FILEREPO:
            clientRepository = FileRepository(ClientValidator, clientsFile)        
            movieRepository = FileRepository(MovieValidator, moviesFile)
            rentalRepository = FileRepository(RentalValidator, rentalsFile)         
    
        if repositoryChose == PropertiesHandler.BINARYREPOSITORY:
            clientRepository = BinaryRepository(ClientValidator, clientsFile)        
            movieRepository = BinaryRepository(MovieValidator, moviesFile)
            rentalRepository = BinaryRepository(RentalValidator, rentalsFile)
    
    try:
        undoController = UndoController()
        clientControler = ClientControllerUndo(clientRepository, undoController)
        movieControler = MovieControllerUndo(movieRepository, undoController)
        rentalControler = RentalControllerUndo(rentalRepository, movieRepository, clientRepository, undoController)
        statisticsControler = StatisticsControler(rentalRepository, movieRepository, clientRepository)
        
        #TODO Implement a GUI
        if propertiesHandler.getUi() == PropertiesHandler.GUI:
            pass
        
        if propertiesHandler.getUi() == PropertiesHandler.CONSOLE:
            cons = Console(movieControler, clientControler, rentalControler, statisticsControler, undoController)
            cons.runConsole()
            
    except MovieException as me:
        print(me)
        
    print("Program terminated")
