# LATT-Rancher
Learn All The Things - Rancher

## Rancher Server Components

Rancher Server is made up of API Server, Authentication proxy, and one cluster controler for each ckuster that Rancher Manages.

Uses ETCD for its datastore.

Downstream clusters managed by Rancher run a Cluster Agent that bridges between Cluster Controller and the K8 API Server that runs inside the cluster.

Node Agent runs on every Node

## Authentication Porxy

Recieves requests and then sets K8 impersonation headers before forwarding request to K8 Cluster API Server

## Cluster Controller

- Watches for resource changes in the downstream cluster
- Brings the current state of the downstream cluster to the desiredstate
- Configures access control policies to clusters and projects
- Provisions clusters by calling the required Docker machine driversand Kubernetes engines, such as RKE and GKE

## Cluster Agent

Agent on every downstream cluster that opens a tunnel back to the rancher server controller.

- Connecting to the Kubernetes API of Rancher-launched Kubernetes clusters
- Managing workloads, pod creation and deployment within each cluster
- Applying the roles and bindings defined in each cluster’s globalpolicies
- Communicating through the tunnel between the cluster and Rancher server about events, stats, node info, and health

## Node Agent

Runs as a DaemonSet. Interacts with nodes-pecific functions

- Upgrading K8
- Restoring etcd snapshots.

## Installing RKE

RKE is a K8 Distribution and an installer. Provisions a cluster over SSH


## Preparing Nodes for K8s

Can provision them manually. 
Make sure to install supported version of Docker
Need to be able to access port 22 and 6643

## Create Cluster Config File

Can either use the default cluster.yml file that comes with Rancher. Easily stand up single node "Cluster".

Can also run "rke config" to go through a walkthrough for installing K8

## Certificate Options

K8 secures communication between nodes with TLS certs. RKE can auto generate certs.

Can provide your own custom Certs however.

## Deploy K8 with RKE

Run "rke up" with the config file. 

Reaches out to systems with SSH and builds K8 clusters.

## Secure the Installation Files

Once rke up is finished, you'll have a config file for kubectl and a cluster.rkestate, contains certificate and credential info.

Copy your kube_config to your .kube directory.

Save for backups but keep secure.

## Backing up the cluster

RKE defaults to making a snapshot every six hours and holding snapshots for one day.

Can save by "rke etcd snapshot-save" 

Can also configure etcd service to have "backup_config" key to backup by interval_hours, retention, and s3backupconfig.

## Restoring from a backup.

"rke etcd snapshot-restore". This is a destructive process.

## Upgrading K8

Rancher only supports latest 3 minor versions.
Change "kubernetes_version" in cluster.yaml and run "rke up".
Upgrade will start.

## Certificate Rotation

"rke cert rotate"

## Adding/Removing Nodes.

Just add/remove nodes at a cluster.yaml - Just make sure to do it one at a time. Add first before removing.

## Installing Rancher

Have two versions, Docker version and HA method that installs into RKE. Not compatible with each other.

### Docker - Installing Rancher

When you start the container, you'll pass it, at the minimum, the following options:
- -d to daemonize
- -p 80:80 -p 443:443 to pass through ports 80 and 443
- --restart=unless-stopped - you want this because the backup and upgrade processes require stopping the container. If you use always then you won't ever be able to stop it. You'll have to kill it, and then you can't restart it.

### Docker - Backing up Rancher

Need to back up data at "/var/lib/rancher" 

Docker Volume
- Stop container
- Create data container that uses same volume
- Extract path to tarball
- Move backup off the host

Bind-Mounted Volume
- Stop container
- Extract path to tarball
- Move backup off the host

### Docker - Restoring Rancher from backup

Docker-Volume
- Move the tarball you want to restore onto the Rancher server and place it in /opt/backup
- Stop the Rancher container
- Make a fresh backup of the current state of the Rancher server container
-  Run a temporary container that uses the volumes from the Rancher container and with a single command, remove the contents of /var/lib/rancher and then extract the tarball into it.
- Start the Rancher container

Bind-Mounted Volume
- Move the tarball you want to restore onto the Rancher server and place it in /opt
- Stop the Rancher container
- Move /opt/rancher to /opt/rancher.bak
- Extract the tarball. This will create a new /opt/rancher
- Start the Rancher container

### Docker - Upgrading Rancher

Docker Volume
- Stop the Rancher container
- Create a data container that uses the same volume
- Launch a temporary container that extracts `/var/lib/rancher` to alocal tarball
- Pull the latest or desired version of the Rancher server containerimage
- Start a new container with the same certificate options as the original container, adding a `--volumes-from` directive that pointsto the data container.
- Verify the upgrade by logging into the new Rancher server and confirming that it is operating correctly.
- Delete the stopped Rancher container so that it doesn't restart if the host is rebooted.

Bind-Mounted Volume
- Stop the Rancher container
- Create a tarball from the bind-mount directory
-  Pull the latest or desired version of the Rancher server container image
- Start a new container with the same certificate options as the original container, mounting the bind-mount host directory to "/var/lib/rancher"
- Verify the upgrade by logging into the new Rancher server and confirming that it is operating correctly.
- Delete the stopped Rancher container so that it doesn't restart if the host is rebooted.

### Kubernetes - Installing Rancher
Rancher can only be deployed into an RKE cluster for Rancher 2.4 and before.
Rancher 2.4 after can also be deployed into a K3s cluster

### Kubernetes - Deploying into RKE
- Choose a host name for rancher server: Select hostname for Rancher server environemnt
- Provision an RKE Cluster
- Deploy a Load Balancer in Front of the Cluster: Needs to be at layer 4 only
- Rancher is installed with Helm
- Create namespace

### Kubernetes - Making Backups
etcd datastore is used to hold Rancher configuration. Just back up cluster.

## Where will my Downstream Cluster Live?

- Hosted/Infrastructure Provide: EKS, AKS, GKE. Does full lifecycle of the resources
- Custom Provider: 
- Imported Clusters: Rancher will give you a "kubectl apply" command to run against the cluster that installs Rancher Agent

## Node Resource Requirements

- Try to keep control planes, etcd, workers on separate nodes
- Deploy workloads with resource constraints

## RKE Tempaltes 

- Templates that allow for specific cluster deploys.
- When updated, previous used clusters will show it needs to be updated and can be done so by cluster admi

## Node Templates and Cloud Credentials.

- Config to answer all of the questions for deploying a particular type of node in a cloud provider

## Cloud Proivder Configuration

- Need to do this before setting deploys of a certain resource by a cloud provider

## Deploying Downstream Cluster

- Hosted Provider
- Infrastructure Provider
- Custom Cluster

## Troubleshooting: Rancher API Server

- First place to look
- If HA Cluster, 3 pods will be running API server. Need to check each of them for logs.
- You can view the logs of the pods running within the cluster by looking at pods in the cattle-system namespace with the label app=rancher

## Troubleshooting the Container Runetime
- Find info in the logs for the container engine itself. 
- Will be on the host, either in an engine-specific location or in a logfile attached to syslog service

## Troubleshooting Node Service

- kubectl describe for each of the nodes to see specific sensor reports (DiskPressure, memory, etc)

## Troubleshooting: Kubelet on the Worker Nodes
- Check kubelet container logs for information

## Advanced Troubleshooting 

### etcd

- Is etcd constantly electing new leaders? This might indicate that there's something causing leaders to fail.
- Are all the etcd nodes members of the same cluster? If there's been a node partition, they may be trying to connect to each other but are finding that their cluster IDs are different
- Are there any active alarms in etcd that might prevent the cluster from receiving write data?

Log into data plane nodes and look at log output. use "etcdctl" within each of the etcd containers

### Control Plane
- Look at the logs on the control plane nodes. 
- Gotta find which is the leader.
- May have to look at the logs for every container

### Nginx Proxy 

- If service isn't running, other nodes won't be able to communicate with the kube-api-server container

## Using kubectl to communicate with cluster

- Can use kubectl as normal through Rancher UI or use kube-config locally. But gotta have one for each cluster, so use Rancher

## Using rancher CLI to communicate with clusters

- Rancher CLI wraps authenticated API calls in simple commands.
- Works with bearer tokens derived from an API Keys. 
- Most Rancher CLI commands apply to a specific project. A cluster and project, when combined form a context. Make sure to swithc to correct context
- Can also use "rancher kubectl" without all the configs

## Enable Advanced Monitoring

- Advanced monitoring deploys Prometheus and Grafana.

## Can configure Notifiers

- Notifiers are configured at cluster level and can integrate with most tools

## Configure Alerts

- Rancher installs default alerts with RKE, but need notifier set up
- Can bundle into Alert Groups
- Can set alaert timing
- Can set alert urgeny
- Can have Cluster or Project alerts

## Configure Logs
- Logs are captured and can be sent to ES, Splunk, Fluentd, Kafka, or syslog

## Namespaces
- Namespaces are a grouping of resources separate from others.
- A namespace group (Project) is a collection of namespaces. 
- Security can be provided at these levels 

## Projects as NameSpace Groups
- ConfigMaps/Secrets/Certificates/RegistryCredentails can be assigned to a project
- Workloads/Load Balancers/Service Discovery Records/PVC can only be assigned to a namespace within the project

## Resource Quotas
- Define total amount of particular resoure that project can use. 
- Set project limit and default limit for each namespace. 

## Resource Limits
- Resource limits set at a container level for any NEWLY created containers

## Working at Project Level
- Can set Monitoring at Project Level
- Can configure Notifier/Alerts at Projec Level
- Can configure logging at project level

## Namespace management
- Can move a namespace to different project from top-level cluster menu. 
- Not possible to move a namespace into project that already has a resource quota configured

## Deploying K8s Workload

- Can choose type of worload.
- Choose image type either from registry or will be pulled from docker hub. Careful choosing latest
- Add Ports: Will deploy respective Service. Won't work from imported YAML or KUBECTL
- Environment Variables: Specify manually or from ConfigMap/Secrets
- Node Scheduling: choose a node according to the labels that match the rules. Or use Taints/Tolerations.
- Health Check: K8 knows when to restart
- Volumes: Define and attach volumes
- Scaling/Upgrade Policy: Controls how many pods it starts at a time, and whether it starts new pods before killing old pods
- Command: What commands to run on container start
- Networking: Container level networking

You can import YAML directly but lose nice Rancher features
Can also add Sidecars (Another Container on Pod)

## Upgrading Workload
- Edit in UI or YAML

## Rollback Worloads
- Can be done. Pick a point in which to rollback to

## Provisioning Storage
- Static Provisioning: Creates an object for you to point to existing storage
- Dynamic Provising Using Storage Classes: Requests storage from cluster dynamically. 
- Storage Classes Define where to acquire storage and when to make the request.
