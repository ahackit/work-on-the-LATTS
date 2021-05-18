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
      - [IAM Policy Barebones public](#iam-policy-barebones-public)
      - [IAM Policy with CloudFront](#iam-policy-with-cloudfront)
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
- Improve through game days

#### Pillar One: Operational Excellence
- Perform operation as code
- Annotate Documentation
- Make frequent, small, reversible changes
- Refine operation prodecures frequently
- Anticipate Failure
- Learn from operational failure
  
#### Pillar Two: Security
- Implement a strong identity foundation
- Enable traceability
- Apply security at all levels
- Automate security and best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

#### Pillar Three: Reliability
- Test recovery procedures
- Automatically recover from failure
- Scale horizontally to increase availability
- Stop guessing capacity
- Manage changes in automation
  
#### Pillar Four:  Performance Efficiency
- Democratize advanced Technologies
- go global in minutes
- Use serverless architectures
- Experiment more
- Mechnical sympathy

#### Pillar Five: Cost Optimization
- Adopt a consumption model
- Measure overall efficiency
- Stop spending money on data center operations
- Analyze and attribute expenditure
- Use managed and application-level services to reduce the cost of ownership

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


#### IAM Policy Barebones public
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
#### IAM Policy with CloudFront
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