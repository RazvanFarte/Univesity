[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
	

	mov eax,[nr1]
	mov ebx,[nr2]
	cmp eax,ebx
	ja gcd
	
	;Swap them
	swap:
		mov ecx,eax
		mov eax,ebx
		mov ebx,ecx
		
	;Ax - cel mai mare nr, Bx - celalalt numar
	gcd:
		cmp eax,ebx
		je printare
		
		sub eax,ebx
		
		cmp eax,ebx
		jb swap
		jmp gcd
		
	
	printare:
		mov [rezultat],eax
		push DWORD [rezultat]
		push text
		call _printf
		
	push 0
	call _exit
	ret
	
section .data

text:   db      'rezultat=%d',0 
nr1: dd	15
nr2: dd 40
rezultat: dd ?