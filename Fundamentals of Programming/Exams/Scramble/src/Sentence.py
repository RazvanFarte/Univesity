'''
Created on Feb 22, 2017

@author: Razvan
'''

class SentenceValidator(object):
    @staticmethod
    def validate(sentence):
        pass

class Sentence(object):
    '''
    classdocs
    '''
    def __init__(self, listOfWords, validator=SentenceValidator):
        '''
        Input
            listOfWords - wrods contained in sentence
        '''
        self.__words = listOfWords
        self.__validator = validator

    def get_validator(self):
        return self.__validator


    def get_words(self):
        return self.__words

        
    def __str__(self, *args, **kwargs):
        return " ".join(self.words)   

    words = property(get_words, None, None, "words's docstring")
    
    def __eq__(self, other):
        if not isinstance(other, Sentence):
            return False
        
        if len(self.words) != len(other.words):
            return False
        
        for elem in self.words:
            if elem not in other.words:
                return False
            
        return True
    validator = property(get_validator, None, None, "validator's docstring")
    
