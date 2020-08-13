# cloud-functions-sandbox
Try Cloud Functions with Python


## Setup
```
$ git clone git@github.com:tayutaedomo/cloud-functions-sandbox.git
$ cd cloud-functions-sandbox
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```


## Local Development
```
$ functions-framework --target hello_get --debug
```

```
$ functions-framework --target parse_multipart --debug
```


## Cloud Functions
```
$ gcloud functions deploy hello_get --runtime python37 --trigger-http --allow-unauthenticated
```

```
$ gcloud functions deploy parse_multipart --runtime python37 --trigger-http --allow-unauthenticated
```

