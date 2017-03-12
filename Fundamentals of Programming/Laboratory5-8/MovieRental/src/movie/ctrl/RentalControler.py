'''
Created on 8 nov. 2016

@author: Dell
'''
from movie.domain.entities.Rental import Rental
from datetime import date
from util.Utils import Utils
from movie.repo.Repository import Repository
from movie.repo.RepositoryException import RepositoryException
import datetime

class RentalControler(object):

    def __init__(self, rentalRepository, movieRepository, clientRepository):
        self.__rentalRepository = rentalRepository
        self.__movieRepository = movieRepository
        self.__clientRepository = clientRepository
        
    def add(self, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
        if not self.__canRent(movieId, clientId):
            raise RepositoryException("Client with id {0} cannot rent movies anymore".format(clientId))
        
        return self.__rentalRepository.save(Rental(rentalId,movieId, clientId, rentedDate,
                                            dueDate, returnedDate))
        
    def removeClient(self, clientId):
#         l = []
#         for rent in self.get_all():
#             if rent.clientId == clientId:
#                 l.append(rent)
#          
#         for rent in l:    
#             self.remove(rent.entityId)
#         lista = list(self.get_all())
        for rent in list(self.get_all()):
            if rent.clientId == clientId:
                self.remove(rent.entityId)
            
    def removeMovie(self, movieId):
#         l = []
#         for rent in self.get_all():
#             if rent.movieId == movieId:
#                 l.append(rent)
#                 
#         for rent in l:
#             self.remove(rent.entityId)
        for rent in list(self.get_all()):
            if rent.movieId == movieId:
                self.remove(rent.entityId)

    def remove(self, rentalId):
        return self.__rentalRepository.remove(rentalId)
        
    def returnMovie(self, movieId):
        
        if not self.__existMovie(movieId):
            raise RepositoryException("Movie with id {0} does not exists".format(movieId))
        
        for rent in self.__rentalRepository.get_all():
            if movieId == rent.movieId:
                if rent.returnedDate is None:
                    rent.returnedDate = datetime.datetime.today()
                    return rent
                
        raise RepositoryException("Movie with id {0} was not borrowed".format(movieId))


    def get_all(self):
        return self.__rentalRepository.get_all()
    
    def __canRent(self, movieId, clientId):
        if not self.__existMovie(movieId):
            raise RepositoryException("Movie with id {0} does not exists".format(movieId))
        if not self.__existClient(clientId):
            raise RepositoryException("Client with id {0} does not exists".format(clientId))
        if not self.__isMovieAvailable(movieId):
            raise RepositoryException("Movie with id {0} is already taken.".format(movieId))
        
        rentedList = self.__rentedMovies(clientId)
        
        if rentedList == []:
            return True
        
        for i in rentedList:
            if i.returnedDate is None and datetime.date.today() > i.dueDate:
                return False
        
        return True
    
    def __existMovie(self, movieId):
        if self.__movieRepository.find_by_id(movieId) is None:
            return False
        return True
    
    def __existClient(self, clientId):
        if self.__clientRepository.find_by_id(clientId) is None:
            return False
        return True
    
    def __isMovieAvailable(self, movieId):
        '''
        If movie it's rented, returns the rent, els returns None
        '''
        
        for rent in self.__rentalRepository.get_all():
            if movieId == rent.movieId:
                if rent.returnedDate is None:
                    return False
                
        return True
    
    def __rentedMovies(self, clientId):
        '''
        Returns the list of movies rented by client
        '''
        x = []
        for i in self.__rentalRepository.get_all():
            if clientId == i.clientId:
                x.append(i)
        return x