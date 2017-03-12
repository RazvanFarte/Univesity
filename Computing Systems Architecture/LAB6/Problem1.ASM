;Problema 4
assume cs:c, ds:d

d segment
	s db 1,2,4,6,10,20,25
	len equ $-s

	dest db $-s-1 dup(?)
d ends

c segment
viorel:
	mov ax,d
	mov ds,ax
	
	xor bx,bx
	.while:
		mov al,s[bx+1]
		sub al,s[bx]
		
		mov dest[bx],al
		
		inc bx
		
		cmp bx,len-1
		je .end
		jmp .while
	
	.end:
		mov ax,4c00h
		int 21h
	
c ends
end viorel