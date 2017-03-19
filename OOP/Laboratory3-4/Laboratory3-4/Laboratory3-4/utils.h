#pragma once

typedef struct Vector {
	void** elemtents;
	short lenght;
	short maxLenght;

	char* vectAsStr;

	short(*equality)(void *, void *);
	char*(*elementToString)(void *);
	void(*destroyerElements)(void *);
}Vector;


Vector* initVector(int);
void destroyVector(Vector*);
void setEualityForVector(Vector*, short(*)(void *, void *));
void setToStringForVector(Vector*, char* (*toStringElement)(void*));
void setDestroyerForVector(Vector*, void (*)(void*));

int pushToVector(Vector*, void*);
int insertInVectorAt(Vector*, void*, short);

short lenVector(Vector*);

void* popFromVector(Vector*);
void* removeFromVector(Vector*, short);

short indexElemInVector(Vector*, void *);
void* getElementFromVector(Vector*, short);

char* toStringVector(Vector *);
char* toStringElement(Vector*, void*);
