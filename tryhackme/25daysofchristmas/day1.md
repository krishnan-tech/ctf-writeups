# [Day 1] Inventory Management

## Description
Elves needed a way to submit their inventory - have a web page where they submit their requests and the elf mcinventory can look at what others have submitted to approve their requests. It’s a busy time for mcinventory as elves are starting to put in their orders. mcinventory rushes into McElferson’s office.


I don’t know what to do. We need to get inventory going. Elves can log on but I can’t actually authorise people’s requests! How will the rest start manufacturing what they want.  

McElferson calls you to take a look at the website to see if there’s anything you can do to help. Deploy the machine and access the website at http://<your_machines_ip>:3000 - it can take up to 3 minutes for your machine to boot!

Supporting material for the challenge is here!

----
## Answer the questions below

### What is the name of the cookie used for authentication?
Register with a user and then login with the same user, check cookie storage for name of the cookie

Answer: `authid`

### If you decode the cookie, what is the value of the fixed part of the cookie?
Use cyberchef to decode cookie, use `url decode` then `base64` decoding
Answer: `v4er9ll1!ss`

### After accessing his account, what did the user mcinventory request?

Try encoding the `mcinventoryv4er9ll1!ss` cookie, reverse of 2nd answer, and you will get `bWNpbnZlbnRvcnl2NGVyOWxsMSFzcw%3D%3D`. 

Replace the cookie and refresh the page, we will see `mcinventory` is requesting `firewall`.

Answer: `firewall`
