// Lab2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>

int isPrime(int number) {
	/*Checks if number is prime
	Input 
		number - integer number
	Output
		True - if number is prime
		False - otherwise
	Throws
		-
	*/
	if (number < 2)
		return 0;
	
	int div = 2;
	while (div * div <= number) {
		if (number % div == 0)
			return 0;
		div++;
	}
	return 1;
}

int* goldbachConjencture(int sum) {
	/*Returns the prime numbers that compound sum
	
	Input
		sum - positive number > 2
	Output
		pointer to vector with 2 elements
	Throws
		-
	*/
	int it;
	int v[2] = {0};
	for (it = 2; it <= sum - 2; ++it)
		if (isPrime(it) && isPrime(sum - it)) {
			v[0] = it;
			v[1] = sum - it;
			break;
		}

	return v;
}

void readVector(int lenght, int *vect) {
	/*Reads an array of integers of lenght
	Input
		vect - pointer to location where
		lenght - number of elements to be read in vector
	Output
		vect - vector with read elements
	Raises
		IndexOutOfBound - if lenght is greater than number of elemenents allocated to vect*/

	char error[] = "Size of vector is less than needed";

	if (_msize(vect) < sizeof(int)*lenght) {
		perror(error);
		return;
	}
	for (int i = 0; i < lenght; i++) {
		printf("Element[%d] = ", i);
		scanf("%d", (vect + i));
	}
}

void printVector(int lenght, int *const vect) {
	/*Prints a vector*/
	printf("Vector is: ");
	for (int i = 0; i < lenght; i++)
		printf("%d ", *(vect + i));
	printf("\n\n");
}

void (int *vect, int size, int value) {
	/*InitializinitializeVectores a vector of size with value
	*/
	for (int i = 0; i < size; ++i)
		*(vect + i) = value;
	
}

int* getDigits(int number) {
	/*Returns an array of lenght 10, representing how many times each digit appeard*/
	int *v;
	v = (int *)malloc(sizeof(int) * 10);
	initializeVector(v, 10, 0);

	while (number) {
		
		*(v + number % 10) += 1;
		number /= 10;
	}

	return v;
}

int numOfCommonDigits(int number1, int number2) {
	/*Returns the number of common distinct digits between the two numbers*/

	int *digitsNumber1 = getDigits(number1);
	int *digitsNumber2 = getDigits(number2);
	int numOfCommonDigits = 0;

	for (int i = 0; i < 10; ++i)
		if (*(digitsNumber1 + i) && *(digitsNumber2 + i))
			numOfCommonDigits++;

	return numOfCommonDigits;
}

int hasTwoCommonDigits(int number1, int number2) {
	/*Returns 1 if the two numbers share two distinct digits*/
	return numOfCommonDigits(number1,number2) > 1 ? 1 : 0;
}

int* longestContigousSubsequence(int *vect, int lenght, int *subsequence, int *lenSub, int (*condition)(int, int)) {
	/*Finds the longest subsequence of vect (of lenght), fulfilling the condition function
	
	Condition must be a function that takes as parameters 2 integers and returns a integer with values 
	0 for False and not 0 for True*/

	int *p = vect, l = 1;

	for (int i = 1; i < lenght; ++i)
		if ((*condition) (*(vect + i - 1), *(vect + i)))
			l++;
		else {
			if (l > *lenSub) {
				*lenSub = l;
				subsequence = p;
			}
			p = vect + i;
			l = 1;
		}

	if (l > *lenSub) {
		*lenSub = l;
		subsequence = p;
	}
	return subsequence;
}

int exponentOfFactor(int factor, int number) {
	/*Returns the exponent of factor in number decomposition in prime factors

	Input
		factor - factor to which i want to know the exponent
		number - the number to decomose
	Output
		returns the exponent
	*/
	int exponent = 0;
	while (number % factor == 0)
	{
		++exponent;
		number /= factor;
	}

	return exponent;
}

int main()
{
	int command, number = 0;
	int *p;
	int *subsequence, lenSub;

	while (1) {
		printf("Choose a number for fulfilling task:\n0.Exit\n1.Decompose a natural number as a sum of two prime numbers\n"
			"2.Given a vector of numbers, find the longest contiguous subsequence such that any consecutive elements"
			" have at least 2 distinct in .\n3.Give a number and a factor and I will print you"
			"the exponent of that the second number in decomposition of first number\n\nCommand: ");

		scanf("%d", &command);

		switch (command) {
			case 0:
				printf("Bye");
				goto end;
				break;
			case 1:

				printf("Number: ");
				scanf("%d", &number);

				p = goldbachConjencture(number);
				printf("First number: %d\nSecondNumber: %d\n\n", *p, *(p + 1));

				//free(p);
				break;

			case 2:

				printf("Number of elements of vector:");
				scanf("%d", &number);

				p = (int *) malloc(sizeof(int)*number);

				subsequence = p;
				lenSub = 1;
				
				readVector(number, p);
				//TODO: Ask about passing subsequence parameter
				subsequence = longestContigousSubsequence(p, number, subsequence, &lenSub, hasTwoCommonDigits);

				if (lenSub > 1)
					printVector(lenSub, subsequence);
				else
					printf("No such subsequence\n");

				//free(p);
				break;

			case 3:
				printf("Give me the number to decompose: ");
				scanf("%d", &number);

				int primeNumber;
				printf("Give me the prime factor of decomposition: ");
				scanf("%d", &primeNumber);

				printf("The exponent of factor %d in number %d is %d\n\n", primeNumber, number, 
					exponentOfFactor(primeNumber, number));


				break;

			default:
				printf("Invalid ");

		}
	}
	end:

	printf("Press any key to exit...");
	getchar();
    return 0;
}

