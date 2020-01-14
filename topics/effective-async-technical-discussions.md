# Effective Async Technical Discussions

What makes an effective technical discussion?  There are several techniques that significantly enhance a technical discussion.

### Reproducible Code

If a discussion involves code, reproducing the code signficantly enhances the discussion.  If the code that is shared or discussed cannot be run, than it could add zero or even negative value.  Hosted `git` and hosted [Jupyter Notebooks](https://jupyter.org/) are two common ways to solve this problem.

#### Hosted `git`

Three main versions of hosted `git` are: [bitbucket](https://bitbucket.org/product), [github](https://github.com/) and [GitLab](https://about.gitlab.com/).  They all provide ways to share and reproduce code.  This code can be shared within the context of a software development project and it can also be shared in an async based discussion like chat.

Let's focus on Github, the most commonly encountered of these options.  There are two main ways to share code with others.  One method is to [create a public repo.](https://help.github.com/en/github/administering-a-repository/setting-repository-visibility) and share code and/or [markdown](https://guides.github.com/features/mastering-markdown/) files.  One nice side effect of markdown files is that they can also be served out via webpages through [GitHub Pages](https://pages.github.com/) or through a blog engine like [Hugo](https://gohugo.io/) which can build pages  <1 ms per page.

Another powerful feature of Github is a [gist](https://gist.github.com/).  What is particularly useful about a `gist` is that it can be shared with syntax highlighting and formatting.  Here are the steps:

1.  Create gist
![creategist](https://user-images.githubusercontent.com/58792/72302640-b3277f00-3638-11ea-9d3e-2a91ec3de928.png)

2.  Share gist
![sharegist](https://user-images.githubusercontent.com/58792/72302636-aefb6180-3638-11ea-8b4a-118f94c5933d.png)

3.  Here is the url to share:
[Gist Example](https://gist.github.com/noahgift/b6eec243c70ba4f71033954c4da75dd3)
Many chat programs will automatically render out the code snippit.

#### Hosted Jupyter Notebooks

In theory, Jupyter Notebooks solve a huge problem in creating reproducable code, but in practice it needs some help.  A key limitation of Jupyter is the Python packaging environment.  It is a helpless victim to the untamed complexity of the underlying operating system.

Fortunately there is an easy solution.  Jupyter notebooks that have a portable runtime are the ones that are actually reproducible.  Portable runtimes include [docker](https://www.docker.com/) and [colab](https://colab.research.google.com/).  Docker format files can specify exactly what the runtime should be like, including the packages that need to be installed.  

One example of a hosted runtime can be found in this project:  [Container Microservices project](https://github.com/noahgift/container-revolution-devops-microservices).

For a user to recreate the code and run it locally they can do the following:

```bash
#!/usr/bin/env bash

# Build image
docker build --tag=flasksklearn .

# List docker images
docker image ls

# Run flask app
docker run -p 8000:80 flasksklearn
```

This approach is optimized for deployment and has some advantages for communication focused on deploying software.  A second approach is the `colab` approach.  In this [colab example](https://github.com/noahgift/functional_intro_to_python/blob/master/Public_Master_SafariOnline_Day1_Part1.ipynb) the notebook note only has the complete code, but with a click of the "Open in Colab" button a user can completely reproduce what was shared.

![sharecolab](https://user-images.githubusercontent.com/58792/72303703-1ebf1b80-363c-11ea-890a-7512a24dbfd5.png)


### Audio, Video and Images

Adding audio, video and/or images can signficantly enhance a technical discussion.

### Sharing images

One simple "hack" for sharing images is to use Github issues.  Here is an [example of this in action](https://github.com/noahgift/cloud-data-analysis-at-scale/issues/1).

![sharehack](https://user-images.githubusercontent.com/58792/72303792-6a71c500-363c-11ea-9c38-6df9dcb047d8.png)

### Screencasts

Doing a quick screencast can boost a discussion value.  Here is a screencast of how to create an AWS Lambda function.

[![Create Lambda Python](https://img.youtube.com/vi/AlRUeNFuObk/0.jpg)](https://www.youtube.com/watch?v=AlRUeNFuObk "Create Lambda Python")

You can create screencasts quickly using software you probably already have on your machine.  Options include:  [Zoom](https://zoom.us/), [QuickTime Player](https://support.apple.com/guide/quicktime-player/record-your-screen-qtp97b08e666/mac) and [Camtasia](https://www.techsmith.com/video-editor.html).

### Produce Once, Reuse Many

One thing to keep in mind with technical discussion is the concept of *produce once, reuse many*.  There are many outlets for a technical discussion including: classroom discussions, work discusions, books you are writing or software projects you are contributing to.

If you produce high-quality technical notes you can use these notes and code samples for years or even the rest of your life.  Why not produce high-quality comments so you can "reuse" many ways.

### Technical discussions as a form of active learning

One substantional advantage to technical discussions is they serve as a form of active learning.  Writing software in a professional setting with modern software development practices often involves many team interactions (i.e. [pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)).  This is a form of "super-charged" learning that enables software engineers to learn an extraordinary pace..

### Conclusions

Building software or doing data science is not about setting aside a period of time and building something and stopping.  It is an iterative from of group communication.  In turning in homework assignments or finish a ticket for a commercial project, the communication is where the most value is created versus just the raw software code.

### Exercises 

* Topic: Create technical posts
* Directions:  

    - Part A:  Use the techniques described above and create one or more "technical" posts in a chat channel like [Slack](https://slack.com/), [Piazza](https://piazza.com/) or [Canvas](https://canvas.instructure.com/).  Express your idea in code using one or many of the techniques described above.

    - Part B:  Comment and reply to at least one person where you learned a new technique.

    - Part C:  Later after the "dust" has settled in a day or two, write down and document what you learned so you can use it.

    - Part D:  "Demo"  your post
