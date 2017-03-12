[bits 32]

section .text 

%include '..\msdn_defs.inc'

extern  _printf
extern _exit
extern GetComputerName
extern GetLastError

global  _main 

_main: 
		push size
		push name
		call GetComputerName
		cmp eax,0
		je .error
		
		push name
		push msg
		call _printf
		add esp,8
		jmp .end
		
		.error:
			call GetLastError
			push eax
			push err_msg
			call _printf
			add esp,8
		
		.end:
			push    0
			call    _exit
			ret 
		
section .data

name: resb 40
size: dd 40
msg: db 'User name:%s',0
err_msg: db 'Failed with error: %d',0
