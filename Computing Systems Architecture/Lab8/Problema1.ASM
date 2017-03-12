assume cs:code,ds:data

data segment
	s db '123456'
	len equ $-s
	string db 8 dup(?)," | ","$"
	output db 10,"Press any key to exit...","$"
	tabl db "01"
data ends

code segment
start:
	push data
	pop ds
	
	and bx,0
	.loop_string:

		mov al,s[bx]
		mov si,0
		.convert_binary:
			shl al,1
			jc .one
			
			mov string[si],'0'
			inc si
			cmp si,8
			je .print
			jmp .convert_binary
			
			.one:
				mov string[si],'1'
				inc si
				cmp si,8
				je .print
				jmp .convert_binary
				
		.print:
			mov ah,9
			lea dx,string
			int 21h
		
		inc bx
		cmp bx,len
		je .end
		jmp .loop_string
			
	.end:
		mov ah,09h
		mov dx,offset output
		int 21h
		
		mov ah,1
		int 21h
		
		mov ax,4c00h
		int 21h
code ends
end start