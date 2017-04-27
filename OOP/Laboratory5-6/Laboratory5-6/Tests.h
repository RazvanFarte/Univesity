#pragma once
#include <stdexcept>

class DynamicVectorTests
{
private:
	static void _setUp(DynamicVector<int>&, int numberOfElements);
	static void _testConstructors();
	static void _testIterator();
	static void _testPush();
	static void _testInsertAt();
	static void _testRemove();
public:
	static void test();
};

class RepositoryTests
{
private:
	static void _testConstructors();
	static void _testAdd();
	static void _testRemove();
	static void _testUpdate();
public:
	static void test();
};