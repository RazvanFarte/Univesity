'''
Created on 11 dec. 2016

@author: Dell
'''

class RentedMovieDTO(object):
    '''
    Gives information about who rented a movie
    '''
    
    def __init__(self, clientId, clientName, movieId, movieTitle):
        self.__clientId = clientId 
        self.__clientName = clientName
        self.__movieId = movieId
        self.__movieTitle = movieTitle

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
        
    def __str__(self):
        return "Movie id: " + str(self.__movieId) + ", Movie title: " + self.__movieTitle + \
            ", Client id: " + str(self.__clientId) + ", Client name: " + self.__clientName 
            