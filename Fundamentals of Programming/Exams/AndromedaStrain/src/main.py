'''
Created on Feb 17, 2017

@author: Razvan
'''
from src.ui import Console
from src.controllers import PersonController, InfectionController
from src.repo import FileRepository, Repository
from src.domain import PersonValidator

if __name__ == '__main__':
    
    personRepository = FileRepository(PersonValidator, "persons")
    personController = PersonController(personRepository)
    
    illPersonRepository = Repository(PersonValidator)
    illPersonController = InfectionController(personRepository, illPersonRepository)
    
    console = Console(personController, illPersonController)
    try:
        console.run()
    except Exception as ex:
        print(ex)