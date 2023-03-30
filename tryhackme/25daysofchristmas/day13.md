# [Day 13] Accumulate

## Description
mcsysadmin has been super excited with their new security role, but wants to learn even more. In an attempt to show their l33t skills, they have found a new box to play with. 

This challenge accumulates all the things you've learnt from the previous challenges(that being said, it may be a little more difficult than the previous challenges). Here's the general way to attempt exploitation when just given an IP address:

    Start out with an NMAP scan to see what services are running
    Enumerate these services and try exploit them
    use these exploited services to get an initial access to the host machine
    enumerate the host machine to elevate privileges

Credit to DarkStar7471 for creating this challenge! Not all tasks will include supporting material!

----

## Answer the questions below

### A web server is running on the target. What is the hidden directory which the website lives on?
Answer: `/retro`

### Gain initial access and read the contents of user.txt
Answer: `THM{HACK_PLAYER_ONE}`

### [Optional] Elevate privileges and read the content of root.txt
Answer: `THM{COIN_OPERATED_EXPLOITATION}`
