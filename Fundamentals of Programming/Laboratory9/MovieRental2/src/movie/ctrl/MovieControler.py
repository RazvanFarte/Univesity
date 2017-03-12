'''
Created on 8 nov. 2016

@author: Dell
'''
from movie.domain.entities.Movie import Movie
from movie.domain.exceptions.MovieException import MovieException
from movie.domain.entities.MostRentedDTO import MostRentedBookDTO


class ControlerException(MovieException):
    pass

class MovieControler(object):
    '''
    classdocs
    '''
    
    def __init__(self, movieRepository):
        self.__movieRepository = movieRepository
        
    def add(self, movieId, movieTitle, movieDescription, movieGenre):
        self.__movieRepository.save(Movie(movieId, movieTitle, movieDescription, movieGenre))
        
    def get_all(self):
        return self.__movieRepository.get_all()
    
    def get_repository(self):
        return self.__movieRepository
    
    def update(self, movieId, tag, valueUpdate):
        
        movie = self.__movieRepository.find_by_id(int(movieId))
        if movie is None:
            raise ControlerException("Movie with id {0} does not exist".format(movieId))
        comms = {"movieTitle":movie.set_entity_name,
                 "movieDescription":movie.set_entity_description,
                 "movieGenre":movie.set_entity_genre}
        
        comms[tag](valueUpdate)
        self.__movieRepository.update(movieId, movie)
    
    def remove(self, movieId):
        return self.__movieRepository.remove(movieId)
    
    