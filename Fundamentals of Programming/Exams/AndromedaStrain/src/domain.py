'''
Created on Feb 17, 2017

@author: Razvan
'''

class IDObject(object):
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id


    def del_id(self):
        del self.__id

    id = property(get_id, None, del_id, "id's docstring")


class Person(IDObject):
    '''
    classdocs
    '''
    HEALTHY = "healthy"
    ILL = "ill"
    VACCINATED = "vaccinated"
    NONVACCINATED = "non-vaccinated"
    
    def __init__(self, id, immunizationStatus, status, daysInfected):
        IDObject.__init__(self, id)
        self.__immunizationStatus= immunizationStatus
        self.__status = status
        self.__daysInfected = 0

    def get_days_infected(self):
        return self.__daysInfected


    def set_days_infected(self, value):
        self.__daysInfected = value


    def del_days_infected(self):
        del self.__daysInfected


    def get_immunization_status(self):
        return self.__immunizationStatus


    def get_status(self):
        return self.__status


    def set_immunization_status(self, value):
        self.__immunizationStatus = value


    def set_status(self, value):
        self.__status = value


    def del_immunization_status(self):
        del self.__immunizationStatus


    def del_status(self):
        del self.__status

    immunizationStatus = property(get_immunization_status, set_immunization_status, del_immunization_status, "immunizationStatus's docstring")
    status = property(get_status, set_status, del_status, "status's docstring")\
    
    def __str__(self):
        return str(super().id) + " " + self.immunizationStatus + " " + self.status + " " + str(self.daysInfected)
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            raise Exception("Object \"{}\" is not a person".format(other))
        
        if self.id == other.id:
            return True
        return False
    
    daysInfected = property(get_days_infected, set_days_infected, del_days_infected, "daysInfected's docstring")
   
class PersonValidator(object):
    @staticmethod
    def valiate(obj):
        if not obj.id is int:
            raise Exception("Id of object \"{}\" is not integer".format(obj))
        
        if obj.id < 0:
            raise Exception("Id of object \"{}\" is less than 0".format(obj))
        
        if obj.immunizationStatus != Person.NONVACCINATED:
            raise Exception("Person \"{}\" must be \"non-vaccinated\".".format(obj))
        
        if obj.status != Person.HEALTHY:
            raise Exception("Person \"{}\" must be \"healthy\"".format(obj)) 
        
          
          
        