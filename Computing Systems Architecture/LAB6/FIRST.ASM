assume cs:c, ds:d

d segment
	s1 db '1234'
	len1 equ $-s1
	s2 db '567'
	len2 equ $-s2
	
	s db len1+len2 dup(?)
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
		movsb	
		loop repeat	
	
	mov si,offset s2 + len2 - 1
	mov cx,len2
	std
	repeat2:
		lodsb
		cld
		stosb
		std
		loop repeat2

	mov ax,4c00h
	int 21h
	
c ends
end viorel