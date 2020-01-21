# Questions and Answers


## AWS Q&A

These are some common questions and answers about AWS.

---
**Question**: How do I setup a billing alert?  

**Answer**: You can follow the documentation here:  [Billing Alert Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)  

---


---
**Question**: I am having trouble connecting [RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) and sharing connections with a group of people.  Is there an easier method?

**Answer**: You may find it more straightforward to use AWS Cloud9 as a development environment to connect to RDS.  You can see a [walkthrough here](https://aws.amazon.com/getting-started/tutorials/configure-connect-serverless-mysql-database-aurora/)

---
---
**Question**: The cloud services model is confusing.  What is PaaS and how is it different than other models?

**Answer**: One way to think about cloud offerings is to compare it to the food industry.  You can purchase food in bulk at a store like [Costco](https://www.costco.com/).  They have considerable scale and they can pass the purchase price discounts down to the customer.  As a customer though, you may also need to take that food back to your home, prepare it and cook it.  This is similar to IaaS.

Now let's look at a service like [Grubhub](https://www.grubhub.com/) or [Uber Eats](https://www.ubereats.com/en-US/).  Not only do you not have to drive to the store to pickup the food, but it has been prepared, cooked and delivered for you.  This is similar to PaaS.  All you have to do is eat the food.

If you look at PaaS (Platform as a Service), what it means is as the developer you can focus on the business logic.  Many of the complexities of software engineering are eliminated.  A good example of two early PaaS services are [Heroku](https://www.heroku.com/) and [Google App Engine](https://cloud.google.com/appengine/).  A good example of a [PaaS on AWS is AWS Sagemaker](https://aws.amazon.com/blogs/machine-learning/bring-your-own-deep-learning-framework-to-amazon-sagemaker-with-model-server-for-apache-mxnet/).  It solves many of the infrastructure issues involved with creating and deploying machine learning including distributed training and serving predictions.

---
---
**Question**: What is the exact definition of an edge location, it is confusing.

**Answer**: An [AWS edge location](https://aws.amazon.com/cloudfront/features) is a physical location in the world where a server lives.  Edge locations are different than datacenters because they serve a more narrow purpose.  The closer a user of the content is to the physical location of the server, the lower the latency of the request.  This is important in content deliver like streaming videos and music, and also for playing games.  The most commonly referred to edge service on AWS is CloudFront.  CloudFront is a CDN (Content Deliver Service).  Cached, or copies of the same movie file live in these locations all over the world via the CDN.  This allows users to all have a great experience streaming this content.

Other services that use edge locations include:  [Amazon Route 53](https://aws.amazon.com/route53/), [AWS Shield](https://aws.amazon.com/shield/), [AWS Web Application Firewall](https://aws.amazon.com/waf/) and [Lambda@Edge](https://aws.amazon.com/lambda/edge/).

---

---
**Question**: What if one data centers in an AZ and it gets affected by a fire?  Related to this how should a system be architected for data replication?

**Answer**: As part of the [shared security model](https://aws.amazon.com/compliance/shared-responsibility-model/), Amazon is responsible for the cloud and the customer is responsible for what is in the cloud.  This means that data is protected against catastrophic unplanned failures like fires.  If there is an outage, the data may be unavailable during the outage in that region, but will be restored.

As an architect, it is the customers responsibility to take advantage of multi-AZ architectures.  A good example of this is [Amazon RDS multi-AZ configuration](https://aws.amazon.com/rds/details/multi-az/).  In the event of an outage in one region the secondary slave database will already have the data replicated and be able to handle the request.

---

---
**Question**: What is HA (Highly Available)?

**Answer**: An HA (Highly Available) service is one that has been designed with availability in mind.  This means that failure has been expected and the design supports redundancy of data and services.  A good example of a HA service is [Amazon RDS](https://aws.amazon.com/rds/ha/).  RDS Multi-AZ design supports minimal interruption in service by allowing for multiple versions of the database to be replicated across availability zones.

---

---
**Question**: How do you decide between spot and on demand?

**Answer**: Both spot and on-demand instances are billed fixed for the first-minute and then by the second.  Spot instances are the most cost effective because they can provide up to 90% savings.  [Spot instances](https://aws.amazon.com/ec2/spot/) are used when it doesn't matter when a task is run or if it is interrupted.  In practice this creates a very large use case for spot.  What are some examples use cases for spot instances?

* Experimenting with an AWS service
* Training deep learning or machine learning jobs
* Scaling out a webservice or other service in combination with on-demand instances

On-demand instances can be used when a workload is run in steady state.  For example, a web service that is in production wouldn't want to only use spot instances.  Instead it could start with on-demand instances and when the usage of the service was determined (i.e. 2 C3.large instances), then [reserved instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) should be bought.

---
---
**Question**: How does spot hibernation work?

**Answer**: There are a few reasons for [spot instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html) including price (bid higher than maximum price), capacity (there are not enough spot instances unused), constraints (i.e. Availability Zone cannot be met).  To hybernate, it must have an EBS root volume.

---

---
**Question**: What is a tag for in EC2?

![tag](https://user-images.githubusercontent.com/58792/71584976-f33c1d00-2ae2-11ea-8412-cbe5f7a9aa0f.png)


**Answer**: The main reason to use a tag for an EC2 resource is to attach metadata to a group of machines.  Here is one scenario.  Let's say there are 25 EC2 instances running a shopping website and they have no tags.  Later a user spins up another 25 EC2 instances to temporarily do a task like train a machine learning model.  It may be very challenging in the console to determine which machines are the temporary machines (and can be deleted) and which are the production machines that cannot be deleted.

Instead of guessing about the roles of machines, it is a best practice to assign tags to allow a user to quickly identify a role.  This role could be:  Key="role", Value="ml" or it could be Key="role", Value="web".  In the EC2 console a user can query by tag.  This then allows for bulk operations like terminating instances.  Tags can also play an important role in analyzing cost.  If machine roles are set, then cost reports could determine if certain machine types are too expensive or using too many resources.

You can read the [official tag documentation here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

---

---
**Question**: What is PUTTY

![putty](https://user-images.githubusercontent.com/58792/71585331-2af79480-2ae4-11ea-94dd-81935d0e97e9.png)


**Answer**: Putty is a free ssh client used on the Windows operating system.  OS X and Linux has built in support for SSH.  What is SSH?  It is a crypotographic network protocol for performaning network operations.  SSH is typically used to log into a remote machine and manage the machine via terminal commands.

You can read the [official putty documentation here](https://www.chiark.greenend.org.uk/~sgtatham/putty/).

---

---
**Question**: How is Lightsail different than EC2 or other services

**Answer**: Lightsail is a PAAS or Platform as a Service.  This means that a developer only needs to worry about configuring and developing the wordpress application.  EC2 is lower level and is called IAAS (Infrastructure as a Service).  There is a spectrum with cloud computing where lower level services are provided just like bulk ingrediants at a store like Costco.  Those bulk ingrediants can be used to create meals, but it requires skill.  Likewise, a person can order meals to get delivered to their house.  These meals are more expensive but require less or no skill.  Platform as a Service is similar, user pays more for higher level services. 

Other PAAS solutions (outside of AWS) are:  [Heroku](https://www.heroku.com/) and [Google App Engine](https://cloud.google.com/appengine/).

You can read more about types of Cloud Services in the [Cloud Computing chapter of Python for DevOps](https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch09.html#idm45611881596904).

---

---
**Question**: In 3.1 compute services, the AMI has following user case: “use it to copy that to a fleet of machines (deep learning cluster)”. What’s this a fleet of machine means?

![fleet](https://user-images.githubusercontent.com/58792/71586319-c9d1c000-2ae7-11ea-93ae-742f0b95efb7.png)


**Answer**: A fleet works the same way a rental car company works.  When you are asked for a reservation for a car they will ask you to pick a group:  compact, sedan, luxury, or truck.  There is no guarantee of a specific model, only of a specific group.  Likewise, because spot instances are an open market, it is possible that a particulary machine, say C3.8XLarge is not available, but a similar machine is.  By selecting a fleet you can request a group of machines that will have similar:  CPU, Memory and Network capabilities.

You can read more about [EC2 Fleet here](https://aws.amazon.com/blogs/aws/ec2-fleet-manage-thousands-of-on-demand-and-spot-instances-with-one-request/).

---

---
**Question**: In 3.1 compute service, what does spikey means for the sizing of on-demand instance?

![spike](https://user-images.githubusercontent.com/58792/71586546-97749280-2ae8-11ea-99c1-e528b4dd40c4.png)

**Answer**: A "spikey" workload could be a website that suddenly gets 10X the traffic.  Let's say this website sells products.  During the year, it is normally a flat amount of traffic, but around December the traffic spikes to 10X the normal traffic.  This would be a good use case for "on-demand" instances to scale out to meet this requirement.  The normal traffic pattern should use reserved instances, but for the spike, this should use on-demand.  

* You can read more about [spikey traffic here](https://aws.amazon.com/blogs/networking-and-content-delivery/visitor-prioritization-on-e-commerce-websites-with-cloudfront-and-lambdaedge/).

* You can read more about [reserved instances here](https://aws.amazon.com/blogs/aws/new-savings-plans-for-aws-compute-services/)

---

---
**Question**: What does the “SUBSECOND” means for one of the Lambda’s advantage?

**Answer**: This means that you can design a service that is efficient and you only be charged for the duration of your request at 100ms intervals.  This is different that an EC2 instance where you are billed for a constantly running instance every second.  With a Lambda function you can design an event based workflow where a lambda only runs in response to events. A good analogy would be a traditional light that has to be turned off and on.  It is easy to use more electricity because the light has to be manually turned off and on.  A more efficient approach is motion detection lighting.  The lighting will turn off and on according to motion.  This is similar to AWS Lambda, in response to events, it turns on, performs a task and then exits.

* You can read more about [Lambda Here](https://aws.amazon.com/lambda/)
* You can build a [Python AWS Lambda project here](https://github.com/noahgift/awslambda)

---

---
**Question**: For AWS S3, there are several storage classes. Is the IA includes both S3 Standard IA and one-zone IA, but not parallel three shown in the ppt? Because I only see standard and one-zone in the section of INFREQUENT ACCESS in AWS website https://aws.amazon.com/s3/storage-classes/

**Answer**: 

There are two types of IA (Infrequent Access).  Standard-IA which is stored in three AZ (availability zones) and One Zone.  A key difference in the One Zone is availability.  It is designed for 99.5% availability, meaning that is less available than both three zone IA and Standard.  The lower cost is reflected in this diminished availability.

---

**Question**: How does EFS work?

**Answer**: 

EFS conceptually works similar to Google Drive or Dropbox.  You can create a dropbox account and share data with multiple computers or friends.  EFS works in a very similar way.  The exact same file system can be accessed by machines that mount it.  This is very different than EBS (Elastic Block Storage), which can only be used by one machine at a time.

---

---

**Question**: For ELB’s Use Case, don’t understand what’s the first two:
1) what’s “the single point of access” meaning? Is it saying, if you can control your traffic by entering through one port or server, then it’s is more secure?
2) what’s the “decoupling application environment” meaning? 


**Answer**: 

Let's look at a website as an example.  The website will be running on port 443 which is the port for HTTPS traffic.  This site could be https://example.com.  The ELB is the only resource that is exposed to the outside world.  When a web browser conntect to https://example.com it only communicates to the ELB.  At the same time the ELB will ask the webservers behind it for the information.  It then sends that information back to the web browser.

What is an analogy in the real world?  It would be a like a bank teller in a drive through.  You drive up to the window, but are only exposed to the bank teller.  Inside the bank, there are many people working.  You only are exposed to a window though, and interact with one person.


You can read blog posts about (ELB here)[https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/elastic-load-balancing/]

---

---

**Question**: 10.	Why is the use case for ELB the totally the same as the Classic Load Balance? 
(They are both : 1) access through single point of access, 2) Decouple Application Environment; 3) Provide High Availability  and Fault Tolerance 4) Increase Elasticity and Scalability



**Answer**: 

Elastic Load Balancing refers to a category of load balancers.  There is Application Load Balancer, Network Load Balancer and Classic Load Balancer.  At a high level, the classic load balancer is an older load balancer that has less features than the Application Load Balancer.  It should be used in sutuations where older EC2 instances having been in service.  These are called EC2 classic instances.

In a new scenario, an Application Load Balancer would be an ideal choice for something like a HTTP service.
You can read blog posts about (ELB feature comparisons here)[https://aws.amazon.com/elasticloadbalancing/features/#compare]

---