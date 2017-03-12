'''
Created on Feb 16, 2017

@author: Razvan
'''
from src.repo import FileRepository
from src.entities import SentenceValidator
from src.Controller import SentenceController
from src.ui import Console

if __name__ == '__main__':
    
    sentenceRepository = FileRepository(SentenceValidator, "sentences")
    sentenceController = SentenceController(sentenceRepository)
    
    console = Console(sentenceController)
    
    try:
        console.run()
    except Exception as ex:
        print(ex) 