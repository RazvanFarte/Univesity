#include "stdafx.h"
#include "Bottle.h"
#include <Windows.h>
#include <shellapi.h>


Bottle::Bottle() : _breed(""), _age(0), _photograph(""), _name(""), _isAdopted(false), _pricePayback(0)
{
}

Bottle::Bottle(const std::string & breed, const std::string & name,
	int age, const std::string & photograph, int price) : _breed(breed), _name(name),
	_age(age), _photograph(photograph), _isAdopted(false), _pricePayback(price)
{
}

Bottle::Bottle(const Bottle & other)
{
	*this = other;
}

std::string Bottle::toString() const
{
	Bottle bottle = *this;
	return std::string{ bottle.getBreed() + " " + bottle.getName() + " " + std::to_string(bottle.getAge())
			+ " " + std::to_string(bottle.getPrice())};
}

Bottle & Bottle::operator=(const Bottle & rhs)
{
	_breed = rhs._breed;
	_name = rhs._name;
	_age = rhs._age;
	_photograph = rhs._photograph;
	_isAdopted = rhs._isAdopted;
	_pricePayback = rhs._pricePayback;

	return *this;
}

bool Bottle::operator==(const Bottle & rhs) const
{
	return this->getBreed() == rhs.getBreed() && this->getName() == rhs.getName();
		//&& this->getAge() == rhs.getAge() && this->getPhotograph() == rhs.getPhotograph();
}

bool Bottle::operator!=(const Bottle & rhs)
{
	return !(*this == rhs);
}

bool Bottle::operator<(const Bottle & rhs) const
{
	return this->_pricePayback < rhs._pricePayback;
}


void Bottle::loadPage() const
{
	ShellExecuteA(NULL, NULL, "firefox.exe", this->_photograph.c_str(), NULL, SW_SHOWMAXIMIZED);
}

Bottle::~Bottle()
{
}

std::ostream & operator<<(std::ostream & out, const Bottle & bottle)
{
	return out << bottle.toString();;
}
