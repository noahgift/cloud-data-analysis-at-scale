## What is Continuous Delivery and Continuous Deployment?

Continuous Delivery builds upon several powerful tools continuous integration, IaC and Cloud Computing.  Continous Delivery lets the cloud infrastructure be defined as code and allows for near real-time changes of both code and new environments.

## Continuous Delivery for Hugo Static Site from Zero

[Hugo](https://gohugo.io/) is a popular static site generator. This tutorial will guide you through using [AWS Cloud9](https://aws.amazon.com/cloud9/) to create a Hugo website and develop against it using the cloud development environment.  The final step will be the setup a continuous integration pipeline using [AWS Code Pipeline](https://aws.amazon.com/codepipeline/).    

*Note these steps will be similar for other cloud environments or for your OS X laptop, but this particular tutorial is targeted at AWS Cloud9.*

The steps described below are covered in detail in this screencast, **HUGO CONTINOUS DELIVER WITH AWS**:

[![AWS Hugo Continuous Deliver!](https://img.youtube.com/vi/xiodvLdPnvI/0.jpg)](https://youtu.be/xiodvLdPnvI)


* **Step 1:  Launch an AWS Cloud9 Environment**

Use the AWS Free Tier and a Cloud9 Environment with the defaults.

* **Step2:  Download the `hugo` binary and put it in your Cloud9 path**

Go to the latest releases of hugo [https://github.com/gohugoio/hugo/releases](https://github.com/gohugoio/hugo/releases).  Download the latest release using the `wget` command.  It should look something like this:


```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.63.0/hugo_0.63.0_Linux-32bit.tar.gz
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

*([Optional but recommended](https://github.com/noahgift/hugo-continuous-delivery-demo/blob/master/.gitignore) add `public` to `.gitignore)*

2.  In AWS cloud9 in the quickstart directory create a `Makefile` with a `clean` command.  This will `rm -rf` the public html directory that `hugo` creates.  You don't want to check this into source control.

![create Makefile](https://user-images.githubusercontent.com/58792/72996682-1e0b4f80-3dc9-11ea-852a-bfff144fb315.png)


```bash
clean:
	echo "deleting generated HTML"
	rm -rf public
```
3.  Now run `make clean` to delete the `public` directory and all of the source code `hugo` generated (don't worry it regenerates html anytime you run `hugo`).

4.  Add Github repo as a "remote".  This will be the name of the Github repository you just created.  It will look something like this where you change change the name of your site.

```git remote add origin git@github.com:<github_username>/my_hugo_site.git```

My git remote add command looks like this (note I run `git remote -v` to verify afterwards):

```bash
ec2-user:~/environment/quickstart (master) $ git remote add origin git@github.com:noahgift/hugo-continuous-delivery-demo.git
ec2-user:~/environment/quickstart (master) $ git remote -v
origin  git@github.com:noahgift/hugo-continuous-delivery-demo.git (fetch)
origin  git@github.com:noahgift/hugo-continuous-delivery-demo.git (push)
```

5.  Add the source code and push to Github.

Typically I get the "lay of the land" before I commit.  I do this be running `git status`.  Here is my output.  You can see that I need to `Makefile` `archetypes` `config.toml` and `content/`.

```bash
ec2-user:~/environment/quickstart (master) $ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitmodules
        new file:   themes/ananke

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Makefile
        archetypes/
        config.toml
        content/
```

I add them by typing the command `git add *`.  You can see below that this will add all of those files and directories:

```bash
ec2-user:~/environment/quickstart (master) $ git add *
ec2-user:~/environment/quickstart (master) $ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitmodules
        new file:   Makefile
        new file:   archetypes/default.md
        new file:   config.toml
        new file:   content/posts/my-first-post.md
        new file:   themes/ananke
```

Now push these files by doing the following commands (Note you will need to merge the files):

```bash
git pull --allow-unrelated-histories origin master
git branch --set-upstream-to=origin/master
git push
```
You can see what this looks like below:

![git push hugo](https://user-images.githubusercontent.com/58792/73000067-55c8c600-3dce-11ea-9b3f-00f855b5adcf.png)

The github repo looks like this now:

![github repo](https://user-images.githubusercontent.com/58792/73000248-91fc2680-3dce-11ea-9c71-5728fbfc4a72.png)

*NOTE:  Using `git` can be very challenging in edge cases.  If this workflow doesn't work you can also start over from scratch and clone your github repo and manually add `hugo` into it*

*(Optional step:  If you want to verify your `hugo` site, check out this project on your laptop or another AWS Cloud9 instance and run hugo.)*


* **Step9:  Continuous Delivery with AWS CodeBuild**

Now it is time for the final part.  Let's setup continuous delivery using AWS CodeBuild.  This will allow changes that get pushed to Github to automatically deploy.

1.  Go to [AWS CodeBuild](https://aws.amazon.com/codebuild/) and create a new project.  It is should look like this:

![code build](https://user-images.githubusercontent.com/58792/73001043-d3410600-3dcf-11ea-8e70-eb6fec097c7f.png)

*Note create a build in the same region you created your bucket:  i.e N. Virginia!*

2. The source code section should look similar this screenshot.  *Note the `webhook`.  This will do continuous delivery on changes*

![setup source](https://user-images.githubusercontent.com/58792/73007665-ec02e900-3dda-11ea-8102-43da8f562b10.png)


3.  The codebuild environment should look similar to this.  Click the "create build" button:

![codebuild environment](https://user-images.githubusercontent.com/58792/73002518-32077f00-3dd2-11ea-9b36-ba5e07cfca16.png)


4.  After you create the build navigate to "Build details" section and select the service role.  This where the privilages to deploy to S3 will be setup:

![codebuild service role](https://user-images.githubusercontent.com/58792/73002867-ac380380-3dd2-11ea-9347-18806a7fa47e.png)


You will add an "admin" policy that looks like this:


![admin policy](https://user-images.githubusercontent.com/58792/73008299-4badc400-3ddc-11ea-9654-f66c3c0ad08a.png)


Now in AWS Cloud9 go back and create the final step.

The following is a `buildspec.yml` file you can paste it.  You create the file with AWS Cloud9 by typing:  `touch buildspec.yml` then editing.

*NOTE: Something like the following  ```aws s3 sync public/ s3://hugo-duke-jan23/ --region us-east-1 --delete``` is an effective and explict way to deploy if `hugo deploy` is not working properly*

```bash
version: 0.2

environment_variables:
  plaintext:
    HUGO_VERSION: "0.63.0"
    
phases:
  install:
    runtime-versions:
      docker: 18
    commands:                                                                 
      - cd /tmp
      - wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
      - tar -xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
      - mv hugo /usr/bin/hugo
      - cd - 
      - rm -rf /tmp/*
  build:
    commands:
      - rm -rf public
      - hugo
      - aws s3 sync public/ s3://hugo-duke-jan23/ --region us-east-1 --delete
  post_build:
    commands:
      - echo Build completed on `date`
```

Now check this file into git and push:

```bash
git add buildspec.yml 
git commit -m "adding final build step"
git push
```

It should look like this:

![buildspec push](https://user-images.githubusercontent.com/58792/73005690-5f0a6080-3dd7-11ea-8c07-c26f25695c10.png)

Now every time you make changes to content it will "auto-deploy" as shown:

![auto-build](https://user-images.githubusercontent.com/58792/73008532-c1199480-3ddc-11ea-9351-8f5b9781892d.png)

As you create new posts, etc, it will deploy:

![auto deploy](https://user-images.githubusercontent.com/58792/73008737-2ec5c080-3ddd-11ea-90f4-b4d43591aa17.png)

### Hugo AWS Continuous Delivery Conclusion

Continuous Delivery is a powerful technique to master and in this situation it could immediately be put to use to build a portfolio website for a Data Scientist.

* [Example Hugo AWS Repository](https://github.com/noahgift/hugo-duke-jan23)

If you are having issues with the `git` workflow you can simply create the repo first, then `git clone` on Cloud9 to prevent the advanced `git` workflow.

* **Post Setup (Optional Advanced Configurations & Notes)**

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

#### Building Hugo Sites Automatically Using AWS CodeBuild
The first thing that we need is a set of instructions for building the Hugo site. Since the build server starts clean every time this includes downloading Hugo and all the dependencies that we require. One of the options that CodeBuild has for specifying the build instruction is the `buildspec.yaml` file.

Navigate to the CodeBuild console and create a new project using settings similar to this or that meet your project's demands:

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

#### Creating IAM Role
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

### Case Studies 

What are some logical next steps you could improve on?

* Setup the build server to have a more granular security policy. 
* Create an SSL certificate via AWS (for free).
* Publish your content to the AWS Cloudfront CDN.
* Enhance the `Makefile` to use a `deploy` command you also use in the build server instead of the verbose `aws sync` command.
* Try to "deploy" from many spots:  Laptop, editing Github pages directly, a different cloud.

Take some or all of these case study items and complete them.
