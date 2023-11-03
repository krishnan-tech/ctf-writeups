# Flaws Cloud
### URl: http://level4-1156739cfb264ced6de514971a4bef68.flaws.cloud/

# Level 4
- For the next level, you need to get access to the web page running on an EC2 at,
- http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/
- It'll be useful to know that a snapshot was made of that EC2 shortly after nginx was setup on it.

# Writeup

- There is a page at `http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/`, but it is giving `401 Authorization Required` in response.

- Using `ping` command we can able to get where it is hosted. In our case it is hosted on `us-west-2`

```
$ ping level4-1156739cfb264ced6de514971a4bef68.flaws.cloud

PING level4-1156739cfb264ced6de514971a4bef68.flaws.cloud (52.92.209.171) 56(84) bytes of data.
64 bytes from s3-website-us-west-2.amazonaws.com (52.92.209.171): icmp_seq=1 ttl=204 time=78.4 ms
...
```


```
$ aws ec2 describe-instances --region us-west-2
{
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-7c803d1c",
                    "InstanceId": "i-05bef8a081f307783",
                    "InstanceType": "t2.micro",
                    "KeyName": "Default",
                    "LaunchTime": "2017-02-12T22:29:24.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-west-2a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-41-84.us-west-2.compute.internal",
                    "PrivateIpAddress": "172.31.41.84",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-35-165-182-7.us-west-2.compute.amazonaws.com",
                    "PublicIpAddress": "35.165.182.7",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-d962aa90",
                    "VpcId": "vpc-1052ce77",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2017-02-12T22:29:25.000Z",
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "vol-04f1c039bc13ea950"
                            }
                        }
                    ],
```

There are so much information here regarding IPs, Volume, architecture and so on. But let's focus more on volume. We can get details about volume using `--filter` flag.

```
$ aws ec2 describe-snapshots --region us-west-2 --max-items 1 --filter "Name=volume-id,Values=vol-04f1c039bc13ea950"
{
    "Snapshots": [
        {
            "Description": "",
            "Encrypted": false,
            "OwnerId": "975426262029",
            "Progress": "100%",
            "SnapshotId": "snap-0b49342abd1bdcb89",
            "StartTime": "2017-02-28T01:35:12.000Z",
            "State": "completed",
            "VolumeId": "vol-04f1c039bc13ea950",
            "VolumeSize": 8,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "flaws backup 2017.02.27"
                }
            ],
            "StorageTier": "standard"
        }
    ]
}
```

As per the level description, the snapshot was created on Feb, 2017. Going dipper with snapshot with `describe-snapshot-attribute`.

```
$ aws ec2 describe-snapshot-attribute --region us-west-2 --snapshot-id snap-0b49342abd1bdcb89 --attribute createVolumePermission
{
    "CreateVolumePermissions": [
        {
            "Group": "all"
        }
    ],
    "SnapshotId": "snap-0b49342abd1bdcb89"
}
```

It says `"Group": "all"` that means, the snapshot is public, anyone can access it!

