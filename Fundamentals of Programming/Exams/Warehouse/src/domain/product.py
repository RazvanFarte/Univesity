'''
Created on 16 nov. 2016

@author: Dell
'''

class Product(object):
    '''
    Product of type: productName, productPrice,productQuantity
    '''
    
    
    def __init__(self, productName, productPrice, productQuantiy):
        '''
        Constructor
        '''
        self.__productName = productName
        self.__productPrice = int(productPrice)
        self.__productQuantity = int(productQuantiy)
        
        if self.__productPrice < 0 or self.__productQuantity < 0:
            raise Exception("Value for product's price and product's quantity must be positive")
                 
    def get_product_name(self):
        return self.__productName


    def get_product_price(self):
        return self.__productPrice


    def get_product_quantity(self):
        return self.__productQuantity


    def set_product_name(self, value):
        self.__productName = value


    def set_product_price(self, value):
        self.__productPrice = value


    def set_product_quantity(self, value):
        self.__productQuantity = value
        
    def __str__(self):
        return "Product name: {0}, product price: {1}, product quantity: {2}".format(self.get_product_name(),
                                                                                     self.get_product_price(),
                                                                                     self.get_product_quantity())
    
    productName = property(get_product_name, set_product_name, None, None)
    productPrice = property(get_product_price, set_product_price, None, None)
    productQuantity = property(get_product_quantity, set_product_quantity, None, None)
