#pragma once
#include <stdexcept>
#include <vector>

template <typename T>
class Repository
{
private:
	DynamicVector<T> _elements;

	int _find(const T&);
public:
	Repository(int size = 0);
	Repository(const Repository<T>& other);
	
	Repository<T>& operator=(const Repository<T>& rhs);
	
	int getSize();
	
	bool find(const T&);
	T& findElement(const T&);
	void add(const T&);
	T& remove(const T&);
	void update(const T&, const T &);
	DynamicVector<T> getAll() const;

	~Repository();
};

class RepositoryException : public std::runtime_error {
public:
	static constexpr const char* DUPLICATE_OJECT = "Object already add. Duplicate object.";
	static constexpr const char* OBJECT_NOT_FOUND = "Object not found";

	RepositoryException(const std::string& message) : std::runtime_error{ "Repository Exception! " + message + "\n" }{ };
};

template<typename T>
inline int Repository<T>::_find(const T &elem)
{
	for (auto it = this->_elements.begin(); it != this->_elements.end(); ++it) {
		if (*it == elem)
			return it - this->_elements.begin();
	}
	return -1;
}

template<typename T>
inline Repository<T>::Repository(int size = 0) : _elements{size}
{
}

template<typename T>
inline Repository<T>::Repository(const Repository<T>& other)
{
	*this = other;
}

template<typename T>
inline Repository<T> & Repository<T>::operator=(const Repository<T>& rhs)
{
	this->_elements = rhs._elements;
	return *this;
}

template<typename T>
inline int Repository<T>::getSize()
{
	return this->_elements.size();
}

template<typename T>
inline bool Repository<T>::find(const T &elem)
{
	if (_find(elem) == -1)
		return false;
	return true;
}

template<typename T>
inline T& Repository<T>::findElement(const T &elem)
{
	int index = _find(elem);
	if (index == -1)
		throw(RepositoryException{ std::string{ "Error durring finding in Repository!" } +
			RepositoryException::OBJECT_NOT_FOUND });

	return this->_elements[index];
}


template<typename T>
inline void Repository<T>::add(const T & object)
{
	if (this->find(object))
		throw(RepositoryException{ std::string{"Error during adding to repository! "} + 
			RepositoryException::DUPLICATE_OJECT });

	this->_elements.push(object);
}

template<typename T>
T& Repository<T>::remove(const T &element)
{
	int index = _find(element);
	if (index == -1)
		throw(RepositoryException{ std::string{"Error durring removing from Repository!"} +
			RepositoryException::OBJECT_NOT_FOUND });

	/*T elem = _elements[index];
	this->_elements.erase(this->_elements.begin() + index);*/

	return this->_elements.remove(index);
}

template<typename T>
inline void Repository<T>::update(const T &element, const T &newElement)
{
	int index = _find(element);
	if (index == -1)
		throw(RepositoryException{ std::string{"Error durring updating element in Repository!"} +
			RepositoryException::OBJECT_NOT_FOUND });

	if(_find(newElement) != -1)
		throw(RepositoryException{ std::string{ "Error durring updating element in Repository!" } +
			"Can't update to new object, because new object already exists in repository"});

	this->_elements[index] = newElement;

}

template<typename T>
inline DynamicVector<T> Repository<T>::getAll() const
{
	return this->_elements;
}

template<typename T>
inline Repository<T>::~Repository()
{
}

