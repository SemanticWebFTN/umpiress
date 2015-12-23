# Installation

``` shell
$ virtualenv -p <path/to/python3> <env_name>
$ source <path/to/env_name>/bin/activate
$ pip install django
```

# Running

``` shell
$ cd <root/of/project>
$ ./manage.py migrate
$ ./manage runserver
```

# What works?

- POST request to http://localhost:8000/api/ with ```Content-Type 'application/json'``` which have a key ```'query':'<text of a query>'``` returns ```json``` response in format:

``` javascript
{
  "message": "It works fine.",
  "results": [
    "dummy1",
    "dummy2",
    "dummy3"
  ],
  "query": "<text of a query>"
}
```
