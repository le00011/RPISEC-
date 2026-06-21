#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int value = 0;
int main(int argc,char *argv[]){

    if(argc < 2) return 1;

    char buffer[100];
    strcpy(buffer,argv[1]);
    printf(buffer);
    printf("\nADDRESS VALUE : %p\n",&value);
    printf("VALUE : %04x\n",value);

    exit(0);
}