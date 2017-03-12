'''
Created on 16 nov. 2016

@author: Dell
'''
from domain.product import Product
from src.domain.operations import addProduct, totalValue, removeProduct

def uiAddProduct(wareHouse, productName, productQuantity, productPrice):
    '''Adds a new product with (productName, productQuantity, productPrice)
     to wareHouse repository'''
    addProduct(wareHouse,Product(productName, productPrice, productQuantity))

def uiRemoveProduct(wareHouse, productName):
    '''Removes the product with productName from wareHouse repository'''
    removeProduct(wareHouse, productName)

def printAll(wareHouse):
    '''Prints all products in repo list'''
    for item in wareHouse:
        print(item)
        
def printTotal(wareHouse):
    '''Prints the total value of products in warehouse'''
    print("Total value of products in Warehouse is: " + str(totalValue(wareHouse)))
    

def uiList(wareHouse, option):
    '''Prints all wareHouse's products if option = "all" or
        prints the total value of products in wareHouse if option = "total"
    '''
    if option == "all":
        printAll(wareHouse)
    if option == "total":
        printTotal(wareHouse)
        

def uiReadLine():
    '''Reads from the comand line and returns coomands and arguments separated
    '''
    txt = input("Command:")
    
    txt = txt.split(' ')
    cmd = txt[0]
    arg = txt[1:]
    
    return cmd.lower(),arg

def setUp(wareHouse):
    '''Initializes the Warehouse'''
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

def run():
    commands = {"add":uiAddProduct,"remove":uiRemoveProduct,"list":uiList}
    wareHouse = []
    setUp(wareHouse)
    
    while True:
        cmd, arg = uiReadLine()
        
        try:
            if cmd == "exit":
                break
            
            if cmd == "add" and len(arg) < 3:
                l = len(arg)
                raise Exception("The number of arguments for add function must be 3.You gave only {0} arguments".format(l))
            
            commands[cmd](wareHouse, *arg)
        except Exception as e:
            print(e)

run()
