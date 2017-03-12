[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
	
	mov eax,[nr1]
	add eax,[nr2]
	mov [rezultat],eax
	
	push DWord [rezultat]
	push text
	call _printf
	
	push 0
	call _exit
	ret
	
section .data

text:   db      'rezultat=%d',0 
nr1: dd	100
nr2: dd 200
rezultat: dd ?