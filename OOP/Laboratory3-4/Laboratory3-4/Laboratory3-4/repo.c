#include "stdafx.h"

Repository* createRepository(short(*equality)(void *, void *), 
	void(*elementDestroyer)(void *mMaterial), char *(*elementToString)(void *))
{
	/*Creates a empty repository*/
	Repository *mRepository = (Repository *)malloc(sizeof(Repository));

	mRepository->objects = initVector(0);

	setRepositoryEqualityRelation(mRepository, equality);
	setRepositoryElementDestroyer(mRepository, elementDestroyer);
	setRepositoryElementToString(mRepository, elementToString);

	return mRepository;
}

void __destroyElements(Vector *v) {
	for (int i = 0; i < v->lenght; ++i)
		free(getElementFromVector(v, i));
}

void destroyRepository(Repository * mRepo)
{
	Vector *v = getObjectsFromRepository(mRepo);
	//__destroyElements(v);
	destroyVector(v);
	free(v);
}

void setRepositoryEqualityRelation(Repository* mRepository,short(*equality)(void *, void *))
{
	mRepository->equality = equality;
	mRepository->objects->equality = equality;
}

void setRepositoryElementDestroyer(Repository *mRepository, void(*destroyMaterial)(void *mMaterial))
{
	mRepository->elementDestroyer = destroyMaterial;
	mRepository->objects->destroyerElements = destroyMaterial;
}

void setRepositoryElementToString(Repository *mRepository, char *(*elementToString)(void *))
{
	mRepository->elementToString = elementToString;
	mRepository->objects->elementToString = elementToString;
}

Vector * getObjectsFromRepository(Repository * mRepo)
{
	return mRepo->objects;
}



int addObjectToRepository(Repository * mRepository, void * mObject)
{
	/*Adds an object to repository
	Returns
	0 - if mObject was successfull added
	1 - if mObject has been already added
	2 - if mObject is not valid
	*/
	if (indexElemInVector(mRepository->objects, mObject) != -1)
		return 1;

	return pushToVector(mRepository->objects, mObject) == 1 ? 0 : 3;
}

void* removeObjectFromRepository(Repository *mRepository, void *mObject)
{
	short objectIndex = indexElemInVector(mRepository->objects, mObject);

	if (objectIndex == -1)
		return NULL;

	return removeFromVector(mRepository->objects, objectIndex);
}

short updateObject(Repository* mRepository, void *objectToBeFound, void(*tag)(void *object, void *value), void* value) {


	objectToBeFound = findObject(mRepository, objectToBeFound);

	if (objectToBeFound == NULL)
		return  -1;

	(*tag)(objectToBeFound, value);

	return 0;
}

void * findObject(Repository *mRepository, void* object)
{
	void *element;
	for (int i = 0; i < mRepository->objects->lenght; ++i) {
		element = getElementFromVector(mRepository->objects, i);

		if (mRepository->equality(element, object))
			return element;
	}
	return NULL;
}

void* findObjectAt(Repository *mRepository, short index)
{
	if (index >= getObjectsFromRepository(mRepository)->lenght || index < 0)
		return NULL;
	return getElementFromVector(getObjectsFromRepository(mRepository), index);
	
}


