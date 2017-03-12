'''
Created on Feb 22, 2017

@author: Razvan
'''

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, controller):
        '''
        Constructor
        '''
        self.__controller = controller
        self.__undo = [[0,0], [0,0]]

    def get_controller(self):
        return self.__controller

    controller = property(get_controller, None, None, "controller's docstring")
        
    def __readLine(self):
        """Reads a console line and returns it as tuple (arc, argv). argv may be empty
        
        Input
            None
        Output
            argc - command
            argv - varibles
        Raises
            None
        """
        line = input("Command: ")
        
        line = line.strip()
        line = line.split(" ", 1)
        
        return line[0], line[1:] if len(line) > 1 else []
    
    
    def __getInputFromString(self, str):
        """From a string of form "x y - z v" gets [x,y] and [z,v] and return them as a tuple,
        where x,y,z,v are integer values
        
        Input
            str - the string of above type
        Output
            tuple([x,y],[z,v]) 
        Raises
            None
        """
        
        str = str.split("-")
        
        if len(str) != 2:
            raise Exception("Invalid command format")
        
        str[0] = str[0].strip()
        str[1] = str[1].strip()
        
        first = str[0].split(" ")
        second = str[1].split(" ")
        
        if len(first) != 2 or len(second) != 2:
            raise Exception("Invalid command format")
        
        return first, second
        
    
    def run(self):
        
        sentence = self.controller.chooseRandomSentence()
        correctSentence = sentence
        score = self.controller.getScore(sentence)
        sentence = self.controller.scramble(sentence)
        
        while True:
            print("{} [Score is: {}]".format(sentence, score))
            
            if score == 0:
                print("You lost!")
                break
            
            if correctSentence == sentence:
                print("You win! Your score is", score)
                break
            
            comm, args = self.__readLine()
            
            if(comm == "exit"):
                break
            
            try:
                
                if(comm == "swap"):
                    firstLetter, secondLetter = self.__getInputFromString(*args)
                    sentence = self.__uiSwap(sentence, firstLetter, secondLetter)
                    score -= 1
                elif comm == "undo":
                    sentence = self.__uiSwap(sentence, self.__undo[0], self.__undo[1])
                else:
                    raise Exception("Invalid command")
                
            except Exception as ex:
                print("Error:", ex)
            
            
            
    def __uiSwap(self, sentence, firstLetter, secondLetter):
        """Swaps a letter from a word with another letter from some word
        
        Input
            sentence - sentence for which letters will be swaped
            firstLetter - coordinates [wordIndex, letterIndex], each of them being int
            secondLetter - coordinates [wordIndex, letterIndex], each of them being int
        Output
            Sentence - the sentence with letters swaped
        Raises
            None
        """
        self.__undo[0] = firstLetter 
        self.__undo[1] = secondLetter
        return self.controller.swapLetters(sentence, int(firstLetter[0]), int(firstLetter[1]), int(secondLetter[0]), int(secondLetter[1]))
    
    