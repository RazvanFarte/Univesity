'''
Created on 16 nov. 2016

@author: Dell
'''
from domain.product import Product
from domain.operations import addProduct, totalValue
from src.domain.operations import removeProduct, findByName

def testSetUp(wareHouse):
    wareHouse.append(Product("Wasser1", "100", "1"))
    wareHouse.append(Product("Wasser2", "200", "1"))
    wareHouse.append(Product("Wasser3", "300", "1"))
    wareHouse.append(Product("Wasser4", "400", "1"))
    wareHouse.append(Product("Wasser5", "500", "3"))
    wareHouse.append(Product("Wasser6", "600", "5"))
    wareHouse.append(Product("Wasser7", "700", "7"))
    wareHouse.append(Product("Wasser8", "800", "9"))
    wareHouse.append(Product("Wasser9", "900", "100"))
    wareHouse.append(Product("Wasser10", "1000", "20"))

def test_add_product():
    wareHouse = []
    testSetUp(wareHouse)
    lenght = len(wareHouse)
    
    addProduct(wareHouse, Product("Wasser11", 300, 2))
    assert len(wareHouse) > lenght
    for item in wareHouse:
        assert type(item.get_product_price()) is int
        assert type(item.get_product_quantity()) is int
        assert item.get_product_price() >= 0
        assert item.get_product_quantity() >= 0
        
def test_delete_product():
    wareHouse = []
    testSetUp(wareHouse)
    lenght = len(wareHouse)
    
    removeProduct(wareHouse, "Wasser10")
    assert lenght > len(wareHouse)
    assert findByName(wareHouse,"Wasser10") is None
    #IT's not sure, bcs we cand have multiple products with this name yet
    
    try:
        removeProduct(wareHouse, "Wasser11")
        assert False
    except Exception:
        assert True

def test_find_id():
    wareHouse = []
    testSetUp(wareHouse)
    
    assert findByName(wareHouse, "Wasser10") is not None
    assert findByName(wareHouse, "Wasser11") is None
    
def test_total_value():
    wareHouse = [] 
    testSetUp(wareHouse)
    
    t = totalValue(wareHouse)
    
    assert t >= 0
    assert type(t) is int

def test_all():
    test_add_product()
    test_find_id()
    test_delete_product()
    test_total_value()
    
test_all()