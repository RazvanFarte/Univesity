#pragma once
#include <functional>
#include "Repository.h"
class Controller
{
	Repository<Bottle> _repo;
public:
	Controller(const Repository<Bottle>&);
	~Controller();

	void add(const std::string& name, const std::string& breed,
		int age, const std::string& link);
	DynamicVector<Bottle> getAll();
	Bottle& remove(const std::string& breed, const std::string& name);
	void update(const std::string& breed, const std::string& name, const std::string& nameNew, 
		const std::string& breedNew, const std::string & ageNew, const std::string& linkNew);
	Bottle& find(const Bottle&);
};

