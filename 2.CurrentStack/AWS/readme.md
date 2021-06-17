# AWS - Amazon Web Services

- [AWS - Amazon Web Services](#aws---amazon-web-services)
  - [Cloud Computing](#cloud-computing)
    - [Key Terms](#key-terms)
    - [Key Characteristics](#key-characteristics)
    - [Service Models](#service-models)
    - [Deployment Models:](#deployment-models)
    - [Advantages of Cloud](#advantages-of-cloud)
  - [Global Infrastructure](#global-infrastructure)
    - [Global Vs Regional Services](#global-vs-regional-services)
  - [Billing and Pricing](#billing-and-pricing)
    - [Pricing Models](#pricing-models)
    - [Five Pillars of Cost Optimatization](#five-pillars-of-cost-optimatization)
    - [Well-Architected Framework Best Practices for Five Pillars](#well-architected-framework-best-practices-for-five-pillars)
    - [AWS Well-Architected Framework](#aws-well-architected-framework)
      - [Pillar One: Operational Excellence](#pillar-one-operational-excellence)
      - [Pillar Two: Security](#pillar-two-security)
      - [Pillar Three: Reliability](#pillar-three-reliability)
      - [Pillar Four:  Performance Efficiency](#pillar-four--performance-efficiency)
      - [Pillar Five: Cost Optimization](#pillar-five-cost-optimization)
      - [Applying the Framework](#applying-the-framework)
      - [Moden Application Development Tool Kit](#moden-application-development-tool-kit)
      - [Operations, Gamedays, and Incident REsponse](#operations-gamedays-and-incident-response)
      - [Security - Identity](#security---identity)
    - [Reporting and Cost Optimization Tools](#reporting-and-cost-optimization-tools)
  - [AWS CLI](#aws-cli)
  - [Management And Governance](#management-and-governance)
    - [IAM](#iam)
  - [Networking](#networking)
    - [VPC](#vpc)
    - [Security Groups](#security-groups)
  - [Compute](#compute)
  - [Storage](#storage)
    - [Amazon Simple Storage Service - S3](#amazon-simple-storage-service---s3)
      - [Storage Classes/ Tiers](#storage-classes-tiers)
      - [S3 Select](#s3-select)
      - [S3 Permissions](#s3-permissions)
        - [ACLS](#acls)
          - [ACL Permissions](#acl-permissions)
          - [ACL Predefined Groups](#acl-predefined-groups)
        - [Bucket and User Policies](#bucket-and-user-policies)
          - [BUcket Policy Barebones public](#bucket-policy-barebones-public)
          - [Bucket Policy with CloudFront](#bucket-policy-with-cloudfront)
      - [S3 Security](#s3-security)
      - [S3 Monitoring/Logging](#s3-monitoringlogging)
      - [S3 Data Protection](#s3-data-protection)
      - [S3 Life Cycle Management](#s3-life-cycle-management)
      - [S3 Storage Class Analsis](#s3-storage-class-analsis)
      - [S3 Event Notifications](#s3-event-notifications)
      - [S3 Performance Optimization](#s3-performance-optimization)
        - [S3 Performance - CloudFront](#s3-performance---cloudfront)
        - [Optmizing Puts](#optmizing-puts)
        - [Optmizing GETS](#optmizing-gets)
        - [S3 Transfer Acceleration](#s3-transfer-acceleration)
      - [S3 Static Website hosting](#s3-static-website-hosting)
  - [Certicate Manager](#certicate-manager)
  - [CloudFront](#cloudfront)
  - [Elastic Container Service - ECS](#elastic-container-service---ecs)
  - [Elastic Compute Cloud - EC2](#elastic-compute-cloud---ec2)
  - [API Gateway](#api-gateway)
  - [AWS Lambda](#aws-lambda)
    - [Layers](#layers)
  - [Cognito](#cognito)
  - [SNS Events](#sns-events)
  - [SQS](#sqs)
  - [CloudWatch](#cloudwatch)
  - [CloudFormation](#cloudformation)
    - [Terminology](#terminology)
    - [Template Anatomy](#template-anatomy)
    - [Intrinisic Functions Example](#intrinisic-functions-example)
    - [Psuedo Parameters](#psuedo-parameters)
    - [Input Parameters](#input-parameters)
    - [Outputs](#outputs)
    - [Cloudformation Helper Scripts](#cloudformation-helper-scripts)
  - [RDS](#rds)
    - [Terminology](#terminology-1)
    - [Provisioning a Database](#provisioning-a-database)
    - [RDS Pricing](#rds-pricing)
    - [Scaling RDS](#scaling-rds)
    - [Multi-AZ](#multi-az)
    - [Read Replicas](#read-replicas)
    - [Backups](#backups)
    - [Security](#security)
    - [Monitoring RDS](#monitoring-rds)
    - [Amazon Aurora](#amazon-aurora)

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

## Global Infrastructure
- Region: geographical area with 2 or more AZs, isolated from other AWS regions
- Availability Zone(AZ): One or more data centers that are physically separate and isolated from other AZs
- Edge Location: Location with a cache of content that can be delivered at low latency to users - used by CloudFron
- Regional Edge Cache: Part of the CF network, larger caches that sit between AWS services and Edge Locations
- Global Network: Highly available, low-latency private global network interconnectiong every data center, AZ, and AWS Region

### Global Vs Regional Services
- Global:
  - IAM
  - S3
    - Is Global, but data is hosted in specific regions
  - Direct Connect
  - Route 53
  - CloudFront
  - WAF & Shield, Artifact, Trusted Advisor, Personal Health Dashboard

## Billing and Pricing
- Compute: Paying for the amount of time you spend processing (EC2, RDS, ECS, etc)
- Storage: Paying for amount of data you have stored in Amazon (S3, EBS, EFS, etc)
- Outbound Data: Transfers are aggregated accross services and then charged at the outbound data transfer rate

### Pricing Models
- On-Demand: Used for compute and database capacity. No long-term commitments or upfront payments
- Dedicated Instances: Available for EC2 - Hardware is dedicated to a single customer
- Spot Instances: Purchase spare capacity with no commitments. Great discounts from hourly rates
- Reservations: Up to 75% discount in exchange a term commitment. Options for 1 to 3 year terms. No Upfront/Partial Upfront/All upfront
  - EC2, DynamoDB, ElastiCache, RDS, RedShift

### Five Pillars of Cost Optimatization
- Right size your instances
- Increase elasticity
- Choose the right pricing model
- Match storage to usage
- Measure and Monitor

### Well-Architected Framework Best Practices for Five Pillars
- Expenditure Awareness
- Cost-effective resources
- Matcing Supply and Demand
- Optimizing over time

### AWS Well-Architected Framework
- Constists of best practices and ore strategies for architecting systems in the cloud. Helps you design and operate reliable, secure, efficient, and cost-effective systems that will greatly increase your likelihood of success
- Stop guessing capacity needs
- Test systems at production scale
- Automate to make architectural experimatentation easier
- Allow for evolutionary architectures
- Drive architectures using data
- Improve through game days. Practice

#### Pillar One: Operational Excellence
- Principes
  - All operations as code
  - Documentation should always be up to date
    - Annotate documentation
  -  Make frequent, small, reversible changes
  - Refine operation prodecures frequently
  -  Anticipate Failure
  -  Learn from operational failure
-  Prepare 
   -  Prioritze to align with business priorities
   -  What is the business goal
   -  What are the c
-  Operate 
-  Evolve  
  
#### Pillar Two: Security
- Principles
  - Implement a strong identity foundation. Least privelege
  - Enable traceability
  - Apply security at all levels
  - Automate security and best practices
  - Protect data in transit and at rest
  - Keep people away from data
  - Prepare for security events
- Identity & Access
  - Who is allowed to do what? When?
  - Are you apply least privelege
  - Deny root access
  - Reguarly reviewing access
- Detective Controlls
  - Capture and analyze logs
  - Regualarly audit logs
  - Look for unauthorized changes
  - Monitor workload for abnormalities
- Infastrcture Protection
  - Establish trust boundaries
  - Protect network in/out
  - Protect all hosts
  - Configure services to meet security needs
  - Enforece service level protection
- Data Protection
  - How sensitive is the data?
  - Who should have access? When?
  - Encrypt in transit/rest
  - Backup and test backups of the data
- Incident Response
  - Do you hae a plan to tag affected resources
  - Can you adjust permissions to allow for containment
  - Can you redeploy to recover quickly
  - Did you learn from the incident and adjust

#### Pillar Three: Reliability
- Principles
  - Test recovery procedures
  - Automatically recover from failure
  - Scale horizontally to increase availability
  - Stop guessing capacity - reduce idle resources
  - Manage changes in automation
- Understand Default and rquested limits
  - are you planning beyond current limits for a resource?
  - Will you scale past specific resource limits?
  - Can those limits be lifted?
  - Can you plan around those limits?
- Networking
  - IP address space management
  - Subnet structures
  - Resilient toplogies
  - Aility to handle increased traffic
  - Provide consistent performance regardles
- Availability
  - Can users access your application?
  - Deploy without issue
  - Can your pplication withstand partial outages
  
#### Pillar Four:  Performance Efficiency
- Principles
  - let aws do the work whenever possible
  - reduce latency through regions & the aws edge
  - Democratize advanced Technologies
  - go global in minutes
  - Use serverless architectures
  - Experiment more
  - Mechnical sympathy
- Selection
  - What type of compute best suits
  - Which data store is ideal for this workload
  - Does your network design complement compute and data store choices
- Review
  - Is infastrucuted stored as code?
  - Are deployments simple & automated?
  - Can benchmarks be taken automatically?
  - Does load testing interfere with production?
- Monitoring
  - Use active and passive monitoring
  - Understand 5 phases of monitoring
    - Generation
    - Aggregation
    - Real time processing
    - Storage
    - Analytics
  - Create actionable metrics
- Trade-Off
  - Will caching help?
  - Should you partition or shard this workload?
  - Can compression improve performance?
  - Is buffering an option?

#### Pillar Five: Cost Optimization
- Principles
  - Adopt a consumption model
  - Measure overall efficiency
  - Stop spending money on data center operations
  - Analyze and attribute expenditure
  - Use managed and application-level services to reduce the cost of ownership
- Cost Effective REsources
  - Provision to current needs with an eye oo the future
  - Right size to lowest resouce that meta needs
  - Use data to choose your instance
  - Optimize by geography
  - Default to managed service
  - Optimize Data Transfer
- Match Supply & Demand
  - Pay only for what you need
    - Demand Based
    - Buffer-based
    - Time-based
- Awareness of spend
  - Understand yuor stakeholders
  - Implement a governance model
  - Attribute costs to teams/projects
  - Tag AWS resources
  - Track the lifecycle of resources
- Optimize
  - Align utilization with requirements
  - Report and validate findings
  - Elvaute new services for values
  - Continue push to managed services

#### Applying the Framework
- Use resources on demand & reduce idle
- Automate systems enable flexibility
- Test at scale for accuracy
- Remember that architectures must evolve to meet demand
- Gather data to drive data driven decisions
- Use "Game Days" to practice operations and valid architectures
- Questions
  - What are your business priorties?
  - Whats the worst possible scenario?
  - What are your immovable constraints?
  - What data is your solution storing/processing
  - What skills does your team have?
  - What is the timeline of your project?

#### Moden Application Development Tool Kit
- All about tatics
  - Secure
  - Resilient
  - Elastic
  - Modular
  - Automated
  - Interoperable
- Paths to modernization
  - Re-host -- take current from data center to AWS
  - Re-platform -- Take current, but make small modifications
  - Re-factor -- Break up the monolith
  - Re-invent 
- Checklist
  - Build secuirty and compliance into the fabric of your application
  - Microserves by default
  - Serverless is the starting point
  - Everyting is code
  - CI/CD runs application from day one
  - Monitoring, traceability, and observability from day one
- Experiment
- Ideas
- Feedback

#### Operations, Gamedays, and Incident REsponse
- Does the design translate to reality
- Do you know if X is broken
- If x Abreaks, will Y Work?
- A runbook is versioned, tested and the single source of operations
  - Makes operations replicable
  - Reduces errors
  - Cuts down on work
  - Is versioned in Git
  - Starts with a CloudFormation Script
  - Automates everything
- Gamedays
  - Create duplicate environemnts with sumilation data
  - Give teams a chance to react
  - Expect the unexpected
- Incident Response
  - Prepare
  - Identify
  - Contain
  - Eradicate
  - Recover
  - Learn

#### Security - Identity
- 

### Reporting and Cost Optimization Tools
- Right Sizing: Matching instance types and sizes to your demand and workloads, and making sure you have the correct performance and capacity requirements

## AWS CLI
```
$ aws configure
AWS Access Key ID [None]: Some Access Key
AWS Secret Access Key [None]: Some Secret Access Key
Default region name [None]: us-west-2
Default output format [None]: json
```

## Management And Governance
### IAM 
- AWS Identity Managemnt
- Manage resources through use of IAM Policys. Can have users, roles, groups, etc.
- Most IAM roles can be configured with JSON or the policy manager.
- Certain resources need IAM Access
## Networking
### VPC
### Security Groups
- Groups within a VPC that define inbound/outbound traffic
## Compute
## Storage

### Amazon Simple Storage Service - S3
- You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
- Amazon S3 stores data as objects within buckets. An object is a file and any optional metadata that describes the file. To store a file in Amazon S3, you upload it to a bucket. When you upload a file as an object, you can set permissions on the object and any metadata.
- Buckets are containers for objects. You can have one or more buckets. You can control access for each bucket, deciding who can create, delete, and list objects in it. You can also choose the geographical Region where Amazon S3 will store the bucket and its contents and view access logs for the bucket and its objects.
- Can refer to buckets and objects with ARN
- As many items in buckets, but only default 100 buckets
- S3 has universal namespaces, regardless of region, must have unique name
- You can use S3 bucket redirects to send from www. to non-www.
- Objects consist of
  - Key == name of object
  - Value: data being stored (5tb)
  - Version ID: version # assigned when versioning is enabled
  - Bucket + Key + Version ID uniquely identify and object in s3
  - Metadata = Name-value pairs which are used to store info about the object
  - Subresources = Additonal resources specifically assigned to an object
- S3 has flat structure, no folder structures, but directories can be imitated by the use of prefixes
- Use DNS safe naming
- Can tag your objects. Allow for fine grained access control, lifecycle manageemnet, and cloudwatch metrics/logs
  - 10 tags per object
  - Must have unique key
  - Case sensistive
  - Key is 128 unicode characters
  - Value is 256 unicode characters
- S3 Has strong concistency on objects. Bucket operations are eventuall consistent
- S3 does not provide object locking
- S3 is restful web service. Can use HTTP, but often use SDKs/Managemnet Console/CLI
  - GET == Download/Read
  - PUT == Upload/WRite
  - DELETE == Delete
- Charged for
  - Storage
  - Requests
  - Data Transfer Pricing
  - Transfer Acceleration
  - Management Functions -- Optional
    - Monitoring metrics
    - Storage Class analysis
    - S3 Inventory
  - Object Tagging
- use cases:
  - Back up archiving
  - Content Storage and Distribution
  - Static Website Hosting
  - Disaster Recover
  - Big Data/Anayltics

#### Storage Classes/ Tiers
- AWS provides different tiers
  - Depends on use case and access requirement
- When oject is stored, it MUST have storage class associated with it
- If you don't set the storage class, STANDARD Is used
- You can change once object is in S3
- Classes Types
  - Fequently Accessed Objects
    - Standard: Default Storage. Highly Durable, highly available with millisecond access to data
    - REDUCED_REDUNDANCY: Less Durablity. Designed for noncritical, reproducible data
      - Legacy. Not recommended.
  - Infrequently Accessed Objects
    - STANDARD_IA: Highly durable/available, millisecond latency. Minimum billable object size of 128KB and 30 day renetion time. Lower fee than Standard, but charged for retrieval/revival fee
      - Good for recently backed up data
    - ONEZONE_IA: Basically standard, but only in a single AZ. Less available. Lower storage fee.
  - Rarely Accessed Objects
    - Glacier: Highly durable, cheap storage class designed for archive data where portion needs to be retrievable in minutes. Minimum billable time of 90 days. Not available in real-time and must be resotred.
    - Deep-Archive: Glacier but 180 days minimum billable. Restore time is hours
  - Itelligent Tiering:
    - Storage class that automatically moves data between frequent access tiers and infrequent access tiers
      - Days not accessed for 30 days are moved
      - Won't be charged with Revival Fee
      - Must be larger than 128kb to automatically transioned
  - Lifecycle Policies: allow objects to transtion between storage classes
    - Set of rules that S3 applies to a group of objects
    - Transition rules: Define when objects move to another storage class
    - Expiration Rules: Define when objects expire
    - Good when you have defined lifecycles

#### S3 Select
- Allows you to query files from data files instead of Get and then query
- Uses "Query in place"
- Uses subset of SQL
- Supports multiple file formats
  - compressed/non-compressed CSV and JSON.
- Supports encryption
- Supports selective scanning (scan only 100 MB of data)
- Charged on amount of data scanned/retrieved

```
import boto3

s3 = boto3.client('s3')

resp = s3.select_object_content(
    Bucket='s3select-demo',
    Key='sample_data.csv',
    ExpressionType='SQL',
    Expression="SELECT * FROM s3object s where s.\"Name\" = 'Jane'",
    InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
    OutputSerialization = {'CSV': {}},
)

for event in resp['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
        print("Stats details bytesReturned: ")
        print(statsDetails['BytesReturned'])
```

#### S3 Permissions
- By default all s3 resources are private.
- Can grant access by writing a policy.
- Policies can be Resource or User based
  - Resources Policies
      - Acess control lists
        - Grant basic read/write permissions to Accounts and Groups
        - Use an XML Schema
        - Const list of grants identify the grantee and permisionns
      - Bucket Policies
        - Can grant permissions to Accounts and IAM Users
        - Expressed using JSON
        - Can be used to grant fine-grained permissions
        - Most cases replace legacy ACLS
    - User Policies
      - Applied directly to users, groups, or roles using IAM
      - Grant fine-grained permissions
      - Expressed in JSON
      - Cant be used to grant anonymous access
      - Cant be applied to top level user
      - Cross Account Access
        - Grant permission from one account to another account
  - Evaluation of policies
    - If user and bucket all belong to the same AWS account. All policies get evaluated
    - Denys always win
    - In cross-account, user account must first grant access. Then bucket owner must gran them access

##### ACLS
- ACLS assigned to bucket and objects
- Each bucket and object has an ACL attached it it as a sub-resources
- Default ACL grants the resource owner full control over the object
- Can be used to grant permissions to AWS accounts and pre-defined grop

```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>*** Owner-Canonical-User-ID ***</ID>
    <DisplayName>owner-display-name</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xsi:type="Canonical User">
        <ID>*** Owner-Canonical-User-ID ***</ID>
        <DisplayName>display-name</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy> 
```
- Can have up to 100 grants

###### ACL Permissions
- Bucket
  - Read: ALlows grantee to list objects in bucket
  - WRITE: Allows grantee to create, overwrite and delete any objects in the bucket
  - READ_ACP: Allows the grantee to read the bucket ACL
  - WRITE_ACP: Allows the grantee to write the ACL for the bucket
  - FULL_CONTROL
- Object
  - Allows grantee to read the objec and its metadata
  - Not applicable
  - Allows the grantee to read the object ACL
  - Allows the grantee to write the ACL for the object
  - Allows the grantee READ, READ_ACP, WRITE_ACP permissions on the object

###### ACL Predefined Groups
- Replace canonical ID with group URI
- Global AuthenticatedUsers URI
- AllUsers URI
- Log Delivery URI

##### Bucket and User Policies
- Made up of policy elements
  - Principal: Account or user that is allowed to the actions and resources
    - Format:
      - "AWS":"account-ARN"
        - "arn:partition:service:Region:namespace:relative-id"
      - "CanonicalUser:"65-digit-numberical-value"
  - Effect: effect taken when the user requests the action. Either allow or deny
  - Action: The list of permissions
  - Resources: Bucket or object for which the access applies to. Specified as ARNs
    - Format: specified in ARN format
      - "arn:aws:s3:::bucket_name/key_name"
      -  "arn:aws:s3:::bucket_name/*"
      -  "arn:aws:s3:::*"
  - SID: Not required for S3. Generally used as description of the policy statement.
  - User policies don't hae principal (cuz the user is the principal)
  - Buckets " C PEARS, users I " C EARS"
  - Conditions:
    - a condition
    - key/value pair
```
  "Condition": {
    "StringEquals": {
      "s3:x-amz-acl": {
        "public-read"
      }
    }
  }
```

###### BUcket Policy Barebones public
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
###### Bucket Policy with CloudFront
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

#### S3 Security
- Block Public Access
  - Overrides ACLs and Policies
  - Can be bucket or account level or access point level
  - Allows centralised administration of public access
- Options
  - Block public ACLs -- block PUT ACLs
  - Ignore Public ACLs -- Allows puts, but ignore its
  - BlockPublicPolicy -- Blocks any public policies from being PUT
  - RestrictPublicBuckets -- Ignores any public policies
- Pre-Signed URLS
  - Way to give a user temporary access to an object using a signed url. 
  - Usually timed
  - Must be generated by bucket owner
  - Anyone who recieves the pre-signed url can access it.
  - Must be generated programatically.
```
import boto3
s3 = boto3.client("s3")
url = s3.generate_presigned_url(
  "get_object",
  Params={
    "Bucket": bucket_name,
    "Key": key_name
  }
  ExpiresIn=3600,
  HttpMethod="Get"
)
print(url)
```

#### S3 Monitoring/Logging 
- Monitor with CloudWatch
- S3 Metrics
  - Daily Storage Metrics
    - On by Default
    - One reported provided each day
    - No cost
    - Reponrts
      - number of objects
      - size of bucket
    - Retained for 15 months
  - Request/Data Transfer Metrics
    - Optional
    - Available at 1 minute intervals
    - Come at cost (standard cloudwatch billing rates)
    - Reports on all HTTP requests, 
    - 4xx/5xx errors
    - Bytes downloaded/uploaded
    - Latency
    - Enabled at bucket level or all objects
    - Retained for 15 months
- Filtering
  - Bu bucket
  - By storage type
  - By filter ID
    - Prefix
    - Object
    - Tagic
- Metric Delivery
  - Delivered on best effort basis
    - Completelyness and timeliness is not garaunteed
- Access Logging
  - Tracks requests for access to a bucket
    - Records information that is useful for tracking
  - Disabled by default
  - No charge to enable for charged for log ttorage
  - Logs delivered on a best effort basisc
  - Logs are periodically delivered
  - Disabled by default
    - Add logging configuration to the source bucket
    - Specify target bucket where logs should be saved
    - Optionally specify a log prefix
    - Optionally specify additional permissions
      - By default only bucket owner has full permissions
    - Grant write permissions to the S3 Log delivery group on the target bucket 
  - For security audit reasons/ understand AWS bill/ understand nature of your requests
  - Use lifecycle rules to manage old logs
  - Access Logging works at just bucket level
- CloudTrail Logging
  - Providides visibility by tracking the API calls made on your account
  - Enabled when you swtich on CloudTrail
  - Captures Specific API calls made to s3 from your AWS account
    - By default only supported buckete level actions are captured
    - Object level actions can be added by configuring an event slector
    - Ideal for compliance and auditing
    - Does not capture everything, but list is always growing
  - CloudTrail can be integrated with CloudWatch logs
    - Monitor and alert on specific metrics as hhey occur
    - Events: Take a specific acction as events occur

#### S3 Data Protection
- S3 Encryption
  - Refers to proection of data either in ransfer for at rest
- Server Side Encryption
  - S3 encrypts data before writing it to disk and decrypts when data is read from disk
  - SSE-S3 - Server Sidde Encryption S3 Managed Keys
    - Keys managed by s3. No management by uou
    - Each object is encrypted with a unique data key
    - Data key is encrypted by a master key. Rotated automatically/periodacally
    - Encryption is strong (AES-256)
    - Free to Use
  - SSE-KMS - Server-Side Encryption with KMS managed keys
    - Keys managed by KMS
    - You control the keys
      - Creation and use of master keys
      - Creation of data keys
      - Disable & rotate master keys
    - You choose which key the object is encrypted by
    - Data key is encrypted by master key
    - AES-256
    - AWS operators do not have acess to all key
    - KMS is audited by CloudTrail
    - Keys can be reused across other services
    - Charges
  - SSE-C - Server-Side Encryption with CUstomer-Provided Keys
    - Keys are managed by you
    - Symmetric key is uploading along with the data
    - S3 Encrypts the data with the key and then deletes it
    - Too decrypt the data, you must supply the key
    - AES-256
    - If you lose the key, you lose he object
    - Must use HTTPS to upload objects
    - Free to Use
- Client Side Encryption
  - You manage encryption locally, using your own managed keys
  - You manage encryption locally, bu utilise AWS to manage your keys. 
  - Data is encrytped before uploading
- S3 Default Encryption
  - S3 sees un-enrypted file and automatically encrypts it using SSE-S3
  - If it sees encrypted objects, with KMS, it will ignore encryption and send as is.
  - Can be done using SSE-S3 or SSE-KMS
  - You don't have to have encryption bucket policy (in fact you should remove it)
  - Comes at no additional costs
  - Can be monitor using CLoudTrail
    - Monitor bucket level encryption changes
  - Existing objects will remain unencrypted
- S3 Versioning
  - Keep multiple versions of your object in S3.
  - Bucket level operation. 
  - Disabled by default. One enabled, cannot be disabled, only suspended
  - When versioning is enable, each object is given a unique version ID
    - The latest version of the object is current object
  - Raises storages costs
  - Use Versioning with Lifecycle management
  - Wont entirely protect you from switching off versioning or deletes
    - Can use MFA Delete
- S3 Replication
  - Async copy from one bucket to another bucket
    - Good for log aggregation
    - Data sovereignty
    - REplication between AWS accounts
  - Cross- Region Replication (CRR)
    - Compliance
    - Latency
    - Disaster Recovery
  - Enabled by adding replication configuration to a bucket
  - Replicated Objects are exact copies of the original
    - Can change storage class or ownership
  - Objects are replicated over SSL
  - Objects can be replicated to another account
  - Sources must be version enabled
  - S3 must have the permissions, and AWS account must have.
  - Objects that don't get replciated
    - Pre-existing objects
    - Objects that the bucket owner does not have permissions
    - Updates to bucket-level sub-resources
    - Objects encrytped with customer provided Keys
    - Objects encrypted with KMS, unless specified
    - Automatic LIfe Cycle actions
    - Objects that are replicates, created by another replication rules
    - Objects stored in GLACIER or DEEP-ARCHIVE
  - S3 RTC
    - Without RTC, replication is asynchronous
    - Can be enabled to replicate objects within seconds
    - Be monitor RTC metrics
  - Owner Override
    - A replica ACL is a copy of the original
    - Allows you to replace the ACL in transit
    - Grants full access to the desination the bucket owner
    - Set within the replication config
    - Must update permissions to allow
  - Useful when replicating objects toa  bucket in a different account
    - Provides distinct ownership between the original object and the replica

#### S3 Life Cycle Management
- Allows you to automaticaly manage object lifecycle.
- Ideal for objects with a defined lifecycle
- Ability to switch obhects between different storage calsses in order to reduce cost
- Can expire objects automatically after a defined time period
- ENable up to 1000 rules per bucket
- RUles can be applied to the whole bucket of a subset of objects
- Create additional rules on version-enabledbuckets
- Lifecycle rune is defined in XML and stored as a bucket sub-resource
  - JSON in SDKs or UI through Console
- Lifecycle RUles
  - Objects must e stored in standard at least 30 days before transitioning to Standard_IA or ONEZONE_IA
  - Objects must be stored in STANDARD_IA ONEZONE_IA or Intelligent_tiering at least 30 bays before transitioning to Glacier
  - Objects smaller than 128K cannot be transitioned to Standard_IA, Onezone_IA or Intelligent_Tiering
  - Cannot create lifecycle rules on MFA-Enabled BUckets
  - Glacir/DeepArchive
    - Transitioned objects remain in S3 and are NOT accessible via the S3 Glacier SErvice
    - Objects are not available in real time and must be reostred
    - Restored objects are copies of the originaly and are only available for a limited period
    - FOr each stored object, 4kb of extra storage is added in order to hold the object name, index detail and metadata
    -  This increases the storage charge, so bear this in mind when arching large numbers of small files
   -  Rembmer minimum storage charges and the retrieval fee (minimum 90 or 180 days)
-  Version-Enabled Buckets
   -  NonCurrentVersionTransition - transitions the non-current version
   -  NonCUrrentVersionExpieration - expires the non current version
   -  Can specify actions to take on current version or non current
   -  For previous version rules, the action only cccurs after the object becomes non-current and time only starts then as well

#### S3 Storage Class Analsis
- Automatic analysis of your storage classes with recommendations
- Can configure up to 1000 storage class filters
- Can filter by
  - Entire BUcket
  - Prefx
  - Tag
  - Tag & Prefix
- Data is updated daily and visualations are avialable in the S3 COnsole
- Chargeable feature (.10 per million objects analysed)

#### S3 Event Notifications
- Provide the ability to trigger notifications when certain events happen within s3
- enabled by adding a notification configuration to the bucket identify the events to be published and the destionation where the notifications should be sent
- Can send events to
  - SNS
  - SQS
  - Lambdas
- Event Types
  - Object creation
  - Object restoration
  - Object removal
  - Redudeced redundancy storage lost event
- Configure through AWS Console, CLIS, or SDKS
  - By default notifications are off
  - Choose event type you want to notify on
  - Choose the destination for the notification
  - Grant S3 permissions to the use the destination service
  - Create any filter rules

#### S3 Performance Optimization
- Requests per second are by prefix, scale horizontally by using prefixes
- Minimize Latency
  - Place S3 near AWS services or end users
  - Transfer Acceleration
  - Cache Frequenty access Content
    - Use CDN such as CloudFront
    - Use an in-memory cache such as elasticecache
    - Use AWS elemental mediastore to cache video content
  - Implement Retries
    - Exponential backoffs for HTTP 503 errors
- Scale Horizontally
  - Prefixes
  - Parallelise to maximise throughput
    - For Puts: Multi-part upload
    - For GEts: Ranged-based Gets
    - For Lists: Parallelise 
      - Avoid directly querying S3
        - Secondary Indexses
        - S3 Inventory
  
##### S3 Performance - CloudFront
- Global CDN.
- Fetch data from edge location? Data not cached? Go to origin to get it.
- Expires after certain amount of time (24 hours)
- Origin - Location of the origina data is stored. S3 bucket, EC2 Instance, ELB, Route53 endpoint or external system
- Edge Location: Locati:on where content will be cached
- Distribution: Name given to CDN whicch consists of edge locations
- Objects are cached accroding to the TTL
- Objects can be removed from the cache beffore the TTL, but you will be charged
- CloudFront supports both static and dynamic content
- Have web distros (for websites)
- Have RMTP used for media streaming

##### Optmizing Puts
- Parallelize using multi-part upload
  - Breaks files down in many parts and sends it
  - Optimizes network bandwith
- Increases resiliency to network errors
- Provide faster, flexible uploads
- You can pause and resumse your upload
- Choose the right part size
  - 25-50mb on high bandwith, 10mb on mobile
- Too many small parts can increase the connection overhead and overload the network
- Too few parts doesn't ive you the benefits of increase speed or resiliency
- SSL on many parts can leave you CPU bound

##### Optmizing GETS
- Use Cloudfront
- Use Range-based Gets
  - Getting multiple small parts
  - Range HTTP Header, specific range of bytes
  - Maximise network bandwith and improves network performance
- Lists
  - Parallelise lists when you need a sequential list of keys
  - Run multiple list commands each with different search parameters
  - Secondary Indexes
    - When you need to sort by metadata
    - Or timestamp
  - S3 Storage Inventory
    - Provides scheduled inventory of s3 objects and their metadata
    - Runs either daily or weekly
    - Outputs data in CSV format
    - Can decide which metadata


##### S3 Transfer Acceleration
  - Leverages CloudFront globally distrubuted edge locations. Data is routed to your S3 bucket over an optimized network path
  - This is using CloudFront network, not using CloudFront (caching).
  - Larger the file size, the more noticeable imporvement 
  - Additional Charges
  - HAve to use specific s3-accelerate endpoint url. 
  - The endpoint can be used for PUT and GET requests
  - Can still use standard endpoint

#### S3 Static Website hosting
- Can contain static content
- Extremely los cost
- HA
- No need to worry about automatic scaling
- Unlimited Storage
- Configure
  - Enable website hosting
  - Upload content
  - make it publicly accessible
- Changes S3 Website endpoints
- Can use Route53 for custom domains
  - Point the domain root to the s3 bucket
- Can use Bucket and Object redirects
  - Can point a www. bucket to point to non-www bucket
- Returns the index document by default
  - Must have a default one.
  - Can optionally specify error document.
    - You probably want to do this
- Only have GET and HEAD
- CORS
  - Create a CORS configuration on bucket
  - Can have 100 rules on bucket

## Certicate Manager
- Way to provision certificates
- When creating the cert, make sure you creat in US-East-1 and apply to all your required domains (www and not)



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


## CloudFormation
- AWS language to provision resources
- Take YAML and uploads to S3 to be consumed by CloudFormation Orchestrator. 
- Example of provisions EC2 Instance
```
Resources:
  Ec2Instance:
    Type: ' AWS::EC2::Instance'
    Properties:
      InstanceType: t2.micro
      ImageId: ami-467ca739
      UserData:
        !Base64 |
          #!/bin/bash -xe
          yum update -y
          yum install httpd -y
          service httpd start
      Tags:
        Key: Name
        Value: A Simple example
      SecurityGroups:
        - !Ref MySecurityGroup
  MySecurityGroup:
    Type: 'AWS::EC2::SecurityGroup`
    Properties:
      GroupDescription: Enable SSH access
      SecurityGroupIngress:
        - IpProtocal: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
```
- Steps to manually create stack
  - Go to CloudFormation
  - Click Create STack
  - Upload template
  - Give name

### Terminology
- Templates: text input to define resources
- Stack: a single collection of resources is a stack. You create and edit stacks
- Change Set: Can generate a change set to see the changes that will be made by your template to a specific stack

### Template Anatomy
- Description: 
- Metadata: provides additional info about template
- Parameters: allow you to pass values at run time
- Mappings: Set of key/value lookups to provide at run time
- Conditions: Condtionals to determine if resources will be provisioned
- Resources: stack resources
- Outputs: output of stack

### Intrinisic Functions Example
- Join: `!Join[delmiter,[comma-delimited list of values]]`
  - !Join [":", [a, b, c]] = "a:b:c'
- Ref: `!Ref LogicalId`
  - !Ref MySecurityGroup
- FindInMap: `!FindInMap [MapName, TopLevelKey, SecondLevelKey]`
```
Mappings:
  RegionMap:
    us-east-1: 
      AMI: ami-xxxxxx
...
ImageId: !FindInMap 
  - RegionMap
  - !Ref 'AWS::Region'
  - AMI
```

### Psuedo Parameters
- AWS::AcountId : Aws Account
- AWS::NotificationARNS: list of notification Arns
- AWS::StackId - returns id of stack
- AWS::StackName - returns name of the stack
- AWS::Region - returns name of region in wich the resource is being created

### Input Parameters
- String
- Number
- List<Number>
- CommaDelimitedList
- AWs-specific types `AWS::EC2:Image::Id`
- Systems manager parameters types

```
Parameters:
  InstTypeParam:
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - m1.small
      - m1.large
    Description: EC2 Instance Type

Resources:
...
  Instance Type: !Ref InstTypeParam
```

### Outputs 
- Can get output information from a stack, like public IP or DNS
```
Outputs:
  InstanceDns:
    Description: The Instance DNS
  Value:
    !GetAtt
      - EC2Instance
      - PublicDnsName
```

### Cloudformation Helper Scripts
- cfn-init: Reads and interprets Metadata to execute AWS::CloudFormation::Init
- cfn-signal: Used to signal when resources or application is ready
- cfn-get-metadata: used to retrieve metadata based on a key
- cfn-hup: Used to check for updaes to metadata and execute custom hooks

```
Resources:
...
  Metadata:
    AWS::CloudFormation::Init:
      config/Configsets:
        packages:
        groups:
        users:
        sources:
        files:
        commands:
        services:
```

## RDS
- Relatonal Database Service manged by AWS
  
### Terminology
- Database Instance: An isolated DB environment, can have many user created databases within it
- Database Engine: Type of DB to run
- Database Instance Type: Determines type of hardware
- Mutli AZ - Stands for multiple availality zones
- Read Replicas: Separate node to handle only read queries.
- Primary Host - handles all read/writes
- Secondary Host: Doesn't handle writes, acts as failover
- Aurora: MySQL and PostgreSQL compatible Relational DB

### Provisioning a Database
- Database Engine Options
  - Oracle: Enterprise, Standard, Standard Edition One, Standard Edition 2
  - SQL Server: Express, Web, Standard and Enterprise
  - Aurora: MySQL 5.6, MySQL 5.7, PostgreSQL
  - PostgreSQL
  - MySQL
  - MariaDB
- Use Cases:
  - Production
    - Multi-AZ
  - Dev/Test
    - Single AZ
    - 20GB allocated storage
- License Model: BYO License (Only or Oracle)
- Instance Class: Type of hardware
  - t2/t3 family: Burstable instances, 1-8 vCPU, 1-32gb ram, moderate networking performance
  - m3/m4 family: General purpose instances, 2-64 vCPU, 8-256g RAM, High performance networking
  - r3/r4 family: Memory optomized instances, 2-64 vCPU, 16-488GB RAM, High perf. networking
- Multi-AZ:
  - Achieve HA in the case of failure
  - Two database nodes running with replication
  - Primary and stanby in different AZs
- Storage Types/Allocation:
  - General Purpose/GP2: SSD storage, max 16tb, 3IOPS per GB, bursts to 3000IOPS
  - Provisioned IOPS: SSD, 16TB, Max 40k IOPS (20k for sql), I/o intensive workloads
  - Magnetic Storage: 16tb, supported for legacy dbs
- DB Identifier: Identifies DB Instanc,e unique across the region
- Credntials: master user account
- Networking Configuration:
  - VPC - Define virtual networking
  - Subnet Group: Define which subnets and IP ranges the db instance can use in your VPC
  - Public Accessibility: Allocates public IP (seucirty groups must allow inbound traffic)
  - Availability Zone: Any pref for availability zone
  - VPC Security groups: Any pref for availbility zone
- Database Name: name of default DB
- Database port: Port to communicate on 
- Parameter Group: Group of parameters to define config of db
- DB Option Group: Optional functionality on db instance
- Encrypion: Encryption at rest for your DB Instance
- Enhanced Monitoring: Show how different processes or threads use the CPU
- Backups:
  - Retention period: how long to keep abackup
  - Backup window: when the backup occurs
  - Copy tags to snapshots
- Maintenance: 
  - Automatic Minor Version Upgrade
  - Maintenance window: Once a week time range
  - DB Engine Upgrades: REquire downtime
    - Minor Version upgrades: automatic or manually applied
    - Major version upgrades: manually applied
    - Version deprecation - three to six month notification before scheduled upgrades

### RDS Pricing
- Instance Hours
- Database Storage
- Backup Storage: No charge for backup storage up to 100% of total database storage
- Database Transfer: Outgoing traffic only. Regional Data Transfer pricing

### Scaling RDS
- Scale Computer or memory vertically
  - New host is attached to existing volumes
  - In Multi-AZ, Secondary resizes first
- Scale amazon EBS Storage
  - No downtime
- Scale with Read Replicas (horizontal scaling)
  - Only some db engines
  - Helps scale read traffic only
  - No Downtime
- Vertically Scaling
  - Modify RDS Instance
  - Change DB Instance CLass
  - Immediately/During Maintenance Windows
  - Storage and CPU are decoupled
  - Minimal downtime when Mutli-AZ environment
  - Single AZ == Downtime

### Multi-AZ
- Twice the cost of single AZ Config.
- Used for fail-overs. 
- Improves backups cuz using secondary host
- Writes tad slower due to duplicte writes
- Failovers:
  - Application is hosted across two AZs using synchronous data replication
  - If the primary host instance has probs, AWS updates the DNS record to point to the secondary host in AZ2
  - Occurences:
    - When AZ outage occurs
    - When DB Instance fails
    - When DB Instance class changed
    - Software patching
    - Manual Failover (reboots)
    - Not good just for failovers, but planned downtime as well
### Read Replicas
- Read only DB
- Async replication to Read Replica
  - Eventually consistent
  - Querys do not garauntee latest data
  - Replication Lag metric indicates how stale the data could be
- When to use Read Replica:
  - Scaling
  - Source DB Unavailble
  - Reporting or Data Warehouse
  - Disaster Recovery - can promote read recovery
  - Lower Latency:

### Backups
- Automated backups:
  - Stored in hidden S3 buckets of secondary ost.
  - Transaction Logs are stored every 5 minutes
  - Cany copy transaction logs to another region
  - Backup window: when to be taken
  - Retention period: How long backups should be kept
  - Support point in time restore
- Manual Snapshots:
  - kept until you delete them
  - Restore to a saved snapshot
  - Used for checkpoints
- Only store the difference
- Snapshots are incrementals
- Single AZ performance impact: Brief IO Suspension
- Multi-AZ performance impact: taken from the secondary host, should be no impact
- Restoring Backups:

### Security
- Layers of Security: Network Isolation, IAM, Encryption at rest, SSL
  - Network Isolation: Use VPC to place rds instance into private subnet, use security groups for specific traffic, turn off public accessibility, use ClassicLink for non-vpc resources, use direct dconnect to replicate on-prem DBs, and VPC peering to share between VPCs 
  - Access Control: Use IAM to perforamn actions on RDS resources. Use MFA to provide extra level of protection. Dont use master credentials on DB Instance. Use integrated security with AD or IAM Auth
  - Encryption at rest: It's free. AES-256. All nodes are replicated. Encryption performed at volume level. Access to keys are logged. Can encrypt only once. Have two tier encryption
  - SSL Connectivity: SSL is turned on, but must be enforced through Parameter groups

### Monitoring RDS
- Metrics to Watch
  - CPU 
  - Storage Space
  - Network Traffic
  - DB Connections
  - IOPS

### Amazon Aurora
- Cloud-first built RDS instance that abstracts the storage and logging layers away using SOA architecture so they can be indepdently scaled
- Key Concepts
  - Auroa DB CLuster:
    - One or more DB Instances and a cluster volume
    - Primary DB Instance read/write
    - Aurora Replica: Only read replica
  - Auroa DB Connections:
    - Cluster endpoint: only place writes can happen
    - Reader endpoint: read-only connections 
    - Custom endpoint: set of db instances you specify to handle these type of connections
    - instance endpoint: endpoint to a specifc instance
  - Aurora Global DBs:
    - Primary Region -- Read & Write
    - Secondary Region -- Read-Only. Can be promoted
- Aurora Serverless
  - Must connect through VPC endpoints through the Network LOad Balancer. 
  - Allows the managing of connections so they can scale using warm pool of instances
  - No DB Instances. Use ACU, specify min and man, and aurora will scale as needed