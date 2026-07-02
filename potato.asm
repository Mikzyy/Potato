section .data
    m db 'Potato',10
section .text
    global _start
_start:
    mov eax, 1
    mov edi, eax
    mov rsi, m
    mov edx, 7
    syscall
    mov al, 60
    xor edi, edi
    syscall
