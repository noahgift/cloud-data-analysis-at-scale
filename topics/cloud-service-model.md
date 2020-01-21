## Cloud Service Model 

There an overview of Cloud Computing available in the book [Python for DevOps, Chapter 9: Cloud Computing](https://learning.oreilly.com/library/view/python-for-devops/9781492057680/ch07.html).

### SaaS

SaaS (Software as a Service) is a hosted software product.  A google example is [Google Docs](https://www.google.com/docs/about/) or [Office 365](https://www.office.com/).  Generally these software products are hosted on cloud platforms and sold via a subscription model.

### Paas

PaaS (Platform as a Service) is a higher level abstraction for developing software.  A good example of a PaaS is [Heroku](https://www.heroku.com/).  This allows a developer in a language like Ruby, Python, PHP or Go to focus mostly on the business logic of their application.

A real-world scenario comparision would be a self-service car wash versus a drive through car wash.  In the drive through car wash a customer only has to drive through, not use equipment to wash their car.

### IaaS

IaaS (Infrastructure as a Service) refers services that provide low level resources:  Compute, Storage, and Networking.  Typically these service are low cost to use, but require more setup and expertise.  On Amazon these services would be:  EC2 (Compute) and S3 (Storage).

A real-world comparison would be buying grain or beans in bulk from a company like Costco then using those resource to create a meal.  The cost would be much lower than buying a full meal from a restaurant, but requires time and skill to convert to a meal.

### MaaS

MaaS (Metal as a Service) is the ability to rent actual servers that are not virtualized.  One of the advantages of this approach is for specialized scenarios like training deep learning models.  A compute operation may require the highest amount of resources available.  Virtualization causes some overhead and eliminating it will allow these specialized operations to fully access the "metal".

### Serverless

Serverless refers to running without thinking about servers.  A good example of this is [AWS Lambda](https://aws.amazon.com/lambda/).  The benefit to using serverless has many benefits.  One benefit is the ability to focus on writing functions vs managing servers.  Another benefit is the ability to use new paradigms like event driven programming against cloud-native resources.  

### Building Three Websites

This is a step by step Demo of three websites getting built (AWS Static S3, AWS Lambda in Python and EC2 Spot Instance):

<!---
{type: video, poster: "http://img.youtube.com/vi/acmuuHhrmSs/mqdefault.jpg"}
-->

* [Demo:  A Tale of Three Websites](https://www.youtube.com/watch?v=acmuuHhrmSs)

#### Instructions AWS S3 Website

1.  Follow [S3 Hosting Instructions here](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html), (as shown in screencast ["A Tale of Three Websites"](https://www.youtube.com/watch?v=acmuuHhrmSs)) 


#### Instructions AWS Lambda Website

1.  Use AWS Cloud9 and "right click" to a new lambda function (as shown in screencast ["A Tale of Three Websites"](https://www.youtube.com/watch?v=acmuuHhrmSs))

2.  Paste the code below into the editor.

The following example demonstrates the Python code necessary to build a Lambda function that returns HTML.

```python
def lambda_handler(event, context):
    content = """
    <html>
    <p> Hello website Lambda </p>
    </html>
    """
    response = {
        "statusCode": 200,
        "body": content,
        "headers": {"Content-Type": "text/html",},
    }
    return response
```

3.  "Right-click" deploy the lambda function
4.  Log into AWS console and click on the API Gateway icon in the AWS Lambda section.  Verify that it returns "Hello website Lambda".

#### Instructions AWS Lambda Website 

*(Optional)*

1. Follow tutorial on setting up [LAMP Site here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html)

Feel free to improvise and follow the simpler guide shown (as shown in screencast ["A Tale of Three Websites"](https://www.youtube.com/watch?v=acmuuHhrmSs)) 

### Exercise

* Topic:  Create Three Different types of Websites 
* Estimated time:  30+ minutes
* Slack Channel:  #noisy-exercise-chatter
* People:  Individual or Final Project Team
* Directions:
    * Part A:  Create S3 static hosted website
    * Part B:  Create AWS Lambda website
    * Part C:  (If time permits) Create EC2 based website 

