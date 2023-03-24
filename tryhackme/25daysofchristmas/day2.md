# [Day 2] Arctic Forum

## Description
A big part of working at the best festival company is the social live! The elves have always loved interacting with everyone. Unfortunately, the christmas monster took down their main form of communication - the arctic forum! 

Elf McForum has been sobbing away McElferson's office. How could the monster take down the forum! In an attempt to make McElferson happy, she sends you to McForum's office to help. 

P.S. Challenge may a take up to 5 minutes to boot up and configure!

Access the page at http://[your-ip-here]:3000

Check out the supporting material here!

----
## Answer the questions below

### What is the path of the hidden page?
use gobuster: `gobuster dir -u http://10.10.56.226:3000 -w /usr/share/wordlists/dirb/small.txt`

Answer: `/sysadmin`

### What is the password you found?
View source code, there is a hint there

Hint:  Admin portal created by arctic digital design - check out our github repo

Check their github repo (https://github.com/ashu-savani/arctic-digital-design) and there it is, admin and it's password.

Answer: `defaultpass`

### What do you have to take to the 'partay'

The answer is in admin panel.

Answer: `Eggnog`
