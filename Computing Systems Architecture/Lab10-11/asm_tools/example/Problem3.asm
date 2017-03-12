[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
	
		mov ecx, [len]
		mov esi,0
		mov eax,0
		
		_while:
			cmp cx,0
			je final
			
			mov ebx,v[esi]
			cmp ebx,0
			jg pozitiv
			
			neg ebx
			
			pozitiv:
				add eax,ebx
				add esi,4
				sub ecx,4
				
			jmp _while
		
		final:
			push DWORD eax
		
			push    DWORD text 
			call    _printf
			add     esp, 8
			push    0
			call    _exit
			ret 

section .data

text:   db      'hello?%d',0 
v: dd 1,-10,5,2,5,0,-9,17
len: dd $-v