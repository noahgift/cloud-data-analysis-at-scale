### Getting started with Docker

There are two main components of Docker:  [Docker Desktop](https://www.docker.com/products/docker-desktop) and [Docker Hub](https://www.docker.com/products/docker-hub).

![docker-ecosystem](https://user-images.githubusercontent.com/58792/73697366-5d307f00-46ac-11ea-9f85-529a9e3c4f42.png)


#### Docker Desktop Overview

The desktop application contains the container runtime which allows containers to execute.  The Docker App itself orchestrates the local development workflow including the ability to use [Kubernetes](https://github.com/kubernetes/kubernetes), which is an open-source system for managing containerized applications that came out of Google.

#### Docker Hub Overview

So what is Docker Hub and what problem does it solve?  Just as the [`git`](https://git-scm.com/) source code ecosystem has local developer tools like [vim](https://www.vim.org/), [emacs](https://www.gnu.org/software/emacs/), [Visual Studio Code](https://code.visualstudio.com/) or [XCode](https://developer.apple.com/xcode/) that work with it, Docker Desktop works with Docker containers and allows for local use and development.

When collaborating with `git` outside of the local environment, developers often use platforms like [Github](https://github.com/) or [Gitlab](https://about.gitlab.com/) to communicate with other parties and share code.  [Docker Hub](https://hub.docker.com/) works in a similar way.  Docker Hub allows developers to share docker containers that can serve as a base image for building new solutions.  

These base images can be built by experts and certified to be high quality:  i.e. the [official Python developers have a base image](https://hub.docker.com/_/python).  This allows a developer to leverage the expertise of the true expert on a particular software component and improve the overall quality of their container.  This is a similar concept to using a library developed by another developer versus writing it yourself.


#### Why Docker Containers vs Virtual Machines?



### Real-World Examples of Containers

What problem do [Docker format containers](https://docs.docker.com/engine/docker-overview/) solve?  In a nutshell, the operating system runtime can be packaged along with the code, and this solves a particularly complicated problem with a long history.  There is a famous meme that goes "It works on my machine!".  While this is often told as a joke to illustrate the complexity of deploying software, it is also true.  Containers solve this exact problem.  If the code works in a container, then the container configuration can be checked in as code.  Another way to describe this concept is that the actual Infrastructure is treated as code.  This is called IaC (Infrastructure as Code).

Here are a few specific examples:

#### Developer Shares Local Project
A developer can work on a web application that uses `flask` (a popular Python web framework).  The installation and configuration of the underlying operating system is handled by the Docker container file.  Another team member can checkout the code and use `docker run` to run the project.  This eliminates what could be a multi-day problem of configuring a laptop correctly to run a software project.

#### Data Scientist shares Jupyter Notebook with a Researcher at another University
A data scientist working with [jupyter](https://jupyter.org/) style notebooks wants to share a complex data science project that has multiple dependencies on C, Fortran, R, and Python code.  They package up the runtime as a Docker container and eliminate the back and forth over several weeks that occurs when sharing a project like this.  

#### A Machine Learning Engineer Load Tests a Production Machine Learning Model
A Machine learning engineer has been tasked with taking a new model and deploying it to production.  Previously, they were concerned about how to accurately test the accuracy of the new model before committing to it.  The model recommends products to paying customers and, if it is inaccurate, it costs the company a lot of money.  Using containers, it is possible to deploy the model to a fraction of the customers, only 10%, and if there are problems, it can be quickly reverted.  If the model performs well, it can quickly replace the existing models.
