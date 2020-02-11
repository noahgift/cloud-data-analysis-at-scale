## Creating a Locust Loadtest with Flask 


*Screencast* [![Docker Python from Zero in Cloud9!](https://img.youtube.com/vi/bUEYe6AqlXE/0.jpg)](https://youtu.be/bUEYe6AqlXE)

One powerful way to create a simple loadtest is with Locust and Flask.  Here is an example of a simple flask hello world app.  The [entire source code is found here](https://github.com/noahgift/docker-flask-locust).

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
```

The loadtest file is very simple to configure.  Notice the `index` function calls into the main, and only flask route.

```python
from locust import HttpLocust, TaskSet, between

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
```

The login screen requires the number of user and also hostname and port.  In our case this will be the port 8080.

![Screen Shot 2020-02-07 at 7 12 18 PM](https://user-images.githubusercontent.com/58792/74074801-c7635f80-49dd-11ea-9273-a04b587bbc05.png)



You can see how locust works when it runs.

![Screen Shot 2020-02-07 at 7 08 49 PM](https://user-images.githubusercontent.com/58792/74074716-65a2f580-49dd-11ea-943d-f91229a690ef.png)
