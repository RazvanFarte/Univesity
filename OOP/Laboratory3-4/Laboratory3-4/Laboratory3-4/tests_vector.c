#include "stdafx.h"

int __intCast(void* object) {
	return *(int*)object;
}

char* __intToChar(void *object) {
	char* buff = (char*)malloc(sizeof(char) * 7);
	_itoa(*(int*)object, buff, 10);
	strcat(buff, "\n\0");
	return buff;
}

void __deepCopyIntegers(Vector* v1, Vector* v2) {
	int* element;
	for (int i = 0; i < v1->lenght; ++i) {
		element = (int*)malloc(sizeof(int));
		*element = *(int*)getElementFromVector(v1, i);

		pushToVector(v2, (void*)element);
	}
}

int __equalsElementsInInterval(Vector* v1, Vector* v2, int begin, int end, int displacement) {
	/*Compares element from interval [begin, end) from first with those in [begin + displacement, end + displacement)
	
	If begin > end returns -2
	If begin + displacement or end + displacement or begin or end are out of index, returns -1
	*/
	if (begin > end)
		return -2;

	int min = v1->lenght > v2->lenght ? v2->lenght : v1->lenght;
	if (end > min || end + displacement > min)
		return -1;
	if (begin < 0 || begin + displacement < 0)
		return -1;

	for (int i = begin; i < end; i++) {
		if (__intCast(getElementFromVector(v1, i)) != __intCast(getElementFromVector(v2, i + displacement)))
			return 0;
	}
	return 1;
}

void __destroyerInt(void *el) {
	return;
}

void __test_initVector()
{
	Vector *vect1 = initVector(5);
	vect1->destroyerElements = __destroyerInt;
	
	assert(lenVector(vect1) == 0);
	assert(vect1->maxLenght == 5);

	destroyVector(vect1);
	free(vect1);
}

void __test_pushToVector() {
	Vector *vect1 = initVector(5);
	vect1->destroyerElements = __destroyerInt;
	vect1->elementToString = __intToChar;
	//Vector *vect2 = initVector(5);
	int *value;

	for (int i = 0; i < 100; ++i) {
		value = (int*)malloc(sizeof(int));
		*value = i;

		//__deepCopyIntegers(vect1, vect2);

		assert (pushToVector(vect1, value) == 1);
		assert (getElementFromVector(vect1, vect1->lenght - 1) == value);

		//Vector1 was not changed by push
		//assert(__equalsElementsInInterval(vect1, vect2, 0, vect2->lenght, 0) == 1);
		//printf("%s\n%s", toStringVector(vect1), toStringVector(vect2));
	}

	assert(vect1->lenght == 100);
	//assert(vect2->lenght == 999);

	destroyVector(vect1);
	free(vect1);
	//destroyVector(vect2);
	//free(vect2);
}

void __test_popFromVector() {
	Vector *vect1 = initVector(5);
	vect1->destroyerElements = __destroyerInt;
	//Vector *vect2 = initVector(5);

	for (int i = 0; i < 50; ++i) {
		int *elem = (int*)malloc(sizeof(int));
		*elem = i;
		pushToVector(vect1, elem);
	}

	for (int i = 0; i < 50; ++i) {
		//__deepCopyIntegers(vect1, vect2);

		void *element = popFromVector(vect1);

		assert(element != NULL);
		assert(*(int*)element < 50 && *(int*)element >= 0);
		//assert(__equalsElementsInInterval(vect1, vect2, 0, lenVector(vect1), 0) == 1);

		free(element);
	}

	assert(vect1->lenght == 0);
	//assert(vect2->lenght == 1);

	destroyVector(vect1);
	free(vect1);

	//destroyVector(vect2);
	//free(vect2);
}


void __test_insertInVectorAt() {
	Vector *vect1 = initVector(5);
	vect1->destroyerElements = __destroyerInt;
	vect1->elementToString = __intToChar;
	//Vector *vect2 = initVector(5);

	int *value;
	for (int i = 1; i <= 100; ++i) {
		//__deepCopyIntegers(vect1, vect2);

		value = (int*)malloc(sizeof(int));
		*value = i - 1;
		
		int index = vect1->lenght / 2;

		assert(insertInVectorAt(vect1, (void*)value, index) == 1); //Returns 1 if successful
		assert(getElementFromVector(vect1, index) == value);// Same pointer
		assert(*(int*)getElementFromVector(vect1, index) == *value);
		//assert(__equalsElementsInInterval(vect1, vect2, 0, index - 1, 0) == 1);
		//assert(__equalsElementsInInterval(vect1, vect2, index + 1, lenVector(vect1), -1) == 1);
	}

	assert(vect1->lenght == 100);
	//assert(vect2->lenght == 999);
	destroyVector(vect1);
	free(vect1);

	//destroyVector(vect2);
	//free(vect2);
}


void __test_removeFromVector() {
	Vector *vect1 = initVector(5);
	vect1->destroyerElements = __destroyerInt;
	//Vector *vect2 = initVector(5);
	int *value;
	for (int i = 0; i < 100; ++i) {
		value = (int*)malloc(sizeof(int));
		*value = i;

		insertInVectorAt(vect1, value, i);
	}
	
	for (int i = vect1->lenght; i > 1; --i) {
		
		int index = vect1->lenght / 2;
		void* element = removeFromVector(vect1, index);
		assert(element != NULL);
		assert(__intCast(element) >= 0 && __intCast(element) < 1000);

		free(element);
	}

	destroyVector(vect1);
	free(vect1);
}


void tests_vector()
{
	__test_initVector();

	__test_pushToVector();
	__test_insertInVectorAt();
	
	__test_popFromVector();
	__test_removeFromVector();
}
