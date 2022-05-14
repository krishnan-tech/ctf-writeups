---
description: Web Challenges by EZ-CTF
---

# Super Secure

![Screenshot of challenge](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FGhn0OSf58IrV71Z387bZ%2Fuploads%2FBbyOuq6NVqD1u7We0w9q%2Fimage.png?alt=media\&token=762aa653-a6a1-48fe-ad6a-a2c008e876c7)

### Description <a href="#description" id="description"></a>

This is so unbreakable! http://ez.ctf.cafe:8888

### Hint <a href="#hint" id="hint"></a>

Did you get your Covid Injection?

### Writeup

When you open the website, you will see something like this

![homepage of website](../../.gitbook/assets/image.png)

Now, seeing this like of name and password, one thing will directly popup in your mind, what is it?

Yes, that is SQL Injection

When we write `'` in name and password, we can see something like this

![Could not successfully run query (SELECT \* FROM members WHERE username = ''' AND password = '3590cb8af0bbb9e78c343b52b93773c9') from DB: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '3590cb8af0bbb9e78c343b52b93773c9'' at line 1](<../../.gitbook/assets/image (1).png>)

From this, we get to know what this is MySQL Database, and how to do the injection in this website.

My Payload:

name: `admin' or ''='`&#x20;

password: `YouAreHacked`

Boom 💥, we got the Flag!!! 🥳

### Flag <a href="#flag" id="flag"></a>

`EZ-CTF{N0t_S0_S4f3_4ft3r_411}`
