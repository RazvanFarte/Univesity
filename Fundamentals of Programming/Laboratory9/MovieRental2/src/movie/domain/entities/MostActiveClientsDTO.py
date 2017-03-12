'''
Created on 6 dec. 2016

@author: Dell
'''

class MostActiveClientsDTO(object):
    '''
    classdocs
    '''

    def __init__(self, clientID, clientName, rentalDays):
        '''
        Tells us how many times was rented book with bookId and bookTitle
        '''
        
        self.__clientId = clientID
        self.__clientName = clientName
        self.__rentalDays = rentalDays

    def get_client_id(self):
        return self.__clientId


    def get_client_name(self):
        return self.__clientName


    def get_rental_days(self):
        return self.__rentalDays


    def set_client_id(self, value):
        self.__clientId = value


    def set_client_name(self, value):
        self.__clientName = value


    def set_rental_days(self, value):
        self.__rentalDays = value


    def del_client_id(self):
        del self.__clientId


    def del_client_name(self):
        del self.__clientName


    def del_rental_days(self):
        del self.__rentalDays
    
    clientId = property(get_client_id, set_client_id, del_client_id, "clientId's docstring")
    clientName = property(get_client_name, set_client_name, del_client_name, "clientName's docstring")
    rentalDays = property(get_rental_days, set_rental_days, del_rental_days, "rentalDays's docstring")

    def __str__(self):
        return "Id: {0}, Client: {1}, Rented days: {2}".format(self.clientId,self.clientName,
                                                               self.rentalDays)
    
    def __lt__(self,mostActiveClientsDTO):
        return self.rentalDays < mostActiveClientsDTO.rentalDays
    
    def __gt__(self,mostActiveClientsDTO):
        return self.rentalDays > mostActiveClientsDTO.rentalDays
    
    def __le__(self,mostActiveClientsDTO):
        return not self > mostActiveClientsDTO
    
    def __ge__(self,mostActiveClientsDTO):
        return not self < mostActiveClientsDTO
