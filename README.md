# NewsAPI python wrapper

Python wrapper for [newsapi.org](https://newsapi.org/) api.

## Install

```
pip install https://github.com/cyriac/python-newsapi/archive/master.zip
```

## Usage

### API v1
```python
from newsapi.v1 import NewsAPI

key = 'your key goes here'
params = {}

api = NewsAPI(key)
sources = api.sources(params)
articles = api.articles(sources[0]['id'], params)

```

### API v2
```python
from newsapi.v2 import NewsAPI

key = 'your key goes here'
params = {}

api = NewsAPI(key)
sources = api.sources(params)
headlines = api.top_headlines(sources[0]['id'], params)
everything = api.everything(params)

```
