'''
Created on Feb 22, 2017

@author: Razvan
'''
from src.domain import Order, IncomeDTO

class OrderController(object):
    '''
    classdocs
    '''


    def __init__(self, taximetristRepo, orederRepo):
        '''
        Constructor
        '''
        self.__taxiRepo = taximetristRepo
        self.__orederRepo = orederRepo

    def get_taxi_repo(self):
        return self.__taxiRepo


    def get_oreder_repo(self):
        return self.__orederRepo


    def set_taxi_repo(self, value):
        self.__taxiRepo = value


    def set_oreder_repo(self, value):
        self.__orederRepo = value


    def del_taxi_repo(self):
        del self.__taxiRepo


    def del_oreder_repo(self):
        del self.__orederRepo

    taxiRepo = property(get_taxi_repo, set_taxi_repo, del_taxi_repo, "taxiRepo's docstring")
    orederRepo = property(get_oreder_repo, set_oreder_repo, del_oreder_repo, "orederRepo's docstring")
    
    def save(self, id, distance):
        if self.taxiRepo.findById(id) is None:
            raise Exception("Taximetrist with id {} does not exist".format(id))
        
        self.orederRepo.save(Order(id, distance))

    def __getIncomeDTOs(self, objId):
        dtos = []
        
        for elem in self.orederRepo.objects:
            if elem.id == objId:
                taximetrist = self.taxiRepo.findById(objId)
                dtos.append(IncomeDTO(elem.id, taximetrist.name, elem.distance * 0.5))
                
        return dtos
    
    def __getOrdersById(self, id):
        orders = []
        
        for elem in self.orederRepo.objects:
            if elem.id == id:
                orders.append(elem)
                
        return orders
    
    def __getSum(self, id):
        sum = 0
        orders = self.__getOrdersById(id)
        
        for order in orders:
            sum += order.distance * 0.5 
            
        return sum
    
    def getIncome(self, id):
        
        sum = self.__getSum(id)
        name = self.taxiRepo.findById(id).name
        
        return IncomeDTO(id, name, sum)
    
    def getBestTaxi(self):
        
        dtos = []
        for elem in self.taxiRepo.objects:
            sum = self.__getSum(elem.id)
            dtos.append(IncomeDTO(elem.id, elem.name, sum))
        
        sorted(dtos, key=lambda x:x.income, reverse=False)
        
        return dtos