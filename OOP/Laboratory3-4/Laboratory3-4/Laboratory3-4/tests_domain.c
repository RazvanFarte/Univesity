#include "stdafx.h"

char* __allocateForString(char* str) {
	char *mStr = (char*)malloc(strlen(str) * sizeof(char));
	strcpy(mStr, str);
	return mStr;
}

void test_createMaterial()
{
	char name[] = "Aurel";
	char supplier[] = "DSRL";
	char expirationDate[] = "2000/10/01";

	for (int i = 0; i < 100; ++i) {
		short quantity = i;
	
		Material *material1 = createMaterial(name, supplier, quantity, expirationDate);

		assert(strcmp(getName((void*)material1), name) == 0);
		assert(strcmp(getSupplier((void*)material1), supplier) == 0);
		assert(strcmp(getExpirationDate((void*)material1), expirationDate) == 0);
		assert(getQuantity((void*)material1) == quantity );

		destroyMaterial((void*)material1);
		free(material1);
	}
}

void test_equalMaterial() {
	char* name[] = { "Aurel" , "Viorel", "Ducu"};
	char* supplier[] = { "DSRL", "Mimi", "Exa" };
	char* expirationDate[] = { "2000/10/01", "1997/10/20", "2012/09/01" };

	for (int i = 0; i < 3; ++i) {
		Material *material1 = createMaterial(name[i], supplier[i], i, expirationDate[i]);

		for (int j = 0; j < 3; ++j) {
			Material *material2 = createMaterial(name[j], supplier[j], j, expirationDate[j]);

			if (i == j)
				assert(equalMaterial((void*)material1, (void*)material2) == 1);
			else
				assert(equalMaterial((void*)material1, (void*)material2) == 0);

			destroyMaterial((void*)material2);
			free(material2);
		}

		destroyMaterial((void*)material1);
		free(material1);
	}
}

void updateName2(Material * mMaterial, void *name) {
	strcpy(mMaterial->name, (char*)name);
	mMaterial->nameLenght = strlen((char*)name);
}
void updateSupplier2(Material* mMaterial, void *supplier) {
	strcpy(mMaterial->supplier, (char*)supplier);
	mMaterial->supplierLenght = strlen((char*)supplier);
}
void updateQuantity2(Material* mMaterial, void *quantity) {
	mMaterial->quantity += (*(int*)quantity);
}
void updateExpiration2(Material* mMaterial, void *expirationDate) {
	strcpy(mMaterial->expirationDate, (char*)expirationDate);
	mMaterial->expirationDateLenght = strlen((char*)expirationDate);
}

void test_updateTag() {

	char name[] = "Aurel";
	char supplier[] = "DSRL";
	char expirationDate[] = "2000/10/01";
	short quantity = 10;

	Material *material1 = createMaterial(name, supplier, quantity, expirationDate);


	char name2[] = "Miron";
	char supplier2[] = "ABIS";
	char expirationDate2[] = "2001/11/02";
	short quantity2 = 20;
	updateTag(updateSupplier2, (void*)material1, (void*)supplier2);
	updateTag(updateName2, (void*)material1, (void*)name2);
	updateTag(updateExpiration2, (void*)material1, (void*)expirationDate2);
	updateTag(updateQuantity2, (void*)material1, (void*)&quantity2);

	assert(strcmp(getName((void*)material1), name2) == 0);
	assert(strcmp(getSupplier((void*)material1), supplier2) == 0);
	assert(strcmp(getExpirationDate((void*)material1), expirationDate2) == 0);
	assert(getQuantity((void*)material1) == quantity + quantity2);

	destroyMaterial((void*)material1);
	free(material1);
}


void tests_domain() {
	test_createMaterial();
	test_equalMaterial();
	test_updateTag();
}


