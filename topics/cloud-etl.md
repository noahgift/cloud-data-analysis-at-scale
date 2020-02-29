## Cloud ETL

The cloud takes complex problems that could be currently solved by a team of 50 people and allows it to be a button click.  In the "real world" you have to automate the data pipeline via ETL (Extract, Transfer, Load) process.  The diagram below shows how  AWS S3 is the central repo for the data.  

![aws-glue-athena](https://user-images.githubusercontent.com/58792/75614653-067e5f80-5b09-11ea-88a4-dfa94aaa4249.jpeg)

Next, [AWS Glue](https://aws.amazon.com/glue/) indexes the cloud storage bucket and creates a database that can be used by [AWS Athena](https://aws.amazon.com/athena/).  What is unique about this? 

* Almost no code (only a little SQL to query)
* Serverless
* Automatable

Here is a screencast of AWS Glue and AWS Athena working together to catalogue data and search it at scale:

[![AWS Glue](https://img.youtube.com/vi/vqubkjfvx0Q/0.jpg)](https://www.youtube.com/watch?v=vqubkjfvx0Q)

## Real-World Problems with ETL Building a Social Network From Scratch

### Cold-Start Problem

How do you bootstrap a social network and get users?

![cold start](https://user-images.githubusercontent.com/58792/61975603-8e224f80-afb7-11e9-9c4f-c06b89a5b6eb.png)

### Building Social Network Machine Learning Pipeline From Scratch

How can you predict impact on platform from social media signals?

![ml pipeline](https://user-images.githubusercontent.com/58792/61977859-941b2f00-afbd-11e9-99a3-dd915bbe3f69.png)

Results of ML Prediction Pipeline:

![Brett Favre](https://user-images.githubusercontent.com/58792/61978210-aba6e780-afbe-11e9-9923-e09c82452639.png)

![feedback](https://user-images.githubusercontent.com/58792/61978208-a9448d80-afbe-11e9-9768-f1af2c0ab5be.png)

![conor](https://user-images.githubusercontent.com/58792/61978214-ad70ab00-afbe-11e9-943d-aa635a32fc5b.png)

![signals](https://user-images.githubusercontent.com/58792/61978207-a9448d80-afbe-11e9-8683-4903ed1080c8.png)

### How do you construct a news Feed?

* How many users should someone follow?
* What should be in the feed?
* What algorithm do you use to generate the feed? 
* Could you get a feed to be an O(1) lookup? Hint...pre-generate feed.
* What if one user posts 1000 items a day, but you follow 20 users and the feed paginates at 25 results?

### References

* [Social Network Theory Colab Notebook](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/social_network_theory.ipynb)