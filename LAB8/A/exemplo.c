#include <stdio.h>
#include <stdlib.h>
int *global_addr;
int *global_addr_check;

int main(void){

    /* We specialize in words of wisdom */
    char buf[24]; 
    // to avoid the null
    global_addr = (&buf+0x1); // final
    printf("[+] buf %p\n",buf);
    printf("[+] global_addr %p\n",global_addr);

    global_addr_check = global_addr-0x2; // 2 bytes antes do final
    printf("[+] global_addr_check %p\n",global_addr_check);
 
    char lolz[4];

    read(0, buf, 2048); 

    printf("%08x\n",*global_addr);
    printf("%08x\n",*global_addr_check);

    if(((*( global_addr))^(*(global_addr_check))) != ((*( global_addr))^(0x42424242))){
        printf("\n\nWoah There\n");

        exit(EXIT_FAILURE);
    }

    printf("BYPASS MEU AMIGO!!!\n");

    return 0;
}