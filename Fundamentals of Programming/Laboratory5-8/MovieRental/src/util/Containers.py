'''
Created on Jan 9, 2017

@author: Razvan
'''

class MyList(list):

    
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
        
        self.__index = 0
    
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
            return
        
        self.__checkKey(key)
        del self.__l[key]
        
        
    def __iter__(self, *args, **kwargs):
        return self.__l.__iter__( *args, **kwargs)
    
    
    def __str__(self):
        return str(self.__l)
    
    
    def append(self, *args, **kwargs):
        return self.__l.append(*args, **kwargs)
    
    
    def index(self, *args, **kwargs):
        return self.__l.index(*args, **kwargs)
    
    
    def reverse(self, *args, **kwargs):
        return self.__l.reverse(*args, **kwargs)
    
    
    def pop(self, *args, **kwargs):
        return self.__l.pop(*args, **kwargs)
    
    
    def extend(self, *args, **kwargs):
        return self.__l.extend(*args, **kwargs)
    
    
    def __add__(self, *args, **kwargs):
        return self.__l.__add__(*args, **kwargs)
    

    def __contains__(self, *args, **kwargs):
        return self.__l.__contains__(*args, **kwargs)

l = MyList(1, 2, 3, 4, 5, lenght=10)
l[2:4] = ["Razvan","Dan","Farte"]
l.append("Aurel")
for i in l:
    print(i)
    
if 1 in l:
    print(True)
del l[1]
print(l)

li = MyList(*tuple(l))
print(li)
