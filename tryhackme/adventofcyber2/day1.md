# [Day 1] [Web Exploitation] A Christmas Crisis

## Description

The lab is all about cookies. HTTP is an inherently stateless protocol. This means that no data persists between connections; your computer could make two requests immediately after each other, and, without relying on separate software, the web server would have no way to know that it was you making both the requests. This begs the important question: if HTTP is stateless, then how do login systems work? The web server must have a way to identify that you have the right level of access, and it can hardly ask you to enter your password every time you request a new page!

The answer is cookies -- tiny little pieces of information that get stored on your computer and get sent to the server along with every request that you make. Authentication (or session) cookies are used to identify you (these will be very important in your mission today!). The server receives your request with the attached cookie, and checks the cookie to see what level of access you are allowed to have. It then returns a response appropriate to that level of access.

For example, a standard user should be able to see (but not interact with) our control panel; but Santa should be able to access everything! Cookies are also often used for other purposes such as advertising and storing user preferences (light/dark theme, for example); however, this will not be important in your task today. Any site can set cookies with a variety of properties -- the most important of these for today's task are the name and value of the cookies, both of which will always be set. It's worth noting that a site can only access cookies that are associated with its own domain (i.e. google.com can't access any cookies stored by tryhackme.com, and vice versa).

---

## Answer the questions below

### What is the name of the cookie used for authentication?

Register with a user and then login with the same user, check cookie storage for name of the cookie

Answer: `auth`

### In what format is the value of this cookie encoded?

Use cyberchef to decode cookie, use `From Hex` filter
Answer: `hexadecimal`

### Having decoded the cookie, what format is the data stored in?

Answer: `json`

### What is the value of Santa's cookie?

Just encode santa's value to hex.

https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)&input=eyJjb21wYW55IjoiVGhlIEJlc3QgRmVzdGl2YWwgQ29tcGFueSIsICJ1c2VybmFtZSI6InNhbnRhIn0

Answer: `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`

### What is the flag you're given when the line is fully active?

Enable all the toggle button in order to get the flag.
Answer: `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}`
