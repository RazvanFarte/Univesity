#First problem

def sum_of_n(num):
    '''Calculate the sum of "num" numbers read

    Input:
    num - is an natural number that tells us how many numbers will
    be in sum

    Output
    The sum of "num" numbers
    '''
    s = 0
    for i in range(num):
        x = int(input("Give me number " + str(i+1) + ": "))
        s += x
    return s

#======================================================================

#Second problem

from math import sqrt
def is_prime(num):
    '''Determines if a number "num" is prime

    Input:
    num - is an natural number

    Output
    The sum of "num" numbers
    '''
    
    if num == 2:
        return True
    if num < 2:
        return False
    if num%2==0:
        return False
    for d in range(3,int(sqrt(num)),2):
        if num % d == 0:
            return False
    return True
#======================================================================

#Third problem

def gcd(a,b):
    '''Determines the greatest common divisor between a and b

    Input:
    a, b - two natural numbers

    Output
    The greatest common divisor
    '''

    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
#======================================================================

#Main

#1
a = int(input("How many numbers do you want to sum? "))
print("This is the sum of them",sum_of_n(a))

#2
while True:
    b = int(input("Is it prime?"))
    if b < 0:
        print("It's a negative number. Give me a pozitive one")
    else:
        break

if is_prime(b):
    print("It's prime")
else:
    print("No.It's not prime")

#3
print("What's the greatest common divisor of c and d?")
c , d = int(input("c = ")), int(input("d = "))

print("It is: ", gcd(c,d))

