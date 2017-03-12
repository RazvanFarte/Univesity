#SetA.Problem3

def min_mixed_num(n):
    '''
    Finds the minimum number formed with digits of a number n

    Input

    n - natural number

    Output

    - the formed number
    '''
    list1 = [0 for x in range(10)] 
        
    aux = n
    while aux > 0:
        
        list1[ aux%10 ] += 1 
        aux //= 10

    for i in range(10):
        while list1[i] > 0:
            aux *= 10
            aux += i
            list1[i] -= 1

    return aux
#=============================================================================

#SetB.Problem6

from datetime import date

'''def num_of_bissectile(year1,year2):
    the number of bissectile years between year1 and year2
    
    if(year1 > year2):
        year1,year2 = year2,year1
        
    years = year2 - year1
    d = (years//4 + (0 == ((year1 + years % 4)%4)))
    return d'''

def age_to_days(birth_day):
    '''Birth_day is a string (y.m.d)
    Finds the age of person in number of days
    '''
    birth_day = birth_day.split(".")
    birth_day = date(int(birth_day[0]),int(birth_day[1]),int(birth_day[2]))
    today = date.today()
    print(today)
    print(birth_day)
    
    days = (today - birth_day).days
    return days

#=============================================================================

#SetC.Problem15

from math import sqrt

def is_perf(n):
   # print("n=",n)
    sum = 1
    d = 2
    while d <= n/2:
        if n%d == 0:
            sum += d
            #print(d)
        d+=1

  #  print("sum=",sum)
    if n == sum:
      #  print("its here")
        return True
    
    return False

def spn(n):
    '''returns the smallest perfect number after a number n
    '''
    x = n
    while is_perf(x) == False:
        x += 1

    return x

    
#num = int(input("Give me a number: "))
#print("The minimum number formed with digits of number: ", min_mixed_num(num))

birthday = input("Give me his birthday(year.month.day): ")

print("His age in days is: ",age_to_days(birthday))

#x = spn(int(input("Give me a number: ")))
#print("Next perfect number is: ",x)


