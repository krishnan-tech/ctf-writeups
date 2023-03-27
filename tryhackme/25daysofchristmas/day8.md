# [Day 8] SUID Shenanigans

## Description

Elf Holly is suspicious of Elf-ministrator and wants to get onto the root account of a server he setup to see what files are on his account. The problem is, Holly is a low-privileged user.. can you escalate her privileges and hack your way into the root account?

Deploy and SSH into the machine.
Username: holly
Password: tuD@4vt0G*TU

SSH is not running on the standard port.. You might need to nmap scan the machine to find which port SSH is running on.
nmap <machine_ip> -p <start_port>-<end_port>

Read the supporting materials here.

----

## Answer the questions below

### What port is SSH running on?
use nmap to determine port of ssh `nmap -p 1-1000 10.10.244.75`

Answer: `65534`

### Find and run a file as igor. Read the file /home/igor/flag1.txt
- Find suid binaries `find / -perm -4000 2>/dev/null` and I can see `find` has suid bit set.
- then from `https://gtfobins.github.io/gtfobins/find/` run the exploit. 

Answer: `THM{d3f0708bdd9accda7f937d013eaf2cd8}`

### Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?

- There is `system-control` binary with suid bit, run that and enter shell path as input.

Answer: `THM{8c8211826239d849fa8d6df03749c3a2}`