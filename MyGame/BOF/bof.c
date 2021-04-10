#include <stdio.h>

void Flag()
{
    printf("Good!! You got the Flag! \n");
	printf("Flag: This is the first problem I made \n");
}

int main(int argc, char* argv[])
{
	char name[100];
	printf("Your name: ");
	gets(name);
	printf("Hi! %s \n", name);
	printf("You have to find the Flag \n");
}