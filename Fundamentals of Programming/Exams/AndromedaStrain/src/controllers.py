'''
Created on Feb 17, 2017

@author: Razvan
'''
from src.domain import Person

class PersonController(object):
    '''
    classdocs
    '''

    def __init__(self, repo):
        '''
        Constructor
        '''
        self.__repo = repo
        
    def get_repo(self):
        return self.__repo

    repo = property(get_repo, None, None, "repo's docstring")
    
    def save(self, id, immunizationStatus, status, daysInfected):
        self.repo.save(Person(id, immunizationStatus, status, daysInfected))

class InfectionController(object):
    
    def __init__(self, personRepo, infectedRepo):
        self.__personRepo = personRepo
        self.__infectedRepo = infectedRepo
        
        illPersons = self.__getStatusPersons(personRepo.objects, Person.ILL)
        
        for person in illPersons:
            self.infectedRepo.save(person)

    def get_person_repo(self):
        return self.__personRepo


    def get_infected_repo(self):
        return self.__infectedRepo


    def set_person_repo(self, value):
        self.__personRepo = value


    def set_infected_repo(self, value):
        self.__infectedRepo = value


    def del_person_repo(self):
        del self.__personRepo


    def del_infected_repo(self):
        del self.__infectedRepo

    personRepo = property(get_person_repo, set_person_repo, del_person_repo, "personRepo's docstring")
    infectedRepo = property(get_infected_repo, set_infected_repo, del_infected_repo, "infectedRepo's docstring")
    
    def __getNonVaccinatedPersons(self, persons):
        l = []
        for person in persons:
            if person.immunizationStatus == Person.NONVACCINATED:
                l.append(person)
        
        return l
    
    def __getStatusPersons(self, persons, status):
        l = []
        for person in persons:
            if person.status == status:
                l.append(person)
        
        return l
    
    def __increaseNumOfDays(self, illPersons):
        for person in illPersons:
            person.daysInfected += 1
            
    def __vaccinatePerson(self, person):
        person.immunizationStatus = Person.VACCINATED
        person.status = Person.HEALTHY
        
    def __vaccinatePersons(self, persons):
        for person in persons:
            if person.daysInfected >= 3:
                self.__vaccinatePerson(person)
                self.infectedRepo.remove(person)
    
    def __printPersons(self, persons):
        for person in persons:
            print(person)
            
    def vaccinatePerson(self, personId):
        person = self.personRepo.findById(personId)
        
        if person.status == Person.HEALTHY:
            person.immunizationStatus = Person.VACCINATED
    
    def newDay(self):
        if self.infectedRepo.objects == []:
            raise Exception("There are no infected persons")
        
        self.__increaseNumOfDays(self.infectedRepo.objects)
        self.__vaccinatePersons(self.infectedRepo.objects)
        
        listOfNonVaccinatedPersons = self.__getNonVaccinatedPersons(self.personRepo.objects)
        infectablePersons = self.__getStatusPersons(listOfNonVaccinatedPersons, Person.HEALTHY)
        
        
        if infectablePersons == []:
            print("There are no persons to infect")
        else:
            newInfected = []
            for person in self.infectedRepo.objects:
                hPerson = infectablePersons.pop()
                hPerson.status = Person.ILL
                newInfected.append(hPerson)
                if infectablePersons == []:
                    break
            
            for person in newInfected:
                self.infectedRepo.save(person)
        
        self.__printPersons(self.personRepo.objects)
        
    
            
    