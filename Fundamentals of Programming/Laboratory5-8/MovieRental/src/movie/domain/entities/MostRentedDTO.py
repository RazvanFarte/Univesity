'''
Created on 6 dec. 2016

@author: Dell
'''

class MostRentedBookDTO(object):
    '''
    classdocs
    '''

    def __init__(self, bookId, bookTitle, rentedTimes):
        '''
        Tells us how many times was rented book with bookId and bookTitle
        '''
        
        self.__bookId = bookId
        self.__bookTitle = bookTitle
        self.__rentedTimes = rentedTimes

    def get_book_id(self):
        return self.__bookId


    def get_book_title(self):
        return self.__bookTitle


    def get_rented_times(self):
        return self.__rentedTimes


    def set_book_id(self, value):
        self.__bookId = value


    def set_book_title(self, value):
        self.__bookTitle = value


    def set_rented_times(self, value):
        self.__rentedTimes = value


    def del_book_id(self):
        del self.__bookId


    def del_book_title(self):
        del self.__bookTitle


    def del_rented_times(self):
        del self.__rentedTimes

    movieId = property(get_book_id, set_book_id, del_book_id, "bookId's docstring")
    movieTitle = property(get_book_title, set_book_title, del_book_title, "bookTitle's docstring")
    rentedTimes = property(get_rented_times, set_rented_times, del_rented_times, "rentedTimes's docstring")
    
    def __str__(self):
        return "Id: {0}, Book: {1}, Rented times: {2}".format(self.bookId,self.bookTitle,self.rentedTimes)
    
    def __lt__(self,mostRentedBookDTO):
        return self.rentedTimes < mostRentedBookDTO.rentedTimes
    
    def __gt__(self,mostRentedBookDTO):
        return self.rentedTimes > mostRentedBookDTO.rentedTimes
    
    def __le__(self,mostRentedBookDTO):
        return not self > mostRentedBookDTO
    
    def __ge__(self,mostRentedBookDTO):
        return not self < mostRentedBookDTO
