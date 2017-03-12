'''
Created on 7 nov. 2016

@author: Dell
'''
from datetime import date
import configparser

class Utils(object):
    '''
    classdocs
    '''
    
    @staticmethod
    def print_all_indexed(bundle):
        if bundle == []:
            print("Empty list")
            return
        
        i = 1
        for elem in bundle:
            print(str(i) + '.', elem)
            i += 1
    
    @staticmethod
    def print_all(bundle):
        if bundle == []:
            print("Empty list")
            return
        
        for i in bundle:
            print(i)
            
    @staticmethod
    def toDate(s):
        day,month,year = (s.split("."))
        return date(int(year), int(month), int(day))
    
class PropertiesHandler:
    
    CONSOLE = "console"
    GUI = "gui"
    
    FILEREPO = "filerepository"
    MEMORYREPOSITORY = "memoryrepository"
    BINARYREPOSITORY = "binaryrepository"
    
    def __init__(self, fileName,load = True):
        self.config = configparser.ConfigParser()
        self.__filename = fileName
        self.config.add_section('GENERAL')
        if load:
            self.load()
 
 
    def setRepository(self, repository):
        self.config.set('GENERAL', 'repository', repository)
 
    def getRepository(self):
        return self.config.get('GENERAL', 'repository', fallback= PropertiesHandler.MEMORYREPOSITORY)

    def setMovieFile(self, fileName):
        self.config.set('GENERAL', 'movie', fileName)

    def getMovieFile(self):
        '''Returns filename striped'''
        return self.config.get('GENERAL', 'movie', fallback = "").strip(' ')

    def setClientFile(self, fileName):
        self.config.set('GENERAL', 'client', fileName)
        
    def getClientFile(self):
        '''Returns filename striped'''
        return self.config.get('GENERAL', 'client', fallback = "").strip(' ')
        
    def setRentalsFile(self, fileName):
        self.config.set('GENERAL', 'rentals', fileName)
        
    def getRentalsFile(self):
        '''Returns filename striped'''
        return self.config.get('GENERAL', 'rentals', fallback = "").strip(' ')
 
    def setUi(self, uiType):
        self.config.set('GENERAL', 'ui', uiType)

    def getUi(self):
        return self.config.get('GENERAL', 'ui', fallback = PropertiesHandler.CONSOLE)
 
    def save(self):
        with open('settings.properties', 'w') as configfile:
            self.config.write(configfile)
 
    def load(self):
        self.config.read('settings.properties')