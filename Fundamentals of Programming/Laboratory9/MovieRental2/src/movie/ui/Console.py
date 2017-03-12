'''
Created on 8 nov. 2016

@author: Dell
'''
from movie.domain.exceptions.MovieException import MovieException
from util.Utils import Utils
import os
import datetime
from movie.repo.Repository import Repository, BinaryRepository, FileRepository

class Console(object):
    '''
    classdocs
    '''

    
    def __init__(self, movieControler, clientControler, rentalControler, statisticsControler, undoController):
        '''
        Constructor
        '''
        self.__movieControler = movieControler
        self.__clientControler = clientControler
        self.__rentalControler = rentalControler
        self.__statisticsControler = statisticsControler
        self.__undoController = undoController
    
    def __listMovies(self):
        Utils.print_all(self.__movieControler.get_all())

    def __listRental(self):
        Utils.print_all(self.__rentalControler.get_all())
    
    def __listClients(self):
        Utils.print_all(self.__clientControler.get_all())
        
    def __rent(self, movieId, clientId):
        today = datetime.date.today()
        self.__rentalControler.add(None, int(movieId), int(clientId), today, 
                                   today + datetime.timedelta(days=14),
                                    None)
        
    def __return(self, movieId):
        self.__rentalControler.returnMovie(int(movieId))
    
    def __clearScreen(self):
        print('\n'*100)
        
    def __searchMovies(self,keyword):
        Utils.print_all(self.__statisticsControler.searchMovies(keyword))
    
    def __searchClients(self,keyword):
        Utils.print_all(self.__statisticsControler.searchClient(keyword))
        
    def __mostRentedMovies(self):
        Utils.print_all_indexed(self.__statisticsControler.mostRentedMovies())

    def __mostActiveClients(self):
        Utils.print_all_indexed(self.__statisticsControler.mostActiveClients())
        
    def __currentlyRentedMovies(self):
        Utils.print_all_indexed(self.__statisticsControler.allRentedMovies())
    
    def __lateRentals(self):
        Utils.print_all_indexed(self.__statisticsControler.lateRentedMovies())
    
    
    def __removeClient(self, clientId):
        self.__clientControler.remove(int(clientId))
        self.__rentalControler.removeClient(int(clientId))
        
            
    def __addClient(self, clientId, clientName):
        self.__clientControler.add(int(clientId), clientName)
        
    def __addMovie(self, movieId, movieTitle, movieDescription, movieGenre):
        self.__movieControler.add(int(movieId), movieTitle, movieDescription, movieGenre)
        
    def __removeMovie(self, movieId):
        self.__movieControler.remove(int(movieId))
        self.__rentalControler.removeMovie(int(movieId))

        
    def __movieUpdate(self, movieId, tag, valueUpdate):
        self.__movieControler.update(int(movieId), tag, valueUpdate)
        
    def __clientUpdate(self, clientId, clientName):
        self.__clientControler.update(int(clientId), clientName)
        
    def __undo(self):
        self.__undoController.undo()
        
    def __redo(self):
        self.__undoController.redo()
        
    def runConsole(self):
        
        if not isinstance(self.__clientControler.get_repository(), (BinaryRepository,FileRepository)):
            self.__initData()
        commands = {"add":{"movie":self.__addMovie,"client":self.__addClient},
                    "remove":{"movie":self.__removeMovie,"client":self.__removeClient},
                    "update":{"movie":self.__movieUpdate,"client":self.__clientUpdate},
                    "help":{"me":self.__print_help},
                    "list":{"movies":self.__listMovies,"clients":self.__listClients,"rents":self.__listRental},
                    "rent":{"movie":self.__rent},
                    "return":{"movie":self.__return},
                    "clear":{"screen":self.__clearScreen},
                    "search":{"movies":self.__searchMovies,"clients":self.__searchClients},
                    "most":{"rented":self.__mostRentedMovies,"active":self.__mostActiveClients},
                    "rented":{"movies":self.__currentlyRentedMovies, "late":self.__lateRentals},
                    "operation":{"undo":self.__undo, "redo":self.__redo}}
    
        while True:
            comm, tag, arguments = Console.__read_line()
            
            
            if comm == "exit":
                break
             
            try:
                commands[comm][tag](*arguments)
            except KeyError as kerr:
                print("Inexistent command.", kerr)
            except Exception as exc:
                print("Error", exc)
    
    def __print_help(self):
        #TODO how to manage when i have a movieDescription longer than 1 word
        print("Operations for Movie Database:\n\n",
            "\tadd movie <movieId> <movieTilte> <movieDescription> <movieGenre> (Adds a new movie with id <movieId>, title <movieTitle>, description <movieDescription>, genre <movieGenre>)\n",
            "\tremove movie <movieId> (Removes the movie with id <movieId>)\n",
            "\tupdate movie <movieId> movieTitle <movieTitle> (Changes movieTitle of movie <movieId> with <movieTitle>)\n",
            "\tupdate movie <movieId> movieDescription <movieDescription> (Changes movieDescription of movie <movieId> with <movieDescription>)\n",
            "\tupdate movie <movieId> movieGenre <movieGenre> (Changes movieGenre of movie <movieId> with <movieGenre>)\n",
            "\tlist movies (Lists all movies)\n\n",
            
            "Operations for Client Database:\n\n",
            "\tadd client <clientId> <clientName> (Adds a new client with id <clientId> and name <clientName>)\n",
            "\tremove client <clientId> (Removes the client with id <clientId>)\n",
            "\tupdate client <clientId> <clientName> (Changes clientName of client <clientId> with <clientName>)\n",
            "\tlist clients (Lists all clients)\n\n",
            
            "Operations for Renting Database:\n\n",
            "\trent movie <movieId> <clientId>\n",
            "\treturn movie <movieId>\n",
            "\tlist rents\n\n",
            
            """Search
        search movies <key>
        search clients <key>\n\n""",
            
            "Statistics\n\n",
            "\tmost rented\n",
            "\tmost active\n",
            "\trented movies\n"
            "\trented late(Return the list of rented movies which where not returned in due date)\n\n",
            
            "Auxiliary operations:\n\n",
            "\toperation undo\n",
            "\toperation redo\n",
            "\thelp me (prints help menu)\n",
            "\texit (exits the program)\n",
            "\tclear screen\n"
            )
            
    
    @staticmethod
    def __read_line():
        '''Reads a line and returns separately command and arguments (if exists)
        Input
            -
        Output 
            command - a string
            arguments - a list of strings
        '''   
        line = input("Command: ").strip()
        
        # We get the command
        index = line.find(" ")
        if index is not -1:
            command = line[:index]
        
            # We get the arguments    
            arguments = line[index + 1:].split(" ")
            
            return command.lower(), arguments[0].lower(), arguments[1:]
        else:
            return line.lower(), "", ""


    def __initData(self):
        try:
            self.__addMovie(1,"Home alone 1", "Funny", "Comedy")
            self.__addMovie(2,"Home alone 2", "Funny", "Comedy")
            self.__addMovie(3,"Home alone 3", "Funny", "Comedy")
            self.__addMovie(4,"Home alone 4", "Funny", "Comedy")
            self.__addMovie(5,"Home alone 5", "Funny", "Comedy")
            self.__addMovie(6,"Home alone 6", "Funny", "Comedy")
            self.__addMovie(7,"Home alone 7", "Funny", "Comedy")
            self.__addMovie(8,"Home alone 8", "Funny", "Comedy")
            self.__addMovie(9,"Home alone 9", "Funny", "Comedy")
            self.__addMovie(10,"Home alone 10", "Funny", "Comedy")
            
            
            self.__addClient(1,"Viorel")
            self.__addClient(2,"Andrei")
            self.__addClient(3,"Aurel")
            self.__addClient(4,"Ana")
            self.__addClient(5,"Daiana")
            self.__addClient(6,"Marta")
            self.__addClient(7,"Cerasela")
            self.__addClient(8,"Furnal")
            self.__addClient(9,"Gheorghe")
            self.__addClient(10,"Andone")
        except MovieException as me:
            print("Exception when initializing data", me)
            
        self.__rentalControler.add(None,3,2,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,4,1,datetime.date(1997,10,20),
                                   datetime.date(2016,11,1),
                                   None)
        self.__rentalControler.add(None,6,3,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,3,10,datetime.date(1997,10,13),
                                   datetime.date(2006,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,5,2,datetime.date(1997,10,13),
                                   datetime.date(1997,10,22),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,1,7,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,2,8,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,8,9,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,7,5,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
        self.__rentalControler.add(None,10,4,datetime.date(1997,10,13),
                                   datetime.date(1997,10,20),
                                   datetime.date(1997,10,20))
            
            