# [Day 4] Training

## Description
With the entire incident, McElferson has been very stressed.

We need all hands on deck now

To help resolve things faster, she has asked you to help the new intern(mcsysadmin) get familiar with Linux. 
Access the machine via SSH on port 22 using the command

ssh mcsysadmin@[your-machines-ip]

username: mcsysadmin
password: bestelf1234

Check out the supporting material here

----

## Answer the questions below

### How many visible files are there in the home directory(excluding ./ and ../)?
use `ls` to list directory

Answers: `8`

### What is the content of file5?
use `cat` command

Answers: `recipes`

### Which file contains the string ‘password’?
Use grpe command: `grep -R password`

Answers: `file6`

### What is the IP address in a file in the home folder?
Use grep and regex: `grep -REo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"`

Answers: `10.0.0.0`

### How many users can log into the machine?
Two users and one root

Answers: `3`

### What is the sha1 hash of file8?
`sha1sum file8`

Answers: `fa67ee594358d83becdd2cb6c466b25320fd2835`

### What is mcsysadmin’s password hash?
`cat /var/shadow.bak`

Answers: `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/`
