#include "stdafx.h"
#include "Controller.h"


Controller::Controller(const Repository<Bottle>& repo)
{
	this->_repo = repo;
}

Controller::~Controller()
{
}

void Controller::add(const std::string & name, const std::string & breed, int age, const std::string & link)
{
	this->_repo.add(Bottle{ breed, name, age, link });
}

DynamicVector<Bottle> Controller::getAll() 
{
	DynamicVector<Bottle> mVector = _repo.getAll();
	DynamicVector<Bottle> toRemove;
 
	for (auto it : mVector) {
		if (it.getStatus()) {
			toRemove.push(it);
		}
	}

	//for (DynamicVector<Bottle>::iterator it = toRemove.begin(); it != toRemove.end(); ++it) {
	for(auto it : toRemove){
		mVector.remove(mVector.find(it));
	}

	return mVector;
}

Bottle & Controller::remove(const std::string & breed, const std::string & name)
{
	return this->_repo.remove(Bottle{ breed, name });
}

void Controller::update(const std::string & breed, const std::string & name, 
	const std::string & nameNew, const std::string & breedNew, const std::string & ageNew,
	const std::string & linkNew)
{
	Bottle &oldBottle = this->_repo.findElement(Bottle{ breed, name });

	if (nameNew != "NULL")
		oldBottle.setName(nameNew);

	if (breedNew != "NULL")
		oldBottle.setBreed(breedNew);

	if (ageNew != "NULL")
		oldBottle.setAge(stoi(ageNew));

	if (linkNew != "NULL")
		oldBottle.setPhotograph(linkNew);

}

Bottle & Controller::find(const Bottle &toFind)
{
	return this->_repo.findElement(toFind);
}
