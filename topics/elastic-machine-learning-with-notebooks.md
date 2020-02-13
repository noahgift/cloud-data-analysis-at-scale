## Jupyter Notebook Workflow

Jupyter notebooks are increasingly the hub in both Data Science and Machine Learning projects.  All major vendors have some form of Jupyter integration.  Some tasks are more oriented in the direction of engineering and others in the direction of science.  

![jupyter-workflow](https://user-images.githubusercontent.com/58792/74328483-01c15980-4d5c-11ea-8f94-2f93f18fe863.jpg)

A good example of a science focused workflow is the traditional notebook based Data Science workflow.  First, data is collected, it could be anything from a SQL query to a CSV file hosted in Github.  Next, the data is explored using visualization, statistics and unsupervized machine learning.  A model may be created, and then the results are shared via a conclusion. 

![jupyter-datascience-workflow](https://user-images.githubusercontent.com/58792/74330454-bc9f2680-4d5f-11ea-923f-64ef3a85e206.jpg)


 This often fits very well into a markdown based workflow where each section is a Markdown heading.  Often that Jupyter notebook is then checked into source control.  Is this notebook source control or a document?  This is an important consideration and it is best to treat it as both.  

![datascience workflow](https://user-images.githubusercontent.com/58792/74331819-7bf4dc80-4d62-11ea-9e3d-de382ff1322b.png)

### DevOps for Jupyter Notebooks

DevOps is popular technology best practice and it is often used in [combination with Python](https://www.amazon.com/Python-DevOps-Ruthlessly-Effective-Automation/dp/149205769X). The center of the universe for DevOps is the build server.  The build server enables automation.  This automation includes linting, testing, reporting, building and deploying code. This process is called continuous delivery.

![devops](https://user-images.githubusercontent.com/58792/74334543-199eda80-4d68-11ea-99b9-ee2e4908b2f4.jpg)

The benefits of continuous delivery are many. The code is automatically tested, and it is always in a deployable state.  Automation of best practices creates a cycle of continuous improvement in a software project. A question should crop up if you are a data scientist. Isn't Jupyter notebook source code too?  Wouldn't it benefit from these same practices?  The answer is yes.


This diagram exposes a proposed best practices directory structure for a Jupyter based project in source control.  The `Makefile` holds the recipes to build, run and deploy the project via make commands:  `make test`, etc.  The `Dockerfile` holds the actual runtime logic which makes the project truly portable.

```bash
FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Logic to run Jupyter could go here...
# Expose port 8888
#EXPOSE 8888

# Run app.py at container launch
#CMD ["jupyter", "notebook"]
```

![devops-for-jupyter](https://user-images.githubusercontent.com/58792/74336428-3d641f80-4d6c-11ea-9e0a-688c8015bde3.jpg)

The Jupyter notebook itself can be tested via the `nbval` plugin as shown.
```bash
	python -m pytest --nbval notebook.ipynb
```

The requirements for the project are kept in a `requirements.txt` file. Everytime the project is changed the build server picks up the change and runs tests on the Jupyter notebook cells themselves.

DevOps isn't just for software only projects.  DevOps is a best practice that fits well with the ethos of Data Science.  Why guess if your notebook works, your data is reproducible or that it can deploy?

## AWS Sagemaker Elastic Architecture

![sagemaker-example-architecture](https://user-images.githubusercontent.com/58792/74456593-10d80280-4e55-11ea-83ff-218f8d944c3a.jpg)

#### AWS Sagemaker Reference projects

* [Analyze US census data for population segmentation using Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/analyze-us-census-data-for-population-segmentation-using-amazon-sagemaker/)