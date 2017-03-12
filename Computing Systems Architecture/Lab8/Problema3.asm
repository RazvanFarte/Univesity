assume cs:code, ds:data

data segment
	a dw ?
	b db ?
data ends

code segment
start:
	push data
	pop ds
	
	mov ax,440Eh
	mov bl,0
	int 21h
	
	mov ah,4Ch
	int 21h

code ends
end start