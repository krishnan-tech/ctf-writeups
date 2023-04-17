# my-favorite-game

> My favorite game to play in a city is to just go with the flow.
  You (almost) always end up somewhere new or fun!

### Writeup
When we run the chall, it asks for direction, and we have to send `up`, `down`, `left`, `right` as direction. If the direction is correct, it will again ask same question, or else, it will send wrong direction message or exit the program directly. 

![](https://i.imgur.com/EjHNFDi.png)

From the above conditions mentioned, I have made a script that automates this task.

```python 
from pwn import *
import time

context.log_level = "info"


arr = ['up', "up", "down", 'down']
dir = ['down', 'up', 'left', 'right']

def do_all_arr_first():
    target = remote("0.cloud.chals.io", 22980)
    for i, val in enumerate(arr):
        print("do_all_arr", val)
        if i == 0:
            target.sendlineafter(b"down?", val.encode())
            print('line1')
            print(target.recvline())
        else:
            target.sendline(val.encode())
        print(target.recvline())
    return target


flag = False
for i in range(100):
    for d in dir:
        target = do_all_arr_first()
        try:
            print("now sending, ", d)
            target.sendline(d.encode())
            recv = target.recvline()
            if b"Should we go left, right, up, or down?\n" in recv:
                arr.append(d)
                print('arr appended', arr)
                break
            
            if b"jctf" in recv:
                print("\n\n\n")
                print(recv)
                print('\n\n')
                flag = True
                break
        except Exception as e:
            print(e)
        
        target.close()

    if flag:
        break

    print(arr)
```

Flag: `jctf{K0nami_C0d3_w0rks_h3r3_t00}`


