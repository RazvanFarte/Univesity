'''
Created on Feb 16, 2017

@author: Razvan
'''

class Sentence(object):
    '''
    classdocs
    '''
    

    def __init__(self, words):
        '''
        words - list of words
        '''
        self.__words = words

    def get_id(self):
        return self.__id

        
    def get_words(self):
        return self.__words


    def set_words(self, value):
        self.__words = value


    def del_words(self):
        del self.__words

    words = property(get_words, set_words, del_words, "words's docstring")
    
    def __str__(self):
        return " ".join(self.words)


class SentenceValidator(object):
    '''
    classdocs
    '''
    @staticmethod
    def validate(obj):
        if not isinstance(obj, Sentence):
            raise Exception("Object {} is not a Sentence".format(obj))
        
        if len(obj.words) < 1:
            raise Exception("Sentence must have at least 1 word and it has {}".format(obj.words))
        
        for word in obj.words:
            if len(word) < 3:
                raise Exception("Each word must have 3 letters. Word {} has only {}".format(word, len(word)))
            