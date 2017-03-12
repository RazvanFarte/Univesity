assume cs:code, ds:data

	
data segment
	week_day db ?
	year dw ?
	month db ?
	day db ?
	week_days db "Su, ","$","Mo, ","$","Tu, ","$","Th, ","$","Fr, ","$","Sa, ","$"
	five db 5
	days db "01, $02, $03, $04, $05, $06, $07, $08, $09, $10, $11, $"
		db "12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $"
		db "23, $24, $25, $26, $27, $28, $29, $30, $31, $"
	months db "Jan $Feb $Mar $Apr $May $Jun $Jul $Aug $Sep $Oct $"
			db "Nov $Dec $"
	ten db 10
	buffer db 255 dup(?)
data ends

code segment
start:
	push data
	pop ds
	
	mov ah,2Ah
	int 21h
	mov week_day, AL
	mov year, CX
	mov month,DH
	mov day, DL
	
	;Print week day as string
	mul five
	mov dx,ax
	add dx,offset week_days
	mov ah,09h
	int 21h
	
	;Print month day as string
	mov al,day
	dec al
	mul five
	mov dx,ax
	add dx,offset days;Now i have the offset of day as string
	mov ah,09h
	int 21h
	
	;Print month as string
	mov al,month
	dec al
	mul five
	mov dx,ax
	add dx,offset months
	mov ah,09h
	int 21h
	
	;Print year
	mov ax,year
	mov bx,3
	.while:
		cmp ax,0
		je .print_year
		
		div ten
		add ah,'0'
		mov buffer[bx],ah
		dec bx
		mov ah,0
		jmp .while
	
	.print_year:
	mov buffer[4],"$"
	mov dx,offset buffer
	mov ah,9
	int 21h
	
	mov ah,1 
	int 21h
	
	mov ah,4Ch
	int 21h

code ends
end start