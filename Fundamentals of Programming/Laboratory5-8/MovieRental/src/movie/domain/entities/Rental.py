'''
Created on 7 nov. 2016

@author: Dell
'''
from movie.domain.exceptions.MovieException import MovieException
from movie.domain.validators.RentalValidator import RentalValidator
from _datetime import datetime


class Rental(object):
    '''
    classdocs
    '''
    __dateFormat = "%Y.%m.%d"
    rentalCounter = 0

    def __init__(self, rentalId,movieId, clientId, rentedDate, dueDate, returnedDate):
        '''
        Constructor
        '''
        
        #When I delete an element and undo it, i would like to keep the previous id.
        #When I create a new one, I will add the next index.
        Rental.rentalCounter += 1
        self.__rentalId = Rental.rentalCounter
        if rentalId is not None:
            self.__rentalId = rentalId
            
        self.__movieId = movieId
        self.__clientId = clientId
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate
        

    def get_entity_id(self):
        return self.__rentalId


    def get_movie_id(self):
        return self.__movieId


    def get_client_id(self):
        return self.__clientId


    def get_rented_date(self):
        return self.__rentedDate

    def get_due_date(self):
        return self.__dueDate


    def get_returned_date(self):
        return self.__returnedDate


    def set_rented_date(self, value):
        self.__rentedDate = value


    def set_due_date(self, value):
        self.__dueDate = value


    def set_returned_date(self, value):
        self.__returnedDate = value


    def del_entity_id(self):
        del self.__rentalId


    def del_movie_id(self):
        del self.__movieId


    def del_client_id(self):
        del self.__clientId


    def del_rented_date(self):
        del self.__rentedDate


    def del_due_date(self):
        del self.__dueDate


    def del_returned_date(self):
        del self.__returnedDate

    entityId = property(get_entity_id, None, del_entity_id, "rentalId's docstring")
    movieId = property(get_movie_id, None, del_movie_id, "movieId's docstring")
    clientId = property(get_client_id, None, del_client_id, "clientId's docstring")
    rentedDate = property(get_rented_date, set_rented_date, del_rented_date, 
                          "rentedDate's docstring")
    dueDate = property(get_due_date, set_due_date, del_due_date, "dueDate's docstring")
    returnedDate = property(get_returned_date, set_returned_date, del_returned_date, 
                            "returnedDate's docstring")
    
    def __str__(self):
        return ("Rental id: {x1}, movie id: {x2}, client id: {x3}," \
            " rented date: {x4}, due date: {x5}, returned date: {x6}").format(x1 = self.entityId, 
                                                                  x2 = self.movieId,
                                                                  x3 = self.clientId,
                                                                  x4 = self.rentedDate.strftime(Rental.__dateFormat),
                                                                  x5 = self.dueDate.strftime(Rental.__dateFormat),
                                                                  x6 = "-" if self.returnedDate is None else self.returnedDate.strftime(Rental.__dateFormat))
    
    def __eq__(self, other):
        if not isinstance(other, Rental):
            raise TypeError("Second argument must be a Rental")
        return self.entityId == other.entityId
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    