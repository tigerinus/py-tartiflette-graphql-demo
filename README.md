# py-tartiflette-graphql-demo

This is a [tartiflette](https://tartiflette.io/) based demo with subscription over websocket.

## Run

```bash
$ python3 -m venv venv
...

$ . venv/bin/activate
...

$ pip install -r requirements.txt 
Collecting ...
Successfully installed ...

$ python3 -m server
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

## Test

Test code is using a different graphql library: <https://gql.readthedocs.io/>

```bash
$ cd ./test/python
$ python3 -m venv venv
...

$ . venv/bin/activate
...

$ pip install -r requirements.txt 
Collecting ...
Successfully installed ...

$ python subscriber.py
...
```
