<!-- vscode-markdown-toc -->
* 1. [Cloud Computing](#CloudComputing)
	* 1.1. [Key Terms](#KeyTerms)
	* 1.2. [Key Characteristics](#KeyCharacteristics)
	* 1.3. [Service Models](#ServiceModels)
	* 1.4. [Deployment Models:](#DeploymentModels:)
	* 1.5. [Advantages of Cloud](#AdvantagesofCloud)
* 2. [Global Infrastructure](#GlobalInfrastructure)
	* 2.1. [Global Vs Regional Services](#GlobalVsRegionalServices)
* 3. [Billing and Pricing](#BillingandPricing)
	* 3.1. [Pricing Models](#PricingModels)
	* 3.2. [Five Pillars of Cost Optimatization](#FivePillarsofCostOptimatization)
* 4. [AWS Well-Architected Framework](#AWSWell-ArchitectedFramework)
	* 4.1. [Well-Architected Framework Best Practices for Five Pillars](#Well-ArchitectedFrameworkBestPracticesforFivePillars)
		* 4.1.1. [Pillar One: Operational Excellence](#PillarOne:OperationalExcellence)
		* 4.1.2. [Pillar Two: Security](#PillarTwo:Security)
		* 4.1.3. [Pillar Three: Reliability](#PillarThree:Reliability)
		* 4.1.4. [Pillar Four:  Performance Efficiency](#PillarFour:PerformanceEfficiency)
		* 4.1.5. [Pillar Five: Cost Optimization](#PillarFive:CostOptimization)
		* 4.1.6. [Putting the framework to work](#Puttingtheframeworktowork)
		* 4.1.7. [Change is constant](#Changeisconstant)
		* 4.1.8. [Well-Architected Reviews](#Well-ArchitectedReviews)
		* 4.1.9. [Well Architected Tool](#WellArchitectedTool)
	* 4.2. [Reporting and Cost Optimization Tools](#ReportingandCostOptimizationTools)
* 5. [AWS CLI](#AWSCLI)
* 6. [Networking](#Networking)
	* 6.1. [Route53](#Route53)
		* 6.1.1. [Routing Policy](#RoutingPolicy)
	* 6.2. [CloudFront](#CloudFront)
	* 6.3. [VPC](#VPC)
		* 6.3.1. [Costs](#Costs)
		* 6.3.2. [Flowlogs](#Flowlogs)
		* 6.3.3. [Subnets](#Subnets)
		* 6.3.4. [Network ACLs](#NetworkACLs)
		* 6.3.5. [Security Groups](#SecurityGroups)
		* 6.3.6. [NAT Instances + Gateway](#NATInstancesGateway)
		* 6.3.7. [Bastion Host](#BastionHost)
		* 6.3.8. [Direct Connect](#DirectConnect)
		* 6.3.9. [VPC Endpoint](#VPCEndpoint)
		* 6.3.10. [PrivateLink](#PrivateLink)
		* 6.3.11. [Transit Gateway](#TransitGateway)
		* 6.3.12. [VPN CloudHub](#VPNCloudHub)
	* 6.4. [AWS Global Accelerator](#AWSGlobalAccelerator)
	* 6.5. [API Gateway](#APIGateway)
* 7. [Security](#Security)
	* 7.1. [IAM](#IAM)
		* 7.1.1. [ARNS](#ARNS)
		* 7.1.2. [Policies](#Policies)
		* 7.1.3. [Roles](#Roles)
	* 7.2. [RAM](#RAM)
	* 7.3. [AWS SSO](#AWSSSO)
	* 7.4. [Key Managmenet Service](#KeyManagmenetService)
	* 7.5. [CloudHSM](#CloudHSM)
	* 7.6. [Systems Manager](#SystemsManager)
		* 7.6.1. [Parameter Store](#ParameterStore)
	* 7.7. [Secrets Manager](#SecretsManager)
	* 7.8. [AWS Shield](#AWSShield)
	* 7.9. [WAF](#WAF)
		* 7.9.1. [Firewall Manager](#FirewallManager)
		* 7.9.2. [CMKs](#CMKs)
	* 7.10. [Certicate Manager](#CerticateManager)
	* 7.11. [Cognito](#Cognito)
		* 7.11.1. [Pools](#Pools)
		* 7.11.2. [Web Identity Federation](#WebIdentityFederation)
* 8. [Management and Governance](#ManagementandGovernance)
	* 8.1. [CloudWatch](#CloudWatch)
	* 8.2. [CloudTrail](#CloudTrail)
	* 8.3. [Organizations](#Organizations)
	* 8.4. [SAM](#SAM)
	* 8.5. [CloudFormation](#CloudFormation)
	* 8.6. [Terminology](#Terminology)
	* 8.7. [Template Anatomy](#TemplateAnatomy)
	* 8.8. [Intrinisic Functions Example](#IntrinisicFunctionsExample)
	* 8.9. [Psuedo Parameters](#PsuedoParameters)
	* 8.10. [Input Parameters](#InputParameters)
	* 8.11. [Outputs](#Outputs)
	* 8.12. [Cloudformation Helper Scripts](#CloudformationHelperScripts)
* 9. [Compute](#Compute)
	* 9.1. [ Elastic Compute Cloud - EC2](#ElasticComputeCloud-EC2)
		* 9.1.1. [Pricing Models](#PricingModels-1)
		* 9.1.2. [Instance Types](#InstanceTypes)
		* 9.1.3. [Nice to Knows](#NicetoKnows)
		* 9.1.4. [Seucirty Groups](#SeucirtyGroups)
		* 9.1.5. [ENI vs ENA vs EFA](#ENIvsENAvsEFA)
		* 9.1.6. [Ways to achieve HPC](#WaystoachieveHPC)
		* 9.1.7. [Spot Instances](#SpotInstances)
		* 9.1.8. [Hibernate](#Hibernate)
		* 9.1.9. [Placement Groups](#PlacementGroups)
		* 9.1.10. [WAF](#WAF-1)
		* 9.1.11. [Load Balancers](#LoadBalancers)
		* 9.1.12. [Auto Scaling](#AutoScaling)
	* 9.2. [Elastic BeanStalk](#ElasticBeanStalk)
	* 9.3. [ AWS Lambda](#AWSLambda)
		* 9.3.1. [Layers](#Layers)
	* 9.4. [Elastic Container Service - ECS](#ElasticContainerService-ECS)
* 10. [Storage](#Storage)
	* 10.1. [AWS DataSync](#AWSDataSync)
	* 10.2. [Storage Gateway](#StorageGateway)
	* 10.3. [EBS](#EBS)
		* 10.3.1. [Types](#Types)
	* 10.4. [Athena/Macie](#AthenaMacie)
	* 10.5. [EFS](#EFS)
	* 10.6. [Amazon FSx](#AmazonFSx)
	* 10.7. [Amazon Simple Storage Service - S3](#AmazonSimpleStorageService-S3)
		* 10.7.1. [Storage Classes/ Tiers](#StorageClassesTiers)
		* 10.7.2. [S3 Select](#S3Select)
		* 10.7.3. [S3 Permissions](#S3Permissions)
		* 10.7.4. [S3 Security](#S3Security)
		* 10.7.5. [S3 Monitoring/Logging](#S3MonitoringLogging)
		* 10.7.6. [S3 Data Protection](#S3DataProtection)
		* 10.7.7. [S3 Life Cycle Management](#S3LifeCycleManagement)
		* 10.7.8. [S3 Storage Class Analsis](#S3StorageClassAnalsis)
		* 10.7.9. [S3 Event Notifications](#S3EventNotifications)
		* 10.7.10. [S3 Performance Optimization](#S3PerformanceOptimization)
		* 10.7.11. [S3 Static Website hosting](#S3StaticWebsitehosting)
* 11. [Database](#Database)
	* 11.1. [RDS](#RDS)
		* 11.1.1. [Terminology](#Terminology-1)
		* 11.1.2. [Provisioning a Database](#ProvisioningaDatabase)
		* 11.1.3. [RDS Pricing](#RDSPricing)
		* 11.1.4. [Scaling RDS](#ScalingRDS)
		* 11.1.5. [Multi-AZ](#Multi-AZ)
		* 11.1.6. [Read Replicas](#ReadReplicas)
		* 11.1.7. [Backups](#Backups)
		* 11.1.8. [Security](#Security-1)
		* 11.1.9. [Monitoring RDS](#MonitoringRDS)
		* 11.1.10. [Amazon Aurora](#AmazonAurora)
	* 11.2. [DynamoDB](#DynamoDB)
		* 11.2.1. [Eventual vs Consistent Reads](#EventualvsConsistentReads)
		* 11.2.2. [DynamoDB Accelerator](#DynamoDBAccelerator)
		* 11.2.3. [Transactions](#Transactions)
		* 11.2.4. [On-Demand Capacity](#On-DemandCapacity)
		* 11.2.5. [Backup + Restore](#BackupRestore)
		* 11.2.6. [Streams](#Streams)
		* 11.2.7. [Global Tables](#GlobalTables)
		* 11.2.8. [Security](#Security-1)
	* 11.3. [RedShift](#RedShift)
	* 11.4. [ElasticCache](#ElasticCache)
	* 11.5. [Database Migration Service](#DatabaseMigrationService)
	* 11.6. [EMR](#EMR)
* 12. [Application Integration](#ApplicationIntegration)
	* 12.1. [SQS](#SQS)
	* 12.2. [Simple Workflow Service](#SimpleWorkflowService)
	* 12.3. [Simple Notification Service](#SimpleNotificationService)
* 13. [Media Services](#MediaServices)
	* 13.1. [Elastic Transcoder](#ElasticTranscoder)
* 14. [Analytics](#Analytics)
	* 14.1. [Kinesis](#Kinesis)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc --># AWS - Amazon Web Services

##  1. <a name='CloudComputing'></a>Cloud Computing 
###  1.1. <a name='KeyTerms'></a>Key Terms
- Cloud Computing: On-demand delivery of IT services from a third-party provider
- Cloud Service: IT Capabaility that is being provided
- Cloud Provider: Company that provides the service
- Consumer: Organization or individual who uses the cloud service
- "Pay as you go" or "pay per use": charged only for what you use
- Multi-tenant: Multiple consumer consume services delivered using shared infastructure
- "x" as a service: Some cloud capability is delivered to consumers as service
  
###  1.2. <a name='KeyCharacteristics'></a>Key Characteristics
- On-demand, self service: user can consume cloud resources, as needed, autoamtically, and without human interaction
- Broad network access: capabilities are available over the netwrok using standard mechanisms. Can be the internet or WAN.
- resource Pooling: resources pooled and serve multiple consumers using a multi-tenant model
- rapid elasticity: capabilites can scale "elastically" based on demand
- Measured service: Resource Usage is monitored and metered

###  1.3. <a name='ServiceModels'></a>Service Models
- On-Prem:  Gotta manage it all
- IaaS: Gotta manage the VMs
- PaaS: Gotta Manage the App/Data
- SaaS: Don't gotta manage much

###  1.4. <a name='DeploymentModels:'></a>Deployment Models:
- Private Cloud: Enterprise deploys their own infrastructure and applications into their own datacenter
- Public Cloud: IT services that you consume are hosted and delivered from a third-paty and accessed over the internet
- Hybrid Cloud: Combination of on-premises, private cloud, and public cloud services are consumed
- Multicloud: Usage of two or more public clouds at a time and possibly multiple private clouds

###  1.5. <a name='AdvantagesofCloud'></a>Advantages of Cloud
- Trade capital expense for variable expense: Instead of investing in data centers before you know how you're going to use them, pay only when, and for how much, you consume
- Benefit from massive economies of scale: Achieve a lower variable cost due to AWS Scale
- Stop guessing about capacity: Elimate guessing, scale as demand dictates
- Increase speed and agility: Easily and quickyl scale your usage
- Stop spending money running and maintaing data centers: focus on business growth and innovation instead
- Go global in minutes: Easily dploy applications in multiple regoins around the world

##  2. <a name='GlobalInfrastructure'></a>Global Infrastructure
- Region: geographical area with 2 or more AZs, isolated from other AWS regions
- Availability Zone(AZ): One or more data centers that are physically separate and isolated from other AZs
- Edge Location: Location with a cache of content that can be delivered at low latency to users - used by CloudFront
- Regional Edge Cache: Part of the CF network, larger caches that sit between AWS services and Edge Locations
- Global Network: Highly available, low-latency private global network interconnectiong every data center, AZ, and AWS Region

###  2.1. <a name='GlobalVsRegionalServices'></a>Global Vs Regional Services
- Global:
  - IAM
  - S3
    - Is Global, but data is hosted in specific regions
  - Direct Connect
  - Route 53
  - CloudFront
  - WAF & Shield, Artifact, Trusted Advisor, Personal Health Dashboard

##  3. <a name='BillingandPricing'></a>Billing and Pricing
- Compute: Paying for the amount of time you spend processing (EC2, RDS, ECS, etc)
- Storage: Paying for amount of data you have stored in Amazon (S3, EBS, EFS, etc)
- Outbound Data: Transfers are aggregated accross services and then charged at the outbound data transfer rate

###  3.1. <a name='PricingModels'></a>Pricing Models
- On-Demand: Used for compute and database capacity. No long-term commitments or upfront payments
- Dedicated Instances: Available for EC2 - Hardware is dedicated to a single customer
- Spot Instances: Purchase spare capacity with no commitments. Great discounts from hourly rates
- Reservations: Up to 75% discount in exchange a term commitment. Options for 1 to 3 year terms. No Upfront/Partial Upfront/All upfront
  - EC2, DynamoDB, ElastiCache, RDS, RedShift

###  3.2. <a name='FivePillarsofCostOptimatization'></a>Five Pillars of Cost Optimatization
- Right size your instances
- Increase elasticity
- Choose the right pricing model
- Match storage to usage
- Measure and Monitor

##  4. <a name='AWSWell-ArchitectedFramework'></a>AWS Well-Architected Framework
- Constists of best practices and ore strategies for architecting systems in the cloud. Helps you design and operate reliable, secure, efficient, and cost-effective systems that will greatly increase your likelihood of success
- Stop guessing capacity needs
- Test systems at production scale
- Automate to make architectural experimatentation easier
- Allow for evolutionary architectures
- Drive architectures using data
- Improve through game days. Practice

###  4.1. <a name='Well-ArchitectedFrameworkBestPracticesforFivePillars'></a>Well-Architected Framework Best Practices for Five Pillars
- Expenditure Awareness
- Cost-effective resources
- Matcing Supply and Demand
- Optimizing over time

####  4.1.1. <a name='PillarOne:OperationalExcellence'></a>Pillar One: Operational Excellence
- Principles
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
-  Operate 
-  Evolve  
  
####  4.1.2. <a name='PillarTwo:Security'></a>Pillar Two: Security
- Principles
  - Implement a strong identity foundation. Least privilege access
  - Enable traceability
  - Apply security at all levels
  - Automate security and best practices
  - Protect data in transit and at rest
  - Keep people away from data
  - Prepare for security events
- Identity & Access
  - Who is allowed to do what? When?
  - Are you applying least privelege
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

####  4.1.3. <a name='PillarThree:Reliability'></a>Pillar Three: Reliability
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
  
####  4.1.4. <a name='PillarFour:PerformanceEfficiency'></a>Pillar Four:  Performance Efficiency
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

####  4.1.5. <a name='PillarFive:CostOptimization'></a>Pillar Five: Cost Optimization
- Principles
  - Adopt a consumption model
  - Measure overall efficiency
  - Stop spending money on data center operations
  - Analyze and attribute expenditure
  - Use managed and application-level services to reduce the cost of ownership
- Cost Effective Resources
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

####  4.1.6. <a name='Puttingtheframeworktowork'></a>Putting the framework to work
##### Applying the Framework
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

##### Modern Application Development Tool Kit
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
  - Build security and compliance into the fabric of your application
  - Microserves by default
  - Serverless is the starting point
  - Everything is code
  - CI/CD runs application from day one
  - Monitoring, traceability, and observability from day one
- Innovation Flywheel
  - Experiment
  - Ideas
  - Feedback

##### Operations, Gamedays, and Incident Response
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

##### Security - Identity
- Only allow who should be allowed.
- Assume roles when needed

##### Security - Encryption
- Don't roll your own encryption
- Defend against network attacks
  - Use SSL/TLS
  - Aim for end-to-end encryption
  - Use a VPN to connect to on-prem resources

####  4.1.7. <a name='Changeisconstant'></a>Change is constant
- There is no perfect fit. Always trade-offs. 
- Reduce risk by making smaller choices more often. Experiment often.

##### Evaluating New Services
- Always something new
- Resist the tempation to ALWAYS use the latest and greatest
- "Is this a managed service of something already in your techstack?"
- "Does the current state of service fit your need?"
- "What is the level of effort required to refactor to support this new service?" 

##### High Performance Computing Lens
- Dynamic architecture and procurement
- Automate everything
- Enable collaboration via data sharing and architectural choices
- HTC: High Throughput Computing
  - Loosely coupled
  - Highly iterative
  - Many instances all attempting to solve the same problem the most efficiently
  - Designs:
    - Batch
    - Queue
    - Traditional
    - Serverless
- HPC: High Performance Computing
  - Tightly Coupled
  - More sequential
  - One big problem that requires a lot of processing
  - System is reliant on node stability & use regular checkpoints
  - High performance, shared storage is often a requirement
  - Deisgns:
    - Persistent cluster
    - Ephemeral Cluster
    - Microservices Cluster

##### Serverless Application Lens
- Freedom to focus on business value
- Applications built using a collection of abstracted or managed services
- Design
  - Event Driven
  - Speedy, simple, singular
  - Concurrency
  - Share nothing
  - Use state machines to organize work
  - Design for failures/duplicates
- Services
  - Compute:
    - Lambda, Gateway, Step Functions
  - Data Layer
    - S3, Dynamo, ElasticSearch Service, AppSync
  - Message/Streaming
    - SNS, Kinesis, Kinesis Data Firehose
  - Identity/user management 
    - Cognito
  - Edge
    - CloudFront, Lambda@Edge
  - Monitoring/Deployment
    - CloudWatch, XRay, SAM
- Deployment Principles
  - All at once
  - Blue/green
  - Canary
- Distributed services complicate monitoring
- Measuring performance against business KPIs is key
- Simplkified service design eases monitoring efforts and is worth the trade off

##### IOT Application Lens
- 
- Design Workflow
  - Decouple from the real world
  - Offline happens, plan for it
  - Learn data at the edge, enrich at the world
  - Devices need to heartbeat
- Edge Services
  - FreeRTOS, GreenGrass
- Provisioning Services
  - Cert Manager, JIT registration
- Communication Services
  - IoT Core, IoT Device registry, IoT Device Shadow, API Gateway
- Ingestion Services
  - IoT Rules Engine, Kinesis, SQS
- Analytics Services
  - S3, IoT Analytics, Athena, SageMaker
- App Services
  - IoT Device Defender, IoT Device Management, DynamoDB, Aurora, Lambda
- Over the air-updates are practical
- Test on physical devices as well as virtual
- Offline and reducecommunications will happen, plan for it
- Provision is a hard problem
- Physical security of devices is a constant risk & challenge
- Simulate behavoir at scale
- Buffer message delivery
- Design for failure
- Managed services for focus
- Event Driven Designs

####  4.1.8. <a name='Well-ArchitectedReviews'></a>Well-Architected Reviews
- Lower or mitigate risks by understanding risks as you build or optimize your current architectures
- Scale up and down as required
- Automated Systems to ensure consistency and reliability
- Test using an acurrate replica of production on-demand
- Adapt as needed to meet new challenges
- Drive decisions through data
- Practice, practice, practice
- Does your current design adhere to these principles?
- Are your pillars appropriately balanced?
- Which areas can be imrpvoed without upsetting the balanced
- Experienced professionals can perform 3rd party reviews
- Fast, self-service review and report
- Always check your work
- Each best practice is always changing


####  4.1.9. <a name='WellArchitectedTool'></a>Well Architected Tool
- Generates fast, self service reviews
- Question and answer format
- Video explanations for each best practice
- Milestones to mark progress and development
- Medium and high risk issues identified
- PDF report is the end deliverable
- Imrpovement plans provide a roadmap for teams


###  4.2. <a name='ReportingandCostOptimizationTools'></a>Reporting and Cost Optimization Tools
- Right Sizing: Matching instance types and sizes to your demand and workloads, and making sure you have the correct performance and capacity requirements

##  5. <a name='AWSCLI'></a>AWS CLI
```
$ aws configure
AWS Access Key ID [None]: Some Access Key
AWS Secret Access Key [None]: Some Secret Access Key
Default region name [None]: us-west-2
Default output format [None]: json
```

##  6. <a name='Networking'></a>Networking 

###  6.1. <a name='Route53'></a>Route53
- DNS: Converts human friendly name to public ip address
- TopLevel Domain: .com/.edu/etc
  - Second level Domain .co.uk == .co
- A Record: Address. Translate domain name to IP
- TTL: Time to Live. Lower time, faster change to DNS
- CName: Canonical Name - can be used to resolve one domain name to another
- Alias Records: map resource record sets in your host zone to ELBs, CF Distros, or S3 Buckets
  - basically like a CNAME, but CNAME cant be used for naked domain name
- MX Recoerds for mail
- PTR reverse A record
- Can buy domain names from AWS
  - Can take 3 days to register

####  6.1.1. <a name='RoutingPolicy'></a>Routing Policy
- Simple
  - Only have one record with multiple ip addresses. Route 53 returns random to user
- Weighted
  - Split traffic by weighted %s
- Latency
  - Route traffic based lowest network latency
- Failover
  - using health check, will route to DR resources
- GeoLocation
  - Route based on users location.
- GeoProxmity 
  - Use Traffic Policies to handle user location and resource location
- MultiValue
  - Basically Simple, but only returns healthy resources

###  6.2. <a name='CloudFront'></a>CloudFront
- A CDN
- Has many edge locations where content will be cached
- The Origin is of all the files that the CDN willl distribute. 
  - Can be S3 Bucket, EC2 Instance, ELB, or Route53
- Distirubtion - name given to group of edge locations
- Can have Web or RTMP CDN
- Cached for the TTL, can invalidate it, but will be charged
- Make sure to specify all the CNAMES of your domain.
- Provide custom SSL Cert (us-east-1)
- Also make sure you set your default root object (typically index.html)
- Use signed URLs/cookies when you want to securet content
  - Signed url is for individual files
  - Signed cookie is for multiple files
  - If origin is EC2, use cloudfront

###  6.3. <a name='VPC'></a>VPC
- A virtual isolated network for you to control all things
- Can create hardware VPN into your VPC to leverage dual envrionment
- All exists in a region
  - Connect to Internet Gateway or Virtual Private Gateway
  - Go to Route Table
  - Go through Network ACL
  - Go through Security Group
  - Go to Public Subnet
  - Use as jumphost or bastion to Private Subnet
- All come with default vpc
  - Subnets in default have a route out to internet
  - Each EC2 instance has both public and private address
- Create custom starts with
  - Default route table
  - Network ACL
  - Default Security group

####  6.3.1. <a name='Costs'></a>Costs
- Free traffic in through internet is free
- Connection from AZ 1 to 2 private costs
- Connection from AZ 1 to 2 through public costs double

####  6.3.2. <a name='Flowlogs'></a>Flowlogs
- Feature that enables you capture info about the IP traffic. 
- Stored in CloudWatch Logs
- 3 Levels
  - VPC
  - Subnet
  - Network Interface level
- Can be tagged
- Only VPCs in your account, not peered
- Cannot change Flow LOgs after creation

####  6.3.3. <a name='Subnets'></a>Subnets
- Subnets = 1 AZ not multiple AZs
- Amazon reserves 5 Ips
- Private
  - 10.0.0.0 - 10.255.255.255 (10/8 prefix)
  - 17.16.0.0 - 172.31.255.255 (172.16/12)
  - 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
- Largest subnet you can have is /16 smallest is /28

####  6.3.4. <a name='NetworkACLs'></a>Network ACLs
- Comes with default on VPC
- Custom ones deny all by default
- Every subnet must be associated with a NACL
- Can block IP addresses using NACL, not SG
- One NACL to many Subnets

####  6.3.5. <a name='SecurityGroups'></a>Security Groups
- Groups within a VPC that define inbound/outbound traffic

####  6.3.6. <a name='NATInstancesGateway'></a>NAT Instances + Gateway
- Instance = Single EC2 Instance
  - Choose community NAT AMI
  - If private wants to go out to network, must go through NAT through Route 
  - Must be in public Instance
- Gateway = HA Network Gateway
  - Create NAT Gateway with new Elastic IP
  - Change Route to point to NAT Gateway

####  6.3.7. <a name='BastionHost'></a>Bastion Host
- Used to securily  administer EC2 Instances in private subnets
- Cannot use NAT Gateway as Bastion Host
- HA
  - Two hosts in separate AZ. Use a network LB with static ip and health checks to fail over
  - One host in one AZ behind and auto scaling group with health checks and a EIP.
  - Must be layer 4

####  6.3.8. <a name='DirectConnect'></a>Direct Connect
- Creates direct link from On-prem networks to AWS networks
- Useful for high throoughput workloads
- Need stable + reliable connection
- Steps:
  - Create virtual interface  in Direct Connect Console. This is public
  - Go to VPC Console->VPN Connections. Create custmer gateway
  - Create Virtual Private Gateway
  - Attach virtual private gateway to desired vpc
  - Select VPN Connection and create new VPN connection
  - Slect virtual private  and customer gateway
  - Once VPN is available  - set up vpn on the customer gateway or firewall

####  6.3.9. <a name='VPCEndpoint'></a>VPC Endpoint
- VPC to VPC interconnection.
- Stays in AWS
- Attach ENI to EC2 instance and it can traverse AWS
- Interface/Gateway
- Gateway only supports S3/Dynamo

####  6.3.10. <a name='PrivateLink'></a>PrivateLink
- Requires network load balancer on service VPC an ENI on customer VPC
- Avoid peering to 10000 vpcs or exposing yourself to public
- Easier to expose just a single API endpoint

####  6.3.11. <a name='TransitGateway'></a>Transit Gateway
- Simplifies Network Topology
- Allows transitive peering
- Works on hub-and-spoke model
- Works on regional basis, but can be across multiple regions
- Can be used across multiple AWS accounts
- Limit communication through Route Tables
- Good for when you have many VPCs

####  6.3.12. <a name='VPNCloudHub'></a>VPN CloudHub
- Connect multiple VPN sites together
- Hub-and-Spoke Model
- Public, but encrypted

###  6.4. <a name='AWSGlobalAccelerator'></a>AWS Global Accelerator
- Avoid ISP Jumping and use Edge locations to go over Amazon backbone directly to service
- Provides two static IP or you can bring your own

###  6.5. <a name='APIGateway'></a>API Gateway
- Build RESTful or Websocket API services. 
- Endpoints can correspond to AWS Lamda Functions. 
- Scale effortlessly
- Low cost
- Track an dcontorl usage by api key
- Throttle requests
- Connect to CloudWatch for Logs
- Supports multiple stages
- Setup
  - Define API
  - Define resoures/nested resources (url paths)
    - Select HTTP Method
    - Set security  
    - Choose Targets
- Support SSL with Cert Manager
- Supports Caching, caches by TTL
- Can turn on CORS 
##  7. <a name='Security'></a>Security
###  7.1. <a name='IAM'></a>IAM 
- AWS Identity Managemnt
- IAM is universal
- Manage resources through use of IAM Policys. Can have users, roles, groups, etc.
- Most IAM roles can be configured with JSON or the policy manager.
- Certain resources need IAM Access
- Users start with NO permissions
- Users are assigned Access Key ID & Secret Access Keys
- Always set up MFA
####  7.1.1. <a name='ARNS'></a>ARNS
- ARNS always arn:partition:service:region:account_id:
  - partition: aws-awscn
  - service:s3|ec2
  - region: us-east-1
  - account_id: 12312412
  - End with
    - resource
    - resource_type/resource
  - Double :: = omitted values
    - iam example: arn:aws:iam::12312:user/mark
####  7.1.2. <a name='Policies'></a>Policies
- Explicity deny > everything else
- JSON document that defines permissions
- identity policy
-  Resource Policy
- No effect until patched
- List of statements
```
{
  "version":"2012-10-17",
  "Statement": [
    {...}
  ]
}
```
- Statement example
```
{
  "Sid": "SpecificTable",
  "Effect": "Allow|Deny",
  Action": [
  "service:Action"
  ...],
  "Resource": "arn"
}
```

####  7.1.3. <a name='Roles'></a>Roles
- Assign permissions to roles and assign them to resources to avoid adding user credentials to resources

###  7.2. <a name='RAM'></a>RAM
- Resource Access Manager  allows resource sharing between accounts
- Cant share all resources

###  7.3. <a name='AWSSSO'></a>AWS SSO
- Can connect to  Business applications or anyone that supports SAML 2 like AD
- Can grant access to Organizations

###  7.4. <a name='KeyManagmenetService'></a>Key Managmenet Service
- Regiona Secure Key management System
- Manage customer master keys
- Must wait 7 days before deleting key
- Inegrated with most services
- 4kb in size
- Pay per API call
- Audit capability using KMS
- FIPS 140-2 Level 2
- Level 3 is CloudHSM

###  7.5. <a name='CloudHSM'></a>CloudHSM
- Dedicated hardware security model
- FIPS 140-2 Level 3
- Manage your own keys
- No access to aws-managed component
- Runs within a VPC in your account
- Single tenant, dedicated hardware, multi-az cluster
- Only industry-standard APIS, no AWS APIs 
- Supports
  - PKCS#11
  - Java Cryptography Extensions
  - Microsoft CryptoNG
- Keep your keys save, irretrievable if lost

###  7.6. <a name='SystemsManager'></a>Systems Manager 
####  7.6.1. <a name='ParameterStore'></a>Parameter Store
- Serverless storage for config and secrets
  - Password
  - DB Connection Strings
  - License Codes
  - API Keys
- Values can be encrypted or plain text
- Separate data from source control
- Store parameters in heirarchies
  - Can provide access by path security
- Track versions
- Set TTL to expire certain passwords

###  7.7. <a name='SecretsManager'></a>Secrets Manager
- Basically Parameter Store but costs
- Nice feature is be able to rotate secrets and applay the new secrets
- Can generate random secrets

###  7.8. <a name='AWSShield'></a>AWS Shield
- Protects against DDoS attacks
- Standard
  - Enabled for all customers at no cost
  - Protects against common Layer 3 and 4 attacks
    - SYN/UDP floods
    - Reflection Attacks
- Advanced
  - 3000 per month, per org
  - Ehanced protection for EC2, ELB, CloudFront, Global Accelerator, Route 53
  - Get 24/7 access to DDoS support team
  - DDoS Cost Protection

###  7.9. <a name='WAF'></a>WAF
- Lets you monitor HTTP(S) requests to 
  - CloudFront
  - ALB
  - API Gateway
- Control access to content
- Control via Filtering Rules
  - IP Addresses
  - Query Parameters
  - SQL Query Injection Attacks
- Blocked traffic returns 403
- Behaviros
  - Allow all requests
  - Block all requests
  - Count the requests you specify
- Reuqesting properties
  - Orgiinating IP Address
  - Orgiinatin Country
  - Request Size
  - Values in Request Headers
  - Strings in request based on RegEx
  - SQL Code Injection
  - XSS
####  7.9.1. <a name='FirewallManager'></a>Firewall Manager
- Manager WAF rules for an AWS organization


####  7.9.2. <a name='CMKs'></a>CMKs
- AWS managed CMK: Free, used by default if you pick encryption in most services
- AWS Owned CMK: Used by AWS on a shared basis across many accounts. Typically wont see these
- Customer Manage CMK: Allows key rotation. controlled via key policies and can be enabled/disabled
- Symmetric
  - Same key used for encryption and decyption
  - AES-256
  - Never leaves WAS Unencrypted
  - AWS services integrated with KMS use symettric KMS
  - Encryp, decrypt, and re-encrypt data
  - Generate date keys, data key pairs, and random byte strings
- Aysmeetric
  - Math related public/private key pair
  - RSA and elliptic-curve cryptography
  - Private key never leaves AWS unencrypted
  - Must call KMS API to use private key
  - download public key and use outside of AWS
  - Used by outside users of AWS who cant access KMS
  - AWS services dont use asymettric

###  7.10. <a name='CerticateManager'></a>Certicate Manager
- Way to provision certificates
- When creating the cert, make sure you creat in US-East-1 and apply to all your required domains (www and not)

###  7.11. <a name='Cognito'></a>Cognito
- Managed Auth and OAuth through AWS. Allowing you to make pools of users with Authnetication workflows for accessing resoures without managing IAM accounts per user
- Acts as identity broker between your aplpication and Web ID providers
- Synchronizes user data for multiple devices  
####  7.11.1. <a name='Pools'></a>Pools
- User Pools: user directories used to manage sign-up and sign-in functionality for mobile and web applications
- Identity pools: provide temp access to aws credentials for service access 
####  7.11.2. <a name='WebIdentityFederation'></a>Web Identity Federation
- Give access to resources after authneticating through web-based identity provider like Facebook/Google/etc. Trade ID for temporary AWS credentials

##  8. <a name='ManagementandGovernance'></a>Management and Governance
###  8.1. <a name='CloudWatch'></a>CloudWatch
- Can be used to manage, monitor and trigger infastructure
- Can monitor Host level metrics
  - DIsk
  - CPU
  - Network
  - Status Check
- 5 minute logs by default, but can go to 1 minute for EC2
- Can create alarms with CloudWatch trigger notifications

###  8.2. <a name='CloudTrail'></a>CloudTrail
- Records all AWS API calls 
- Tracks user activity in your AWS platform
- Logs to S3
- Can use S3 log file validation to make sure no tampering

###  8.3. <a name='Organizations'></a>Organizations
- Allow you to create organizations to consolidate billing across many accounts
- Paying account should be used for billing purposes only
- Use Service Control Policies either on Organization or on individual acccounts

###  8.4. <a name='SAM'></a>SAM
- Open Source CloudFormation Extension optimized for serverless apps
- New Types: Functions, APIs, Tables
- Supports anything CloudFormation supports
- Run serverless app localy
- Package and Deploy using CodeDeploy

###  8.5. <a name='CloudFormation'></a>CloudFormation
- AWS language to provision resources
- Take YAML and uploads to S3 to be consumed by CloudFormation Orchestrator. 
- Resource is required for template
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

###  8.6. <a name='Terminology'></a>Terminology
- Templates: text input to define resources
- Stack: a single collection of resources is a stack. You create and edit stacks
- Change Set: Can generate a change set to see the changes that will be made by your template to a specific stack

###  8.7. <a name='TemplateAnatomy'></a>Template Anatomy
- Description: 
- Metadata: provides additional info about template
- Parameters: allow you to pass values at run time
- Mappings: Set of key/value lookups to provide at run time
- Conditions: Condtionals to determine if resources will be provisioned
- Resources: stack resources
- Outputs: output of stack

###  8.8. <a name='IntrinisicFunctionsExample'></a>Intrinisic Functions Example
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

###  8.9. <a name='PsuedoParameters'></a>Psuedo Parameters
- AWS::AcountId : Aws Account
- AWS::NotificationARNS: list of notification Arns
- AWS::StackId - returns id of stack
- AWS::StackName - returns name of the stack
- AWS::Region - returns name of region in wich the resource is being created

###  8.10. <a name='InputParameters'></a>Input Parameters
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

###  8.11. <a name='Outputs'></a>Outputs 
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

###  8.12. <a name='CloudformationHelperScripts'></a>Cloudformation Helper Scripts
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


##  9. <a name='Compute'></a>Compute

###  9.1. <a name='ElasticComputeCloud-EC2'></a> Elastic Compute Cloud - EC2
- Provides bare metal instances to deploy and do whatever with.

####  9.1.1. <a name='PricingModels-1'></a>Pricing Models
  - All variable based on instance type
  - On Demand: Pay a fixed rate by the hour with no commitment
  - Reserved:  Proivdes with ccapacity resveration and offer a significant discount on the hourtly charge for instance. 1-3 year terms
  - Spot: Enables you to bid wahtever price you want for instance capacity, provider for even greater savings if you have applications have flexible start and end times
  - Dedicated Hosts: Phyiscal Ec2 server dedicated for your use

####  9.1.2. <a name='InstanceTypes'></a>Instance Types
- F1: Field Programmable Gate Array -- Genomics research, financial analytics, real time video processing, big data, etc
- I3: High Speed Storage: NoSQL, DBs, Datwarehousing
- G3: Graphics Intensive: Video Encoding/3D App Streaming
- H1: High Disk Throughput: MapReduced-based workloads, distrubuted file systems such as HDFS and MapR-FS,
- T3: Lowest Cost, General Purpose: Web Servers/Small DBS
- D2: Dense Storage: FileServers, Datawarehousing, Hadoop
- R5: Memory Optimized: Memory intensive Apps/DBs
- M5: General Purpose: Application Servers
- C5: Compute Optomized: CPU Intensive Apps/DBs
- P3: Graphics/ General Purpose GPU: Machine Learning, Bit Coin Mining, etc
- X1: Memory optimized: SAP Hana/ApacheSpark
- Z1D: High compute capacity and a high memory footprint: Ideal for eletronic design automation and certain RDB workloads with high-per core licensing
- A1: Arm-Based workloads: Scale-out workloads such as web servers
- U6tb1: Bare Metal - Eliminate virtualization overhead
- FIGHTDRMCPXZAU

####  9.1.3. <a name='NicetoKnows'></a>Nice to Knows
- AMI:The type of OS you want on the EC2 Instance
  - Can pick AMI based on EBS Volume or Instance Store
    - Instance store is created from a template store in S3
      - Cant add more after creation. Ephemeral storage as well
    - EBS Volume: Created from EBS Snapshot
- Termination Protection is turned off by default, you must turn it on
- On EBS-baked instance, default action is for the root EBS volume to be deleted - but rest of EBS volumes wont delete
- EBS Root volumes of your default AMI CAN be encrypted

####  9.1.4. <a name='SeucirtyGroups'></a>Seucirty Groups
- All Inbound traffic is blocked by default
- all outbound traffic is allowed
- Changes to security Groups take effect immediately
- Any number of ec2 instances within security group
- Can have multiple security groups attached to ec2 instance
- Security groups can be stateful
- Inbound traffic is allowed out
- Cannot block specific network IP, need to use Network ACLss

####  9.1.5. <a name='ENIvsENAvsEFA'></a>ENI vs ENA vs EFA
- ENI: Elastic network interface: essentially a virtual network card
  - Good for managemnet network
  - use network and security appliances in your vpc
  - creates dual-homed instances with workload/roles on subnets
  - create a low-budget, HA solution
  - Allows primary IPv4
  - Allows one or more second IPv4
- EN: Enhanced networking: Uses single root i/o virtualization  (SR-IOV) to provide high performance  networking capabilities on supported instance types
  - No additonal charge, use where you want good performance. EC2 must support it
  - Enable using ENA
- EFA: Elastic Fabric Adapter: Network device that you can attach to your Amazon EC2 instance to accelerate high performance computing and ML apps

####  9.1.6. <a name='WaystoachieveHPC'></a>Ways to achieve HPC
- Data Transfer
  - Snowball
  - DataSync
  - Direct Connect
- Compute/Networking
  - EC2 Instances that are GPU or CPU Optimized
  - EC2 Fleets
  - Placement Groups (cluster)
  - Enhanced Networking
  - ELastic Network Adapters or Intel VFß
  - Elastic Fabric Adapters
- Storage
  - EBS
  - Instance Store
  - Network
    - Amason S3
    - EFS
    - Luxre
- Orchestration
  - AWS Batch
  - AWS ParalleleClusterß
    - Simple text file to model and provision all the resources needed

####  9.1.7. <a name='SpotInstances'></a>Spot Instances
- Can save up to 90%
- For termination, will be notified 2 minutes through ec2 metadata
- Useful when you dont need persistent storage
- Spot block to stop instances from terminating
- Spot fleet is a collection of spot instances
- Used Flexible Applications
- Choose Spot Price, if spot price goes above your maximum you can terminate your instance
- Used for
  - Big data + analytics
  - Containerized workloads
  - CI/CD + testing
  - Web Services
  - Image + media rendering
  - HPC

####  9.1.8. <a name='Hibernate'></a>Hibernate
- Saves content from RAM to EBS and persists
- Makes faster to reboot. No need to run bootstrap scripts or OS install
- Retains Instance ID
- Ram must be less than 150GB
- Instance families include CMR3-5
- Windows, Amazon Linux AMI, Ubunut
- Can hibernate for more than 60 days

####  9.1.9. <a name='PlacementGroups'></a>Placement Groups
- Cluster
  - grouping of instances within a single AZ
  - Recommended for apps that need low network latency, high network throughput, or both.
  - Only supports certain instances
- Spread 
  - each instance is placed on distinct underlying hardware
  - recommended for applications that have a small number of cirtifical instances they should be kept separate from eachother

####  9.1.10. <a name='WAF-1'></a>WAF
- Configure conditions such as what IP addresses are allowed to make this request
- Configure what query string parameters need to be passed
- Passes to ALB ClourFront or API Gateway.
- Gives 403 if not recieved
- Can also provide extra protections like
  - IP Addresses filtering
  - Country origin filtering
  - Value in request headers
  - Strings that appear in requests
  - Length of requests
  - Presense of SQL code sql injection
  - Presence of a script in XSS

####  9.1.11. <a name='LoadBalancers'></a>Load Balancers
- Must configure Static IP address, not by odefault
- ALB
  - Best used for HTTP/S. 
  - Operate at Layer 7. 
  - Application Aware
- NLB
  - Balancing TCP
  - Used for extreme performance
  - Operates at Layer 4
- Classic LB
  - Levle 7
  - HTTP/S
  - Not App Aware
- 504 error means gatewaey timed out
- X-Forwarded-For Header is the original IP address
- Configure Health Checks
- Load Balancers have only domain
- Sticky Sessions
   - Binds specific user session to an instance of LB
   - Disable sticky sessions if you arent seeing traffic to another instance
- Cross Zone LB
  - Allow equal weight across many zones
- Path Routing
  - Create listeners to route based on URL
- If no endpoints are healthy, ELB will try to send to all hosts

####  9.1.12. <a name='AutoScaling'></a>Auto Scaling
- Groups
  - Logical Component (Web Server, etc)
- Configuration Templates
  - Specify information such as AMi, instance tpye, key pair
- Scaling Options
  - Can scale based on dynamic conditions or schedule
  - Options
    - Maintain current instance levels at all times
    - Scale manually
    - Scale based on a schedule
    - scale based on demand
    - use predictive scaling


###  9.2. <a name='ElasticBeanStalk'></a>Elastic BeanStalk
- Quick way to scaffold entire applications based on templates of popular application infrastructures
- Can auto scale

###  9.3. <a name='AWSLambda'></a> AWS Lambda 
- Serverless Functions  - lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes.
- Use as event system
- Use as compute service  based on HTTP requests or using AWS SDKs
- Pricing
  - Number of requests
    - First 1 million requests are free
    - .20 per 1 million thereafter
  - Duration
    - from the time your code begins executing until it returns or otherwise terminates
    - This pricing depends on how much memory is adjusted
- Scales out atuomatically
- 1 event = 1 function
- Use X-Ray to Debug 

####  9.3.1. <a name='Layers'></a>Layers
- Use Layers to reduce bundle per lambda sizing

###  9.4. <a name='ElasticContainerService-ECS'></a>Elastic Container Service - ECS
- Amazons built in way of deploying and scaling containers outside of the context of K8s.
- You deploy Clusters, which have Services, which have Familys or Tasks that are responsible for deploying your containers.
- Try to reuse names where possible to make your life easier. 
- To have a custom domain on top of this, you will need a ELB to resolve the load balancing requirements for containers

##  10. <a name='Storage'></a>Storage

###  10.1. <a name='AWSDataSync'></a>AWS DataSync
- Used to move large amounts of data from on-prem to AWS
- Used with NFS- and SMB-compat file systems
- Replication can be done hourly, daily, or weekly
- Install the DataSync agent on server
- Can be used to replicate EFS to EFS as well

###  10.2. <a name='StorageGateway'></a>Storage Gateway
- Connects on prem appliciance with cloud based storage to provide seamless and secure integration between an orgs on prem It environment and AWS storage infra.
- Has Software appliance with a VM image that you install on host in data center.
  - File Gateway (NFS & SMB)
  - Volume Gateway (iSCI)
    - Stored Volumes
    - Cached Volumes
  - Tape Gateway (VTL)ss

###  10.3. <a name='EBS'></a>EBS
- Provides persistent block storage volumes. 
- Automatically replicated in AZ
- To Migrate EBS
  - Create EBS Snapshot of Root OS EBS
  - Create AMI based on Snapshot
  - Launch new instance in region
- Only the root EBS gets deleted
- Snapshots exist on S3 and are incremental
- Can Encrypt by taking Snapshot and copy to Encrypted than create AMI and launch EC2

####  10.3.1. <a name='Types'></a>Types
- General Purpose SSD: Most Load works
- Provisioned IOPs: Databses
- Throoughput Optimised Hard Disk Drive: Big Data & Data Warehouses
- Cold Hard Disk Drive: File Servers
- Magnetic: Workloads where data is infrequently accessed

###  10.4. <a name='AthenaMacie'></a>Athena/Macie
- Athena
  - Interactive query service which enables you to run querues against s3 using SQL
    - Serverless
    - No need to set up complex ETL processes
    - Works directly with data stored in s3
- Macie
  - Security service which uses ML and MLP to disocver, classify, and protect sensitive data stored in s3
  
###  10.5. <a name='EFS'></a>EFS
- Elastic File System
- Easy to use file system that attaches to EC2.
- Storage grows and expands based on how you uses it
- Great for fileservers
- Supports NFSv4
- Only pay for what you use
- Data is stored across many AZs
- Read After Write consistency
- Expands up to petabytes

###  10.6. <a name='AmazonFSx'></a>Amazon FSx
- Managed window server that runs window server message block based file services
- Designed for Windows and windows applications
- Supports AD users, Access control lists, groups and security polices
- FSx For Lustre is fully managed FS that is otpimized for HPC

###  10.7. <a name='AmazonSimpleStorageService-S3'></a>Amazon Simple Storage Service - S3
- You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
- Amazon S3 stores data as objects within buckets. An object is a file and any optional metadata that describes the file. To store a file in Amazon S3, you upload it to a bucket. When you upload a file as an object, you can set permissions on the object and any metadata.
- Buckets are containers for objects. You can have one or more buckets. You can control access for each bucket, deciding who can create, delete, and list objects in it. You can also choose the geographical Region where Amazon S3 will store the bucket and its contents and view access logs for the bucket and its objects.
- Can refer to buckets and objects with ARN
- As many items in buckets, but only default 100 buckets
- S3 has universal namespaces, regardless of region, must have unique name
- You can use S3 bucket redirects to send from www. to non-www.
- Objects consist of
  - Key == name of object
  - Value: data being stored (maximum of 5tb)
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

####  10.7.1. <a name='StorageClassesTiers'></a>Storage Classes/ Tiers
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

####  10.7.2. <a name='S3Select'></a>S3 Select
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

####  10.7.3. <a name='S3Permissions'></a>S3 Permissions
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

####  10.7.4. <a name='S3Security'></a>S3 Security
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

####  10.7.5. <a name='S3MonitoringLogging'></a>S3 Monitoring/Logging 
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

####  10.7.6. <a name='S3DataProtection'></a>S3 Data Protection
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

####  10.7.7. <a name='S3LifeCycleManagement'></a>S3 Life Cycle Management
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

####  10.7.8. <a name='S3StorageClassAnalsis'></a>S3 Storage Class Analsis
- Automatic analysis of your storage classes with recommendations
- Can configure up to 1000 storage class filters
- Can filter by
  - Entire BUcket
  - Prefx
  - Tag
  - Tag & Prefix
- Data is updated daily and visualations are avialable in the S3 COnsole
- Chargeable feature (.10 per million objects analysed)

####  10.7.9. <a name='S3EventNotifications'></a>S3 Event Notifications
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

####  10.7.10. <a name='S3PerformanceOptimization'></a>S3 Performance Optimization
- Requests per second are by prefix, scale horizontally by using prefixes
- Remember KMS Request limits
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

####  10.7.11. <a name='S3StaticWebsitehosting'></a>S3 Static Website hosting
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

##  11. <a name='Database'></a>Database


###  11.1. <a name='RDS'></a>RDS
- Relatonal Database Service manged by AWS
  
####  11.1.1. <a name='Terminology-1'></a>Terminology
- Database Instance: An isolated DB environment, can have many user created databases within it
- Database Engine: Type of DB to run
- Database Instance Type: Determines type of hardware
- Mutli AZ - Stands for multiple availality zones
- Read Replicas: Separate node to handle only read queries.
- Primary Host - handles all read/writes
- Secondary Host: Doesn't handle writes, acts as failover
- Aurora: MySQL and PostgreSQL compatible Relational DB

####  11.1.2. <a name='ProvisioningaDatabase'></a>Provisioning a Database
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

####  11.1.3. <a name='RDSPricing'></a>RDS Pricing
- Instance Hours
- Database Storage
- Backup Storage: No charge for backup storage up to 100% of total database storage
- Database Transfer: Outgoing traffic only. Regional Data Transfer pricing

####  11.1.4. <a name='ScalingRDS'></a>Scaling RDS
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

####  11.1.5. <a name='Multi-AZ'></a>Multi-AZ
- Available for all DBS but Aurora, cuz Aurora is already fault tolerant
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

####  11.1.6. <a name='ReadReplicas'></a>Read Replicas
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

####  11.1.7. <a name='Backups'></a>Backups
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

####  11.1.8. <a name='Security-1'></a>Security
- Layers of Security: Network Isolation, IAM, Encryption at rest, SSL
  - Network Isolation: Use VPC to place rds instance into private subnet, use security groups for specific traffic, turn off public accessibility, use ClassicLink for non-vpc resources, use direct dconnect to replicate on-prem DBs, and VPC peering to share between VPCs 
  - Access Control: Use IAM to perforamn actions on RDS resources. Use MFA to provide extra level of protection. Dont use master credentials on DB Instance. Use integrated security with AD or IAM Auth
  - Encryption at rest: It's free. AES-256. All nodes are replicated. Encryption performed at volume level. Access to keys are logged. Can encrypt only once. Have two tier encryption
  - SSL Connectivity: SSL is turned on, but must be enforced through Parameter groups

####  11.1.9. <a name='MonitoringRDS'></a>Monitoring RDS
- Metrics to Watch
  - CPU 
  - Storage Space
  - Network Traffic
  - DB Connections
  - IOPS

####  11.1.10. <a name='AmazonAurora'></a>Amazon Aurora
- Cloud-first built RDS instance that abstracts the storage and logging layers away using SOA architecture so they can be indepdently scaled
- 10GB to 64TB storage
- Compute resources can scale  up to 32vCPUS to 244 GB of Memory
- 2 Copies of your data i scontained in each availability zone. Minimum of 3 AZ
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
  - Automatically scales and only is charged for use
- Backups
  - Backups are always enabled.
  - Do not impact performance
  - Can take Snapshots
- Migrate from MySQL
  - Create Snapshot then restore Aurora from snapshot
  - Create read replica aurora then promote


###  11.2. <a name='DynamoDB'></a>DynamoDB
- Support document and key-value stores
- Stored on SSD Storage
- Spread across 3 geographically distinct data centres

####  11.2.1. <a name='EventualvsConsistentReads'></a>Eventual vs Consistent Reads
- Eventual reads Consistency across all copies of data is usually reached within a second
- Strong consistent reads - Always most up to date data

####  11.2.2. <a name='DynamoDBAccelerator'></a>DynamoDB Accelerator
- Fully managed, highly available, in-memory cache
- 10x performance improvement
- Reduces request time from milliseconds to microseconds 
- No need for devs to manage caching logic
- Compatible with DynamoDB API calls

####  11.2.3. <a name='Transactions'></a>Transactions
- Multiple all-or-nothing conditions
- Two underlying reads or writes - prepare commit
- Up to 25 items or 4mb of data

####  11.2.4. <a name='On-DemandCapacity'></a>On-Demand Capacity
- Pay-per-request pricing
- Balance cost and performance
- No minimum capacity
- Pay more for requests
- Use for new products and maybe switch once you recognize workload

####  11.2.5. <a name='BackupRestore'></a>Backup + Restore
- On-Demand
  - Full backjups at any time
  - Zero Impat on table performance or availability
  - Consistent within seconds and retained until deleted
  - Operates within same region as source table
- PTTR
  - Protects against accidental writes or deletes
  - Restores to any point in the last 35 days
  - Incremental backups
  - Not enbabled by default
  - Latest restorable: five minutes in the past

####  11.2.6. <a name='Streams'></a>Streams
- Time-ordered sequence of item-level changes in a table
- Stored for 24 hours
- Inserts, updates, and deletes are published
- Combine with Lambda functions for functionality like stored procedures

####  11.2.7. <a name='GlobalTables'></a>Global Tables
- Globablly Distrubted applications
- Based on DynamoDB Stream
- Multio-region redundancy for DR or HA
- No application rewrites
- Replicaiton latency under one sefcond

####  11.2.8. <a name='Security-1'></a>Security
- Encreyption at rest using KMS
- site-to-site VPN
- Direct Connect
- IAM Policies and Roles
- Fine-grained access
- CloudWatch and CloudTrail
- VPC Endpoints

###  11.3. <a name='RedShift'></a>RedShift
- fast powerfuly, fully managed, petabyte scale data warehouse
- Can store up to 8PBP of Data
- Does not support multi-az deployments currently
- Automatic backups retained 1 day

###  11.4. <a name='ElasticCache'></a>ElasticCache
- Managed in-memory cache server
- MemCache or Redis
- Use MemCache if you want horitonztable scalings
- Redis has lot more options for more specific caching needs
  - Like Multi-AZ
  - Backup + Restores
  - Persistence

###  11.5. <a name='DatabaseMigrationService'></a>Database Migration Service
- Migrate from On-Prem or cloud DBs to the Cloud
- Server that creates replicas
- You create source and tell where from and to to etract/load data
- DMS creates tables and keys on destination if they dont exist
- Can also precreate using AWS Schema Conversion Tool
- Supports different database migration to different database migration

###  11.6. <a name='EMR'></a>EMR
- Elastic Map Reduce
- Run petabyte scale analysis on less than half the cost of tradtional on-prem solutions and over 3 times faster than Spark
- EMR is cluster of EC2 instances (nodes). Each node has a role referred as node type
- Master node
  - Node manageres the cluster.
  - Tracks status of tasks
  - Log data stored here
  - Log data can be configured to write every 5 minutes. 
    - Can only configure first
- Core Node
  - runs tasks and stores data in a HDFS
  - Always one Core Node
- Task Node
  - Only runs tasks, does not store data in HDFS. 
  - Optional


##  12. <a name='ApplicationIntegration'></a>Application Integration

###  12.1. <a name='SQS'></a>SQS
- Way to store messages on a queue
- Allows decoupled services by allow communication to happen on the queue
- Messages can be up to 256 KB of TXT. 
  - Can go up to 2gb but extra is stored in S3
- Access messages from SQS API
- Standard Queues
  - Default  Queue Type
  - nearly unlimited number of transactions per seconds
  - Garauntees messages delivered once
  - Standard queue may send things out of order, but attempts to send things in order
- FIFO Queues
  - First In and First Out Queue
  - Exactly-One processing event
  - Remains until consumer deltes it
  - Support message groups that allow multiple ordered message groups
  - Limited to 300 transactions per second, have all capabilites on standard queues
- Visibility Timeout
  - Amount of time a message is invisible in the SQS queue after a reader picks up that message
  - If job is processed before visibility timeout expires, message will be deleted from the queu
  - If not processed in time, job will be sent back and processed again
-  Polling
  - Long
    - Way to retrieve messages from queue. Sits and polls until message arrives or times out
  - Short
    - Returns immediately
- Rention period of 14 days

###  12.2. <a name='SimpleWorkflowService'></a>Simple Workflow Service
- Web service makes it easy to coordinate work across distrbuted services using tasks/workflows
- Tasks can last up to a year
- Task oriented-API
- Task is assigned only once and never duplicated
- Keep tracks of all tasks or events
- Actors
  - Workflow Starters: application can initiate a workflow
  - Deciders: Controls the flow of activity in a tasks
  - Activity Workers:  Carry out the activity tasks

###  12.3. <a name='SimpleNotificationService'></a>Simple Notification Service
- Setup and send notifications from the cloud.
- Publishes (push notifications) to other services
- Cam deliver messages  by SMS or email
- Can send to SQS or HTTP Endpoint
- One topic can support many deliveries to multiple endpoint types
- Messages store redunantly across many AZs
- Pay as you go model

##  13. <a name='MediaServices'></a>Media Services
###  13.1. <a name='ElasticTranscoder'></a>Elastic Transcoder
- Media transcoder in the cloud
- Convert media  files from original source format into different formats
- provides popular output formats
- Pay based on minutes and resolution you transcode

##  14. <a name='Analytics'></a>Analytics

###  14.1. <a name='Kinesis'></a>Kinesis
- Streaming Data is data that is generated continously by thousands of data sources
- Data is sent in small sizes incrementally
- Kinesis loads and anaalyze streaming data
- Types
  - Streams 
    - Stores data from multiple sources in shards
    - Real time-streaming of dfata
    - Consumers can pull that data
    - Shards
      - 5 transactions per second for reads, up to max of 2mb per second.
      - Up to 1000 seconds per write
  - Firehose
    - No persistent storage
    - Must analyze and output 
  - Analytics


