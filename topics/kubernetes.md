## Kubernetes

### Install Kubernetes

The simplest way to install Kubernetes is to use [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/#kubernetes) or [Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/kubernetes/). This comes with the `kubectl` kubernetes command line tool.

The next recommended way is to use a cloud shell environment like [AWS Cloud9](https://aws.amazon.com/cloud9/) or [Google Cloud Shell](https://cloud.google.com/shell/).  These cloud environments dramatically simplify issues that crop up on a laptop or workstation.  You can follow the [native packagement guide from the official documentation here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux).

A more advanced method for experts could be to directly download the latest binary. *HINT:  You probably don't want to use this method and should use an easier method above*  

OS X install latest `kubectl` release:

```bash
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
```

Linux install latest `kubectl` release:

```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
```

### Overview of Kubernetes

What is [Kubernetes](https://github.com/kubernetes/kubernetes)?  It is an open source orchestration system for containers developed by Google and open sourced in 2014.  Kubernetes is a useful tool for working with containerized applications. Given our previous work with Docker containers and containerizing an app, working with Kubernetes is the next logical step. Kubernetes was born out of the lessons learned in [scaling containerized apps at Google](https://queue.acm.org/detail.cfm?id=2898444), and is used for automating deployment, scaling and managing such containerized applications.

* What are benefits of using Kubernetes?

Kubernetes is the standard for container orchestration.  All major cloud providers support Kubernetes. Amazon through [Amazon EKS](https://aws.amazon.com/eks/), Google through [Google Kubernetes Engine GKE](https://cloud.google.com/kubernetes-engine) and Microsoft through [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/kubernetes-service/).

Kubernetes is also a framework for running distributed systems at ["planet scale"](https://kubernetes.io/).  Google uses it to run billions of containers a week. 

* A few of the Capabilities of kubernetes include:
    - High availability architecture
    - Auto-scaling
    - Rich Ecosystem
    - Service discovery
    - Container health management
    - Secrets and configuration management

The downside of these features is the high complexity and learning curve of Kubernetes.  You can read more about the features of Kubernetes through the [official documentation](https://kubernetes.io/docs/home/).

* What are the basics of Kubernetes?

The core operations involved in Kubernetes include creating a Kubernetes Cluster, deploying an application into the cluster, exposing an application ports, scaling an application and updating an application.

![kubernetes-basic-workflow](https://user-images.githubusercontent.com/58792/73751322-e4253c00-472c-11ea-8caf-6ce84d89f2c8.png)

* What is the Kubernetes (cluster) architecture?

The core of Kubernetes is the cluster.  Containers run in the cluster.  The core components of the cluster include a cluster master and nodes.  Inside there nodes there is another hierarchy.  This is shown in the diagram. A Kubernetes node can contain multiple pods, which in turn can contain multiple containers and/or volumes.

![kubernetes-hierarchy](https://user-images.githubusercontent.com/58792/73753736-22245f00-4731-11ea-9196-ba22b71e89c2.png)

* How do you setup a Kubernetes cluster?

There are two main methods:  setup a local cluster (preferably with Docker Desktop) or provision a cloud cluster: Amazon through [Amazon EKS](https://aws.amazon.com/eks/), Google through [Google Kubernetes Engine GKE](https://cloud.google.com/kubernetes-engine) and Microsoft through [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/kubernetes-service/).

If you are using Docker and have [enabled kubernetes](https://docs.docker.com/docker-for-mac/#kubernetes) then you already have a standalone Kubernetes server running.  This would be the recommended way to get started with Kubernetes clusters.

* How do you launch containers in a Kubernetes cluster?

Now that you have Kubernetes running via Docker desktop how to do you launch a container?  One of the [easiest ways is via](https://docs.docker.com/docker-for-mac/kubernetes/) the `docker stack deploy --compose-file` command.

The `yaml` example file looks like the following:

```yaml
version: '3.3'

services:
  web:
    image: dockersamples/k8s-wordsmith-web
    ports:
     - "80:80"

  words:
    image: dockersamples/k8s-wordsmith-api
    deploy:
      replicas: 5
      endpoint_mode: dnsrr
      resources:
        limits:
          memory: 50M
        reservations:
          memory: 50M

  db:
    image: dockersamples/k8s-wordsmith-db
```

This could be deployed with the following command:

```bash
docker stack deploy --namespace my-app --compose-file /path/to/docker-compose.yml mystack
```


### Autoscaling Kubernetes

One of the "killer" features of Kubernetes is the ability to setup auto-scaling via the [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). How does this work? The Kubernetes HPA (Horizontal Pod Autoscaler) will automatically scale the number of pods (*remember they can contain multiple containers*) in a replication controller, deployment or replica set.  The scaling is based on CPU utilization, memory or custom metrics defined in the Kubernetes Metrics Server.

![kubernetes-hpa](https://user-images.githubusercontent.com/58792/73760449-53099180-473b-11ea-8710-854d6068959e.png)

There is a Docker article[Kubernetes autoscaling in UCP](https://success.docker.com/article/kubernetes-autoscaling-in-ucp) that is a good guide to go deeper on this topic and experiment with it yourself.

## Cloud Kubernetes Services

### EKS (Amazon Elastic Kubernetes Service)

### GKE (Google Kubernetes Engine)


### Kubernetes Summary

There are many compelling reasons to use Kubernetes.  Let's summarize them:

* Created, Used and Open Sourced by Google
* High availability architecture
* Auto-scaling is built in
* Rich Ecosystem
* Service discovery
* Container health management
* Secrets and configuration management

Another advantage is that Kubernetes is cloud agnostic and it could be a solution for companies that are willing to take on the additional complexity to protect against "vendor lockin".



### Exercise

* Topic:  Go through Kubernetes Engine: [Qwik Start Lab](https://www.qwiklabs.com/focuses/878?parent=catalog)
* Estimated time:  20-30 minutes
* People:  Individual or Final Project Team
* Slack Channel:  #noisy-exercise-chatter
* Directions:
    * Part A:  Complete Lab
    * Part B:  Try to convert Docker project to Kubernetes (In class or at home)

### References

* [Kubeflow Fairing:  ML models with kubernetes](https://github.com/kubeflow/fairing)