# [Day 4] [Web Exploitation] Santa's watching

## Description

Deploy both the instance attached to this task (the green deploy button) and the AttackBox by pressing the blue "Start AttackBox" button at the top of the page. After allowing 5 minutes, navigate to the website (10.10.213.174) in your AttackBox browser.

It is up to you to decide if you wish to create the wordlist yourself or use a larger wordlist located in /opt/AoC-2020/Day-4/wordlist on the AttackBox. The wordlist is also available for download if you are using your own machine.

In summary, use the tools and techniques outlined in today's advent of cyber; search for the API, find the correct post and bring back Elf's forums!

---

## Answer the questions below

### Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

Answer: `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`

### Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?

`└─$ gobuster dir -u http://10.10.213.174/ -w /usr/share/wordlists/dirb/small.txt`

Answer: `site-log.php`

### Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

Download wordlist from here: https://assets.tryhackme.com/additional/cmn-aoc2020/day-4/wordlist
`└─$ wfuzz -c -z file,wordlist -u http://10.10.213.174/api/site-log.php?date=FUZZ`

Answer: `THM{D4t3_AP1}`
