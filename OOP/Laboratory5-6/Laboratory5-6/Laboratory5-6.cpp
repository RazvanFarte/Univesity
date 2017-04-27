// Laboratory5-6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <crtdbg.h>

void testProgram() {
	DynamicVectorTests::test();
	RepositoryTests::test();

	DynamicVector<Bottle> bottles;
	bottles.push(Bottle{ "Soda", "Cola_Coca", 10, "http://www.budgetdumpster.com/blog/wp-content/uploads/2015/06/coke-bottle-1024x576.jpg" });

	bottles = bottles - Bottle{ "Soda", "Cola_Coca" };
}

int main()
{
	{
	testProgram();

	Repository<Bottle> mRepository{};
	mRepository.add(Bottle{ "Soda", "Cola_Coca", 10, 
		"http://www.budgetdumpster.com/blog/wp-content/uploads/2015/06/coke-bottle-1024x576.jpg", 10 });
	mRepository.add(Bottle{ "Milk", "Milka", 9, 
		"https://sc01.alicdn.com/kf/HTB14BI7LXXXXXXvXVXXq6xXFXXXP/Milka-Water-Bottle.jpg", 15 });
	mRepository.add(Bottle{ "Meer", "Urmus", 5, 
		"https://cdn.beeradvocate.com/im/beers/41840.jpg", 13 });
	mRepository.add(Bottle{ "Soda", "La_Moara_La_Niculai", 3, 
		"https://img.tesco.com/Groceries/pi/611/5035766044611/IDShot_540x540.jpg", 20 });
	mRepository.add(Bottle{ "Milk", "Fulga", 11, 
		"http://supermarketclaudia.ro/image/cache/data/produse%20alimentare/lactate,oua/lapte/Lapte_Fulga_UHT_1-5l-500x500-500x500.jpg", 39 });
	mRepository.add(Bottle{ "Water", "Aqua_Clujatica", 200,
		"http://evomarketonline.ro/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/a/q/aqua1_1.jpg",20 });
	mRepository.add(Bottle{ "Soda", "Apple_Juice", 31, 
		"https://i5.walmartimages.com/asr/7e794247-ad59-492f-a4a0-a239461dcbaa_1.0b75d3a25bd8d4e41b44933923df7bb9.jpeg", 9 });
	mRepository.add(Bottle{ "Milk", "Zuzu", 15, 
		"http://www.albalact.ro/resources/produse/Z-1454684765.png", 16 });
	mRepository.add(Bottle{ "Meer", "Tubork", 17, 
		"https://mir-s3-cdn-cf.behance.net/project_modules/disp/f84dcf23789661.56328d947c20f.jpg", 2 });


	Controller mController{ mRepository };
	Console console{ mController };


	/*std::function<void(Console&)> run = &Console::run;
	run(console);
*/
	console.run();
	//system("pause");
	}
	_CrtDumpMemoryLeaks();

    return 0;
}

