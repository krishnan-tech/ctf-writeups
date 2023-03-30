# [Day 21] Reverse Elf-ineering

## Description
McSkidy has never really touched low level languages - this is something they must learn in their quest to defeat the Christmas monster.

Download the archive and apply the command to the following binary files: chmod +x file-name

Please note that these files are compiled to be executed on Linux x86-64 systems.

The questions below are regarding the challenge1 binary file.

Read the supporting materials here.

----

## Answer the questions below

this is disassembly, we can easily get answer from this
```
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000400b4d <+0>:	push   rbp
   0x0000000000400b4e <+1>:	mov    rbp,rsp
   0x0000000000400b51 <+4>:	mov    DWORD PTR [rbp-0xc],0x1
   0x0000000000400b58 <+11>:	mov    DWORD PTR [rbp-0x8],0x6
   0x0000000000400b5f <+18>:	mov    eax,DWORD PTR [rbp-0xc]
   0x0000000000400b62 <+21>:	imul   eax,DWORD PTR [rbp-0x8]
   0x0000000000400b66 <+25>:	mov    DWORD PTR [rbp-0x4],eax
=> 0x0000000000400b69 <+28>:	mov    eax,0x0
   0x0000000000400b6e <+33>:	pop    rbp
   0x0000000000400b6f <+34>:	ret    
End of assembler dump.
pwndbg> 

```

### What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?
Answer: `1`

### What is the value of eax when the imull instruction is called?
Answer: `6`

### What is the value of local_4h before eax is set to 0?
Answer: `6`
