# Projects
## Projects (Individual)

There are four individual projects.  The deliverables for each project are:

*   Github project with source code and README.md explaining project
*   30 second to one minute Demo video showing how it works.  This demo video should be submitted into group discussion for the week it is due.  This will allow other students to learn from each other and exchange ideas.

### [Project 1](#project-1)
### Cloud Continuous Delivery of Microservice (MLOps or Data Engineering Focused)

*   Create a Microservice in Flask or Fast API
*   Push source code to Github
*   Configure Build System to Deploy changes
*   Use IaC (Infrastructure as Code) to deploy code
*   Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
*   Containerization is optional, but recommended

Reference Video(s):

*   Data Engineering with Python and AWS Lambda: [https://learning.oreilly.com/videos/data-engineering-with/9780135964330](https://learning.oreilly.com/videos/data-engineering-with/9780135964330)
*   Building AI & ML Applications on Google Cloud Platform: [https://learning.oreilly.com/videos/building-ai-applications/9780135973462](https://learning.oreilly.com/videos/building-ai-applications/9780135973462)

Reference Source Code: [https://github.com/noahgift/gcp-hello-ml](https://github.com/noahgift/gcp-hello-ml)

### [Project 2](#project-2)
### Kubernetes based Continuous Delivery

*   Create a customized Docker container from the current version of Python that deploys a simple python script.
*   Push image to DockerHub, or Cloud based Container Registery (ECR)
*   Project should deploy automatically to Kubernetes cluster
*   Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)

Reference Reading:  [https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch09.html#containers-docker](https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch09.html#containers-docker)

Reference Source Code: [https://github.com/noahgift/container-revolution-devops-microservices](https://github.com/noahgift/container-revolution-devops-microservices)

### [Project 3](#project-3)
### Cloud-based Big Data Systems Project

* Use a major Big Data system to perform a Data Engineering related task
* Example systems could be:  (AWS Athena, AWS Spark/EMR, AWS Sagemaker, Databricks, Snowflake)

Reference Labs:

* [Launching Dataproc Jobs with Cloud Computer-Qwiklabs](https://www.qwiklabs.com/focuses/3357?catalog_rank=%7B%22rank%22%3A9%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=4914241)
* [Distributed Image Processing in Cloud Dataproc-Qwiklabs](https://www.qwiklabs.com/focuses/5834?catalog_rank=%7B%22rank%22%3A7%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=4914974)
* [Perform advanced streaming data transformations with Apache Spark and Kafka in Azure HDInsight-Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/perform-advanced-streaming-data-transformations-with-spark-kafka/)
* [Getting Started: K-Means Clustering on SageMaker with SageMaker Spark SDK](https://github.com/aws/sagemaker-spark/blob/master/README.md)

Reference Readings:

* [Read Yahoo! Hadoop Tutorial](https://developer.yahoo.com/hadoop/tutorial/)
* [A very brief introduction to MapReduce](https://hci.stanford.edu/courses/cs448g/a2/files/map_reduce_tutorial.pdf)

(Optional) Reference Readings:  

* [https://learning.oreilly.com/library/view/python-for-programmers/9780135231364/ch16.xhtml#ch16](https://learning.oreilly.com/library/view/python-for-programmers/9780135231364/ch16.xhtml#ch16)
* [Programming Hive](https://learning.oreilly.com/library/view/programming-hive/9781449326944/ch01.html)


### [Project 4](#project-4)
### Serverless Data Engineering Pipeline

*   Reproduce the architecture of the example serverless data engineering project or perform something similar using only serverless technologies
*   Enhance the project by extending the functionality of the NLP analysis:  adding entity extraction, key phrase extraction, or some other NLP feature or doing Applied Computer Vision.

Reference Reading:  [https://github.com/noahgift/awslambda](https://github.com/noahgift/awslambda)

(Optional) Reference Media:  [https://learning.oreilly.com/videos/data-engineering-with/9780135964330](https://learning.oreilly.com/videos/data-engineering-with/9780135964330)

Reference Architecture Diagram:  [https://user-images.githubusercontent.com/58792/55354483-bae7af80-547a-11e9-9909-a5621251065b.png](https://user-images.githubusercontent.com/58792/55354483-bae7af80-547a-11e9-9909-a5621251065b.png)

### [Team Project](#team-project)
### Team Final Project Description (Team: 3-4)

*   Build a containerized or PaaS machine learning prediction model and deploy it in a scalable, and elastic platform:
    *   Options:
        *   ML Framework
            *   Sklearn, MXNet, PyTorch or Keras/TF
        *   Model
            *   Your own supervised ML prediction model or a Kaggle Prediction Model
        *   Platform
            *   Flask + Kubernetes deployed to EKS (Elastic Kubernetes) or Google Kubernetes Engine
            *   Flask + Google App Engine
            *   AWS Sagemaker
            *   Other (Upon Request)
*   Verify Elastic Scale-Up Performance via Load Test with [Locust](https://locust.io/), [Loader.io](https://loader.io), or a similar load test framework. (Start with 1 container or endpoint) and verify 2 or more inference endpoints scale up to 1K requests per second.
*   Deliverables:
    *   Source code in Github Project with README.md file that explains the project.
    *   Demo video showing project scaling to 1K+ requests served by multiple endpoints that scale-up.   The video should be between **one** to **five** minutes.  Videos over five minutes or under one minute will have points deducted.
    *   **One** to **five** minute in-person class presentation
*   Reference Project:
    *   [https://github.com/noahgift/container-revolution-devops-microservices](https://github.com/noahgift/container-revolution-devops-microservices)
*   (Optional) Reference Videos:
    *   Data Engineering with Python and AWS Lambda:  [https://learning.oreilly.com/videos/data-engineering-with/9780135964330](https://learning.oreilly.com/videos/data-engineering-with/9780135964330)
    *   Building AI & ML Applications on Google Cloud Platform:  [https://learning.oreilly.com/videos/building-ai-applications/9780135973462](https://learning.oreilly.com/videos/building-ai-applications/9780135973462)
    *   AWS Certified Machine Learning: _[https://learning.oreilly.com/videos/aws-certified-machine/9780135556597](https://learning.oreilly.com/videos/aws-certified-machine/9780135556597)
    
#### Additional considerations for final project

* Are you utilizing each person for what they do best:  Presentation, Coding, Math/Statistics/Data Science?
* Is this project resume worthy?
* How does the final presentation make your team look?
* Could this project land you a dream job?

## (Optional, but recommended:)

* The video should be at least 1080p with 16:9 aspect ratio.
* Consider recording with a  low-cost mic like follows:  https://www.amazon.com/Samson-Mic-Portable-Condenser-Microphone/dp/B001R76D42/ or equivalent at 48 kHz to 96 kHz.
* Build this into public Github portfolio with links to your videos in YouTube.
    
