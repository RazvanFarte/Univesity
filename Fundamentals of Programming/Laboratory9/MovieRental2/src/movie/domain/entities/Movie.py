'''
Created on 7 nov. 2016

@author: Dell
'''
from movie.domain.validators.MovieValidator import MovieValidator


class Movie(object):
    '''
    classdocs
    '''
#     TODO:For later implementation use constants
#     COMEDY = 1
#     DRAMA = 2
#     ROMANCE = 3
#     THRILLER = 4

    def __init__(self, movieId, movieTitle, movieDescription, movieGenre):
        '''
        Constructor
        movieId - integer
        movieTitle - string
        movieDescription - string
        movieGenre - string
        '''
        self.__movieId = movieId
        self.__movieTitle = movieTitle
        self.__movieDescription = movieDescription
        self.__movieGenre = movieGenre
        
    def get_entity_id(self):
        return self.__movieId


    def get_entity_name(self):
        return self.__movieTitle


    def get_entity_description(self):
        return self.__movieDescription


    def get_entity_genre(self):
        return self.__movieGenre


    def set_entity_name(self, value):
        self.__movieTitle = value


    def set_entity_description(self, value):
        self.__movieDescription = value


    def set_entity_genre(self, value):
        self.__movieGenre = value


    def del_entity_id(self):
        del self.__movieId


    def del_entity_name(self):
        del self.__movieTitle


    def del_entity_description(self):
        del self.__movieDescription


    def del_entity_genre(self):
        del self.__movieGenre

    entityId = property(get_entity_id, None, del_entity_id, "movieId's docstring")
    entityName = property(get_entity_name, set_entity_name, del_entity_name, "movieTitle's docstring")
    entityDescription = property(get_entity_description, set_entity_description, del_entity_description, "movieDescription's docstring")
    entityGenre = property(get_entity_genre, set_entity_genre, del_entity_genre, "movieGenre's docstring")

    def __str__(self,):
        return ("Movie id: {x1}, title: {x2}, movie description: {x3}" \
                ", movie genre: {x4}").format(x1 = self.entityId, x2 = self.entityName,
                                             x3 = self.entityDescription, x4 = self.entityGenre)
        
    def __eq__(self, other):
        if not isinstance(other, Movie):
            raise("Second argument is not a Movie")
        return self.entityId == other.entityId
    
    def __ne__(self, other):
        return not self.__eq__(other)
