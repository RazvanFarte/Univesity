'''
Created on Feb 16, 2017

@author: Razvan
'''
import random
from src.entities import Sentence

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, sentenceController):
        '''
        Constructor
        '''
        self.__sentenceController = sentenceController
        
    def get_sentence_controller(self):
        return self.__sentenceController


    def set_sentence_controller(self, value):
        self.__sentenceController = value


    def del_sentence_controller(self):
        del self.__sentenceController

    sentenceController = property(get_sentence_controller, set_sentence_controller, del_sentence_controller, "sentenceController's docstring")
    
    def __readLine(self):
        line = input("Command: ")
        line = line.strip()
        line = line.split(" ", 1)
        
        return line[0],line[1:] if len(line) > 1 else []
    
    def run(self):
        
        commands = {"add": self.__addSentence, "start": self.__startGame,
                    "printSentences": self.__printSentences}
        
        while True:
            comm, args = self.__readLine()
            
            if comm == "exit":
                break
            
            try:
                commands[comm](*args)
            except Exception as ex:
                print("Error occured " + str(ex))
    
    def __addSentence(self, listOfWords):
        self.sentenceController.save(listOfWords)
    
    def __chooseSentence(self, sequence):
        return random.choice(sequence)
    
    def __createEmptySentence(self, sentence):
        emptyListOfWords = []
        for word in sentence.get_words():
            emptyListOfWords.append("_"*len(word))
            
        return Sentence(emptyListOfWords)
    
    def __startGame(self):
        #They are both senteces(list of words)
        sentence = self.__chooseSentence(self.sentenceController.get_objects())
        sentenceWords = sentence.get_words()
        emptySentence = self.__createEmptySentence(sentence)
        emptySentenceWords = emptySentence.get_words() 
        
        #Now we fill the emptySequence with heads of words
        listOfFills = self.__createListOfFills(sentenceWords)
        
        #Fill the words at start of game
        for letter in listOfFills:
            emptySentenceWords = self.__fillLetterInWords(emptySentenceWords, sentenceWords, letter)
        
        hangmanText = "hangman"
        hangmanIndex = 0
        
        allLetters = self.__getAllLetters(sentenceWords)
        
        while hangmanIndex < len(hangmanText):
            print(str(emptySentenceWords) + "\t- " + hangmanText[:hangmanIndex])
            
            letter = input("Give a letter: ")
            
            emptySentenceWords2 = self.__fillLetterInWords(emptySentenceWords, sentenceWords, letter)
            
            if self.__listsEqual(emptySentenceWords, emptySentenceWords2):
                hangmanIndex += 1
            else:
                listOfFills.append(letter)
            
            emptySentenceWords = emptySentenceWords2
            
            if self.__listsEqual(sorted(listOfFills),sorted(allLetters)):
                break
        
        if hangmanIndex == len(hangmanText):
            print("You lost!")
        else:
            print("You win!")
            
        
    def __getAllLetters(self, listOfWords):
        allLetters = []
        for word in listOfWords:
            for letter in word:
                if letter not in allLetters:
                    allLetters.append(letter)
        return allLetters
    
    def __listsEqual(self, list1, list2):
        if len(list1) != len(list2):
            return False
        
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        
        return True
    
    def __getFirstLetter(self, word):
        return word[0]
    
    def __getLastLetter(self, word):
        return word[-1]
    
    def __createListOfFills(self, words):
        """Iterate through words, get heads of words and create a list of letters
        """
        listOfFills = []
        for word in words:
            firstLetter = self.__getFirstLetter(word)
            lastLetter = self.__getLastLetter(word)
            
            if not firstLetter in listOfFills:
                listOfFills.append(firstLetter)
            if not lastLetter in listOfFills:
                listOfFills.append(lastLetter)
        
        return listOfFills
    
    def __stringToList(self, st):
        return [x for x in st]
    
    def __listToString(self, li):
        st = ""
        
        for letter in li:
            st += letter
            
        return st
    
    def __fillLetterAtIndex(self, word, letter, index):
        """Fill letter in word at index index
        Input
            word - an empty word "___"
            letter
        Output:
            returns the word as "a__"
        """
        listOfLetters = self.__stringToList(word)
        listOfLetters[index] = letter
        
        return self.__listToString(listOfLetters)

    def __fillLetterInWord(self, emptyWord, fullWord, letter):
        """Fills in emptyWord at indexes where letter is in fullWord
        """
        for i in range(len(fullWord)):
            if fullWord[i] == letter:
                emptyWord = self.__fillLetterAtIndex(emptyWord, letter, i)
                
        return emptyWord
    
    def __fillLetterInWords(self, emptyWords, fullWords, letter):
        """Returns the filled words with letter
        """
        emptyWords2 = []
        for i in range(len(emptyWords)):
            emptyWords2.append(self.__fillLetterInWord(emptyWords[i], fullWords[i], letter))
        
        return emptyWords2
            
        
    def __printSentences(self):
        for elem in self.sentenceController.get_objects():
            print(elem)
            
    def testFillLetterInWords(self):
        l = ["ana","are","mere"]
        emptyList = self.__createEmptySentence(Sentence(l))
        
        emptyList = self.__fillLetterInWords(emptyList.get_words(), l, "a")
        
        assert self.__listsEqual(emptyList, ["a_a","a__","____"]) == True

if __name__ == "__main__":
    
    console = Console(None)
    
    console.testFillLetterInWords()