import requests
from .exceptions import TokenRequestError


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
        token = response.json()['accessToken']
        if token:
            return token
        else:
            http_error_msg = ''
            if 400 <= response.status_code < 500:
                http_error_msg = '%s Client Error: %s' % (
                    response.status_code, response.json()['message'])
            elif 500 <= response.status_code < 600:
                http_error_msg = '%s Server Error: %s' % (
                    response.status_code, response.json()['message'])
            if http_error_msg:
                raise TokenRequestError(http_error_msg, response.status_code)
