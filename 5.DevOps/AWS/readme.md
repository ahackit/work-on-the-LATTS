# AWS - Amazon Web Services

## AWS CLI
```
$ aws configure
AWS Access Key ID [None]: Some Access Key
AWS Secret Access Key [None]: Some Secret Access Key
Default region name [None]: us-west-2
Default output format [None]: json
```

## Amazon Simple Storage Service - S3
- You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
- Amazon S3 stores data as objects within buckets. An object is a file and any optional metadata that describes the file. To store a file in Amazon S3, you upload it to a bucket. When you upload a file as an object, you can set permissions on the object and any metadata.
- Buckets are containers for objects. You can have one or more buckets. You can control access for each bucket, deciding who can create, delete, and list objects in it. You can also choose the geographical Region where Amazon S3 will store the bucket and its contents and view access logs for the bucket and its objects.
- You can use S3 bucket redirects to send from www. to non-www.

### IAM Policy Barebones public
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::sifting-frontend/*"
        }
    ]
}
```

### IAM Policy with CloudFront
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::&&.com/*"
        },
        {
            "Sid": "2",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity &&"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::&&.com/*"
        }
    ]
}
```

## Certicate Manager
- Way to provision certificates
- When creating the cert, make sure you creat in US-East-1 and apply to all your required domains (www and not)

## Route 53
- Used to manage your domains
- When doing domain name transfer, make sure you update your naming servers.
- We use Simple Routes (A) to S3 Buckets OR CloudFront Distro

## CloudFront
- A CDN
- Make sure to specify all the CNAMES of your domain.
- Provide custom SSL Cert (us-east-1)
- Also make sure you set your default root object (typically index.html)

## Elastic Container Service - ECS
- Amazons built in way of deploying and scaling containers outside of the context of K8s.
- You deploy Clusters, which have Services, which have Familys or Tasks that are responsible for deploying your containers.
- Try to reuse names where possible to make your life easier. 
- To have a custom domain on top of this, you will need a ELB to resolve the load balancing requirements for containers

##  Elastic Compute Cloud - EC2
- The instance will be charged per hour with different rates based on the type of the instance chosen. AWS provides multiple instance types for the respective business needs of the user.

