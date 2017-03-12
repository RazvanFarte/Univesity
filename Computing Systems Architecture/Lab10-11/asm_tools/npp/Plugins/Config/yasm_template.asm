[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
        push    DWORD text 
        call    _printf
        add     esp, 8
        push    0
        call    _exit
        ret 

section .data

text:   db      'hello?',0 