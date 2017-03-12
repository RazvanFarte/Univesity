'''
Created on 8 nov. 2016

@author: Dell
'''
from movie.domain.entities.Client import Client
from movie.domain.entities.MostActiveClientsDTO import MostActiveClientsDTO


class ClientControler(object):
    '''
    classdocs
    '''

    def __init__(self, clientRepository):
        '''
        Constructor
        '''
        self.__clientRepository = clientRepository
        
    def add(self, clientId, clientName):
        self.__clientRepository.save(Client(clientId, clientName))

    def get_repository(self):
        return self.__clientRepository
        
    def get_all(self):
        return self.__clientRepository.get_all()
    
    def update(self, clientId, clientName):
        self.__clientRepository.update(clientId, Client(clientId, clientName))
        
    def remove(self, clientId):
        return self.__clientRepository.remove(clientId)
   
    
