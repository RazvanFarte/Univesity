#include "stdafx.h"

void test_createRepository() {
	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	Repository *repo2 = createRepository(NULL, NULL, NULL);

	assert(lenVector(getObjectsFromRepository(repo)) == 0);
	assert(lenVector(getObjectsFromRepository(repo2)) == 0);
	
	setRepositoryElementDestroyer(repo2, destroyMaterial);

	destroyRepository(repo);
	destroyRepository(repo2);
	free(repo);
	free(repo2);
}

void test_addObjectToRepository() {
	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	void* elements[] = { createMaterial("Bannanas", "SerSRL", 10, "2017/03/28") , //This is same with nr 3
						createMaterial("Bannanas", "SerSRL", 25, "2018/04/26"), 
						createMaterial("Bannanas", "SerSRL", 22, "2017/03/28"), // With this
						createMaterial("Orange", "SerSRL", 25, "2018/05/26"),
						createMaterial("Pineapple", "SerSRL", 25, "2018/02/22"),
						createMaterial("Chocolate", "SerSRL", 25, "2018/03/26"),
						createMaterial("Caccao", "SerSRL", 25, "2018/04/26"),
						createMaterial("Kiwi", "SerSRL", 25, "2018/04/25"),
						createMaterial("Kiwi", "SerSRL", 25, "2018/04/26") };

	for (int i = 0; i < 9; ++i) {
		int ret = addObjectToRepository(repo, elements[i]);

		if (i == 2) // Look over the list 3rd == 1st
			assert(ret == 1);
		else
			assert(ret == 0);
	}

	destroyRepository(repo);
	free(repo);
}

void test_removeObjectFromRepository() {
	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	Material* elements[] = { createMaterial("Bannanas", "SerSRL", 10, "2017/03/28") , //This is same with nr 3
		createMaterial("Bannanas", "SerSRL", 25, "2018/04/26"),
		createMaterial("Bannanas", "SerSRL", 22, "2017/03/28"), // With this
		createMaterial("Orange", "SerSRL", 25, "2018/05/26"),
		createMaterial("Pineapple", "SerSRL", 25, "2018/02/22"),
		createMaterial("Chocolate", "SerSRL", 25, "2018/03/26"),
		createMaterial("Caccao", "SerSRL", 25, "2018/04/26"),
		createMaterial("Kiwi", "SerSRL", 25, "2018/04/25"),
		createMaterial("Kiwi", "SerSRL", 25, "2018/04/26") };

	for (int i = 0; i < 9; ++i) 
		addObjectToRepository(repo, elements[i]);

	Material* mat;
	for (int i = 0; i < 8; ++i) {
		if (i == 2) {
			destroyMaterial(elements[i]);
			free(elements[i]);
			continue;
		}
		mat = removeObjectFromRepository(repo, elements[i]);
		assert(mat != NULL);
		assert(repo->equality(mat, elements[i]) != 0);

		destroyMaterial(mat);
		free(mat);
	}
	
	mat = removeObjectFromRepository(repo, createMaterial(elements[8]->name, elements[8]->supplier, 0, elements[8]->expirationDate));
	assert(mat != NULL);
	assert(repo->equality(mat, elements[8]) != 0);

	destroyMaterial(mat);
	free(mat);

	destroyRepository(repo);
	free(repo);

}

void test_updateObject() {
	Repository *repo = createRepository(equalMaterial, destroyMaterial, toStringMaterial);
	Material* elements[] = { createMaterial("Bannanas", "SerSRL", 10, "2017/03/28") , //This is same with nr 3
		createMaterial("Bannanas", "SerSRL", 25, "2018/04/26"),
		createMaterial("Bannanas", "SerSRL", 22, "2017/03/28"), // With this
		createMaterial("Orange", "SerSRL", 25, "2018/05/26"),
		createMaterial("Pineapple", "SerSRL", 25, "2018/02/22"),
		createMaterial("Chocolate", "SerSRL", 25, "2018/03/26"),
		createMaterial("Caccao", "SerSRL", 25, "2018/04/26"),
		createMaterial("Kiwi", "SerSRL", 25, "2018/04/25"),
		createMaterial("Kiwi", "SerSRL", 25, "2018/04/26") };

	for (int i = 0; i < 9; ++i)
		addObjectToRepository(repo, elements[i]);

	for (int i = 0; i < 9; ++i) {
		updateObject(repo, elements[i], elements[i]->updateQuantity, &i);

		if (i == 2) {
			assert(getQuantity(findObjectAt(repo, 0)) == i);
			continue;
		}
		assert(getQuantity(elements[i]) == i);
	}

	destroyRepository(repo);
	free(repo);

}

void tests_repo()
{
	test_createRepository();
	test_addObjectToRepository();
	test_removeObjectFromRepository();
	test_updateObject();
}
