'''
Created on Feb 16, 2017

@author: Razvan
'''
from src.entities import Sentence


class SentenceController(object):
    '''
    classdocs
    '''


    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__repo = repository
    def get_repo(self):
        return self.__repo


    def set_repo(self, value):
        self.__repo = value
    
    def get_objects(self):
        return self.repo.get_objects()

    def del_repo(self):
        del self.__repo

    repo = property(get_repo, set_repo, del_repo, "repo's docstring")

    def save(self, sentence):
        """Saves a sentence in repository as Sentence object
        
        Input:
            sentence - a sentence as string
        Output:
            None
        """
        listOfWords = sentence.split(" ")
        self.repo.save(Sentence(listOfWords))
        
    