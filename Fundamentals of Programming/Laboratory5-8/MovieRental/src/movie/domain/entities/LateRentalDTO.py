'''
Created on 11 dec. 2016

@author: Dell
'''

class LateRentlaDTO(object):
    '''
    classdocs
    '''

    def __init__(self, clientId, clientName, movieId, movieTitle, numberOfDaysDelayed):
        self.__clientId = clientId 
        self.__clientName = clientName
        self.__movieId = movieId
        self.__movieTitle = movieTitle
        self.__numberOfDaysDelayed = numberOfDaysDelayed

    def get_number_of_days_delayed(self):
        return self.__numberOfDaysDelayed


    def set_number_of_days_delayed(self, value):
        self.__numberOfDaysDelayed = value


    def del_number_of_days_delayed(self):
        del self.__numberOfDaysDelayed


    def get_client_id(self):
        return self.__clientId


    def get_client_name(self):
        return self.__clientName


    def get_movie_id(self):
        return self.__movieId


    def get_movie_title(self):
        return self.__movieTitle


    def set_client_id(self, value):
        self.__clientId = value


    def set_client_name(self, value):
        self.__clientName = value


    def set_movie_id(self, value):
        self.__movieId = value


    def set_movie_title(self, value):
        self.__movieTitle = value


    def del_client_id(self):
        del self.__clientId


    def del_client_name(self):
        del self.__clientName


    def del_movie_id(self):
        del self.__movieId


    def del_movie_title(self):
        del self.__movieTitle

    clientId = property(get_client_id, set_client_id, del_client_id, "clientId's docstring")
    clientName = property(get_client_name, set_client_name, del_client_name, "clientName's docstring")
    movieId = property(get_movie_id, set_movie_id, del_movie_id, "movieId's docstring")
    movieTitle = property(get_movie_title, set_movie_title, del_movie_title, "movieTitle's docstring")
    numberOfDaysDelayed = property(get_number_of_days_delayed, set_number_of_days_delayed, del_number_of_days_delayed, "numberOfDaysDelayed's docstring")
        
    def __str__(self):
        return "Movie id: " + str(self.__movieId) + ", Movie title: " + self.__movieTitle + \
            ", Client id: " + str(self.__clientId) + ", Client name: " + self.__clientName  + \
            ", Days delayed: " + str(self.__numberOfDaysDelayed)
    
    
    def __lt__(self,lateRentalDTO):
        return self.numberOfDaysDelayed < lateRentalDTO.numberOfDaysDelayed
    
    def __gt__(self,lateRentalDTO):
        return self.numberOfDaysDelayed > lateRentalDTO.numberOfDaysDelayed
    
    def __le__(self,lateRentalDTO):
        return not self > lateRentalDTO
    
    def __ge__(self,lateRentalDTO):
        return not self < lateRentalDTO
 
            