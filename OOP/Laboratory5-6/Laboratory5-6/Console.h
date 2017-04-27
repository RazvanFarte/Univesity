#pragma once
#include <vector>
#include <stdexcept>
#include <map>
#include "Controller.h"
#include <functional>

class Console
{
private:

	Controller _controller;

	static constexpr const char* ADMINISTRATOR = "administrator";
	static constexpr const char* USER = "user";
	static constexpr const char* EXIT = "exit";


	static constexpr const char* SEPARATOR = "----------------------------------------\n";

	std::string fLineBuffer;
	std::string fCommand;
	std::vector<std::string> fCommandArguments;

	std::string _readLine();
	void _splitLine(const std::string &line, std::string &command, std::vector<std::string> &arguments);
	inline bool hasNumberOfArguments(int nArgs) const { return fCommandArguments.size() == nArgs; }
	
	void _administratorMode();

	void _printMainMenu();
	void _printCommandText(std::string factor);
	void _printInvalidCommand();

	class Administrator {

	public:
		static constexpr const char* EXIT = "exit";
		static constexpr const char* HELP = "help";
		static constexpr const char* ADD_BOTTLE = "addBottle";
		static constexpr const char* DELETE_BOTTLE = "deleteBottle";
		static constexpr const char* UPDATE_BOTTLE = "updateBottle";
		static constexpr const char* SHOW_ALL_BOTTLES = "showAllBottles";
		static constexpr const char* SHOW_PRICE = "showPrice";

		static void printHelp();
		//void addElement();


	};

	class User {
	private:
		Console& _console;
		DynamicVector<Bottle> _bottles;
		DynamicVector<Bottle>::iterator _currentBottle;
		DynamicVector<Bottle> _addoptionList;

		std::map < std::string, std::pair<std::function<void(User&)>, int>> _commands;
		
		void help();
		void seeBottles();
		void adoptBottle();
		void nextBottle();
		void showByBreed();
		void adoptionList();
	public:

		static constexpr const char* EXIT = "exit";
		static constexpr const char* HELP = "help";
		static constexpr const char* SEE_BOTTLES = "seeBottle";
		static constexpr const char* ADOPT_BOTTLE = "adoptBottle";
		static constexpr const char* NEXT_BOTTLE = "nextBottle";
		static constexpr const char* SHOW_BY_BREED = "showByBreed";
		static constexpr const char* ADOPTON_LIST = "adoptionList";


		User(Console& console) : _console{ console }, _currentBottle{nullptr} {
			//Pairs{function, numberOfArguments}
			_commands[User::HELP] = std::make_pair(&User::help,0);
			_commands[User::SEE_BOTTLES] = std::make_pair(&User::seeBottles, 0);
			_commands[User::ADOPT_BOTTLE] = std::make_pair(&User::adoptBottle, 2);
			_commands[User::NEXT_BOTTLE] = std::make_pair(&User::nextBottle, 0);
			_commands[User::SHOW_BY_BREED] = std::make_pair(&User::showByBreed, 2);
			_commands[User::ADOPTON_LIST] = std::make_pair(&User::adoptionList, 0);
			
		};

		void userMode();
	};

	User _user;
	//Administrator administrator;
public:
	Console(const Controller&);
	~Console();
	void run();

};

class ConsoleException : public std::runtime_error {
public:
	static constexpr const char* INVALID_COMMAND = "Invalid command!";
	static constexpr const char* WRONG_NUMBER_OF_ARGUMENTS = "Wrong number of arguments!";
	static constexpr const char* BOTTLE_ALREADY_ADOPTED = "This bottle was already adopted!";
	
	ConsoleException(const std::string& message) : std::runtime_error{ "Console error! " + message + "\n" } {};
};