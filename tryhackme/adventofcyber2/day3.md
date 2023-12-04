# [Day 3] [Web Exploitation] Christmas Chaos

## Learning Objectives

1. Understanding Authentication
2. Understand the use of default credentials and why they're dangerous
3. Bypass a login form using BurpSuite

Use BurpSuite to brute force the login form. Use the following lists for the default credentials:

```
Username    Password
--------------------
root	    root
admin	    password
user	    12345
```

Use the correct credentials to log in to the Santa Sleigh Tracker app. Don't forget to turn off Foxyproxy once BurpSuite has finished the attack!

---

## Answer the questions below

### What is the flag?

Steps:

1. Intercept request using burpsuite and send it to intruder
2. use cluster bomb method in intruder
3. add this to payload list
4. start the attack and from the content length we can get to know which are username and password.

Username: `admin`
Password: `12345`

Answer: `THM{885ffab980e049847516f9d8fe99ad1a}`
