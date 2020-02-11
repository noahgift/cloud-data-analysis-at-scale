## Operationalizing a Microservice Overview

One important factor in developing a microservice is to think about the feedback loop.  In this diagram, a [GitOps](https://queue.acm.org/detail.cfm?id=3237207) style workflow is described.  

* Application is stored in Git
* Changes in Git trigger the continuous delivery server which tests and deploys the code to a new environment.  This environment is configured as code Infrastructure as Code (IaC).
* The microservice which could be a containerized service running in Kubernetes or a FaaS (Function as a Service) running on AWS Lambda has logging, metrics, and instrumentation.
* A load test using a tool like [locust](https://locust.io/)

![operationalize-microservice](https://user-images.githubusercontent.com/58792/73959929-11621d80-48d8-11ea-9d9a-8a29b802cb96.png)

* When the performance and auto-scaling is verified the code is merged to production and deployed

What are some of the items that could be alerted on with Kubernetes?

* Alerting on application layer metrics
* Alerting on services running on Kubernetes
* Alerting on the Kubernetes infrastructure
* Alerting on the host/node layer

How could you collect metrics with Kubernetes and Prometheus?  Here is a diagram that walks through a potential workflow. A few things to note here are that are two pods.  One pod is dedicated to the Prometheus collector and the second pod has a "sidecar" Prometheus container that sits alongside the Flask application.  This all propagates up to a centralized monitoring system that visualizes the health of the clusters and trigger alerts.

![prometheus-kubernetes](https://user-images.githubusercontent.com/58792/73962194-f691a800-48db-11ea-8969-0d6c74827599.png)

Another helpful resource is an official sample project from Google Cloud [Monitoring apps running on multiple GKE clusters using Prometheus and Stackdriver](https://cloud.google.com/solutions/monitoring-apps-running-on-multiple-gke-clusters-using-prometheus-and-stackdriver)

### Creating effective alerts

At one company I worked at there was a homegrown monitoring system (again initially created by the founders) that alerted on average every 3-4 hours, 24 hours a day.

Because everyone in engineering except the CTO was on call, most of the engineering staff was always sleep deprived because it guaranteed that every night there were alerts about the system not working.  The "fix" to the alerts was to restart services.  I volunteered to be on call for one month straight to allow engineering the time to fix the problem.  This sustained period of suffering and lack of sleep led me to realize several things.  One, the monitoring system was no better than random.  I could potentially replace the entire system with a random coin flip.

![prometheus-kubernetes](https://user-images.githubusercontent.com/58792/73963359-1e820b00-48de-11ea-8d22-dc5e1271e4b4.png)

Even more distressing in looking at the data was that engineers had spent YEARS of their life responding to pages and getting woken up at night and it was utterly useless.  The suffering and sacrifice accomplished nothing and reinforced the sad truth that life is not fair.  The unfairness of the situation was quite depressing, and it took quite a bit of convincing to get people to agree to turn off the alerts.  There is a built-in bias in human behavior to continue to do what you have always done.  Additionally, because the suffering was so severe and sustained, there was a tendency to attribute a deeper meaning to it.  Ultimately, it was a false God. *Reference: Gift, Noah (2020) Python for DevOps: pg. 226*
