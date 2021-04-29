#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getFlag()
{
    printf("Good!! You know env \n");
}

int main(void)
{
    int modify;
    char buf[100];
    char* value;

    value = getenv("FLAG");

    strcpy(buf, value);

    if(modify == 0xdeadbeef)
    {
        getFlag();
    }

    printf("Are you success? \n");
}