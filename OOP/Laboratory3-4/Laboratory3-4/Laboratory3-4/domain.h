#pragma once

typedef struct Material Material;

struct Material{
	char name[20];
	short nameLenght;

	char supplier[20];
	short supplierLenght;

	short quantity;

	char expirationDate[12];
	short expirationDateLenght;

	char* (*toString)(Material*);
	void(*update)(void(*tag)(Material *, void *), Material *, void *);
	void(*updateName)(Material * , void *);
	void(*updateSupplier)(Material* , void *);
	void(*updateQuantity)(Material* , void *);
	void(*updateExpiration)(Material* , void *);

	char* string;
};

Material* createMaterial(char* name, char* supplier, short quantity, char* expirationDate);
void destroyMaterial(void *mMaterial);

void setName(void* mMaterial, char *);
void setSupplier(void* mMaterial, char *);
void setQuantity(void* mMaterial, short);
void setExpirationDate(void* mMaterial, char *);

const char* getName(void* mMaterial);
const char* getSupplier(void* mMaterial);
short getQuantity(void* mMaterial);
const char* getExpirationDate(void* mMaterial);

char* toStringMaterial(void *);
short equalMaterial(void*, void*);
extern short isEqualToName(void *mMaterial, void *name);

Material* voidToMaterial(void *);
void updateTag(void(*tag)(void *structure, void *value), void *structure, void *value);
