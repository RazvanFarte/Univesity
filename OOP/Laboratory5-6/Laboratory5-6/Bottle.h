#pragma once
#include <string>
#include <ostream>
class Bottle
{
private:
	std::string _breed;
	std::string _name;
	int _age;
	std::string _photograph;
	bool _isAdopted;
	int _pricePayback;

public:
	Bottle();
	Bottle(const std::string& breed,const std::string& name, int age = 0,
		const std::string& photograph = "", int price = 0);
	Bottle(const Bottle& other);
	
	std::string toString() const;

	Bottle& operator=(const Bottle& rhs);
	friend std::ostream& operator<<(std::ostream& out, const Bottle& bottle);
	bool operator==(const Bottle& rhs) const;
	bool operator!=(const Bottle& rhs);
	bool operator<(const Bottle& rhs) const;

	inline std::string getBreed() const { return _breed; }
	inline std::string getName() const { return _name; }
	inline int getAge() const { return _age; }
	inline std::string getPhotograph() const { return _photograph; }
	inline bool getStatus() const { return _isAdopted; }
	inline int getPrice() const { return _pricePayback; }

	inline void setBreed(const std::string& newBreed) { this->_breed = newBreed; }
	inline void setName(const std::string& name) { this->_name = name; }
	inline void setAge(int age) { this->_age = age; }
	inline void setStatus(bool status) { this->_isAdopted = status; }
	inline void setPhotograph(const std::string& photograph) { this->_photograph = photograph; }
	inline void setPrice(int price) { this->_pricePayback = price; }

	void loadPage() const;

	~Bottle();
};

