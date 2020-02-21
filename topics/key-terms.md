# Key Terms and Industry Jargon

## Build Server

A build server is an application that is used in both the testing and deployment of software.  Popular build servers can be both SaaS or open source.  Here are a few popular options:

* [Jenkins](https://jenkins.io/):  Open source build server that can run anywhere including AWS, GCP, Azure a docker container or on your laptop.
* [CircleCI](https://circleci.com/):  A SaaS build service that integrates with popular git hosting providers like [Github](https://github.com/).


### Microservice  

A lightweight loosely coupled service.  It can be as small as a function.

### FaaS (Function as a Service)

A type of cloud computing that facilitates functions that respond to events.

### AWS Lambda

A serverless compute platform by AWS that has FaaS capability.

### Cloud-Native applications

Cloud-Native applications are services that utilize the unique capabilities of the cloud, like serverless.

### SQS Queue

A distributed messaging queue built by Amazon with near-infinite reads and writes.

### Serverless

Serverless is a technique of building applications based on functions and events.

### Moore's Law

The perception that for some time the number of transistors on a microchip doubles every two years.

### AWS Cloud9

AWS Cloud9 cloud-based development environment running in AWS.  It has special hooks for developing serverless applications.

### Python Virtual Environment

A python virtual environment is created by isolating a python interpreter to a directory and installing packages in that directory.  The python interpreter can perform this action via `python -m venv yournewenv`.

### Container

A container is a set of processes that are isolated from the rest of the operating system.  They are often megabytes in size.

### Virtual Machine

A virtual machine is the emulation of a physical operating system.  The can be Gigabytes in size.

### Docker Format Container

There are several formats for containers.  An emerging form is Docker, which involves the definition of a `Dockerfile.`

### pip

The `pip` tool installs Python packages.

### pylint

The `pylint` tool checks the Python source code for syntax errors.

### black

The `black` tool formats the text of Python source code automatically.

### pytest

The `pytest` tool is a framework for running tests on Python source code.

### IPython

The `ipython` interpreter is an interactive terminal for Python.  It is the core of the Jupyter notebook.

### Makefile

A `Makefile` is a file that contains a set of directives used to build software.  Most Unix and Linux operating systems have built-in support for this file format.

### CircleCI

A popular SaaS (Software as a Service) build systems used in DevOps workflows.

### Docker

Docker is a company that creates container technology, including an execution engine, collaboration platform via DockerHub and a container format called `Dockerfile.`

### Amazon ECR

Amazon ECR is a container registry that stores Docker format containers.

### Swagger

A swagger tool is an open-source framework that simplifies the creation of API documentation.

### Data Engineering

Data Engineering is the process of automating the flow of data.

### Ports

A port is a network communication endpoint.  An example of a port is a web service running on port 80 via the protocol HTTP.

### JSON

JSON stands for JavaScript Object Notation, and it is a lightweight, human-readable data format used heavily in web services.


### Kubernetes

Kubernetes is an open-source system for automating the operations of containerized applications.  Google created it and open-sourced in 2014.

### Amazon EKS

Amazon EKS is a managed Kubernetes service created by Amazon.

### Google GKE

Google GKE is a managed Kubernetes service created by Google.

### Azure Kubernetes Service AKS

Azure Kubernetes Service is a managed Kubernetes service created by Google.

### YAML

YAML is a human-readable serialization format often used in configuration systems.  It is easily portable to JSON format.

### Kubernetes Pods

A Kubernetes pod is a group of one or more containers.

### Kubernetes Containers

A Kubernetes container is a Docker image that deploys into a Kubernetes cluster.

### Kubernetes Clusters

A Kubernetes cluster is a deployment of Kubernetes that contains the entire ecosystem of Kubernetes components, including nodes, pods, the API, and containers.

### Prometheus

Prometheus is an open-source monitoring system with an efficient time-series database.

### Logging

Logging is a process of creating messages about the running state of a software application.

### Autoscaling

Autoscaling is the process of scaling load up or down automatically based on how many resources the nodes are using.

### Alerts

Alerts are health metrics that have actions associated with them.  An example would be an alert that sends a text message to a software engineering when a web service returns multiple error status codes.

### Operationalization

The process of making an application ready for production deployment.  These actions could include monitoring, load-testing, setting up alerts, and load-testing.

### Metrics

Metrics are the creation of KPIs (Key Performance Indicators) for a software application.  An example of a parameter is the percentage of CPU used by a server.

### Disaster recovery

Disaster recovery is the process of designing a software system to recover despite a disaster.  This process could include archiving data to another location.

### Migrate

Migrate is the ability to move an application from one environment to another.  

### Continuous Integration

Continuous Integration is the process of automatically testing software upon check in to the source control system.

### Continuous Delivery

Continuous Delivery is the process of delivering tested software automatically to any environment.

### Load Testing

Load testing is the process of verifying the scale characteristics of a software system.

### Locust

Locust is a load-testing framework that accepts Python formatted load test scenarios.