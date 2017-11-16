from . import NewsAPIBase

class NewsAPI(NewsAPIBase):
    API_VERSION = "v2"

    def get_base_endpoint(self):
        return  'https://beta.newsapi.org/{}/'.format(self.get_api_version())

    def top_headlines(self, sources, params={}):
        params['sources'] = sources
        return self.request('top-headlines', 'articles', params)

    def everything(self, params={}):
        # requred_keys = ['sources', 'domains', 'q', 'language', 'country', 'category']
        # if len(params) == 0 or not bool(set(requred_keys) & set(params.keys())):
        return self.request('everything', 'articles', params)


    def sources(self, params={}):
        return self.request('sources', 'sources', params)
