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

	mov si,0
	mov cx,len1
	
	Repeta1:
		
		mov al,byte ptr s1[si]

		mov byte ptr s[si],al
		
		inc(si)
		
		loop Repeta1

	mov di,si
	mov si,len2 - 1

	mov cx, len2

	Repeta2:
		mov al, byte ptr s2[si]
		mov byte ptr s[di],al
		
		inc(di)
		dec(si)
		
		loop Repeta2
	
	mov ax,4c00h
	int 21h
	
c ends
end viorel