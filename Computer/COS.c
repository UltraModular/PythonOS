#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main (void) {

	printf ("Booting up COS.\n");
	printf ("Booting up COS..\n");
	printf ("Booting up COS...\n");
	printf ("Booting up COS.\n");
	printf ("Booting up COS..\n");
	printf ("Booting up COS...\n");
	printf ("Booting up COS.\n");
	printf ("Booting up COS..\n");
	printf ("Booting up COS...\n\n");
	printf ("Which user? (Type Number)\n");
	printf ("Ian\n");
	printf ("Guest\n");
	
	int userGuest, userIan, program, subProgram;
	char login[6], loginIan[4] = "Ian", loginGuest[6] = "Guest", yesOrNo;

	scanf (" %s", login);
	userIan = strcmp ( login, loginIan );
	userGuest = strcmp ( login, loginGuest );

	if ( userIan == 0 || userGuest == 0 ) {
		printf ("Welcome!\n");

		printf ("	Which program?\n");
		printf ("	1. Math\n");
		printf ("	2. PaintINDEV\n");
		printf ("	3. GamesIndev\n");
		printf ("	4. Other ProgramsINDev\n");
		printf ("	Exit?\n");
		
		scanf ("%i", &program);
		
		if ( program == 3 ) {

			printf ("Choose which game you want to play:\n	0. Quit\n	1. Riddles\n	2. Tic Tac Toe\n	3. Text Adventure\n	10. Next page...\n	Game No.");
			scanf ("%i", &subProgram);

			if ( subProgram = 1 ) {

				printf ("Welcome to Riddles!\nDo you want to start?\n");
				scanf (" %c", &yesOrNo);
				if ( yesOrNo == 'Y' )
					printf ("Hello!\n");

			}
		}

		if ( program == 2 ) {

			printf ("Welcome to Paint\nStart? (Y/N) ");
			scanf (" %c", &yesOrNo);
			if ( yesOrNo == 'Y')
				printf ("Welcome!\n");
			if ( yesOrNo == 'N' )
				printf ("Ok!\n");

		}

		if ( program == 1 ) {
			char operator;
			double firstNumber,secondNumber;
			printf("Type operator (+, -, *,): ");
			scanf(" %c", &operator);
 
			printf("Type two numbers: ");
			scanf("%lf %lf",&firstNumber, &secondNumber);
 
			switch(operator)
			{
			case '+':
			printf("%.1lf + %.1lf = %.1lf\n",firstNumber, secondNumber, firstNumber + secondNumber);
			break;
 
			case '-':
			printf("%.1lf - %.1lf = %.1lf\n",firstNumber, secondNumber, firstNumber - secondNumber);
			break;
 
			case '*':
			printf("%.1lf * %.1lf = %.1lf\n",firstNumber, secondNumber, firstNumber * secondNumber);
			break;
 
			case '/':
			printf("%.1lf / %.1lf = %.1lf\n",firstNumber, secondNumber, firstNumber / secondNumber);
			break;
 
			// operator doesn't match any case constant (+, -, *, /)
			default:
			printf("Error! operator is not correct");
			}
		}
	} else
		printf ("Wrong user.\n");

return 0;
}
