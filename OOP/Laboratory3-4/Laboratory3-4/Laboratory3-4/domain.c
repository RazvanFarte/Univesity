#include "stdafx.h"

void updateName(Material* mMaterial, void *name) {
	strcpy(mMaterial->name, (char*)name);
	mMaterial->nameLenght = strlen((char*)name);
	mMaterial->string = NULL;
}
void updateSupplier(Material* mMaterial, void *supplier) {
	strcpy(mMaterial->supplier, (char*)supplier);
	mMaterial->supplierLenght = strlen((char*)supplier);
	mMaterial->string = NULL;
}
void updateQuantity(Material* mMaterial, void *quantity) {
	mMaterial->quantity = *(int*)quantity;
	mMaterial->string = NULL;
}
void updateExpiration(Material* mMaterial, void *expirationDate) {
	strcpy(mMaterial->expirationDate, (char*)expirationDate);
	mMaterial->expirationDateLenght = strlen((char*)expirationDate);
	mMaterial->string = NULL;
}

Material* voidToMaterial(void *material)
{
	return (Material*)material;
}

void setName(void * mMaterial, char *name)
{
	strcpy(((Material*)mMaterial)->name, name);
}

void setSupplier(void * mMaterial, char *supplier)
{
	strcpy(((Material*)mMaterial)->supplier, supplier);
}

void setQuantity(void * mMaterial, short quantity)
{
	((Material*)mMaterial)->quantity = quantity;
}

void setExpirationDate(void * mMaterial, char *expirationDate)
{
	strcpy(((Material*)mMaterial)->expirationDate, expirationDate);
}

const char * getName(void * mMaterial)
{
	return ((Material*)mMaterial)->name;
}

const char * getSupplier(void * mMaterial)
{
	return ((Material*)mMaterial)->supplier;
}

short getQuantity(void * mMaterial)
{
	return ((Material*)mMaterial)->quantity;
}

const char * getExpirationDate(void * mMaterial)
{
	return ((Material*)mMaterial)->expirationDate;
}


char* toStringMaterial(void *mMaterial)
{
	/*Returns a string to material as string*/
	if ((voidToMaterial(mMaterial)->toString != NULL))
		return voidToMaterial(mMaterial)->string;

	short stringLength = (4 + 1 + 1) + voidToMaterial(mMaterial)->expirationDateLenght + voidToMaterial(mMaterial)->nameLenght + voidToMaterial(mMaterial)->supplierLenght;

	char *stringMaterial;
	stringMaterial = (char *)malloc(sizeof(char) * stringLength);

	char quantityStr[7];
	_itoa(voidToMaterial(mMaterial)->quantity, quantityStr, 10);

	strcpy(stringMaterial, voidToMaterial(mMaterial)->name);
	strcat(stringMaterial, " ");
	strcat(stringMaterial, voidToMaterial(mMaterial)->supplier);
	strcat(stringMaterial, " ");
	strcat(stringMaterial, quantityStr);
	strcat(stringMaterial, " ");
	strcat(stringMaterial, voidToMaterial(mMaterial)->expirationDate);
	strcat(stringMaterial, "\n\0");

	return stringMaterial;
}

short isEqualToName(void * mMaterial, void * name)
{
	if (strcmp(((Material*)mMaterial)->name, (char*)name) == 0)
		return 1;
	return 0;
}

short isEqualToDate(void * mMaterial, void * date)
{
	if (strcmp(((Material*)mMaterial)->expirationDate, (char*)date) == 0)
		return 1;
	return 0;
}

short isEqualToSupplier(void* mMaterial, void *supplier)
{
	if (strcmp(((Material*)mMaterial)->supplier, (char*)supplier) == 0)
		return 1;
	return 0;
}

Material* createMaterial(char * name, char * supplier, short quantity, char * expirationDate)
{
	/*Creates a material with given input and returns a pointer to that object
	*/

	Material *mMaterial;


	mMaterial = (Material*)malloc(sizeof(Material));

	strcpy(mMaterial->name, name);
	mMaterial->nameLenght = (short)strlen(name);

	strcpy(mMaterial->supplier, supplier);
	mMaterial->supplierLenght = (short)strlen(supplier);

	mMaterial->quantity = quantity;

	strcpy(mMaterial->expirationDate, expirationDate);
	mMaterial->expirationDateLenght = strlen(expirationDate);

	mMaterial->toString = toStringMaterial;
	//mMaterial->cast = voidToMaterial;

	mMaterial->string = NULL;

	mMaterial->updateExpiration = updateExpiration;
	mMaterial->updateName = updateName;
	mMaterial->updateQuantity = updateQuantity;
	mMaterial->updateSupplier = updateSupplier;

	return mMaterial;
}

void destroyMaterial(void *mMaterial) {
	if (voidToMaterial(mMaterial)->string != NULL)
		free(((Material*)mMaterial)->string);
}

short equalMaterial(void* material1, void* material2) {
	/*Returns 1 if material1 and material2 are equal and 0 otherwise*/

	return isEqualToName(material1, ((Material*)material2)->name ) && 
		isEqualToDate(material1, ((Material*)material2)->expirationDate ) &&
		isEqualToSupplier(material1, ((Material*)material2)->supplier);

	//return (strcmp(mMaterial1->name, mMaterial2->name) != 0 ? 0 : 1) && (strcmp(mMaterial1->expirationDate, mMaterial2->expirationDate) != 0 ? 0 : 1) && (strcmp(mMaterial1->supplier, mMaterial2->supplier) == 0 ? 1 : 0);

	/*(mMaterial1->quantity == mMaterial2->quantity);*/
}

void updateTag(void(*tag)(void *structure, void *value), void *structure, void *value) {
	(*tag)(structure, value);
	//After we update material, string is no more the same
}
