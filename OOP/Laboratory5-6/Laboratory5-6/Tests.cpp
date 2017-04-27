#include "stdafx.h"
#include <random>
#include <vector>
#include <iterator>

void DynamicVectorTests::_testConstructors()
{
	DynamicVector<int> mVector{ 10 };
	assert(mVector.size() == 0);

	_setUp(mVector, 10);
	
	DynamicVector<std::string> mVector2{};
	assert(mVector2.size() == 0);

	DynamicVector<int> mVector3{mVector};
	assert(mVector.size() == mVector3.size());
}


void DynamicVectorTests::_setUp(DynamicVector<int>& mVector, int numberOfElements) {
	std::default_random_engine generator;
	std::uniform_int_distribution<int> range{ 0, 10 * numberOfElements };

	while (numberOfElements--) {
		mVector.push(range(generator));
	}
}

void DynamicVectorTests::_testIterator()
{
	DynamicVector<int> mVector{0};
	_setUp(mVector, 10);

	for (DynamicVector<int>::iterator it = mVector.begin(); it != mVector.end(); ++it) {
		assert(*it >= 0 && *it < 10 * 10);
	}

	DynamicVector<int> mVector2;
}

void DynamicVectorTests::_testPush()
{
	DynamicVector<int> intVector{};
	_setUp(intVector, 10);

	int counter = 100;

	while (counter--) {

		short prevSize;

		prevSize = intVector.size();
		intVector.push(counter);
	
		assert(intVector.size() == prevSize + 1);
	}

}

void DynamicVectorTests::_testInsertAt()
{
	DynamicVector<int> mVector;
	_setUp(mVector, 25);

	
	int counter = 100, index;
	while (counter--) {
		index = counter % 20 * (counter / 20);
		if (index > mVector.size()) {
			try{
				mVector.insertAt(index, counter);
				assert(false);
			} catch(DynamicVectorException& err) {
				assert(true);
				continue;
			}
		}
		mVector.insertAt(index, counter);
	}
}

void DynamicVectorTests::_testRemove()
{
	int index;
	DynamicVector<int> mVector;
	_setUp(mVector, 25);

	int indexes[] = { 30,-1, 26, 25 };
	for (auto i : indexes) {
		try {
			mVector.remove(i);
			assert(false);
		}
		catch (DynamicVectorException& err) {
			assert(true);
			continue;
		}
		assert(false);
	}

	while (mVector.size()) {
		index = (mVector.size() - 1) % 20;
		mVector.remove(index);
	}

	
}

void DynamicVectorTests::test()
{
	_testConstructors();
	_testIterator();
	_testPush();
	_testInsertAt();
	_testRemove();
}

void RepositoryTests::_testConstructors()
{
	Repository<Bottle> mBottles;

	Repository<Bottle> mBottles2{mBottles};
}

void RepositoryTests::_testAdd()
{
	Repository<Bottle> mBottles;
	Bottle bottles[] = { Bottle{"b", "b", 1, "b"}, Bottle{ "b", "c", 1, "b" } , Bottle{ "b", "b", 1, "b" } };

	try {
		mBottles.add(bottles[1]);
		mBottles.add(bottles[0]);
		assert(true);
	}
	catch (RepositoryException& rexcept) {
		assert(false);
	}

	try {
		mBottles.add(bottles[2]);
		assert(false);
	}
	catch(RepositoryException& rexcept){
		assert(true);
	}
}

void RepositoryTests::_testRemove()
{
	Repository<Bottle> mBottles;
	Bottle bottles[] = { Bottle{ "b", "b", 1, "b" }, Bottle{ "b", "c", 1, "b" } , Bottle{ "b", "d", 1, "b" } };

	mBottles.add(bottles[0]);
	mBottles.add(bottles[1]);
	mBottles.add(bottles[2]);

	try {
		mBottles.remove(Bottle{ "b", "b" });
		mBottles.remove(Bottle{ "b" , "c" });
		assert(true);
	}
	catch (RepositoryException& rexcept) {
		assert(false);
	}
	
	try {
		mBottles.remove(Bottle{"b", "c"});
		assert(false);
	}
	catch (RepositoryException& rexcept) {
		assert(true);
	}
}

void RepositoryTests::_testUpdate()
{
	Repository<Bottle> mBottles;
	Bottle bottles[] = { Bottle{ "b", "b", 1, "b" }, Bottle{ "b", "c", 1, "b" } , Bottle{ "b", "d", 1, "b" } };

	mBottles.add(bottles[0]);
	mBottles.add(bottles[1]);
	mBottles.add(bottles[2]);

	try {
		mBottles.update(Bottle{ "b","b" }, Bottle{ "b", "f", 4, "da" });
		assert(true);
	}
	catch (RepositoryException& rexcept) {
		assert(false);
	}

	try {
		mBottles.update(Bottle{ "b","c" }, Bottle{ "b", "f", 4, "da" });
		assert(false);
	}
	catch (RepositoryException& rexcept) {
		assert(true);
	}

	try {
		mBottles.update(Bottle{ "c","c" }, Bottle{ "b", "f", 4, "da" });
		assert(false);
	}
	catch (RepositoryException& rexcept) {
		assert(true);
	}


}

void RepositoryTests::test()
{
	_testConstructors();
	_testAdd();
	_testRemove();
	_testUpdate();
}
