// Laboratory3-4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <crtdbg.h>  

int main()
{
	test_app();
	printf("Are there memory leaks? %c\n", _CrtDumpMemoryLeaks() == 0 ? 'F' : 'T');

	system("pause");

    return 0;
}

