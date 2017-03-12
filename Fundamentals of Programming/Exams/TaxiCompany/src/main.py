'''
Created on Feb 22, 2017

@author: Razvan
'''
from src.domain import Taximestrist
from src.validators import TaximetristValidator, OrderValidator
from src.repository import FileRepository
from src.controllers import OrderController
from src.console import Console

if __name__ == '__main__':
    
    taxiRepo = FileRepository(TaximetristValidator, "taxi")
    orderRepo = FileRepository(OrderValidator, "order")
    
    orderController = OrderController(taxiRepo, orderRepo)
    
    console = Console(orderController)
    
    try:
        console.run()
    except Exception as ex:
        print(ex)
    
    print("Exit!")