# [Day 24] Elf Stalk

## Description
McDatabaseAdmin has been trying out some new storage technology and came across the ELK stack(consisting of Elastic Search, Kibana and Log Stash). 

The Christmas Monster found this insecurely configured instance and locked McDatabaseAdmin out of it. Can McSkidy help to retrieve the lost data?

While this task does not have supporting material, here is a general approach on how to go about this challenge:

    scan the machine to look for open ports(specific to services running as well)
    as with any database enumeration, check if the database requires authentication. If not, enumerate the database to check the tables and records
    for other open ports, identify misconfigurations or public exploits based on version numbers

The machine may take up to 5 minutes to boot.

----

## Answer the questions below

### Find the password in the database
Answer: `9Qs58Ol3AXkMWLxiEyUyyf`
 
### Read the contents of the /root.txt file
Answer: `someELKfun`
