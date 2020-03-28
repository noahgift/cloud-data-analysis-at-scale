## Faas (Function as a Service)

The function is the center of the universe with cloud computing.

![functions-python](https://user-images.githubusercontent.com/58792/77485388-682da300-6e03-11ea-9474-f83d5af41a79.jpg)




## Chalice Framework on AWS Lambda

Another option for developing serverless applications on AWS is to use the [chalice framework](https://github.com/aws/chalice).

Create credentials.

```bash
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
```

Next setup a project.

```bash
python3 -m venv ~/.hello && source ~/.hello/bin/activate
chalice new-project hello && hello
```

Inspect the `app.py` file.

```python
from chalice import Chalice

app = Chalice(app_name='hello')


@app.route('/')
def index():
    return {'hello': 'world'}
```

Then run local

```bash
(.chalicedemo) ec2-user:~/environment/helloworld4000 $ chalice local
Serving on http://127.0.0.1:8000
```

It can also run timed lambdas.

```
from chalice import Chalice, Rate

app = Chalice(app_name="helloworld")

# Automatically runs every 5 minutes
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    return {"hello": "world"}
```

It can also run event driven lambdas.

```python
from chalice import Chalice

app = Chalice(app_name="helloworld")

# Whenever an object is uploaded to 'mybucket'
# this lambda function will be invoked.

@app.on_s3_event(bucket='mybucket')
def handler(event):
    print("Object uploaded for bucket: %s, key: %s"
          % (event.bucket, event.key))

```

## Serverless


[Serverless Framework](https://serverless.com/framework/docs/getting-started/)

## Google Cloud Functions

Google Cloud Functions have much in common with AWS Lambda.  They work by invoking a function in response to an event.
You can view a screencast of this workflow here.

*Screencast* 

[![Google Cloud Screencast!](https://img.youtube.com/vi/SqxdFykehRs/0.jpg)](https://youtu.be/SqxdFykehRs)

Why would you use Cloud Functions on GCP?  According the official docs the use cases include ETL, Webooks, APIs, Mobile Backends and IoT.

![Screen Shot 2020-03-26 at 2 20 44 PM](https://user-images.githubusercontent.com/58792/77682254-02f5c100-6f6d-11ea-9483-3676f63402ac.png)


The editor allows you add "packages" on the fly.

![Screen Shot 2020-03-26 at 1 55 15 PM](https://user-images.githubusercontent.com/58792/77679806-74337500-6f69-11ea-86b1-fabfa92c8286.png)

```python
import wikipedia

def hello_wikipedia(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()

    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        print(entity)
        res = wikipedia.summary(entity, sentences=1)
        return res
    else:
        return f'No Payload'
```

One the Google Cloud Function is deployed it can be tested in the console.

![Screen Shot 2020-03-26 at 2 05 52 PM](https://user-images.githubusercontent.com/58792/77680910-fcfee080-6f6a-11ea-8873-1550b7a119df.png)

The logs can also be inspected.  There is where `print` statements show up.

![Screen Shot 2020-03-26 at 2 07 17 PM](https://user-images.githubusercontent.com/58792/77681061-2fa8d900-6f6b-11ea-8475-7a40aa459769.png)


Notice that the GCP Console can also invoke this same function.  First, let's describe it and make sure it is deployed.

```bash
gcloud functions describe function-2
```

![Screen Shot 2020-03-26 at 2 14 58 PM](https://user-images.githubusercontent.com/58792/77681737-3257fe00-6f6c-11ea-9c79-c01938c2a9b4.png)

Next, we can invoke it from the terminal.

```bash
gcloud functions call function-2 --data '{"entity":"google"}'
```

The results are here.

![Screen Shot 2020-03-26 at 2 16 14 PM](https://user-images.githubusercontent.com/58792/77681952-81059800-6f6c-11ea-9e67-26c18e835f1c.png)

Now, let's try a new company, this time Facebook.

```bash
gcloud functions call function-2 --data '{"entity":"facebook"}'
```

The output shows the following.

```bash
executionId: 6ttk1pjc1q14
result: Facebook is an American online social media and social networking service
  based in Menlo Park, California and a flagship service of the namesake company Facebook,
  Inc.
```

Can we go further and call an AI API?  Yes, we can.
First add this library to the requirements.txt

```bash
# Function dependencies, for example:
# package>=version
google-cloud-translate
wikipedia
```

Next run this function.


```python
import wikipedia

from google.cloud import translate

def sample_translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code="fr",
    )
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
    return u"Translated text: {}".format(translation.translated_text)

def translate_test(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()

    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        print(entity)
        res = wikipedia.summary(entity, sentences=1)
        trans=sample_translate_text(text=res, project_id="cloudai-194723")
        return trans
    else:
        return f'No Payload'
```

![Screen Shot 2020-03-26 at 3 05 52 PM](https://user-images.githubusercontent.com/58792/77686419-510dc300-6f73-11ea-830a-983dc2131f37.png)

Can you expand this even further to accept a payload that allows any language from the list of languages gcp [supports here](https://cloud.google.com/translate/docs/languages)?  Here is a [gist of this code](https://gist.github.com/noahgift/de40ac37b3d51b22835c9260d41599bc).

```python
import wikipedia

from google.cloud import translate

def sample_translate_text(text="YOUR_TEXT_TO_TRANSLATE", 
    project_id="YOUR_PROJECT_ID", language="fr"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code=language,
    )
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
    return u"Translated text: {}".format(translation.translated_text)

def translate_test(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()
    print(f"This is my payload {request_json}")
    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        language = request_json['language']
        print(f"This is the entity {entity}")
        print(f"This is the language {language}")
        res = wikipedia.summary(entity, sentences=1)
        trans=sample_translate_text(text=res, 
            project_id="cloudai-194723", language=language)
        return trans
    else:
        return f'No Payload'
```

The main takeaway in this change is grabbing another value from the `request_json` payload.  In this case `language`.  To test it the trigger accepts a new payload with the `language` added.

```json
{"entity": "google", "language": "af"}
```

![Screen Shot 2020-03-28 at 1 12 11 PM](https://user-images.githubusercontent.com/58792/77829053-d8833f80-70f5-11ea-916c-24a1bbd1c6e4.png)


Another item to mention is that you also may want to use the `curl` command to test out your cloud function.  Here is an example of a curl command that you could tweak.

```bash
curl --header "Content-Type: application/json"   --request POST   --data '{"entity":"google"}' https://us-central1-<yourproject>.
cloudfunctions.net/<yourfunction>
```


Reference GCP Qwiklabs

* [Cloud Functions: Qwik Start - Console](https://www.qwiklabs.com/focuses/1763?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=4929264)
* [Cloud Functions: Qwik Start - Command Line](https://google.qwiklabs.com/focuses/916?parent=catalog)


## Kubernetes FaaS with GKE

