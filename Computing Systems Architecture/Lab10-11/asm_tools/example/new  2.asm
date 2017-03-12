[bits 32]

section .text 

extern  _printf
extern _exit
extern _fopen

global  _main 

_main: 
		push read
		push text
		call _fopen
		
        push    0
        call    _exit
        ret 

section .data
read: db 'r',0
text:   db      'Project2Input.txt',0 