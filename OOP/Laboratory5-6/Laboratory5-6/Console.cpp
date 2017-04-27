#include "stdafx.h"
#include "Console.h"
#include <sstream>
#include <functional>
#include <map>
#include <iterator>
#include <stdexcept>
#include <algorithm>

std::string Console::_readLine()
{
	std::string line;
	std::getline(std::cin, line);

	return line;
}

/*Splits line into a comand and arguments separated by space. Take care that Console
can accept only 10 arguments.
*/
void Console::_splitLine(const std::string &line, std::string &command, std::vector<std::string> &arguments)
{
	command = "";
	arguments.resize(0);

	std::istringstream iss{ line };

	iss >> command;

	for (std::string argument; iss >> argument;) {
		arguments.push_back(argument);
	}

}

void Console::_administratorMode()
{
	std::function<bool(const std::vector<std::string>&,int)> hasNumberOfArguments =
		[](const std::vector<std::string>&  arr, int size) { return arr.size() == size; };

	std::cout << "Administrator mode. Login successful.\n";
	std::cout << "Call for 'help' if is 'any' problem.\n";
	Administrator::printHelp();


	while (true) {

		_printCommandText("Admin$~/");

		fLineBuffer = _readLine();
		_splitLine(fLineBuffer, fCommand, fCommandArguments);

		try {
			if (fCommand == Administrator::EXIT) {
				std::cout << "Exit administrator mode! Have a good night!\n";
				break;
			}

			if (fCommand == Administrator::HELP) {
				Administrator::printHelp();
				continue;
			}

			if (fCommand == Administrator::ADD_BOTTLE) {
				if (!hasNumberOfArguments(fCommandArguments, 4))
					throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
						std::string{ " addBottle command expects 4 arguments" } };

				this->_controller.add(fCommandArguments[1], fCommandArguments[0],
					stoi(fCommandArguments[2]), fCommandArguments[3]);
				continue;
			}

			if (fCommand == Administrator::SHOW_ALL_BOTTLES) {
				if (!hasNumberOfArguments(fCommandArguments, 0))
					throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
					std::string{ " showAllBottles command expects 0 arguments" } };

				DynamicVector<Bottle> bottles = this->_controller.getAll();
				std::copy(bottles.begin(), bottles.end(), std::ostream_iterator<Bottle>{std::cout, "\n"});
				continue;
			}

			if (fCommand == Administrator::DELETE_BOTTLE) {
				if (!hasNumberOfArguments(fCommandArguments, 2))
					throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
					std::string{ " deleteBottle command expects 2 arguments" } };

				Bottle &mBottle = this->_controller.remove(fCommandArguments[0], fCommandArguments[1]);
				continue;
			}

			if (fCommand == Administrator::UPDATE_BOTTLE) {
				if (!hasNumberOfArguments(fCommandArguments, 6))
					throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
					std::string{ " updateBottle command expects 6 arguments" } };

				this->_controller.update(fCommandArguments[0], fCommandArguments[1],
					fCommandArguments[2], fCommandArguments[3], fCommandArguments[4], 
					fCommandArguments[5]);

				continue;
			}

			if (fCommand == Administrator::SHOW_PRICE) {
				if(!hasNumberOfArguments(fCommandArguments, 1))
					throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
					std::string{ " showPrice command expects 1 arguments" } };

				DynamicVector<Bottle> bottles = this->_controller.getAll();
				Bottle mBottle = Bottle{ "", "" };
				mBottle.setPrice(std::stoi(fCommandArguments[0]));

				std::copy_if(bottles.begin(), bottles.end(), std::ostream_iterator<Bottle>{std::cout, "\n"},
					//[mBottle](const Bottle& other) {return mBottle.getPrice() > other.getPrice(); });
					[mBottle](const Bottle& other) {return mBottle < other; });
				continue;
			}

			throw(ConsoleException{ ConsoleException::INVALID_COMMAND });
		} catch(ConsoleException& cExcept) {
			std::cerr << cExcept.what();
		}
		catch (DynamicVectorException& dvExcept) {
			std::cerr << dvExcept.what();
		}
		catch (RepositoryException& rExcept) {
			std::cerr << rExcept.what();
		}


	}

}

void Console::_printMainMenu()
{
	std::cout << "Adopt an Empty Bottle!\n"
		"Billions of years in the future there was no bottle. Now bottles are everywhere, waiting for "
		"good people to collect(adopt) them. Please, if you care about these lonely beings, find them "
		"place in your home. Another solution is to get them to heaven(recycle bin)..\n"
		"Loreum ipsum..\n"
		"To be continued..\n";

	std::cout << this->SEPARATOR;

	std::cout << "Please choose one of the mode to continue:\n"
		"administrator (Administrator mode - If you wish to continue the deployment of DynamicArray..)\n"
		"user (User mode - If you wish to help the for a clean bottleNET)\n";

}

void Console::_printCommandText(std::string factor = "")
{
	std::cout << factor + "Command: ";
}

void Console::_printInvalidCommand()
{
	std::cout << "Invalid command!\n";
}

Console::Console(const Controller& controller) : _controller(controller), _user{*this} {
}

Console::~Console()
{
}

void Console::run()
{
	_printMainMenu();
		
	while (true) {
		_printCommandText();

		fLineBuffer = _readLine();
		//_splitLine(fLineBuffer, fCommand, fCommandArguments);

		if (fLineBuffer == Console::EXIT)
			goto endMainLoop;

		if (fLineBuffer == Console::ADMINISTRATOR) {
			_administratorMode();
			continue;
		}

		if (fLineBuffer == Console::USER) {
			_user.userMode();
			continue;
		}
		
		_printInvalidCommand();

	}

endMainLoop:
	//Dealocation stuff
	return;
}

void Console::Administrator::printHelp()
{
	std::cout << Console::SEPARATOR;
	std::cout << "Help Menu:\n";
	std::cout << "\taddBottle <type> <name> <age> <photograph>\n"

		"\tdeleteBottle <type> <name> (If bottle was not adopted, then deleting is not possible)\n"

		"\tupdateBottle <oldType> <oldName> <type> <name> type name age "
		"photograph(If you desire not to change one of them tags, use NULL keyword)\n"

		"\tshowAllBottles\n"

		"\tshowPrice <value>\n"

		"\texit\n";
	std::cout << Console::SEPARATOR;
}

//Administrator
//================================================================================================================

//void Console::Administrator::addElement()
//{
//
//}

//User
//================================================================================================================

void Console::User::help()
{
	std::cout << Console::SEPARATOR;
	std::cout << "User Help Menu:\n";
	std::cout << "\t" + std::string{User::SEE_BOTTLES} + "\n"

		"\t" + std::string{User::ADOPT_BOTTLE} + "<type> <name>\n"

		"\t" + std::string{User::NEXT_BOTTLE} + "\n"

		"\t" + std::string{User::SHOW_BY_BREED} + " <breed> <age> (Breed may miss - NULL)\n"

		"\t" + std::string{User::ADOPTON_LIST} + "\n" 

		"\texit\n";
	std::cout << Console::SEPARATOR;
}

void Console::User::userMode()
{
	_addoptionList = DynamicVector<Bottle>{};
	_bottles = DynamicVector<Bottle>{};
	auto bottles = _console._controller.getAll();
	for (auto it = bottles.begin(); it != bottles.end(); ++it)
		if (!it->getStatus())
			_bottles.push(*it);

	/*std::copy_if(bottles.begin(), bottles.end(), _bottles.begin(),
		[](const Bottle& bottle) {return !bottle.getStatus(); });
*/
	_currentBottle = _bottles.begin();

	std::cout << "User mode. Login successful.\n";
	std::cout << "Call for 'help' if is 'any' problem.\n";
	help();

	while (true) {

		_console._printCommandText("User$FFh~/");

		_console.fLineBuffer = _console._readLine();
		_console._splitLine(_console.fLineBuffer, _console.fCommand, _console.fCommandArguments);

		if (_console.fCommand == EXIT) {
			std::cout << "Exit user mode! Have a good night!\n";
			break;
		}

		try {
			auto pair = this->_commands.at(this->_console.fCommand);

			if(!this->_console.hasNumberOfArguments(pair.second))
				throw ConsoleException{ ConsoleException::WRONG_NUMBER_OF_ARGUMENTS +
					std::string{this->_console.fCommand} +
					" command expects " + std::to_string(pair.second) +
					"arguments!"};

			pair.first(*this);
		}
		catch (std::out_of_range& orExcept) {
			std::cerr << ConsoleException::INVALID_COMMAND << "\n";
		}
		catch (ConsoleException& cExcept) {
			std::cerr << cExcept.what() << "\n";
		}
		catch (DynamicVectorException& dvExcept) {
			std::cerr << dvExcept.what();
		}
		catch (RepositoryException& rExcept) {
			std::cerr << rExcept.what();
		}
	}
}

void Console::User::seeBottles()
{
	std::cout << *_currentBottle << "\n";
	_currentBottle->loadPage();
}

void Console::User::adoptBottle()
{
	std::string type = _console.fCommandArguments[0];
	std::string name = _console.fCommandArguments[1];

	try {
		Bottle& unadopted = _console._controller.find(Bottle{type, name});
		if (std::find(_addoptionList.begin(), _addoptionList.end(),
			Bottle{ type, name }) != _addoptionList.end())
			throw(ConsoleException{ ConsoleException::BOTTLE_ALREADY_ADOPTED });

		unadopted.setStatus(true);
		_addoptionList.push(unadopted);
	}
	catch (RepositoryException& rExcept) {
		throw ConsoleException{ "Bottle not found!" };
	}
}

void Console::User::nextBottle()
{
		_currentBottle++;

		if (!(_currentBottle != _bottles.end())) {
			_currentBottle = _bottles.begin();
		}

		if (std::find(_addoptionList.begin(), _addoptionList.end(), *_currentBottle) != _addoptionList.end())
			nextBottle();
}

void Console::User::showByBreed()
{
	std::string type = _console.fCommandArguments[0];
	int age = stoi(_console.fCommandArguments[1]);

	_bottles = DynamicVector<Bottle>{};

	auto bottles = _console._controller.getAll();
	for (auto it = bottles.begin(); it != bottles.end(); ++it) {
		if (type == "NULL") 
			if (it->getAge() < age) {
				_bottles.push(*it);
				continue;
			}

		if (it->getAge() < age && it->getBreed() == type)
			_bottles.push(*it);
	}

	this->_currentBottle = _bottles.begin();
}

void Console::User::adoptionList()
{
	std::copy(_addoptionList.begin(), _addoptionList.end(), std::ostream_iterator<Bottle>(std::cout, "\n"));
}
