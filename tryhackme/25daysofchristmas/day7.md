# [Day 7] Skilling Up

## Description
Previously, we saw mcsysadmin learning the basics of Linux. With the on-going crisis, McElferson has been very impressed and is looking to push mcsysadmin to the security team. One of the first things they have to do is look at some strange machines that they found on their network. 

Check out the supporting material here.

----

## Answer the questions below

use nmap scan 
- `nmap -sC -sV 10.10.244.75`
- `nmap -A -T5 10.10.244.75`
- `nmap -p 1-1000 10.10.244.75`

### how many TCP ports under 1000 are open?

Answer: `3`

### What is the name of the OS of the host?

Answer: `linux`

### What version of SSH is running?

Answer: `7.4`

### What is the name of the file that is accessible on the server you found running?

Visit port `999`

Answer: `interesting.file`
