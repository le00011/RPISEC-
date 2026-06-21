#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MEMORY 4097

void __messsage_error(const char *);
int  __read_file(FILE *,size_t);

int main(int argc,char *argv[]){

    if ( argc < 2 ) {
        __messsage_error("Informe o arquivo");
    }

    FILE *file;

    file = fopen(argv[1],"rw");
    if(!file)
        __messsage_error("FILE error");

    fseek(file,0,SEEK_END);
    long len = ftell(file);
    fseek(file,0,SEEK_SET);

    if ( len > MEMORY )
        __messsage_error("Informe um arquivo menor!!!");
    
    printf("File size : {%ld}\n",len); 
    __read_file(file,(size_t)len);


    fclose(file);

    return 0;
}


void __messsage_error(const char *__mss){

    fprintf(stderr,"[X] %s \n",__mss);
    exit(EXIT_FAILURE);

}

int  __read_file(FILE *file,size_t len) {

    char buffer[MEMORY];
    memset(buffer,'\0',MEMORY);

    size_t count_read = fread(buffer,1 * sizeof(char), len,file);
    if ( count_read  < len )
        __messsage_error("fread()");

    for(int i=0;i<len;i++) {

        printf("\\x%02x",(unsigned char)buffer[i]);

        //if ( (i + 1) % 4 == 0 )
            //printf("\n");
        
    }
    printf("\n");
}