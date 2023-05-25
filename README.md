## How to run the app:

### 1-  with docker:
You can build the docker image and run the application.
This app exposes port (5000), and you may bind the local server
port to 5000.

You can use the commands below to run the application:
```
docker build -t flask-app .
sudo docker run -it -p 5000:5000 -d flask-app
```

### 2-  without using docker:
To run the application on your host directly without running it on the docker container
You can use the commands below to run the application:
```
pip3 install -r requirements.txt
python3 app.py
```


## How to call the endpoints and use the API:

You can call these endpoints via curl or with your browser:

```
#for calling the first endpoint to get the first comments of top stories
{base_url for local use 127.0.0.1}/comments
#for calling the second endpoint to get the most used words of the first comments of top stories
{base_url for local use 127.0.0.1}/words
#for calling the third endpoint to get the most used words of all comments of top stories
{base_url for local use 127.0.0.1}/words/nested comments
```

## How to configure the application:
You can find the configurations, such as the story number for each endpoint, on the config.py file


# Questions:

### What has been the more difficult part?

Testing the code was the most difficult part because it took a lot of time to run it over and over, and I
had no test case to check. In the end, I chose to config the app with small numbers and try to check it with the result I tried
to gain manually.

### What part of the system could be improved?
At first, I can get the configurations and numbers in the request
instead of putting them in the config file, but I don't have time for this change right now.
If we do this, we need to put a lot of restrictions for users to handle the errors it may get, like
the limit for numbers or other cases.

Second, if I rewrite the app again, I will definitely use the update
endpoint in HN API and store the last data we calculate and  
answer the request with a combination of updated stories and
the data I stored. It gives us speed but adds complexity to the code.

### How would you scale it to be able to handle 1K calls per sec? and to handle 1M?
There are multiple ways to scale this. I try to mention some of them:

1- you can implement some sort of caching, as I mentioned in the last questions

2- you can deploy multiple instances of this app behind load balance each
response to some of the requests.

3- Increasing resources such as CPU and memory helps.

4- If we can find a duration like we need fresh data with 5 min error.
We can call the endpoints every 5 minutes and answer requests in that duration with
the same response. Specifically for getting top stories, we can use this one.

5- Again, we can use the database to store a map for each comment which is key = word, value = number of the key on that comment.
When we face comment-id that we get the data before we can retrieve the map and
just use that for calculations.

### How would you automate the testing?
Mock the HN API. Response as HN API with specific jsons, and then we can call
the endpoints or just test the functions and check the calculations.
I should mention If I want to add a test for this code, I will refactor the app.py
and make the get functions just to pass the response. I use new functions for
code inside these get functions.

### How would you automate the testing?
How would you implement a continuous development system (pipelines) for this particular case?
When push commits:

1- build for test and run unit tests and integration test

2- check to format ( use something like lint )

3- If we use some tools to check common security issues, it should run right now

When deploying:

1- build and push the image and deploy it on staging

2- if we have some smoke tests or check this app version with the QA team, it is the time

3- if we use a canary host, we should deploy on that

4- check the monitoring and alerting

5- deploy on production

6- again, check the monitoring 