;Sir bytes. Octetii impari intr-un sir destinatie
assume cs:c, ds:d

d segment
	s1 db '1234567'
	len1 equ $-s1
	
	s db len1 dup(?)
d ends

c segment
viorel:
	mov ax,d
	mov ds,ax
	mov es,ax

	lea si,s1
	lea di,s
	mov cx,len1
	cld
	repeat:
		
		
		mov ah,0

		mov bl,2
		div bl

		cmp al,0
		je label1
		
		lodsb		
		stosb
		
		label1:
			inc(si)
		
		loop repeat	

	mov ax,4c00h
	int 21h
	
c ends
end viorel