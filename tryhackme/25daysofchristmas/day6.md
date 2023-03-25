# [Day 6] Data Elf-iltration

## Description
"McElferson! McElferson! Come quickly!" yelled Elf-ministrator.

"What is it Elf-ministrator?" McElferson replies.

"Data has been stolen off of our servers!" Elf-ministrator says!

"What was stolen?" She replied.

"I... I'm not sure... They hid it very well, all I know is something is missing" they replied.

"I know just who to call" said McElferson...

Check out the supporting material here.

Challenge and supporting material created by Sq00ky.

----

## Answer the questions below

### What data was exfiltrated via DNS?
open pcap with wireshark, and we can see the traffic was sent to this url `43616e64792043616e652053657269616c204e756d6265722038343931.holidaythief.com`
It is in hex, so using `xxd` we can decode it.

Answer: `Candy Cane Serial Number 8491`

### What did Little Timmy want to be for Christmas?
Download http files from wireshark and we can see there are two files.
1st one is `christmaslists.zip` (password protected)
Use `john` to crack password
```
$zip2john christmaslists.zip > hash.hash

ver 1.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdan.tx PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=79, crc=FF67349B
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdark.txt PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=82, crc=5A38B7BB
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistskidyandashu.txt PKZIP Encr: 2b chk, TS_chk, cmplen=108, decmplen=116, crc=BCA00B27
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslisttimmy.txt PKZIP Encr: 2b chk, TS_chk, cmplen=105, decmplen=101, crc=7069EA51
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.

$john hash.hash 

Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 8 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 3 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 3 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
december         (christmaslists.zip)
1g 0:00:00:00 DONE 2/3 (2023-03-25 14:07) 9.090g/s 642527p/s 642527c/s 642527C/s 123456..faithfaith
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

from the timmy's files, we can get answer

Answer: `PenTester`

### What was hidden within the file?
use steghide `steghide --extract -sf TryHackMe.jpg` and you will get the answer

Answer: `rfc527`
