## Cloud Onboarding 

### AWS (Amazon Web Services)

* AWS Free Tier
* AWS Academy 
    - official certification training material
    - labs (Vocareum)
* AWS Educate

### GCP (Google Cloud Platform)

* [GCP Cloud Free Tier](https://cloud.google.com/free/docs/gcp-free-tier)

There is a 12-month free trial with $300 credit to use cloud services.  In addition, there are many cloud resources that are in an *Always Free* tier.

* [Qwiklabs](https://www.qwiklabs.com/)

Qwiklabs is a lab solution that is used by Google education and also AWS Education (less frequently though since Google purchased Qwiklabs). Both the faculty and students at Universities can request ["free" Qwiklab credits](https://edu.google.com/programs/credits/?modal_active=none).  For users without a ".edu" address, they can also purchase Qwiklab credits or often get them for free at a training event.

#### Qwiklab Gotchas

There are a few non-intuitive gotchas about Qwiklabs:

* To get "free" Qwiklab credits from a university you will need to use the .edu address your university provided.
* The credentials Qwiklabs generates when a lab is created are temporary and ephemeral.  These credentials
* *DO NOT USE UNIVERSITY EMAIL* to log into GCP.  Typically the IT department has setup GCP to restrict any usage of GCP with a .edu address.     
* You will need to keep Qwiklabs open and follow the lab instructions as you log into a new GCP login using the *temporary* credentials.

### Exercise

* Topic:  Onboard to AWS and GCP Labs
* Estimated time:  15 minutes
* Slack Channel:  #noisy-exercise-chatter
* Directions:
    * Part A:  Log into Qwiklabs and run a lab you haven't run before.  Paste a screenshot into slack of something interesting you found.
    * Part B:  Log into Vocareum and run a lab you haven't run before.  Paste a screenshot into slack channel of something interesting you found.
    * (Optional for the ambitious):  Use what we learned about effective technical communication and write this up in Github as brief tutorial.  Share this "post" instead of the raw screenshot.

### Setup Cloud Environment Continuous Integration from Zero

Using cloud based development environments solves many significant problems:

* Security Roles are simplified
* Faster communication pathway
* Enhanced IDEs and productivity with cloud environment.

The **FIRST** thing that should be setup with any new cloud development project is a Continuous Integration.

![Cloud based CI](https://user-images.githubusercontent.com/58792/72550405-aeddaa80-3860-11ea-9a9b-af264b115446.png)

#### Setup and use Github

To setup and use Github you need a Github account and internet access.  The minimal steps to start are:

1.  Create a repository, for example `hello`.
2.  Add an [SSH key to your Github account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
3.  Clone the repository locally, for example:

{caption: "Clone a repo"}
```bash
git clone git@github.com:paiml/hello.git
```
4.  Create a change and push it.  This would be an example of a good first change (inside the cloned repo).

{caption: "Clone a repo"}
```bash
echo "# hello" >> README.md
git add README.md
git commit -m "adding name of repo to README"
git push
```

##### Setting up and using Virtualenv

The Python standard library includes a module called [`venv`](https://docs.python.org/3/tutorial/venv.html). A virtual environment solves a very important problem in Python.  It isolates the Python interpreter to a specific directory. In this example a virtual environment is created in a user's home directory.

{caption: "Create Hello World Virtual Environment in Python"}
```bash
python3 -m venv ~/.hello
```

To use this virtual environment it needs to be activated.

{caption: "Activate Hello World Virtual Environment in Python"}
```bash
source  ~/.hello/bin/activate
```

##### Using a repeatable convention to create virtual environments

Conventions are a powerful way to simplify complex software engineering tasks in a series of easy to remember steps.  A convention based workflow with virtual environments can also dramatically simplify using them.  Here is a simple convention to use:

1.  Create a virtual environment with a `~/.`[reponame] format

This removes the decision about where to put the virtual environment and what to name it.  If your git repository is called `hello`, then you would run the following command:

```bash
python3 -m venv ~/.hello
```

Note, that the `.` makes the virtual environment invisible.  This will prevent your home directory overflowing with virtual environments when you open it in a GUI or list the contents with `ls -l`.

2.  Create an alias in your Bash or ZSH environment.

With ZSH, the config file to edit would be `~/.zshrc` in Bash it would be `~/.bashrc`.  Inside of this config file add the following:

{caption: "Create an alias for Git repo and virtual environment"}
```bash
## Hello repo
alias hello="cd ~/hello && source ~/.hello/bin/activate"
```

The next time you open your default shell, this alias will be available.  Here is an example of what this workflow looks like on my ZSH environment, which uses a package called [oh-my-zsh](https://ohmyz.sh/).

{caption: "Use alias that performs `cd` and activates `hello` virtual environment"}
```bash
➜ hello
(.hello) ➜  hello git:(master)
(.hello) ➜  hello git:(master) which python
/Users/noahgift/.hello/bin/python
```

This convention based workflow, if followed, makes a tedious and error prone process easy to remember.

##### Setup Makefile

Just like `vim`, mastering `Makefiles` can take years, but a minimialstic approach provides immediate benefits.  A main benefit to a `Makefile` is the ability to enforce a convention. If everytime you work a project you follow a few simple steps, it reduces the possibility of errors in building and testing a project.

A typical Python project can be improved by adding a `Makefile` with the following steps:  `make setup`, `make install`, `make test`, `make lint` and `make all`.

{caption: "Example Makefile"}
```bash
setup:
	python3 -m venv ~/.myrepo

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=myrepolib tests/*.py
	python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C myrepolib cli web

all: install lint test
```

This example is from a tutorial repository called [`myrepo`](https://github.com/noahgift/myrepo).  There is also an article about how to use it from [CircleCI](https://circleci.com/blog/increase-reliability-in-data-science-and-machine-learning-projects-with-circleci/).


<!---
{type: video, poster: "http://img.youtube.com/vi/xYX7n5bZw-w/mqdefault.jpg"}
-->
You can watch the following screencast on how to setup a Data Science build system:

* [Data Science Build Systems](https://www.youtube.com/watch?v=xYX7n5bZw-w)

The general idea is that a convention eliminates the need to think about what to do.  For every project, there is a common way to install software, a common way to test software and a common way to test and lint software.  Just like `vim`, a `Makefile` build system is often already on a Unix or Linux system.  Even Microsoft uses the [Linux operating system in Azure](https://azure.microsoft.com/en-us/overview/linux-on-azure/), and the result is that Linux is the preferred deployment target for most software.

### Extending a Makefile for use with Docker Containers

Beyond the simple `Makefile`, it is also useful to extend it to do other things.  An example of this is as follows:

{caption: "Example Makefile for Docker and Circleci"}
```bash
setup:
	python3 -m venv ~/.container-revolution-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

validate-circleci:
	# See https://circleci.com/docs/2.0/local-cli/#processing-a-config
	circleci config process .circleci/config.yml

run-circleci-local:
	# See https://circleci.com/docs/2.0/local-cli/#running-a-job
	circleci local execute

lint:
	hadolint demos/flask-sklearn/Dockerfile
	pylint --disable=R,C,W1203,W1202 demos/**/**.py

all: install lint test
```

A `Dockerfile` linter is called [`hadolint`](https://github.com/hadolint/hadolint) checks for bugs in a `Dockerfile`.  A [local version of the CircleCI build system](https://circleci.com/docs/2.0/local-cli/) allows for testing in the same environment as the SaaS offering.  The minimism is still present:  `make install`, `make lint` and `make test`, but the `lint` step is more complete and powerful with the inclusion of `Dockerfile` as well as `Python` linting.

*Notes about installing `hadolint` and `circleci`:  If you are on OS X you can `brew install hadolint` if you are on another platform follow the instructions from [`hadolint`](https://github.com/hadolint/hadolint)/  To install the local version of `circleci` on OS X or linux you can run `curl -fLSs https://circle.ci/cli | bash` or follow the official instructions for [local version of the CircleCI build system](https://circleci.com/docs/2.0/local-cli/)* 

### Exercise

* Topic:  Setup Continuous Integration Round-Trip from Cloud Environment
* Estimated time:  30+ minutes
* Slack Channel:  #noisy-exercise-chatter
* People:  Individual or Final Project Team
* Directions:
    * Part A:  Using a Cloud Development environment:  [GCP Cloud Shell](https://cloud.google.com/shell/) or [AWS Cloud 9](https://aws.amazon.com/cloud9/) setup a Github Project and create:
        - Makefile
        - hello world script
        - lint it with `pylint`
        - hook up Circleci and `lint` on checkin
    * Part B:  Document your setup and share via post on slack.

### Exercise

* Topic:  Create Continuous Integration
* Estimated time:  20-30 minutes
* People:  Individual or Final Project Team
* Slack Channel:  #noisy-exercise-chatter
* Directions:
    * Part A:  Log into Qwiklabs and run a lab you haven't run before.  Paste a screenshot into slack of something interesting you found.
    * Part B:  Log into Vocareum and run a lab you haven't run before.  Paste a screenshot into slack channel of something interesting you found.
    * (Optional for the ambitious):  Use what we learned about effective technical communication and write this up in Github as brief tutorial.  Share this "post" instead of the raw screenshot.

### Onboarding Day Prize

* Best technical discussion (as voted by peers in slack via "likes") gets [AWS Deep Lense](https://aws.amazon.com/deeplens/).

![Deep Lense](https://user-images.githubusercontent.com/58792/72547991-c8302800-385b-11ea-9c72-7b9546b85b9d.jpg)

* Can group (your team) or individual submission.


