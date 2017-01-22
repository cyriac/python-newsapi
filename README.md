# NewsAPI python wrapper

Python wrapper for [newsapi.org](https://newsapi.org/) api.

## Usage

```python
from newsapi import NewsAPI

key = 'your key goes here'

api = NewsAPI(key)
sources = api.sources()
articles = api.articles(sources[0]['id'])

```
