#pragma once
#include "utils.h"

typedef struct Repository
{
	Vector *objects;
	short(*equality)(void*, void*);
	void(*elementDestroyer)(void *mMaterial);
	char *(*elementToString)(void *);
}Repository;

Repository* createRepository(short(*elemetnsEquality)(void *, void *),
	void(*elementDestroyer)(void *mMaterial), char *(*elementToString)(void *));
void destroyRepository(Repository* mRepo);

void setRepositoryEqualityRelation(Repository*, short(*equality)(void*, void*));
void setRepositoryElementDestroyer(Repository*, void(*destroyMaterial)(void *mMaterial));
void setRepositoryElementToString(Repository *mRepository, char *(*elementToString)(void *));

Vector* getObjectsFromRepository(Repository*);

/*Adds an object to repository
Returns
0 - if mObject was successfull added
1 - if mObject has been already added
2 - if mObject is not valid
*/
int addObjectToRepository(Repository*, void*);

void* removeObjectFromRepository(Repository*, void*);
void* findObject(Repository*, void *object);
void* findObjectAt(Repository*, short index);
short updateObject(Repository*, void *objectToBeFound, void(*tag)(void *object, void *value), void* value);