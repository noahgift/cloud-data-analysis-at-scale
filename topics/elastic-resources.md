## Elastic Resources

One of the benefits of the cloud is the ability to use elastic capabilities.  One such resource is an Elastic File System (EFS) on AWS.  It works well with other ephemeral resources like spot instances.  

### Build Continuous Delivery with EFS (NFS OPS)


* launch an Amazon Linux instance using Amazon Linux AMI.

* Login to your Amazon Linux instance by using AWS Cloud9.

* Become root using ```sudo su -``` command.

* Update your repositories

```yum update```

* Fix JAVA

```bash
[ec2-user ~]$ sudo yum remove java-1.7.0-openjdk
[ec2-user ~]$ sudo yum install java-1.8.0
```

* Get Jenkins running in a python virtual env.

https://jenkins.io/doc/book/installing/#war-file

* Setup build server that deploys to EFS mount point