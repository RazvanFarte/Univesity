ASSUME CS:CODE,DS:DATA

DATA SEGMENT
	SIR DD 12345678H,1256ABCDH,12AB4344H,0ABCD4444h
	len equ ($-SIR)/4
	d dw ?
DATA ENDS

code segment
start:
	push data
	pop ds

	lea bx,sir
	mov cx, len - 1
	jcxz .end
	.while1:
		lea dx,[bx+4]
		mov si,dx

		.while2:
			mov ax,[si]
			cmp [bx],ax
			ja .keep
			
			;inversare
			mov ax,[bx]
			mov dx,[bx+2]
			
			push [si]
			push [si+2]

			pop [bx+2]
			pop [bx]

			mov [si],ax
			mov [si+2],dx

			.keep:
			add si,4
			cmp si, OFFSET d
			jae .continue
			jmp .while2
			
			
			
		.continue:		
		dec cx
		add bx, 4
		cmp cx,0
		je .end
		jmp .while1

.end:
	mov ah,4ch
	int 21h
	
code ends	
end start