'''
Created on Feb 23, 2017

@author: Razvan
'''

class Repository(object):
    '''
    classdocs
    '''


    def __init__(self, validator):
        '''
        Constructor
        '''
        self.__validator = validator
        self.__objects = []

    def get_objects(self):
        return self.__objects


    def set_objects(self, value):
        self.__objects = value


    def del_objects(self):
        del self.__objects

        
    def get_validator(self):
        return self.__validator


    def set_validator(self, value):
        self.__validator = value


    def del_validator(self):
        del self.__validator

    validator = property(get_validator, set_validator, del_validator, "validator's docstring")
    objects = property(get_objects, set_objects, del_objects, "objects's docstring")
    
    def __removeFirst(self):
        return self.objects.pop(0)

    def save(self, obj):
        removed = None
        
        if self.validator != obj.validator:
            raise Exception("Object {} not for repository {}".format(obj, self))
        
        try:
            self.validator.validate(obj)
        except Exception as ex:
            raise Exception("Error during validation:", ex)
        
        if len(self.objects) == 2:
            removed = self.__removeFirst()

        if obj in self.objects:
            if not removed is None:
                self.objects.insert(0, removed)
            raise Exception("Error during validation: ship overlaps")
        
        self.objects.append(obj)
        
            
        