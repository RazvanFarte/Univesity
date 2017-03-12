[bits 32]

section .text 
%include '..\msdn_defs.inc'

extern  _printf
extern _exit
extern _fgets
extern GetLastError
extern _fopen
extern CreateFile
extern ReadFile
extern _fclose
extern _sscanf

global  _main 

_main: 	
		;Open file
		push access_mode
		push filename
		call _fopen
		
		;Checks if function was succesful
		cmp eax,0
		je .error
		
		;If yes, save the pointer to file
		mov [file],EAX
		
		;Read from file the number of students (as a string)
		push dword [file]
		push buffer_size
		push buffer
		call _fgets
		
		;Convert the number to an integer
		xor ebx,ebx
		xor ax,ax
		.loop_convert:
			mov dl, [buffer + ebx]
			
			; if it's new line, jump
			cmp dl, [ten]
			je .end_loop_convert
			
			sub dl, '0'
			mul byte [ten]
			add al,dl
			
			inc ebx
			cmp ebx, buffer_size ;End of buffer
			je .end_loop_convert
			jmp .loop_convert
			
		.end_loop_convert:
			mov [num_students],ax
			xor edx,edx ; Students Counter
			mov ebx,students ; Actual position in vector
			
		.loop_students:
			push dword [file]
			push buffer_size
			push buffer
			call _fgets
			
			inc(edx)
			
			;Only read to structure| Doesn't matter how is implemented :D
			add ebx,42
			push dword [ebx]
			sub ebx,1
			push ebx
			sub ebx,1
			push ebx 
			sub ebx,20
			push ebx 
			sub ebx,20
			push ebx
			push students_format
			push buffer
			call _sscanf
			
			mov eax, [students + 20 + 20 + 1]
			
			cmp [num_students],edx
			je .keyboard_read
			add ebx,57
			jmp .loop_students
			
		.keyboard_read:
		
		.error:
			call GetLastError
			push EAX
			push error_msg
			call _printf
			jmp .end
		
		.end:
			push dword [file]
			call _fclose
			
			push    0
			call    _exit
			ret 

section .data

filename: 	db 	'Project2Input.txt',0 
file: dd ?
buffer: resb 100
buffer_size: equ $ - buffer
error_msg: db "Error with ID: %d",0
access_mode: db 'r',0
ten: db 10
num_students: dw ?
students: resb (20 + 20 + 1 + 1 + 15) * 50 ;50 Students; 20 - name| 20 - surname| 1 - age| 3 - height| 15 - eye color
students_format: db "%s,%s,%d,%d,%s"
