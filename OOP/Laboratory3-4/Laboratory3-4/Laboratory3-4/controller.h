#pragma once
#include "repo.h"

typedef struct BakeryController BakeryController;

struct BakeryController {
	Repository* repo;
	
	/*Return 
		"Object added!\n" - if object was succsesfully added
		"Object already added. Quantity updated!\n" - if object already added
	*/
	char*(*addObjectController)(BakeryController* bakeryController, 
		char* name, char* supplier, int quantity, char* expirationDate);

	char*(*updateObjectController)(BakeryController* bakeryController, 
		char* nameOld, char* supplierOld, char* expirationDateOld,
		char nameNew, char* supplierNew, int quantityNew, char* expirationDateNew);

	char*(*removeObjectController)(BakeryController* bakeryController,
		char* name, char* supplier, char* expirationDate);

	Material* (*findObjectController)(BakeryController* bakeryController,
		char* name, char* supplier, char* expirationDate);
};

BakeryController* createController(Repository*);
void destroyController(BakeryController*);