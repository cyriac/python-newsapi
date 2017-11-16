import urllib.request, urllib.parse, urllib.error

import requests

class NewsAPIBase(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_api_version(cls):
        return cls.API_VERSION

    def get_base_endpoint(self):
        return  'https://newsapi.org/{}/'.format(self.get_api_version())

    def request(self, endpoint, endpoint_key, params={}):
        params['apiKey'] = self.api_key
        endpoint_url = '{}{}?{}'.format(self.get_base_endpoint(),
                                        endpoint,
                                        urllib.parse.urlencode(params))
        self.response = requests.get(endpoint_url)
        response_dict = self.response.json()

        if self.response.status_code == 200 and \
           response_dict['status'] == 'ok' and \
           endpoint in response_dict:
            self.data = response_dict[endpoint_key]
        else:
            self.data = []

        return self.data
