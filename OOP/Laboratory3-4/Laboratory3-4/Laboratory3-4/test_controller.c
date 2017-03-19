#include "stdafx.h"

void __test_createController() {

	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	BakeryController *contr = createController(repo);

	assert(contr->addObjectController != NULL);
	assert(contr->removeObjectController != NULL);
	assert(contr->updateObjectController != NULL);
	assert(contr->repo == repo);

	destroyController(contr);
	free(contr);
}

void __test_addController() {
	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	BakeryController *contr = createController(repo);
	char* nameMaterial[] = { "Banane", "Portocale", "Kiwi" };
	char* supplier[] = { "BananeSRL", "PortocaleSRL", "KiwiSRL" };
	short quantity[] = { 10, 5 , 10 };
	char* expirationDate[] = { "2017/03/24", "2017/03/24", "2017/10/05" };

	for (int i = 0; i < 3; ++i) {
		assert(strcmp(contr->addObjectController(contr, nameMaterial[i], supplier[i], quantity[i], expirationDate[i]), "Object added!\n") == 0);
	}

	destroyController(contr);
	free(contr);
}


void test_controller() {
	__test_createController();
}


