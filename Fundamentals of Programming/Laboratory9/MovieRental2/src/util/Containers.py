'''
Created on Jan 9, 2017

@author: Razvan
'''
from random import shuffle
from nt import stat
from movie.domain.entities.Client import Client

class MyList(object):

    
    def __init__(self, *elements, lenght=0):
        '''Creates an zero initialized list of given lenght
        
        Input:
            - elements - tuple of elements to be added to list
            - lenght - keyword argument. Will create a zero initialized list of its value
        '''
        
        x = len(elements)
        if lenght > x:
            self.__len = lenght
        else:
            self.__len = x
            
        self.__l = [0] * len(self)
        
        for i, element in enumerate(elements):
            self.__setitem__(i, element)
            
        self.__currentIndex = 0

    
    def __setitem__(self, key, value):
        '''Sets the element "value" at index "key"
        
        Input:
            key - must be a positive/negative integer. If index is negative, it will number
                 from the end.
            value - any object
            
        Raises:
            TypeError - if index is not an integer
            IndexError - if index exceeds the lenght of list
        '''
        if isinstance(key, slice):
            self.__l[key.start: key.stop: key.step] = value
            self.__len = len(self.__l)
            return
        
        self.__checkKey(key)
        self.__l[key] = value

    
    def __checkKey(self, key):
        '''Checks if key is a valid one or not
        '''
        if not isinstance(key, int):
            raise TypeError("Index must be an integer")
        if key >= len(self):
            raise IndexError("Index out of range")
        if key < 0:
            if key > -len(self):
                raise IndexError("Index out of range")
            key = len(self) + key
    
    
    def __getitem__(self, key):
        '''Returns the element positioned at index "key"
        
        Input:
            key - must be a positive/negative integer. If index is negative, it will number from the end.
            
        Raises:
            TypeError - if index is not an integer
            IndexError - if index exceeds the lenght of list
        '''
        if isinstance(key, slice):
            return self.__l[key.start: key.stop: key.step]
        
        self.__checkKey(key)
        return self.__l[key]
    
    
    def __len__(self):
        return self.__len
        
        
    def __delitem__(self, key):
        if isinstance(key, slice):
            del self.__l[key.start: key.stop: key.step]
            self.__len = len(self.__l)
            return
        
        self.__checkKey(key)
        del self.__l[key]
        self.__len = len(self.__l)
        
        
    def __iter__(self, *args, **kwargs):
        return self.__l.__iter__( *args, **kwargs)
    
    
    def __str__(self):
        return str(self.__l)
    
    
    def append(self, *args, **kwargs):
        x =  self.__l.append(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    
    def insert(self, *args, **kwargs):
        x = self.__l.insert(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    
    def index(self, *args, **kwargs):
        return self.__l.index(*args, **kwargs)
    
    
    def reverse(self, *args, **kwargs):
        return self.__l.reverse(*args, **kwargs)
    
    
    def remove(self, *args, **kwargs):
        x = self.__l.remove(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    
    
    def __next__(self):
        if self.__currentIndex == len(self):
            pass
    
    def pop(self, *args, **kwargs):
        x = self.__l.pop(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    
    
    def extend(self, *args, **kwargs):
        x = self.__l.extend(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    
    
    def __add__(self, *args, **kwargs):
        x = self.__l.__add__(*args, **kwargs)
        self.__len = len(self.__l)
        return x
    

    def __contains__(self, *args, **kwargs):
        return self.__l.__contains__(*args, **kwargs)


class Sorter():
    @staticmethod
    def sort(cont,key=None,reverse=False):
        container = cont[:]
        k = len(container)//2
        while k > 0:
            i = k
            while i < len(container):
                element = container[i]
                j = i-k
                while j > -1 and Sorter.__isOrdered(element, container[j], key,True,reverse):
                    container[j+k] = container[j]
                    j -= k
                container[j+k] = element
                
                i += 1
            k = k // 2
        
        return container
    
    @staticmethod
    def filter(container, function=None):
        '''Filters the elements from container which returns True from function
            container - an iterable
            function - a function pointer (or a None object) which returns True or False 
        '''
        if function is None:
            return [x for x in container]
        return [x for x in container if function(x)]
    
    @staticmethod
    def __isOrdered(element1, element2, key, eq, reverse):
        if key is None:
            key = lambda x:x        
        if key(element1) == key(element2):
            return eq
        if not reverse:
            return key(element1) < key(element2)
        return key(element1) > key(element2)

if __name__ == "__main__":
    l = MyList(1, 2, 3, 4, 5,6,7,8,9,10)
    
    shuffle(l)
    print(l)
    
#     for i in range(1,len(l)):
#         j = i
#         element = l[i]
#         while j > 0 and element < l[j-1]:
#             l[j] = l[j-1]
#             j -= 1
#             
#         l[j] = element
# 
#     for j in range(0,len(l)):
#         m = min(l[j:])
#         i = l.index(m)
#         
#         l[i],l[j] = l[j],l[i]
#     v = sorted(l)
#     while True:
#         if l == v:
#             break
#         shuffle(l) 
    l = MyList(Client(1, "Aurel"), Client(2, "Andrei"), Client(3, "Viorel"), Client(4, "Razvan"))
    l = Sorter.sort(l, lambda x:x.entityName, reverse=False)
    l = Sorter.filter(l, lambda x: "A" in x.entityName)
    
    for e in l:
        print(e)