## AWS Lambda

AWS Lambda is a building block for many things on AWS.  

SCREENCAST:  AWS Lambda as a Garage Lightbulb
[![Hello World Lambda](https://img.youtube.com/vi/nNKYwxf96bk/0.jpg)](https://youtu.be/nNKYwxf96bk)


SCREENCAST:  Hello World Lambda
[![Hello World Lambda](https://img.youtube.com/vi/Z6DhCYv42P4/0.jpg)](https://youtu.be/Z6DhCYv42P4)


SCREENCAST:  Marco Polo Lambda
[![Hello World Lambda](https://img.youtube.com/vi/AlRUeNFuObk/0.jpg)](https://youtu.be/AlRUeNFuObk)

[gist for Marco](https://gist.github.com/noahgift/3b51e8d800ea601bb54d093c7114f02e)

```python
def lambda_handler(event, context):
  if event["name"] == "Marco":
    return "Polo"
```

[gist for Polo](https://gist.github.com/noahgift/f2f5f2bc56a3f39bf16de61dbc2988ec)

```python
def lambda_handler(event, context):
  if event["name"] == "Polo":
    return "Marco"
```

## Developing AWS Lambda Functions with AWS Cloud9

Cloud9 has many capabilities built in the make developing with AWS Lambda easier.  These include debugging, importing remote lambda functions and a wizard.

SCREENCAST:  Develop AWS Lambda functions with AWS Cloud9
[![Hello World Lambda](https://img.youtube.com/vi/QlIPPNxd7po/0.jpg)](https://youtu.be/QlIPPNxd7po)

### Building an API

The following code can be used as an API via API Gateway.

*Python Lambda API Gateway Example*

```python
import json
import decimal


def lambda_handler(event, context):

  print(event)
  if 'body' in event:
    event = json.loads(event["body"])
  
  amount = float(event["amount"])
  res = []
  coins = [1,5,10,25]
  coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
  coin = coins.pop()
  num, rem  = divmod(int(amount*100), coin)
  res.append({num:coin_lookup[coin]})
  while rem > 0:
    coin = coins.pop()
    num, rem = divmod(rem, coin)
    if num:
      if coin in coin_lookup:
        res.append({num:coin_lookup[coin]})

  response = {
    "statusCode": "200",
    "headers": { "Content-type": "application/json" },
    "body": json.dumps({"res": res})
  }

  return response
```


## AWS Step Functions

A key advantage of AWS Step functions is the ability to pipeline actions together.

![Screen Shot 2020-03-24 at 2 24 27 PM](https://user-images.githubusercontent.com/58792/77462944-30126a00-6ddb-11ea-8fbc-bdc2e19bab25.png)

SCREENCAST:  Develop AWS Lambda functions with AWS Cloud9
[![Hello World Lambda](https://img.youtube.com/vi/UFGwKXe9NtQ/0.jpg)](https://youtu.be/UFGwKXe9NtQ)

Reference:  [Web Scraping Pipeline Github Project](https://github.com/noahgift/web_scraping_python)


Here is a Marco Polo Step Function:

* [gist of marco polo step function](https://gist.github.com/noahgift/017a083fcd3f008567aca581e5fd29ea)

```json
{
  "Comment": "This is Marco Polo",
  "StartAt": "Marco",
  "States": {
    "Marco": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:561744971673:function:marco20",
      "Next": "Polo"
    },
    "Polo": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:561744971673:function:polo",
      "Next": "Finish"
    },
    "Finish": {
      "Type": "Pass",
      "Result": "Finished",
      "End": true
    }
  }
}
```
Note that the input of one Lambda goes into the input of another:

![Screen Shot 2020-03-24 at 6 38 40 PM](https://user-images.githubusercontent.com/58792/77483553-cf952400-6dfe-11ea-8659-4904214210ec.png)



## Building a serverless data engineering pipeline

One strong use case for AWS Lambda is to build serverless data engineering pipelines.

![serverless_ai_pipeline](https://user-images.githubusercontent.com/58792/55354483-bae7af80-547a-11e9-9909-a5621251065b.png)

SCREENCAST:  Build Serverless Data Engineering Pipeline
[![Build Serverless Data Engineering Pipeline](https://img.youtube.com/vi/zXxdbtamoa4/0.jpg)](https://youtu.be/zXxdbtamoa4)

* [Reference Github Project AWS Lambda](https://github.com/noahgift/awslambda)

### Exercise:  AWS Lambda + Step Functions

* Topic:  Build a step function pipeline
* Estimated time:  20 minutes
* People:  Individual or Final Project Team
* Slack Channel:  #noisy-exercise-chatter
* Directions (Do one or both):

    * Basic Version: Create an AWS Lambda function that takes an input and run it inside of a Step Function
    * Advanced Version: Create an AWS Lambda function that takes an input and run it inside of a Step Function, then send the output to another AWS Lambda.  See the Marco Polo Step Function above.
    * Share screenshot + gist in slack.