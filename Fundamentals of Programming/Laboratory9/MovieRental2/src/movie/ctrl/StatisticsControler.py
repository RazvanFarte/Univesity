'''
Created on 6 dec. 2016

@author: Dell
'''
import datetime

from movie.domain.entities.MostActiveClientsDTO import MostActiveClientsDTO
from movie.domain.entities.MostRentedDTO import MostRentedBookDTO
from movie.domain.entities.RentedMovieDTO import RentedMovieDTO
from movie.domain.entities.LateRentalDTO import LateRentlaDTO
from util.Containers import MyList, Sorter


class StatisticsControler(object):
    '''
    classdocs
    '''

    def __init__(self, rentalRepository, movieRepository, clientRepository):
        self.__rentalRepository = rentalRepository
        self.__movieRepository = movieRepository
        self.__clientRepository = clientRepository
        
           
    def __mostRentedMovies(self):
        '''
        Returns rented movies DTO'S
        '''
        listOfDTOs = MyList()
        r = self.__rentalRepository.get_all()
        
        for movie in self.__movieRepository.get_all():
            
            numOfRents = 0
            for rent in r:
                if movie.entityId == rent.movieId:
                    numOfRents += 1
                    
            if numOfRents != 0:
                listOfDTOs.append(MostRentedBookDTO(movie.entityId, movie.entityName, numOfRents))
                
        return listOfDTOs
    
    def mostRentedMovies(self):
        return list(Sorter.sort(self.__mostRentedMovies(),reverse=True))

    def __mostActiveClients(self):
        '''
        Returns active clients dto
        '''
        listOfDTOs = MyList()
        
        for elem in self.__clientRepository.get_all():
            
            numOfDays = 0
            for rent in self.__rentalRepository.get_all():
                if elem.entityId == rent.clientId:
                    numOfDays += ((datetime.date.today() if rent.returnedDate is None 
                                   else rent.returnedDate) - rent.rentedDate).days
                                   
            listOfDTOs.append(MostActiveClientsDTO(elem.entityId, elem.entityName, numOfDays))
                
        return listOfDTOs
    
    def mostActiveClients(self):
        return list(Sorter.sort(self.__mostActiveClients(), reverse=True))
         
    def searchClient(self, keyword):
        ''' Looks for any matching in name for fields of each Client and returns
        the list of matches'''
        
        listOfMatches = MyList()
        
        keyword = keyword.lower()
        for e in self.__clientRepository.get_all():
            if keyword in str(e.entityId): 
                listOfMatches.append(e)
                continue
            if keyword in e.entityName.lower():
                listOfMatches.append(e)
                continue
            
        return listOfMatches
        
    def searchMovies(self, keyword):
        ''' Looks for any matching in name for fields of each Movie and returns
        the list of matches'''
        
        listOfMatches = MyList()
        
        keyword = keyword.lower()
        for e in self.__movieRepository.get_all():
            if keyword in str(e.entityId): 
                listOfMatches.append(e)
                continue
            if keyword in e.entityName.lower():
                listOfMatches.append(e)
                continue
            if keyword in e.entityDescription.lower():
                listOfMatches.append(e)
                continue
            if keyword in e.entityGenre.lower():
                listOfMatches.append(e)
                continue
            
        return listOfMatches
     
    def __findActiveRentalByMovieId(self, movieId):
        #If the movie is still rented, returns the rent, otherwise returns None
        for rent in self.__rentalRepository.get_all():
            if movieId == rent.movieId:
                if rent.returnedDate is None:
                    return rent
        return None     
    
    def allRentedMovies(self):
        
        rentedMoviesDTOs = MyList()
        
        for movie in self.__movieRepository.get_all():
            rental = self.__findActiveRentalByMovieId(movie.entityId)
            if not rental is None:
                client = self.__clientRepository.find_by_id(rental.clientId)
                rentedMoviesDTOs.append(RentedMovieDTO(client.entityId, client.entityName, \
                                                   movie.entityId, movie.entityName))
        return rentedMoviesDTOs
    
    def __lateRentedMovies(self):
        
        
        rentedMoviesDTOs = []
        
        for movie in self.__movieRepository.get_all():
            rental = self.__findActiveRentalByMovieId(movie.entityId)
            if not rental is None:
                today = datetime.date.today()
                if today > rental.dueDate:
                    client = self.__clientRepository.find_by_id(rental.clientId)
                    rentedMoviesDTOs.append(LateRentlaDTO(client.entityId, client.entityName, \
                                                       movie.entityId, movie.entityName, \
                                                       (today - rental.dueDate).days))
        return rentedMoviesDTOs
         
    def lateRentedMovies(self):
        return list(Sorter.sort(self.__lateRentedMovies(),reverse=True))