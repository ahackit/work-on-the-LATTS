# LATT-K8
Learn All The Things - Kubernetes

## Containers

### What are Containers?

Containers : Application-centric methods to deliver high-performing, scalable applications on any infrastructure of your choice. 

OS in software

Microservices: Lightweght applications or services deploying independently.

Container Image: bundles the application along with its runtime and depdendencies. 

### What is Container Orchestration?

Tools which group systems together to form clusters where containers' deployment and management is automated at scale

- Fault-tolerance
- On-demand scalability
- Optimal resource usage
- Auto-discovery to automatically discover and communicate with each other
- Accessibility from the outside world
- Seamless updates/rollbacks without any downtime.

### Different Container Orchestrators?

- Amazon Elastic Container Service: Amazons way to host Docker containers at scale
- Azure Container Instances: Basic container orchestration service by Microsoft
- Azure Service Fabric: Open source container orchestrator from Microsoft
- Kubernetes: Open Source orchestrion tool, started by google, part of the CNCF project.
- Marathon: Framework to run containers at scale on Apache Mesos
- Nomad: Container orchestrator provided by HashiCorp
- Docker Swarm: container orchestror provided by Docker

### Why use Container Orchestrators?

- Group hosts together while creating a cluster
- Schedule containers to run on hosts in the cluster based on resources availability
- Enable containers in a cluster to communicate with each other regardless of the host they are deployed to in the cluster
- Bind containers and storage resources
- Group sets of similar containers and bind them to load-balancing constructs to simplify access to containerized applications by creating a level of   abstraction between the containers and the user
- Manage and optimize resource usage
- Allow for implementation of policies to secure access to applications running inside containers.

### Where to Deploy Container Orchestrators?

Any infastructure of your choice.

## Kubernetes

### What is Kubernetes?
Kubernetes comes from a Greek word, means helmsman or ship pilot. K8s is the pilot on a ship of containers.

### Kubernetes Features

- Automatic bin packing :Kubernetes automatically schedules containers based on resource needs and constraints, to maximize utilization without - sacrificing availability.
- Self-healing: Kubernetes automatically replaces and reschedules containers from failed nodes. It kills and restarts containers unresponsive to health checks, based on existing rules/policy. It also prevents traffic from being routed to unresponsive containers.
- Horizontal scaling : With Kubernetes applications are scaled manually or automatically based on CPU or custom metrics utilization.
- Service discovery and Load balancing: Containers receive their own IP addresses from Kubernetes, while it assigns a single Domain Name System (DNS) name to a set of containers to aid in load-balancing requests across the containers of the set.
- Automated rollouts and rollbacks: Kubernetes seamlessly rolls out and rolls back application updates and configuration changes, constantly monitoring the application's health to prevent any downtime.
- Secret and configuration management: Kubernetes manages secrets and configuration details for an application separately from the container image, in order to avoid a re-build of the respective image. Secrets consist of confidential information passed to the application without revealing the sensitive content to the stack configuration, like on GitHub.
- Storage orchestration: Kubernetes automatically mounts software-defined storage (SDS) solutions to containers from local storage, external cloud providers, or network storage systems.
- Batch execution: Kubernetes supports batch execution, long-running jobs, and replaces failed containers.

### What is the CNCF?

Projects hosted by Linux foundation encompassing all sorts of software to managing cloud-native apps. 

## Kubernetes Components

### Kubernetes Architecture

- One or more Master Nodes
- One or more Worker Nodes
- Distributed key-value store, such as etcd

### Master Node

- Provides running environment for the control plane responsible for managing the state of a K8s cluster. 
- Control plane components are agents with very distinct roles in the clusters management. 
- Need to keep control plane running at all costs. Can add many control plane nodes so if one goes down the other can take over, even though only one is ever working.
- K8s cluster state is persisted to etcd, which is usually hosted on a master node or dedicated host. 

#### Master Node - Components

- API Server
- Scheduler
- Controller Managers
- etcd

#### Master Node - Components: API Server

- Administrative tasks are coordinate by kube-apiserver. 
- Central control plane component running on the master node. 
- API takes http request, checks state of etcd, updates state, then updates cluster.  

#### Master Node - Components: Scheduler
- Kube-scheduler responsible for assigning pods to nodes based on cluster state and object requirements. 

#### Master Node - Components: Controller Managers

- Controller managers are control plane components on the master node running controllers to regulate the state of the K8s cluster.
- Kube-controller-manager runs controllers responible to act when nodes become unavailable, ensure pod counts are as expected, create endpoints, service accounts and api tokens
- cloud-controller-manager runs controllers responsible to interact with the underlying infrrastructure of a cloud provider when nodes be unavailable, to manage store volumes, and to manage load balancing and routing.

#### Master Node - Components: etcd

- Distributed key-value data store used to persist a K8s clusters state. 
- New data is written to the data store by appending, never by replacing. 
- Has backup, snapshot, and restore capabilities. 
- etcd also stores config details like subnets, configmaps, secrets, etc.

### Worker Node

- Provides running environment for client apps. 
- Apps are encapsulated in Pods, controlelr by cluster control plane agents running on master node.

#### Worker Node - Components

- Container runtime
- kubelet
- kube-proxy
- Addons for DNS, Dashboard, cluster-level monitoring and logging

#### Worker Node - Components: Container Runtime

- K8s doesn't have the capability to directly handle containers. Needs a container runtimes.  
- Runtimes include Docker, CRI-O, containerd, rkt, rklet

#### Worker Node - Components: kubelet

- kubelet is an agent running on each node and communicates with the control plane components from the master node. 
- Communicates with container runtime on node to allocate pods. Connects using CRI
- CRI implements two services, ImageSerivce and RuntimeSerivce. ImageService = image related operations. RunTime service is responsible for Pod/container-related operations

##### Worker Node - Components: kubelet - CRI shims

- dockershim
- cri-containered
- CRI-O

#### Worker Node - Components: kube-proxy

- Network agent which runs on each node responsible for dynamic updates and maintenance of all networking rules on the nodes.

#### Worker Node - Components: Addons

- Cluster feature and functionality not yet availabe in K*s, implemented through 3rd-party pods and servies
- DNS : Cluster DNS, DNS server require to assigned DNS records to k8s object and resources
- Dashboard: general purpose web-based user interface for cluster management
- Monitoring: Collects cluster-level container metrics and saves them to a central data store
- Logging: collects cluster-level container logs and saves them to a central log store for analysis.

### Networking Challenges

- Microservices rely heavily on networking in order to mimic the tight-coupling once availabe in the monolithic area.
- Container-to-container communication inside Pods
- Pod-to-Pod communication o nthe same node and across cluster nodes
- Pod-To-Service communication within the same namespace and across cluster namespaces
- External-To-Service communication for clients to access applications in a cluster

#### Container-to-Container communication inside Pods
- Container runetime creates an isolated network space for each container it starts. 
- Referred to as network namespace.
- Namespace is shared across containers.
- Pod is started, network namespace is created inside the pod, and all containers running inside the pod will share that network namespace.

#### Pod-to-Pod Communication Across Nodes

- Since pods are scheduled on nodes randomly, K8s assigns an IP address for each Pod which it treats as a VM "IP-Per_pod" 
- Containers share Pods network namespace and must coorindate prot assignments in side the pod and communicate with eachother on local hoster. 
- Containers are integrated with the k8s networking model through the use of CNI (Container Network Interface) supported by CNI plugins.
- CNI is specification and libraries which allow plugins to configure the netowkring for container. 
- Most CNI plugins use 3rd-party Software Defined Networking (SDN) implemting the k8 networking model. Flannel/Weave/Calico

#### Pod-To-External

- Accessibility from the outside world is done through services. Conplex constructs which encapsulate networking rules definitions on a cluster by nodes. 
- Exposes services through kube-proxy.

## Kubernetes Installation

### Kubernetes Installation Configuration

- All-in-One Single-Node Installation :In this setup, all the master and worker components are installed and running on a single-node. While it is useful for learning, development, and testing, it should not be used in production. 
- Single-Node etcd, Single-Master and Multi-Worker Installation:we have a single-master node, which also runs a single-node etcd instance. Multiple worker nodes are connected to the master node.
- Single-Node etcd, Multi-Master and Multi-Worker Installation: we have multiple-master nodes configured in HA mode, but we have a single-node etcd instance. Multiple worker nodes are connected to the master nodes.
- Multi-Node etcd, Multi-Master and Multi-Worker Installation: etcd is configured in clustered HA mode, the master nodes are all configured in HA mode, connecting to multiple worker nodes. This is the most advanced and recommended production setup.

### Infrastrcute for the K8s installation
- Should we set up Kubernetes on bare metal, public cloud, or private cloud?
- Which underlying OS should we use? Should we choose RHEL, CoreOS, CentOS, or something else?
- Which networking solution should we use?

### Localhost Installation
- Minikube: single-node local Kubernetes cluster
- Docker Desktop: single-node local Kubernetes cluster for Windows and Mac
- CDK on LXD: multi-node local cluster with LXD containers.

### On-Premise Installation
- On-Premise VMs: Kubernetes can be installed on VMs created via Vagrant, VMware vSphere, KVM, or another Configuration Management (CM) tool in conjunction with a hypervisor software. There are different tools available to automate the installation, such as Ansible or kubeadm.
- On-Premise Bare Metal: Kubernetes can be installed on on-premise bare metal, on top of different operating systems, like RHEL, CoreOS, CentOS, Fedora, Ubuntu, etc. Most of the tools used to install Kubernetes on VMs can be used with bare metal installations as well.

### Cloud Installation

- Pretty much everyone has an offering. Big difference is between hosted and turnkey solutions
- AKS/EKS are Hosted solutions by AWS. EC2 is a turn-key solution

### Kubernetes Installation Tools/Resources
- kubeadm: first-class system of k8 ecosystem. Secure and recommended way to bootstrap a single or multie node K8 cluster. 
- kubespray: Can install HA k8 clusters on AWS/GCE/etc. Based on ansible
- kops: create, destroy, upgrade, and maintain production-grade, HA k8 clusters from the CLI.
- kubeaws: create, upgrade, and destroy k8 clusters on AWS from the CLI
- If you are mad, you can install K8 from scratch. Check out "Kubernetes The Hard Way"

## Minikube Example

### Requirements for Minikube
- Can run loca Linux, macOs, or Windows. 
- Needs type-2 hypervisor.
- kubectl: binary used to access and manage k8 cluster. Installed separate from Minikube. Safe to disregard kubectl messages since we install aftter. 
- Type 2 Hypervisor - VirtualBox, HyperKit, Vmware Fusion'
- VT-x/AMD-v virtualization must be enabled at BIOS level
- Internet connection for initial setup and subsequent docker image downloads

#### Installing Minikube

- Install Type2 Hypervisor
- Install Minikube
- Start Minikube with "minikube start" - Disregard warnings
- Check status with "minikube status" - Display status of minikube
- Stop minikube with "minikube stop" - Stops minikube

### Minikube CRI-O

- CRI-O is an implementation for the K8 CRI to enable using OCI( Open Container Initiative) compatitiable runtimes. 
- Start minikube with CRI-O as container runtime "minikube start --container-runtime=cri-o"
- login "minikube ssh"
- Cant run docker commands since its not working
- Gotta run CRI-o commands "sudo runc list"

## Accessing  K8 Cluster - Minikube

### Accessing K8 Cluster

- CLI Tools and scripts
- Web UI 
- APIS from CLI

#### Accessing K8 Cluster: CLI 

- kubectl is the Kubernetes Command Line Interface client to manage cluster resources and appiclations. 
- Can be usted standalone or part of scripts. 
- Require credentials and cluster access points to be configured.

#### Accessing K8 Cluster: Web UI

- K8s dashboard provides web UI to interact with k8 cluster.

#### Accessing k8 Cluster: APIs

- Can connect to API server using API endpoints and send commands.

##### HTTP API Space
- Core Group (/api/v1/): includes objects such as Pods, Services, Nodes, Namespaces, configmaps, secrets, etc.
- Named Group (/apis/$name/%version): Alpha/Beta/Stable. 
- System Wide: System wide endpoints like /healthz - /logs - /metrics - /ui

### Kubetl

- Generally installed before minikube, but can be after. 
- kubectl receives its config automatically for minikube k8s cluster access. 
- Other environments need to manually confugre kubectl.
- Should try to keep kubectl as same version as one running on cluster.

#### kubectl: Configuration File

- kubectl client needs master node endpoints and appropirate credentials to interact with API server running on master node.
- Starting minikube creates by default a config file inside .kube directory (dot-kube-config). Usually in home directory. 
- Can run kubectl config view to see details or view file

### Kubernetes Dashboard
- Access dashboard from minikube "minikube dashboard"

#### Kubectl Proxy
- "kubectl proxy" authenticates with API server on master node and makes dashobard avaiable on different URL. 

### API with kubectl proxy
- Run kubectl proxy then can run curl commands against endpoint to explore API.

### API without kubectl proxy
- Get the token: $ TOKEN=$(kubectl describe secret -n kube-system $(kubectl get secrets -n kube-system | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t' | tr -d " ")
- Get the API server endpoint: $ APISERVER=$(kubectl config view | grep https | cut -f 2- -d ":" | tr -d " ")  
- Confirm API endpoints are the same by "echo $APISERVER" and "kubectl cluster-info"
- Access the API server using the curl command: $ curl $APISERVER --header "Authorization: Bearer $TOKEN" --insecure

## Kubernete Building Blocks

### Kubernetes Object Model

Kubernetes has object model representing different persistent entities in the K8 Cluster.
- What containerized apps we are running and on which node
- App resource consumption
- Different policies attached to applications, like restart/upgrade policues, fault tolerance, etc.
Each obejct as a "spec" section. K8 manages the status section for objects, where it records actual state. 

K8 objects are Pods, ReplicaSets, Deployments, Namespaces, etc.

Creating an object: 
- Object config data below the "spec" is to be subbmited to the K8 API server. 
- Spec section describe desired state and basic info. 
- API requre to create and object must have the spec section. 
- Can accept JSON but should try to conform to YAML overlords.

See basic-object.yaml for example
- apiVersion: required field. Specifies the API endpoint we want to connect to. 
- kind: object type
- metadata: basic information
- spec: desired state of deployment

### Pod 
- Smallest and simplest K8 object. 
- Represents single instance of an app. 
- Pod is a logical collection of one more or containers.
- Scheduled together on same host with the pod.
- Share same network space
- Have access to same external storage
- Pods work with controllers which handle self-healing, etc. 
- Controllers are deployments, replicasets, replicationControllers, etc. 

See pod-spec.yml.

### Labels

Key-value pairs attached to k8 Objects. Used to organizae and select a subset of object. 

#### Label Selectors

Controllers use label selectors to select a subset of objects. 

- Equality-Based Selectors : == or !=
- Set-Base selectors : in, notin or exist/does not exist 

### ReplicationController

- Not recommend anymore, ensures a specified number of replicas of a pod is running at a given time. 
- Default controller is a Deployment, this configures a ReplicaSet to manage Pod's lifecycle.

### ReplicaSet
- Next-generation ReplicationCotroller. 
- Supports both equality and set-based selectors.

### Deployments

- Provide delcarative updates to Pods and ReplicaSets
- DeploymentController is part of the master node's controller manager.
- Allows for rollouts and rollbacks. 

### Namespaces

- names of resources/objects inside a namespace are uniquie, but not across namespaces in cluster. 
- kubectl get namespaces

k8 creates four default namespaces
- kube-system: contains objects created by the k8 system, mostly control plane agents.
- kube-public: node heartbeart data
- kube-node-lease:  unsecured and reable by anyone.
- default: contains objects and resources created by admins and developers

## Authentication, Authorization, Adminission Control

An API request goes through three steps:

- Authentication: Logs in a user
- Authorizaton : Authorizes API requests added by the logged-in user
- Admission Control: Software that can modify or reject requests based on additional checks

### Authentication

K8 doesn't have an object called user, or it doesn't sotre usernames. Can still use usernames for access control and logging.

- Normal User: Managed outside of the k8 cluster via services like User/Client certificates, a file listing username,password, google accounts, etc.
- Service Account: Automatically created accounts used to talk to API server, but can be created manually. Tied to a given namespace.

K8 has different authentication modules

- Client certificates: Pass the certificate to the API service. "-- client-ca-file=SOMEFILE"
- Static Token File: Pass a file with pre-defined bearer tokens. Indefinite. "--token-auth-file=SOMEFILE"
- Bootstrap Token: In beta. Used for bootstrapping a k8 cluster
- Static Password file: Pass a file with basic auth details. "--basic-auth-file=SOMEFILE"
- Service Account Tokens: automatically enabled authenticator that uses signed bearer tokens to verify the requests. These tokens get attached to Pods using the ServiceAccount Admission Controller, which allows in-cluster processes to talk to the API server.
- OpenID Connect Token: Connect with OAuth2 Providers. 
- Webhook Token Authentication: bearer tokens can be offloaded to remote service
- Authenticating proxy: programmable authentication logic.

### Authorization 

After successfull authentication, authorization check happens.  

Auth modules, which K8 cluster can have many are:
#### Node Authorizer
Specifically authoerizes API requests made by kubelets.
#### Attribute-Based Access Control: 
Authorized at an attribute level. Use "--authorization-mode=ABAC" to start API server. Also need to set a authoerization policy by " --authorization-policy-file=PolicyFile.json.". See PolicyFile.json as an example
#### Webhook: 

Authorized by third party service. Configure using "authorization-webhook-config-file=SOME_FILENAM"

#### Role-Based Access Control:
 authorization based on roles of users. Restrict resources by speciifc operations such as create, get, update ,aptch. Role and ClusterRole manage either a specific namespace or clusterwide respectively.

 See role.yaml for example yaml for Role and Bindings

### Admission Control

Specify granular access control policies like priveleged containers or checking resource quote.  force these policies using different admission controllers, like ResourceQuota, DefaultStorageClass, AlwaysPullImages, etc.

--enable-admission-plugins=NamespaceLifecycle,ResourceQuota,PodSecurityPolicy,DefaultStorageClass

## Services

Service logically groups Pods and defines a polcy to access them. Grouping is achieved by Labels and Selectors
Services can expose single Pods, ReplicaSets, Deployments, DaemonSets, and StatefulSets

See service-object.yaml for example.

- Services provide load balancing by default for traffic forwarding to ClusterIP
- Service forwards traffic through targetPort on the Pod. If port not defined, goes to default service port
- Service endpoints are managed automatically by the service, not the admin.

### Kube-proxy

Worker nodes run a daemon called kube-proxy, which watches API server on master node for addition/removal of Service and endpoints.

### Service Discovery

Two modes for discovering Services

- Environemnt Variables: Once pod starts on Node, it gets environment variables for all active service. Services created after wont be there.
- DNS Add-on: creates a dns record for each Service and its format is my-svc.mynamespace.svc.cluster.local. Can see the service by just the service name within same namespace or by service name.namespace

### ServiceType

Can define the access scope.

- Only accessible in a Cluster
- Accessible from within a cluster and the external world.
- Maps to an entity which resides either inside or outside the cluster.

#### ServiceTypes: ClusterIP and NodePort
ClusterIP: default ServiceType. Service receives a Virtual IP address known as its ClusterIP. Virtual IP address only used for communicating within cluster.

NodePort ServiceType: Picked from a high-port range 30000-32767 typically. 

#### ServiceType: LoadBalance

- NodePort and ClusterIP are automatically created, and external load blanacer will route to them.
- Service is exposed at a static port on each worker node
- Service is exposted externally using the underlying cloud provides load balance feature
- Needs to have cloud service with underlying Load Balance (AWS or GCP)

#### ServiceType: ExternalIP

If a route goes to one or more worker nodes. Requires external cloud provider.

### ServiceType: External Name

Does not define any endpoint. When access within cluster, returns a cname record of an externally configured service

- Makes externally configured services like my-database.example.com available to apps inside te cluster. 
- If external app within the same namespace, using just the name my-databbase would make it available to other apps and services within that namespace.

## Deploying a Stand-Alone Application

- Delete any object using "kubectl delete"
- Create deployment using -f "kubectl create -f webserver.yaml"
- Create service using -f "kubectl create -f webserver-svc.yaml" 
- can also use existing deployment "kubectl expose deployment webserver --name=web-service --type=NodePort"
- minikube ip or minikube service -servicename- to see deploy

### Liveness Probe

If container is not responding to request, liveness probe can manage container

Can be set by 
- Liveness Command
- Liveness HTTP Request
- TCP Liveness Probe

### Readiness Probe

App needs to meet certain conditions before traffic can be served.

## Kubernetes Volume Management

### Volumes

Containers in Pods are ephemeral. K8S uses Volumes, essentially a directory backed by a storage medium. 
- Volumes are attached to a Pod and can be shared across containers. 

### Volume Types
- emptyDir: Data on volume is deleted as Pod is terminated.
- hostPath: still available on host if pod is deleted
- gcePersistentDisk: Google Compute Engine into pod
- awsElasticBlockStore: EBS volume into pod
- azureDisk: Azure Data Disk int pod
- cephfs: existing CephFS volume is mounted into pod
- nfs: NFS as volume
- iscsi 
- secret: Pass sensitive info to Pod
- configMap: config data or shell commands into Pod
- persistentVolumeClaim: 

### PersistentVolumes
- Can be dynamically provised based on StorageClass Resource
- StorageClass contains pre-defined provisions and parameters to create a PersistentVolume. 

### PersistenVolumeClaims
- Request for storage by User.
- Three access mode: ReadWriteOnce, ReadOnlyMany, ReadWriteMany.

### Container Storage Interface (CS)
- Interface used to standarardzed Storage Interface between providers.

## ConfigMaps and Secrets

### ConfigMaps

- Allow us to decouple configuration details from the container image. 
- Pass as key-value pairs.
- Can be passed to Containers as inidvidual environment variables or volumes.

#### Create ConfigMap

- kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
- kubectl get configmaps my-config -o yaml
- kubectl create -f customer1-configmap.yaml

### Secret

Stored as plain text inside etcd. Used to hide import info.
- Can be used in container as a file or environment variable

#### Create a Secret

- kubectl create secret generic my-password --from-literal=password=mysqlpassword
-  kubectl get secret my-password
- kubectl describe secret my-password
- kubectl create -f mypass.yaml

## Ingress

Decouple the routing rules from the application and centralize the rules management, you can then update the application without worrying about its external access. Incoming Ingress

Ingress configures a Layer 7 HTTP/HTTPS load balancer for services and provides

- TLS (Transport Layer Security)
- Name-based virtual hosting 
- Fanout routing
- Loadbalancing
- Custom rules.

Just does rules. Ingress controller does routing


### Ingress Controller 

Watches Master Node API server for changes in the Ingress resources and updates the l7 load balancer accrodingly. K8 supports all sorts of Controlelrs like Nginx

## Advanced Topics

### Annotations

Not used to identify and select objects. Just used for 

- Store build/release IDs, PR numbers, git branch, etc.
- Phone/pager numbers of people responsible, or directory entries specifying where such information can be found
- Pointers to logging, monitoring, analytics, audit repositories, debugging tools, etc.
- Etc.

### Jobs and CronJobs

Job creates one or more pods to perform a given task. 

Can be configured with things like

- parallelism: to set the number of pods allowed to run in parallel;
- completions: to set the number of expected completions;
- activeDeadlineSeconds: to set the duration of the Job;
- backoffLimit: to set the number of retries before Job is marked as failed;
- ttlSecondsAfterFinished: to delay the clean up of the finished Jobs.

CronJobs are Jobs with set scheduled times/dates. Additional config options in 
- startingDeadlineSeconds: to set the deadline to start a Job if scheduled time was missed;
- concurrencyPolicy: to allow or forbid concurrent Jobs or to replace old Jobs with new ones

### Quota Management

Use ResourceQuota API to provide constraints that limit aggregate resource consumption per NameSpace

- Compute Resource Quota: We can limit the total sum of compute resources (CPU, memory, etc.) that can be requested in a given Namespace.
- Storage Resource Quota: We can limit the total sum of storage resources (PersistentVolumeClaims, requests.storage, etc.) that can be requested.
- Object Count Quota: We can restrict the number of objects of a given type (pods, ConfigMaps, PersistentVolumeClaims, ReplicationControllers, Services, Secrets, etc.).

### Autoscaling
Dynamically adds or removes objects from cluster based on resource utilization, availability, and requirements.

- Horizontal Pod Autoscaler (HPA): HPA is an algorithm based controller API resource which automatically adjusts the number of replicas in a ReplicaSet, Deployment or Replication Controller based on CPU utilization.
- Vertical Pod Autoscaler (VPA) : VPA automatically sets Container resource requirements (CPU and memory) in a Pod and dynamically adjusts them in runtime, based on historical utilization data, current resource availability and real-time events.
- Cluster Autoscaler: Cluster Autoscaler automatically re-sizes the Kubernetes cluster when there are insufficient resources available for new Pods expecting to be scheduled or when there are underutilized nodes in the cluster.

### DaemonSets

A Pod that will get installed on all new Nodes for instances like Logging or Storage. 
- if DaemonSet is deleted, all Pods from daemonSet will be removed.
- Can be set to only specifc nodes by nodeSelectors and affinity rules.

### StatefulSets

Used for stateful applications which require a unique identify, such as name, network identifications, strict ordering, etc.

### Kubernetes Federation

With Kubernetes Cluster Federation we can manage multiple Kubernetes clusters from a single control plane. We can sync resources across the federated clusters and have cross-cluster discovery. This allows us to perform Deployments across regions, access them using a global DNS record, and achieve High Availability. 

Still in alpha. Avoid Platform-lock in.

### Custom Resources

Resources is an API endpoint. Allows for custom resources managed by a custom controller. 

### Helm 

Helm is a package manager that can install charts, which is bundled K8 Manifests. 
- Client is called Helm which runs on workstation.
- Server is called tiller which runs inside cluster.

### Security Contexts and Pod Security Polotices

Specific priveleges and access control settings for Pods and Containers

### Monitoring and Loggins
 
- Metrics Server: Cluster wide aggregator of resource usage data.
- Promethus: scrape the resource usage from K8 component and objects. 
- Most common way to collect logs is using ElasticSearch with fluentd.