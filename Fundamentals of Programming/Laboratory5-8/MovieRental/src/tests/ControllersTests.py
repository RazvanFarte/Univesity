'''
Created on 21 dec. 2016

@author: Dell
'''
from unittest.case import TestCase
from movie.repo.Repository import Repository
from movie.domain.validators.RentalValidator import RentalValidator
from movie.domain.validators.MovieValidator import MovieValidator
from movie.domain.validators.ClientValidator import ClientValidator
from movie.domain.entities.Rental import Rental
import datetime
from movie.domain.entities.Movie import Movie
from movie.domain.entities.Client import Client
from movie.ctrl.StatisticsControler import StatisticsControler
from movie.ctrl.ClientControler import ClientControler

class StatisticsControllerTest(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.__rentalRepository = Repository(RentalValidator)
        self.__movieRepository = Repository(MovieValidator)
        self.__clientRepository = Repository(ClientValidator)

        self.__movieRepository.save(Movie(1, "Ana", "Bun", "Comedie"))
        self.__clientRepository.save(Client(1, "Aurica"))
        self.__rentalRepository.save(Rental(1, 1, 1, datetime.date(1997,10,20), datetime.date(1997,11,10), None))
                
        self.__movieRepository.save(Movie(2, "Dana Film", "Nebun", "Drama"))
        self.__clientRepository.save(Client(2, "Daniel"))
        self.__rentalRepository.save(Rental(2, 2, 2, datetime.date(2016,12,15), datetime.date(2017,1,5), None))
                
        self.__movieRepository.save(Movie(3, "Bolt", "D-amar", "Actiune"))
        self.__clientRepository.save(Client(3, "Liviu"))
        self.__rentalRepository.save(Rental(3, 3, 3, datetime.date(1997, 10, 20), datetime.date(1997, 11, 10), datetime.date(1997, 11, 13)))
                
        self.__movieRepository.save(Movie(4, "Flash", "Great", "Actiune"))
        self.__clientRepository.save(Client(4, "Radu"))
        self.__rentalRepository.save(Rental(4, 4, 4, datetime.date(1997,10,20), datetime.date(1997,11,10), datetime.date(1997,11,5)))
        
        self.__rentalRepository.save(Rental(5, 4, 4, datetime.date(1997,10,20), datetime.date(1997,11,10), datetime.date(1997,11,5)))
        
        self.__statisticsController = StatisticsControler(self.__rentalRepository, self.__movieRepository, self.__clientRepository)
    
    def tearDown(self):
        TestCase.tearDown(self)
        Rental.rentalCounter -= 5
        
    def testAllRentedMovies(self):
        rentedMovies = self.__statisticsController.allRentedMovies()
        
        self.assertEqual(len(rentedMovies), 2, "There are no other rented movies")
        self.assertEqual(rentedMovies[0].clientId, 1, "It is rented by client 1")
        self.assertEqual(rentedMovies[0].movieId, 1, "Movie Id is 1")
        
        
    def testLateRentedMovies(self):
        lateRented = self.__statisticsController.lateRentedMovies()
        
        #Take care. After 5.01.2017, the len will be 2
#         self.assertEqual(len(lateRented), 2)

        self.assertEqual(len(lateRented), 1)
        self.assertEqual(lateRented[0].clientId, 1)
        
        #After 5.01.2017 also
#         self.assertEqual(lateRented[1].movieId, 2)
#         self.assertGreaterEqual(lateRented[0].numberOfDaysDelayed, lateRented[1].numberOfDaysDelayed)
        
    
    def testMostActiveClients(self):
        mostActive = self.__statisticsController.mostActiveClients()
        
        self.assertEqual(len(mostActive), 4, "There should be 4 clients")
        
        self.assertEqual(mostActive[0].clientId, 1)
        self.assertEqual(mostActive[1].clientId, 4)
        self.assertEqual(mostActive[2].clientId, 3)
        self.assertEqual(mostActive[3].clientId, 2)
        
        self.assertEqual(mostActive[0].rentalDays, (datetime.date.today() - datetime.date(1997,10,20)).days)
    
    
    def testMostRentedMovies(self):
        mostRented = self.__statisticsController.mostRentedMovies()
        
        self.assertEqual(len(mostRented), 4)
        
        self.assertEqual(mostRented[0].movieId, 4)
        
    
    def testSearchClient(self):
        string = "l"
        clientMatches = self.__statisticsController.searchClient(string)
        
        self.assertEqual(len(clientMatches), 2)
        
        for match in clientMatches:
            if not string in match.entityName.lower():
                self.fail("Not good matching")
    
    
    def testSearchMovies(self):
        string = "ana"
        movieMatches = self.__statisticsController.searchMovies(string)
        
        self.assertEqual(len(movieMatches), 2)
        
        for match in movieMatches:
            if not ((string in match.entityName.lower()) or (string in match.entityDescription.lower()) or \
                (string in match.entityGenre.lower())):
                self.fail("Not good matching")

class ClientControllerTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.__clientRepository = Repository(ClientValidator)
        self.__clientRepository.save(Client(1, "Aurica"))
        self.__clientRepository.save(Client(2, "Daniel"))
        
        self.__clientControler = ClientControler(self.__clientRepository)
        
        
    def testAdd(self):
        self.__clientControler.add(3, "Dana")
        self.assertEqual(len(self.__clientControler.get_all()), 3)
        
        #It is not the responsabilty of controller to check if entity is duplicated
#         try:
#             self.__clientControler.add(1,"Aurica")
        
    def testRemove(self):
        self.__clientControler.remove(1)
        self.assertEqual(len(self.__clientControler.get_all()), 1)
        
