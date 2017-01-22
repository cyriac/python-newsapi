import urllib

import requests

class NewsAPI(object):
    def __init__(self, api_key, version='v1'):
        self.version = version
        self.base_endpoint = 'https://newsapi.org/{}/'.format(self.version)
        self.api_key = api_key

    def request(self, endpoint, params={}):
        params['apiKey'] = self.api_key
        endpoint_url = '{}{}?{}'.format(self.base_endpoint, endpoint, urllib.urlencode(params))
        self.response = requests.get(endpoint_url)
        response_dict = self.response.json()

        if self.response.status_code == 200 and \
           response_dict['status'] == 'ok' and \
           endpoint in response_dict:
            self.data = response_dict[endpoint]
        else:
            self.data = []

        return self.data

    def articles(self, source, params={}):
        params['source'] = source
        return self.request('articles', params)


    def sources(self, params={}):
        return self.request('sources', params)

