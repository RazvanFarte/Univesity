'''
Created on 16 nov. 2016

@author: Dell
'''

def addProduct(repo, product):
    '''Adds to a repository list a product
    Input:
        repo - list of products
        product - an Product object
        
    Output:
        Adds an product object to list
        return - None'''
    repo.append(product)
    
def totalValue(repo):
    '''Calulates  the total value of products in warehouse
    Input:
        repo - list of products
        
    Output:
        return - the total value of products in warehouse'''
    valueProducts = 0
    for item in repo:
        valueProducts += item.get_product_price() * item.get_product_quantity()
    return valueProducts

def findByName(repo, productName):
    '''Finds the product with name productName and returns it. If it does not exists, it returns
    None
    Input:
        repo - list of products
        productName - product which must be found in list of Products
        
    Output:
        return - product object if it exists
                -None otherwise'''
    for item in repo:
        if item.get_product_name() == productName:
            return item
    return None

def removeProduct(repo, productName):
    '''Removes an item with name productName. If it does not exists, it raises an exception
    Input:
        repo - list of products
        productName - product whcih must be removed from list of products
    Output:
        Delete product with product name
        return - None
    Exception:
        If product with productName does not exist, it raises an exception'''
    product = findByName(repo,productName)
    if product is None:
        raise Exception("Product with name {0} does not exist".format(productName))
    repo.remove(product)
    