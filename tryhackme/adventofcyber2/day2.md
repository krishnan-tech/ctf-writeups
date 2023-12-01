# [Day 2] [Web Exploitation] The Elf Strikes Back!

## Description

This was a lot of information, so let's put it all together and look at the full process for exploiting a file upload vulnerability in a PHP web application:

1. Find a file upload point.
2. Try uploading some innocent files -- what does it accept? (Images, text files, PDFs, etc)
3. Find the directory containing your uploads.
4. Try to bypass any filters and upload a reverse shell.
5. Start a netcat listener to receive the shell
6. Navigate to the shell in your browser and receive a connection!

---

## Answer the questions below

### What string of text needs adding to the URL to get access to the upload page?

ID is already provided in the task description

Answer: `id=ODIzODI5MTNiYmYw`

### What type of file is accepted by the site?

Check source code and we will see that it only accepts .jpeg,.jpg,.png file. That means Image files.

Answer: `Image`

### In which directory are the uploaded files stored?

It's just a guess, because most of the uploaded files are stored in /uploads folder, but if there might be other directory, we can simply bruteforce using `gobuster`.

Answer: `/uploads/`

### What is the flag in /var/www/flag.txt?

Upload rev shell from here with this extension. `shell.jpg.php`

https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

Answer: `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`
