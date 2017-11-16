from . import NewsAPIBase

class NewsAPI(NewsAPIBase):
    API_VERSION = "v1"

    def articles(self, source, params={}):
        params['source'] = source
        return self.request('articles', 'articles', params)


    def sources(self, params={}):
        return self.request('sources', 'articles', params)
