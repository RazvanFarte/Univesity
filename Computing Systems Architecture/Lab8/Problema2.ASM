assume cs:code,ds:data

data segment
	char db ?
	buffer db 256 dup(?)
	len_buff equ $-buffer
	press_any db 10,"Press any key to continue...$"
data ends

code segment
start:
	
	push data
	pop ds
	
	;Read from console while true
	mov bx,0
	.while:
		mov ah,08h
		int 21h
		
		mov char,al
		
		;If character is $ end program
		cmp al, "$"
		je .end
		
		;If it is under "0" or above "9", then is another character
		cmp al,"0"
		jb .other_char
		
		cmp al,"9"
		ja .other_char
		
		;Otherwise it's a digit print it
		mov ah,02h
		mov dl,al
		int 21h
		jmp .while
		
		.other_char:
			mov buffer[bx],al
			inc bx
			jmp .while
	
	
	.end:
		;It will print the buffer of characters readed (only characters different from 1-9 or $)
		mov buffer[bx],"$"
		mov ah,09h
		mov dx,offset buffer
		int 21h
		
		;It will print the text from press_any buffer
		mov ah,09h
		mov dx,offset press_any
		int 21h
		
		;Get character from console; It will actually block the console, untill you press some key
		mov ah,01h
		int 21h
		
	
		mov ax,4c00h
		int 21h

code ends
end start