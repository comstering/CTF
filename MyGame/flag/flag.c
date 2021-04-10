#include <stdio.h>

char* flag = "Good! You know memory analysis";

int main(int argc, char* argv[])
{
    printf("I know flag address \n");
    printf("Umm.... Where is the flag? \n", 0x0804c020);
}