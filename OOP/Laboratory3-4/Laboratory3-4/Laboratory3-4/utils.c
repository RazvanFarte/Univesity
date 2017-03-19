#include "stdafx.h"

void shiftVectorLeft(Vector* mVector, short position, short numOfPositions);
void shiftVectorRight(Vector* mVector, short position, short numOfPositions);
short truncateVector(Vector* mVector, short beginPosition, short endPosition);

void __resize(Vector* mVector) {
	if (mVector->lenght >= mVector->maxLenght) {
		mVector->maxLenght *= 2;
		mVector->elemtents = (void **)realloc(mVector->elemtents, sizeof(mVector->elemtents) * ++mVector->maxLenght);
		return;
	}
	if (mVector->lenght <= (mVector->maxLenght / 4)) {
		mVector->maxLenght /= 2;
		mVector->elemtents = (void **)realloc(mVector->elemtents, sizeof(mVector->elemtents) * mVector->maxLenght);
	}
}

short defaultEquality(void *object1, void *object2) {
	/*Default equality applies only for integer numbers*/
	if (*(int*)object1 == *(int*)object2)
		return 1;
	return 0;
}

Vector* initVector(int length)
{
	Vector *mVector;
	mVector = (Vector *)malloc(sizeof(Vector));

	mVector->elemtents = (void **)malloc(sizeof(void*) * length);
	mVector->maxLenght = length;

	mVector->lenght = 0;

	mVector->equality = NULL;
	mVector->vectAsStr = NULL;
	mVector->elementToString = NULL;
	mVector->destroyerElements = NULL;

	return mVector;
}

void destroyVector(Vector* mVector) {
	while (mVector->lenght) {
		void *elem = popFromVector(mVector);
		mVector->destroyerElements(elem);
		free(elem);
	}

	if(mVector->elemtents != NULL)
		free(mVector->elemtents);

	if (mVector->vectAsStr != NULL)
		free(mVector->vectAsStr);
}

void setEualityForVector(Vector* mVector, short(*equality)(void *, void *)) {
	mVector->equality = equality;
}

void setToStringForVector(Vector *mVector, char *(*toStringElement)(void *))
{
	mVector->elementToString = toStringElement;
}

void setDestroyerForVector(Vector *mVector, void(*destroyer)(void*)) {
	mVector->destroyerElements = destroyer;
}

int pushToVector(Vector* mVector, void* mElement)
{
	/*Pushes mElement to the end of the mVector

	Reallocates memory*/
	return insertInVectorAt(mVector, mElement, lenVector(mVector));
}

int insertInVectorAt(Vector* mVector, void* object, short index) {
	/*Return 0 for Failure and 1 for Success*/
	if (index > mVector->lenght) {
		return 0;
	}

	__resize(mVector);
	
	shiftVectorRight(mVector, index, 1);
	mVector->lenght++;
	mVector->elemtents[index] = object;

	return 1;
}

short lenVector(Vector* mVector) {
	return mVector->lenght;
}

void* popFromVector(Vector* mVector)
{
	/*Pops the last element of mVector and returns a pointer to it. Returns NULL if there
	is no element in mVector.
	Reallocates memory.
	*/
	return removeFromVector(mVector, lenVector(mVector) - 1);
}

void* removeFromVector(Vector* mVector, short mIndex) {
	/*Removes the element at mIndex. Returns a pointer to that element. Returns NULL if there is no element in
	vector or if mIndex is out of range.
	*/
	if (mVector->lenght == 0 || mIndex >= mVector->lenght)
		return NULL;

	void *removedElement = mVector->elemtents[mIndex];

	shiftVectorLeft(mVector, mIndex, 1);
	mVector->lenght--;

	__resize(mVector);

	return removedElement;
}

void shiftVectorLeft(Vector* mVector, short position, short numOfPositions) {
	if (mVector->maxLenght < mVector->lenght + numOfPositions)
		return;
	if (numOfPositions <= 0 || position >= mVector->lenght || position < 0)
		return;
	
	for (short i = position; i < mVector->lenght; ++i) {
		mVector->elemtents[i] = mVector->elemtents[i + numOfPositions];
	}

}

void shiftVectorRight(Vector* mVector, short position, short numOfPositions) {
	if (mVector->maxLenght < mVector->lenght + numOfPositions)
		return;
	if (numOfPositions <= 0 || position >= mVector->lenght || position < 0)
		return;

	for (short i = mVector->lenght + numOfPositions - 1; i > position; --i) {
		//mVector->elemtents[i] = (void*) malloc(sizeof(void*));
		mVector->elemtents[i] = mVector->elemtents[i - numOfPositions];
	}
}

short truncateVector(Vector* mVector, short beginPosition, short endPosition) {
	/*Truncates mVector between [beginPosition, endPosition - 1].

	Returns
	0 - if trunctaing was successful
	1 - if beginPosition or endPosition are out of range*/

	if (beginPosition >= mVector->lenght || endPosition < 0)
		return 1;

	endPosition = lenVector(mVector) <= endPosition ? lenVector(mVector) - 1 : endPosition;
	beginPosition = 0 > beginPosition ? 0 : beginPosition;

	shiftVectorLeft(mVector, beginPosition, endPosition - beginPosition);

	return 0;
}

short indexElemInVector(Vector* mVector, void* mElement) {
	/*Returns index of mElement in mVector. If mElement is not in mVector, returns -1.
	Make sure to initialize the equality before use this function!*/
	for (int i = 0; i < mVector->lenght; ++i)
		if ((*mVector->equality)(mElement, mVector->elemtents[i]))
			return i;

	return -1;
}

void* getElementFromVector(Vector* mVector, short mIndex)
{
	/*Returns element in mVector at mIndex. If mIndex out of range, returns NULL*/
	if (mIndex >= mVector->lenght)
		return NULL;
	return mVector->elemtents[mIndex];
}

char* toStringElement(Vector* mVector, void* element) {
	if (element == NULL) {
		return "NULL";
	}

	return mVector->elementToString(element);
}

short __getSizeOfStrElement(Vector* mVector,void *element) {
	char* elemen = mVector->elementToString(element);
	short size = strlen(elemen);
	free(elemen);
	return size;
}

short __getSizeofStrElements(Vector *mVector) {
	short sizeOfStr = 5;
	for (short iter = 0; iter < mVector->lenght; ++iter)
		sizeOfStr += __getSizeOfStrElement(mVector, getElementFromVector(mVector, iter));

	return sizeOfStr;
}

char* toStringVector(Vector* mVector) {
	/*String ends wiht \0*/
	if (mVector->vectAsStr != NULL) {
		free(mVector->vectAsStr);
		mVector->vectAsStr = NULL;
	}

	char *vectStr = NULL;
	char *elemStr;
	vectStr = (char*) calloc(sizeof(char), __getSizeofStrElements(mVector));

	for (short iter = 0; iter < lenVector(mVector); iter++) {
		elemStr = toStringElement(mVector, getElementFromVector(mVector, iter));
		strcat(vectStr, elemStr);
		free(elemStr);
	}

	mVector->vectAsStr = vectStr;
	return vectStr;
}
