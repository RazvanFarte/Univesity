#include "stdafx.h"

char* __removeObjectController(BakeryController* bakeryController,
	char* name, char* supplier, char* expirationDate) {

	Material* found = removeObjectFromRepository(bakeryController->repo, createMaterial(name, supplier, 0, expirationDate));

	if (found == NULL)
		return "Object not found!\n";

	free(found);
	return "Object removed!\n";
}


Material* __findObjectController(BakeryController* bakeryController,
	char* name, char* supplier, char* expirationDate) {

	Material* mMaterial = createMaterial(name, supplier, 0, expirationDate);
	Material* found = findObject(bakeryController->repo, mMaterial);

	if (found == NULL) {
		destroyMaterial(mMaterial);
		free(mMaterial);
		return NULL;
	}

	return found;
}

char* __addObjectController(BakeryController* bakeryController,
	char* name, char* supplier, int quantity, char* expirationDate) {
	
	Material *mMaterial = createMaterial(name, supplier, quantity, expirationDate);
	if (addObjectToRepository(bakeryController, mMaterial)) {
		updateObject(bakeryController->repo, mMaterial, mMaterial->update, quantity);
		return "Object already added. Quantity updated!\n";
	}

	return "Object added!\n";
}

char* __updateObjectController(BakeryController* bakeryController,
	char* nameOld, char* supplierOld, char* expirationDateOld,
	char nameNew, char* supplierNew, int quantityNew, char* expirationDateNew) {

	Material* found = createMaterial(nameOld, supplierOld, 0, expirationDateOld);

	if (strcmp(nameNew, "-") != 0) 
		if (updateObject(bakeryController->repo, found, found->updateName, nameNew)) 
			goto objectNotFound; //Object not found
	
	if (strcmp(supplierNew, "-") != 0)
		if (updateObject(bakeryController->repo, found, found->updateSupplier, supplierNew))
			goto objectNotFound; //Call update supplier 

	if (quantityNew != 0)
		if (updateObject(bakeryController->repo, found, found->updateQuantity, quantityNew))
			goto objectNotFound;

	if (strcmp(expirationDateNew, "-") != 0)
		if (updateObject(bakeryController->repo, found, found->updateExpiration, expirationDateNew))
			goto objectNotFound;

	return "Object updated!\n";

objectNotFound:
	destroyMaterial(found);
	free(found);
	return "Object not found!\n";

}

BakeryController * createController(Repository *repository)
{
	BakeryController *mController = (BakeryController*) malloc(sizeof(BakeryController));

	mController->repo = repository;
	mController->removeObjectController = __removeObjectController;
	mController->updateObjectController = __updateObjectController;
	mController->addObjectController = __addObjectController;
	mController->findObjectController = __findObjectController;

	return mController;
}

void destroyController(BakeryController *mController)
{
	destroyRepository(mController->repo);
	free(mController->repo);
}

