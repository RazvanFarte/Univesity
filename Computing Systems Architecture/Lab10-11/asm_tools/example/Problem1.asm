[bits 32]

section .text 

%include '..\msdn_defs.inc'

extern  _printf
extern _exit
extern CreateFile
extern ReadFile
extern WriteFile
extern GetFileSize
extern SetFilePointer
extern GetLastError
extern CancelIo
extern CloseHandle

global  _main

_main: 
		;Create file
			push NULL
			push FILE_ATTRIBUTE_NORMAL
			push OPEN_EXISTING
			push NULL
			push 0
			push GENERIC_READ|GENERIC_WRITE
			push filename
			call CreateFile
		
		;Checks if was created properly | Jumps to error section if not
			cmp EAX, INVALID_HANDLE_VALUE
			je .error
		
		;If yes, saves the handle
			mov [handle], EAX
		
		.loop_file:
			;Read from file
			push NULL
			push bytes_readed
			push dword [buffer_size]
			push buffer
			push dword [handle]
			call ReadFile
			
			;If was an error, it will return 0(False)
			cmp EAX,0
			je .error
			
			;Loop over the buffer to lowercase letters
			mov ecx, [bytes_readed]
			jecxz .end
			.loop_buffer:
				mov al, [buffer + ecx - 1]
				cmp al, 'A'
				jl .not_changable
				cmp al, 'Z'
				jg .not_changable
				
				;It's an uppercase letter
				add al, 'a' - 'A'
				mov buffer[ecx - 1],al
				
				.not_changable:
				loop .loop_buffer
			
			;Get back [bytes_readed] positions to in order to write
			mov eax, [bytes_readed]
			neg eax
			push FILE_CURRENT
			push NULL
			push eax
			push dword [handle]
			call SetFilePointer
			
			cmp EAX, INVALID_SET_FILE_POINTER
			je .error
			
			;Write over
			push NULL
			push bytes_writed
			push dword [bytes_readed] ; Number of bytes to write
			push buffer
			push dword [handle]
			call WriteFile
			
			cmp EAX, 0
			je .error
			
			jmp .loop_file
		
		
		
		.error:
			call GetLastError
			push EAX
			push error_msg
			call _printf
			jmp .end
		
		.end:
			push DWORD [handle]
			call CloseHandle
			push    0
			call    _exit
			ret 

section .data


filename: db "Problem1In.txt",0
handle: dd ?
buffer: resb 100
buffer_size: dd 100
bytes_readed: dd ?
bytes_writed: dd ?
error_msg: db "Error with ID: %d",0