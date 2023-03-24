# Drobots (WEB)

Pandora's latest mission as part of her reconnaissance training is to infiltrate the Drobots firm that was suspected of engaging in illegal activities. Can you help pandora with this task?

## Writeup

1. On checking the source files, from `entrypoint.sh`. I get to know that there is user with `admin` as username and I have to bypass the login form in order to get the flag.

2. In order to bypass the login page, I have checked the login function from `database.py` and from the query itself, it is obvious that we can bypass using sql injection.

Payload: username: `admin" OR 1=1 -- -` and password `any-pass`


And boom, we get our flag.

## Flag:

`HTB{p4r4m3t3r1z4t10n_1s_1mp0rt4nt!!!}`
