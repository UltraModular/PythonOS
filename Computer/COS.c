#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(void) {

	printf("Booting up COS.\n");
	printf("Booting up COS..\n");
	printf("Booting up COS...\n");
	printf("Booting up COS.\n");
	printf("Booting up COS..\n");
	printf("Booting up COS...\n");
	printf("Booting up COS.\n");
	printf("Booting up COS..\n");
	printf("Booting up COS...\n\n");
	printf("Which user? (Type Number)\n");
	printf("Ian\n");
	printf("Guest\n");

	int userGuest, userIan, program, subProgram;
	char login[6], loginIan[4] = "Ian", loginGuest[6] = "Guest", yesOrNo;

	scanf(" %s", login);
	userIan = strcmp(login, loginIan);
	userGuest = strcmp(login, loginGuest);

	if (userIan == 0 || userGuest == 0) {
		printf("Welcome!\n");

		printf("	Which program?\n");
		printf("	1. Math\n");
		printf("	2. PaintINDEV\n");
		printf("	3. GamesIndev\n");
		printf("	4. Other ProgramsINDev\n");
		printf("	Exit?\n");

		scanf("%i", &program);

		if (program == 3) {

			printf("Choose which game you want to play:\n	0. Quit\n	1. Riddles\n	2. Tic Tac Toe\n	3. Text Adventure\n	10. Next page...\n	Game No.");
			scanf("%i", &subProgram);

			if (subProgram = 1) {

				printf("Welcome to Riddles!\nDo you want to start?\n");
				scanf(" %c", &yesOrNo);
				if (yesOrNo == 'Y') {
					char firstQuestion[6] = "Lakes", secondQuestion[6] = "Human", thirdQuestion[7] = "Candle";
					char firstAnswer[6], secondAnswer[6], thirdAnswer[7];
					int firstCorrect, secondCorrect, thirdCorrect;
					printf("What flows and has banks?\n");
					scanf(" %s", firstAnswer);
					firstCorrect = strcmp(firstQuestion, firstAnswer);
					if (firstCorrect == 0)
						printf("Correct! \n");
					else
						printf("Wrong!\n");
					printf("Do you want to do next?\n");
					scanf(" %c", &yesOrNo);
					if (yesOrNo == 'Y') {
						printf ("In the morning, I walk on 4 legs. In the afternoon, I walk on 2 legs. At night, I walk on 3 legs. What am I?\n");
						scanf(" %s", secondAnswer);
						secondCorrect = strcmp(secondQuestion, secondAnswer);
						if (secondCorrect == 0)
							printf("Correct 2\n");
						else
							printf("Wrong2\n");
						printf("Do you want to do next?\n");
						scanf(" %c", &yesOrNo);
						if (yesOrNo == 'Y') {
							printf("I am tall when I am young, and I am short when I am old.\n");
							scanf(" %s", secondAnswer);
							thirdCorrect = strcmp(thirdQuestion, thirdAnswer);
							if (thirdCorrect == 0)
								printf("Correct 3\n");
							else
								printf("Wrong 3\n");
						}

					}
					else
						printf ("Exit Riddles\n");
				}
				else
					printf ("Exit\n");


			}
		}

		if (program == 2) {

			printf("Welcome to Paint\nStart? (Y/N) ");
			scanf(" %c", &yesOrNo);
			if (yesOrNo == 'Y')
				printf("Welcome!\n");
			if (yesOrNo == 'N')
				printf("Ok!\n");

		}

		if (program == 1) {
			char operator;
			double firstNumber, secondNumber;
			printf("Type operator (+, -, *,): ");
			scanf(" %c", &operator);

			printf("Type two numbers: ");
			scanf("%lf %lf", &firstNumber, &secondNumber);

			switch (operator)
			{
			case '+':
				printf("%.1lf + %.1lf = %.1lf\n", firstNumber, secondNumber, firstNumber + secondNumber);
				break;

			case '-':
				printf("%.1lf - %.1lf = %.1lf\n", firstNumber, secondNumber, firstNumber - secondNumber);
				break;

			case '*':
				printf("%.1lf * %.1lf = %.1lf\n", firstNumber, secondNumber, firstNumber * secondNumber);
				break;

			case '/':
				printf("%.1lf / %.1lf = %.1lf\n", firstNumber, secondNumber, firstNumber / secondNumber);
				break;

				// operator doesn't match any case constant (+, -, *, /)
			default:
				printf("Error! operator is not correct");
			}
		}
	}
	else
		printf("Wrong user.\n");

	return 0;
}
