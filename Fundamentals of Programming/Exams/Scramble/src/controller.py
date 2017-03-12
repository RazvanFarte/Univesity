'''
Created on Feb 22, 2017

@author: Razvan
'''
import random
from src.Sentence import Sentence, SentenceValidator
import unittest
from src.repo import FileRepository

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__repo = repository
    
    def chooseRandomSentence(self):
        """Returns a random sentence from repository"""
        return self.__repo.chooseObject()
    
    def getScore(self, sentence):
        """Returns the score of the given sentence. Score = number of letters in sentence (without
            white spaces)
            
        Input
            sentence - Sentence object
        Output
            score - int object, representing number of letters
        Raises
            None
        """
        
        score = 0
        
        for word in sentence.words:
            score += len(word)
            
        return score
    
    def __lettersToString(self, words):
        """Converts each list of letters from words into a string
        
        Input
            words - a list of words, where each word is a list of letters
        Output
            words - a list of words, where each word is a string
        Raises
            None
        """
        
        li = []
        
        for word in words:
            li.append("".join(word))
            
        return li
    
    def __stringToLetters(self, words):
        """Converts each string of words into a list of letters
        
        Input
            words - a list of words, where each word is a string
        Output
            words - a list of words, where each word is a list of letters
        Raises
            None
        """
        li = []
        
        for word in words:
            li.append(list(word))
            
        return li
    
    def __swapLetters(self, listSentence, word1, letter1, word2, letter2):
        """Swaps letter located at position (word1, letter1) with letter (word2, letter2)
        
        Input
            listSenetence - a list of lists of letters(representing letters from each word)
        Output
            None
        Raises
            None
        """
        listSentence[word1][letter1] ,listSentence[word2][letter2] = listSentence[word2][letter2], listSentence[word1][letter1] 
        return listSentence
    
    def __validateIndex(self, index, lenght):
        """Checks if letter at index can be swaped. First and last letter of a word can't be swaped
        
        Input
            index - int
            lenght - int
        Output
            None
        Raises
            Exception - if letter at index can't be changed or if index is out of range 
        
        """
        if index >= lenght or index < 0:
            raise Exception("Can't change these letters")

    
    def swapLetters(self, sentence, word1, letter1, word2, letter2):
        """Checks if coordinates are valid and swap letters"""
                
        listSentence = self.__stringToLetters(sentence.words)
        
        self.__validateIndex(word1, len(listSentence))
        self.__validateIndex(word2, len(listSentence))
        self.__validateIndex(letter1 - 1, len(listSentence[word1]) - 2)
        self.__validateIndex(letter2 - 1, len(listSentence[word2]) - 2)
        
        listSentence = self.__swapLetters(listSentence, word1, letter1, word2, letter2)
        
        return Sentence(self.__lettersToString(listSentence))
    
    def scramble(self, sentence):
        """Scrambles(shuffle its letters) a Sentence and returns it.
        
        Input
            sentence - Sentence object
        Output
            Sentence - the same sentence with letters shuffled
        Raise
            None
        """
        listSentence = self.__stringToLetters(sentence.words)
        
        while True:
            nrOfShuffles = random.randint(10, 50)
            
            while nrOfShuffles:
                nrOfShuffles -= 1
                
                word1 = random.randint(0, len(listSentence) - 1)
                
                while True:
                    l = len(listSentence[word1]) - 1
                    letter1 = random.randint(0, l)
                    if not (letter1 == 0 or letter1 == l):
                        break
                word2 = random.randint(0, len(listSentence) - 1)
                
                while True:
                    l = len(listSentence[word2]) - 1
                    letter2 = random.randint(0, l)
                    if not (letter2 == 0 or letter2 == l):
                        break
                
                listSentence = self.__swapLetters(listSentence, word1, letter1, word2, letter2)
                
            resultSentence = Sentence(self.__lettersToString(listSentence))
            if resultSentence == sentence:
                continue
            return resultSentence
    
