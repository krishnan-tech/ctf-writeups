# [Day 3] Evil Elf

## Description
An Elf-ministrator, has a network capture file from a computer and needs help to figure out what went on! Are you able to help?

Supporting material for the challenge can be found here! 

----

## Answer the questions below

### Whats the destination IP on packet number 998?
open packet in wireshark and check destination column
Answer: `63.32.89.195`

### What item is on the Christmas list?
Search `telnet` in wireshark and check packets
Check `2255` packet

Answer: `ps4`

### Crack buddy's password!
Search `telnet` in wireshark and check packets
Check `2908` packet

Use hashcat `hashcat -m 1800 hash /usr/share/wordlists/rockyou.txt --force`

Answer: `rainbow`
