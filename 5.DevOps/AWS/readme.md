# AWS - Amazon Web Services

## Cloud Computing 
### Key Terms
- Cloud Computing: On-demand delivery of IT services from a third-party provider
- Cloud Service: IT Capabaility that is being provided
- Cloud Provider: Company that provides the service
- Consumer: Organization or individual who uses the cloud service
- "Pay as you go" or "pay per use": charged only for what you use
- Multi-tenant: Multiple consumer consume services delivered using shared infastructure
- "x" as a service: Some cloud capability is delivered to consumers as service
  
### Key Characteristics
- On-demand, self service: user can consume cloud resources, as needed, autoamtically, and without human interaction
- Broad network access: capabilities are available over the netwrok using standard mechanisms. Can be the internet or WAN.
- resource Pooling: resources pooled and serve multiple consumers using a multi-tenant model
- rapid elasticity: capabilites can scale "elastically" based on demand
- Measured service: Resource Usage is monitored and metered

### Service Models
- On-Prem:  Gotta manage it all
- IaaS: Gotta manage the VMs
- PaaS: Gotta Manage the App/Data
- SaaS: Don't gotta manage much

### Deployment Models:
- Private Cloud: Enterprise deploys their own infrastructure and applications into their own datacenter
- Public Cloud: IT services that you consume are hosted and delivered from a third-paty and accessed over the internet
- Hybrid Cloud: Combination of on-premises, private cloud, and public cloud services are consumed
- Multicloud: Usage of two or more public clouds at a time and possibly multiple private clouds

### Advantages of Cloud
- Trade capital expense for variable expense: Instead of investing in data centers before you know how you're going to use them, pay only when, and for how much, you consume
- Benefit from massive economies of scale: Achieve a lower variable cost due to AWS Scale
- Stop guessing about capacity: Elimate guessing, scale as demand dictates
- Increase speed and agility: Easily and quickyl scale your usage
- Stop spending money running and maintaing data centers: focus on business growth and innovation instead
- Go global in minutes: Easily dploy applications in multiple regoins around the world

## AWS CLI
```
$ aws configure
AWS Access Key ID [None]: Some Access Key
AWS Secret Access Key [None]: Some Secret Access Key
Default region name [None]: us-west-2
Default output format [None]: json
```

## IAM 
- AWS Identity Managemnt
- Manage resources through use of IAM Policys. Can have users, roles, groups, etc.
- Most IAM roles can be configured with JSON or the policy manager.
- Certain resources need IAM Access

## VPC

### Security Groups
- Groups within a VPC that define inbound/outbound traffic


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
- Provides bare metal instances to deploy and do whatever with.
- The instance will be charged per hour with different rates based on the type of the instance chosen. AWS provides multiple instance types for the respective business needs of the user.

## API Gateway
- Build RESTful or Websocket API services. Endpoints can correspond to AWS Lamda Functions. 
  
##  AWS Lambda 
- Serverless Functions  - lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes.

### Layers
- Use Layers to reduce bundle per lambda sizing

## Cognito
- Managed Auth and OAuth through AWS. Allowing you to make pools of users with Authnetication workflows for accessing resoures without managing IAM accounts per user

## SNS Events
- A pub/sub topic notification system that can send out events to all subscribers and trigger various AWS functions

## SQS 
- A messaging Queue to store messages to be processed in a queue. 

## CloudWatch
- Can be used to manage, monitor and trigger infastructure


