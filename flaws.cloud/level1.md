# Flaws Cloud
### URl: http://flaws.cloud/

# Level 1
### This level is *buckets* of fun. See if you can find the first sub-domain.

# Writeup
- as flaws.cloud is a bucket name. So in order to access bucket we have to visit this url: ``<bucket_name>.s3.amazonaws.com``.
- so for us, it is `http://flaws.cloud.s3.amazonaws.com/`
- we can see there is `secret-dd02c7c.html` file.
- on visiting that url: `http://flaws.cloud.s3.amazonaws.com/secret-dd02c7c.html` we can see `Congrats! You found the secret file!`.
- Boom, we have completed level 1.

Next, Level 2: http://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud/

# Extra:
## Vulnerability.
- Directory Listing

## How to stop it?
- setup "bucket policy" - meaning, set permissions of who can assess what in the bucket.
