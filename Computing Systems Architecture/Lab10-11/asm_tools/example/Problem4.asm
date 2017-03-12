[bits 32]

section .text 

extern  _printf
extern _exit
extern __time32
extern _getchar

global  _main 

_main: 
		
		push 0
		call __time32
			
		bucla:	
			;Obtin bitii 8-23 ; rand = seed[8...23]
			shl eax,9
			shr eax,16		
			;AX^2 ;Calculez rand^2
			mul ax
			
			;Adaug constanta K; seed = rand^2 + K
			add ax,[const]
			adc dx,[const+2]
			
			;Rezultatul din DX:AX il pun in EBX, ca sa fie mai usor de lucrat
			push dx
			push ax
			pop ebx
			
			;Daca numarul random e pozitiv, sar mai departe
			cmp ebx,0
			jg pozitiv
			
			;Altfel, daca e negativ, il fac pozitiv
			neg ebx
			
			pozitiv:
			;Citesc de la tastatura
			push 0
			call _getchar
			
			;Daca se citeste caracterul CTRL^Z = -1, atunci ies din program
			cmp eax, -1
			je final
			
			;Altfel afisez numarul
			;p.s. Daca scrii un caracter + tasta enter, o sa fie 2 caractere si afiseaza 2 numere random
			push ebx
			push    DWORD text 
			call    _printf
			
			;Afisez o linie noua
			push DWORD newLine
			call _printf
			
			;In urma apelurilor eax a fost schimbat, asa ca ii reatribui copia din ebx
			mov eax,ebx
			jmp bucla
			
		;Iesire din program
		final:
			push    0
			call    _exit
			ret 

section .data

text:   db      '%d',0 
newLine: dd 10,0
const: dd 1002345h
