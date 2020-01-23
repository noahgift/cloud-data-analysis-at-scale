## What is Continuous Delivery and Continuous Deployment?


## Continuous Delivery for Hugo Static Site from Zero

[Hugo](https://gohugo.io/) is a popular static site generator. This tutorial will guide you through using [AWS Cloud9](https://aws.amazon.com/cloud9/) to create a Hugo website and develop against it using the cloud development environment.  The final step will be the setup a continuous integration pipeline using [AWS Code Pipeline](https://aws.amazon.com/codepipeline/).    

*Note these steps will be similar for other cloud environments or for your OS X laptop, but this particular tutorial is targeted at AWS Cloud9.*

* **Step 1:  Launch an AWS Cloud9 Environment**

You can refer to this screencast if you haven't set it up already. *DEMO VIDEO HERE OF ENTIRE PROCESS:  [![CI PIPELINE AWS Cloud9!](https://img.youtube.com/vi/4SIFF1PAMbw/0.jpg)](https://youtu.be/4SIFF1PAMbw*

* **Step2:  Download the `hugo` binary and put it in your Cloud9 path**

Go to the latest releases of hugo [https://github.com/gohugoio/hugo/releases](https://github.com/gohugoio/hugo/releases).  Download the latest release using the `wget` command.  It should look something like this:


```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.62.2/hugo_0.62.2_Linux-32bit.tar.gz
```

*Note that you shouldn't just blindly cut and paste the code above!  Make sure you get the latest release or if not on Cloud9, use the appropriate version*

Now put this file in your `~/.bin` directory using these commands (again make sure you put your version of hugo here:  i.e. ```hugo_0.99.x_Linux-32bit.tar.gz```):

```bash
tar xzvf hugo_0.62.2_Linux-32bit.tar.gz
mkdir -p ~/bin
mv ~/environment/hugo . #assuming that you download this into ~/environment
which hugo              #this shows the `path` to hugo
```  

The output of `which hugo` should be something like:

```bash
ec2-user:~/environment $ which hugo
~/bin/hugo
```

Finally check to see that the version flag works as a basic sanity check. This is what it looks like on my cloud9 machine (*your version number will likely be different*)

```bash
ec2-user:~/environment $ hugo version
Hugo Static Site Generator v0.62.2-83E50184 linux/386 BuildDate: 2020-01-05T18:51:38Z
```

These steps should get you access to `hugo` and you can run it like any other tool.  If you cannot or get stuck, refer to the screencast later on and/or look at the [quickstart guide](https://gohugo.io/getting-started/installing#step-2-download-the-tarball).

* **Step3:  Make a `hugo` website locally and test it in Cloud9**

One great thing about `hugo` is that it just a `go` binary.  It makes it simple to both develop and deploy `hugo` sites.  The following section is loosely based on the official [`hugo` quickstart guide](https://gohugo.io/getting-started/quick-start/).

1.  Create a new site using the following command:  ```hugo new site quickstart```
2.  Add a theme (you could swap this part with [any theme](https://themes.gohugo.io/) you want).

```bash
cd quickstart
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml
```

* **Step4:  Create a post**

To create a new blog post type the following command.

```bash
hugo new posts/my-first-post.md
```

This post is easily editable inside of AWS Cloud9 as shown

![aws cloud 9 edit hugo post](https://user-images.githubusercontent.com/58792/72943287-b8c14b00-3d43-11ea-82d8-d9129f56c0e8.png)

* **Step5:  Run Hugo locally in Cloud9**

Up to this point things have been fairly straightforward.  In this section we are going to run `hugo` as a development server.  This will require us to open up a port on EC2 security groups.  This is fairly easy to find. 

1.  Open a new tab on the AWS Console and type in `EC2` and scroll down to security groups and look for the security group with the same name as your AWS Cloud9 environment as shown:

![AWS Cloud9 environment](https://user-images.githubusercontent.com/58792/72944297-7f3e0f00-3d46-11ea-915e-5a1c17eee168.png).

2.  Open up via new TCP rule port `8080` and the `edit` button.  You will see this change has been made.  This will allow us to browse to port `8080` to preview our website as we develop it locally on AWS Cloud9.

3.  Navigate back to AWS Cloud9 and run this command to find out the IP Address (we will use this IP Address when we run `hugo`).


```bash
curl ipinfo.io
````

You should see something like this (*but with a different IP Address*)

```
ec2-user:~/environment $ curl ipinfo.io
{
  "ip": "34.200.232.37",
  "hostname": "ec2-34-200-232-37.compute-1.amazonaws.com",
  "city": "Virginia Beach",
  "region": "Virginia",
  "country": "US",
  "loc": "36.8512,-76.1692",
  "org": "AS14618 Amazon.com, Inc.",
  "postal": "23465",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
  ```

4.  Run hugo with the following options, you will need to swap this IP Address out with the one you generated earlier.  Notice that the `baseURL` is important so you can test navigation.

```bash
hugo serve --bind=0.0.0.0 --port=8080 --baseURL=http://34.200.232.37/
```

If this was successful you should get something similar to the following output.

![hugo local](https://user-images.githubusercontent.com/58792/72945003-9da50a00-3d48-11ea-9562-e60b4ffa69e8.png)

5.  Open in a new tab in your browser and type paste in the url in the output. In my output it is `http://34.200.232.37:8080/`, but it will be *different for you*.

![hugo website](https://user-images.githubusercontent.com/58792/72945272-6420ce80-3d49-11ea-9ed1-5661218713cb.png)

If you edit the markdown file it will render out the changes live.  This allows for a an interactive development workflow.

* **Step6:  Create Static Hosted Amazon S3 website and deploy to bucket**

The next thing to do is to deploy this website directory to an AWS S3 bucket.  You can follow the instructions [here on how to create an s3 bucket and set it up for hosting](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/static-website-hosting.html).


Note this also means setting a `bucket policy` via the bucket policy editor as shown below.  The name of your bucket *WILL NOT BE `cloud9-hugo-duke`* you must change this.

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::cloud9-hugo-duke/*"
            ]
        }
    ]
}
```

The bucket policy editor workflow looks as follows.

![bucket policy editor](https://user-images.githubusercontent.com/58792/72947411-e6ac8c80-3d4f-11ea-8842-137b276a86c7.png)



* **Step7:  Deploy the website manually before it becomes fully automated**

With automation it is very important to first manually write down the steps for a workflow before fully automating it.  The following items will need to be followed:


1.  The `config.toml` will need to be edited as shown below.  Note that your s3 bucket url will be different.


```bash
baseURL = "http://cloud9-hugo-duke.s3-website-us-east-1.amazonaws.com"
languageCode = "en-us"
title = "My New Hugo Sit via AWS Cloud9"
theme = "ananke"

[[deployment.targets]]
# An arbitrary name for this target.
name = "awsbucket"
URL = "s3://cloud9-hugo-duke/?region=us-east-1" #your bucket here
```

2.  Now you can deploy by using the built in `hugo deploy` command.  The deployment command output should look like this after you run `hugo deploy`.  You can read more about the `deploy` command [in the official docs](https://gohugo.io/hosting-and-deployment/hugo-deploy/).

```bash
ec2-user:~/environment/quickstart (master) $ hugo deploy                                                                                    
Deploying to target "awsbucket" (s3://cloud9-hugo-duke/?region=us-east-1)                                                                   
Identified 15 file(s) to upload, totaling 393 kB, and 0 file(s) to delete.                                                                  
Success!
```    

The contents of the AWS S3 bucket should look similar to this.

![bucket contents](https://user-images.githubusercontent.com/58792/72947506-31c69f80-3d50-11ea-92b0-87a7980ecce8.png)


The website demonstrated in this tutorial is visible here:  [http://cloud9-hugo-duke.s3-website-us-east-1.amazonaws.com/](http://cloud9-hugo-duke.s3-website-us-east-1.amazonaws.com/)

* **Step8:  Check into Github**

1.  Create a new Github repo (and add `.gitignore`)

![add git repo](https://user-images.githubusercontent.com/58792/72995683-50b44880-3dc7-11ea-861e-26c98a4260e4.png)

*([Optional but recommended](https://github.com/noahgift/hugo-continuous-delivery-demo/blob/master/.gitignore) add `/public` to `.gitignore)*



* **Step9:  Continuous Delivery with AWS CodeBuild**


#### Building Hugo Sites Automatically Using AWS CodeBuild
The first thing that we need is a set of instructions for building the Hugo site. Since the build server starts clean every time this includes downloading Hugo and all the dependencies that we require. One of the options that CodeBuild has for specifying the build instruction is the `buildspec.yaml` file.

Navigate to the CodeBuild console and create a new project using the following settings:

-   **Project name:**  `somename-hugo-build-deploy`
-   **Source provider:** `GitHub`
-   **Repository:** `Use a repository in my account`
-   **Choose a repository:** `Choose your GitHub repository`
-   Click on **Webhook**  checkbox for rebuilding project  every time a code change is pushed to this repository
-   **Environment image:**  `Use an image managed by AWS CodeBuild`
-   **Operating System:** `Ubuntu` 
-   **Runtime:** `Base`
-   **Runtime version:** `Choose a runtime environment version`
-   **Buildspec name:** `buildspec.yml`
-   **Artifact type:**  `No artifact`
-   **Cache:** `No cache`
-   **Service role:**  `Create a service role in your account`

#### Creating IAM user
For building project, deploy to S3  and enable CloudFront Invalidation we need to create an individual  IAM role. Add IAM role and attach **CloudFrontFullAccess**  and **AmazonS3FullAccess** policies.  After that click **Add permissions** button again select "Attach existing policies directly" and click **Create policy** button. Select "JSON" and paste following user policy:
```js
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "cloudfront:CreateInvalidation",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::s3-<bucket-name>",
                "arn:aws:s3:::s3-<bucket-name>/*"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::s3-<bucket-name>",
                "arn:aws:s3:::s3-<bucket-name>/*"
            ]
        }
    ]
}
```
Also, you need to add a policy for the IAM role, which will be called *CodeBuildBasePolicy-**[codebuild-project-name]**-**[aws-region-name]***

* **Post Setup (Optional)**

#### Setting up SSL for CloudFront

Go to  AWS Certificate Manager and click **Request a certificate** button.
First, we need to add domain names, in our case (example.com). When you enter the domain name as `*.example.com`, click **Add another name to this certificate** button and add plain domain `example.com` too. On a next step select **DNS validation** option and click **Confirm and request** button in Review.
To use DNS validation, you must be able to add a CNAME record to the DNS configuration for your domain.  Add CNAME record created on ACM to the DNS configuration for your domain on **Route 53**.

#### CloudFront configurations

Create a web distribution in the CloudFront section. In the **Origin Domain Name** field select Endpoint of your bucket. Select "Redirect HTTP to HTTPS" from the **Viewer Protocol Policy**. Add your domain names in the **Alternate Domain Name** filed and select the SSL certificate you have created in the ACM. In the **Default Root Object** type `index.html`. Once done please proceed and create the distribution.

### Integrating Route53 with CloudFront distribution:
Copy the domain name from the CloudFront distribution and edit A record in your Route53. Select **Alias**, in **Alias Target**, enter your CloudFront domain URL which is ******.cloudfront.net. Click **Save Record Set**. Now that you have created A record. The domain name example.com will route to your **CloudFront distribution**.
We need to create a CNAME record to point other sub-domains like `www.example.com` to map to the created **A record** 
Click  **Create Record Set**, enter `*` in name textbox. Select  **CNAME**  from Type. In value, type the A record, in our case, it will be  example.com. Click  **Save Record Set**. Now even  www.example.com will forward to  example.com  which in-turn will forward to CloudFront distribution.