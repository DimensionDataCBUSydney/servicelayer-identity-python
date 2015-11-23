import requests


class StsClient(object):
    def __init__(self, base_url, client_id, client_secret, audience):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = audience

    def get_token(self, verify=False):
        payload = {"clientId": self.client_id,
                   "secret": self.client_secret,
                   "audience": self.audience}
        response = requests.post(self.base_url + "token/issue",
                                 data=payload,
                                 verify=verify)
        return response.json()['accessToken']
