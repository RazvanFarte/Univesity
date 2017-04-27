#pragma once
#include <stdexcept>
#include <algorithm>

template <typename T>
class DynamicVector
{
public:
	class iterator : public std::iterator<std::random_access_iterator_tag, T, ptrdiff_t, T*, T&>
	{
	private:
		T* current;

	public:
		iterator(T* pointer) : current{ pointer } {}

		iterator operator++(int) { return iterator{ current++ }; }
		iterator operator++() { return iterator{ ++current }; }
		iterator operator--(int) { return iterator{ current-- }; }
		iterator operator--() { return iterator{ --current }; }

		iterator operator+(int offset) { return iterator{ current + offset }; }
		iterator operator-(int offset) { return iterator{ current - offset }; }

		int operator-(const iterator& rhs) { return current - rhs.current; }
		bool operator<(const iterator& rhs) { return current < rhs.current; }

		T operator*() { return *current; }
		T* operator->() { return current; }

		bool operator!=(const iterator& other) { return current != other.current; }
		bool operator==(const iterator& other) { return current = other.current; }


	};

	iterator begin() { return iterator{ elements }; };
	iterator end() { return iterator{ elements + this->length }; };


private:
	T* elements;
	int length;
	int maxLength;

	void _resize();
	void _shiftRight(int from, int numberOfPositions = 1);
	void _shiftLeft(int from, int numberOfPositions = 1);

public:
	DynamicVector<T>(int capacity = 10);

	DynamicVector<T>(const DynamicVector<T>& otherV);

	~DynamicVector();

	DynamicVector<T>& operator=(const DynamicVector<T>& other);
	DynamicVector<T>& operator-(const T&);

	int size();

	void insertAt(int index, const T& element);
	void push(const T& element);

	T& remove(int index);

	T& operator[](int pos);
	int find(const T&);
};

class DynamicVectorException : public std::runtime_error{

public:
	static constexpr const char* INDEX_OUT_OF_BOUNDS = "Index out of bounds!";
	static constexpr const char* ELEMENT_NOT_FOUND = "Element not found!";


	DynamicVectorException(std::string message) : std::runtime_error{ "DynamicVector Error! " + message + "\n"}{}
};

template<typename T>
inline void DynamicVector<T>::_resize()
{
	maxLength = maxLength++ * 2;
	T* copyEl = new T[maxLength];

	std::copy(this->begin(), this->end(), copyEl);

	delete[] this->elements;
	elements = copyEl;
}

template<typename T>
inline void DynamicVector<T>::_shiftRight(int from, int numberOfPositions)
{
	std::copy_backward(this->begin() + from, this->end(), this->elements + length + numberOfPositions);
}

template<typename T>
inline void DynamicVector<T>::_shiftLeft(int from, int numberOfPositions)
{
	//std::copy(this->begin() + from + numberOfPositions, this->end(), this->elements + from );
	/*for (auto it = this->begin() + from; it != this->end() - numberOfPositions; ++it)
		*it = *(it + numberOfPositions);*/
	for (int i = from; i < this->length - numberOfPositions; ++i)
		this->elements[i] = this->elements[i + numberOfPositions];
}

template<typename T>
inline DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template<typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& other)
{
	if (this != &other) {
		delete[] this->elements;

		this->length = other.length;
		this->maxLength = other.maxLength;
		this->elements = new T[maxLength];
		for (int i = 0; i < length; ++i)
			this->elements[i] = other.elements[i];
	}
	
	return *this;
}

template<typename T>
inline DynamicVector<T>& DynamicVector<T>::operator-(const T &element)
{
	int it = find(element);

	if (it == this->length)
		throw(DynamicVectorException{ std::string() + "Error during removing from vector!"
			+ DynamicVectorException::ELEMENT_NOT_FOUND });

	this->remove(it);

	return *this;
}

template<typename T>
inline int DynamicVector<T>::size()
{
	return length;
}

template<typename T>
void DynamicVector<T>::insertAt(int index, const T & element)
{
	if (index < 0 || index > this->length)
		throw DynamicVectorException{ std::string{ "Error during insertion in vector." } +DynamicVectorException::INDEX_OUT_OF_BOUNDS };

	if (this->length == this->maxLength)
		_resize();

	_shiftRight(index);
	elements[index] = element;
	this->length++;
}

template<typename T>
inline void DynamicVector<T>::push(const T & element)
{
	if (this->length == this->maxLength)
		_resize();

	elements[this->length++] = element;
}

template<typename T>
T& DynamicVector<T>::remove(int index)
{
	if (index < 0 || index >= this->length)
		throw DynamicVectorException{ std::string{ "Error during removing from vector." } + 
		DynamicVectorException::INDEX_OUT_OF_BOUNDS };

	T element = elements[index];

	_shiftLeft(index);
	this->length--;

	return element;
}

template<typename T>
inline T & DynamicVector<T>::operator[](int pos)
{
	return this->elements[pos];
}

template<typename T>
int DynamicVector<T>::find(const T &element)
{
	for (auto it = this->begin(); it != this->end(); ++it)
		if (element == *it)
			return it - this->begin();
	return this->end() - this->begin();
}

template<typename T>
inline DynamicVector<T>::DynamicVector(int capacity)
{
	maxLength = capacity;
	elements = new T[maxLength];
	length = 0;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(const DynamicVector<T>& other)
{
	this->length = other.length;
	this->maxLength = other.maxLength;
	this->elements = new T[maxLength];
	for (int i = 0; i < length; ++i)
		this->elements[i] = other.elements[i];
}
