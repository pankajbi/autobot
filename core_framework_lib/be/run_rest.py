from requests import request

class RunRest(object):

    def __init__(self):
        pass

    def run_rest(self, method, url, log=None, json=None, params=None, headers=None, data=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, cookies=None):

        response = request(method, url,params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)

        return response