'''
Created on 7 nov. 2016

@author: Dell
'''

from movie.domain.exceptions.ValidatorException import ValidatorException
from movie.repo.RepositoryException import RepositoryException
from movie.domain.entities.Movie import Movie
from movie.domain.entities.Client import Client
from _datetime import datetime
from movie.domain.entities.Rental import Rental
from movie.domain.validators.ClientValidator import ClientValidator
from movie.domain.validators.MovieValidator import MovieValidator
from movie.domain.validators.RentalValidator import RentalValidator
import pickle
from util.Containers import MyList

class Repository(object):


    def __init__(self, validator_class):
        '''
        Constructor
        '''
        self.__validator = validator_class
        self.__entities = MyList()
        
    def find_by_id(self, entity_id):
        for entity in self.__entities:
            if entity.entityId == entity_id:
                return entity
        return None
    
    def save(self, entity):
        if (self.find_by_id(entity.entityId)) is not None:
            raise RepositoryException("Duplicated id for element: {0}".format(entity))

        try:
            self.__validator.validate(entity)
        except ValidatorException as ve:
            raise RepositoryException(ve)
        self.__entities.append(entity)
        
        return entity
        
    def remove(self, entity_id):
        if not len(self.__entities):
            raise RepositoryException("Repository is empty")
        entity = self.find_by_id(entity_id)
        if entity is None:
            raise RepositoryException("Entity with id {0} does not exists".format(entity_id))
        self.__entities.remove(entity)
        return entity
    
    def get(self):
        return {i:self.__entities[i] for i in range(len(self.__entities))}
        
    def get_all(self):
#         return self.__entities.values()
        return self.get().values()
    
    def update(self, entity_id, entity):
        x = self.find_by_id(entity_id)
        if x is None:
            raise RepositoryException("Entity with id {0} does not exists".format(entity_id))
        
        if entity.entityId != entity_id:
            raise RepositoryException("Id's mismatch. You are not allowed to change the Id.")
        
        index = self.__entities.index(x)
        
        self.__entities[index] = entity
        
class FileRepository(Repository):
    
    DATE_FORMAT = "%Y.%m.%d"
    
    def __init__(self, validator_class, fileName):
        Repository.__init__(self, validator_class)
        self.__validator = validator_class
        self.__fileName = fileName
        self.__loadFromFile(self.__fileName)
    
    def save(self, entity):
        entity = Repository.save(self, entity)
    
        self.__saveToFile(self.__fileName)
        
        return entity
    
    def remove(self, entity_id):
        entity = Repository.remove(self, entity_id)
        
        self.__saveToFile(self.__fileName)
        
        return entity
    
    def update(self, entity_id, entity):
        Repository.update(self, entity_id, entity)
        
        self.__saveToFile(self.__fileName)
    
    def __saveToFile(self, fileName):
        
        with open(fileName, "w") as file:
            for entity in self.get_all():
                
                if type(entity) is Client:
                    file.write(str(entity.entityId) + ',' + entity.entityName + '\n')

                if type(entity) is Movie:
                    file.write(str(entity.entityId) + ',' + entity.entityName + entity.entityDescription + \
                                ',' + entity.entityGenre + '\n')
                
                if type(entity) is Rental:
                    file.write(str(entity.entityId) + ',' + str(entity.movieId) + ',' + \
                               str(entity.clientId) + ',' + entity.rentedDate.strftime(FileRepository.DATE_FORMAT) + \
                               ',' + entity.dueDate.strftime(FileRepository.DATE_FORMAT) + \
                               ',' + (entity.returnedDate.strftime(FileRepository.DATE_FORMAT) if entity.returnedDate is not None else '-') + '\n')                   
                           
    def __loadFromFile(self, fileName):
        with open(fileName) as file:
            for line in file:
                line = line.strip('\n')
                arguments = line.split(',')
                
                if self.__validator == MovieValidator:
                    super().save( Movie( int(arguments[0]), arguments[1], arguments[2], arguments[3]) )
                    
                if self.__validator == ClientValidator:
                    super().save(Client(int(arguments[0]), arguments[1]))
                    
                if self.__validator == RentalValidator:
                    rentalDate = arguments[3].split(".")
                    dueDate = arguments[4].split(".")
                    
                    if arguments[5] == "-":
                        super().save(Rental(int(arguments[0]), int(arguments[1]), int(arguments[2]),datetime(int(rentalDate[0]),int(rentalDate[1]),int(rentalDate[2])), datetime(int(dueDate[0]),int(dueDate[1]),int(dueDate[2])),None))
                    else:
                        returnedDate = arguments[5].split(".")
                        super().save(Rental(int(arguments[0]), int(arguments[1]), int(arguments[2]),datetime(int(rentalDate[0]),int(rentalDate[1]),int(rentalDate[2])), datetime(int(dueDate[0]),int(dueDate[1]),int(dueDate[2])),datetime(int(returnedDate[0]),int(returnedDate[1]),int(returnedDate[2]))))
                    
class BinaryRepository(Repository):
    
    
    def __init__(self, validator_class, fileName):
        Repository.__init__(self, validator_class)
        self.__validator = validator_class
        self.__fileName = fileName
        self.__loadFromFile(self.__fileName)
    
    def save(self, entity):
        entity = Repository.save(self, entity)
    
        self.__saveToFile(self.__fileName)
        
        return entity
    
    def remove(self, entity_id):
        entity = Repository.remove(self, entity_id)
        
        self.__saveToFile(self.__fileName)
        
        return entity
    
    def update(self, entity_id, entity):
        Repository.update(self, entity_id, entity)
        
        self.__saveToFile(self.__fileName)
        
    def __saveToFile(self, fileName):
        with open(fileName, "wb") as f:
            pickle._dump(super().get(), f)
            
    def __loadFromFile(self, fileName):
        try:
            f = open(fileName, "rb")
            dictionary = pickle.load(f)
            for it in dictionary.keys():
                super().save(dictionary[it])
                
        except EOFError:
            """
                This is raised if input file is empty
            """
            return None
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e
