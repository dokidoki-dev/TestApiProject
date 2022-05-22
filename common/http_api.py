import json

import requests
import config.base_config as base_config
from common.logger import log

logger = log()


class HttpRequest:
    """
        request请求类，支持post、get请求
        此类不支持session保持
    """
    def __init__(self, url=base_config.Config.base_url):
        self.base_url = url

    def post(self, path, headers, payload):
        url = self.base_url + path
        logger.info("url: " + url)
        r = requests.post(url=url, headers=headers, data=json.dumps(payload))
        return r

    def get(self, path, headers, params=None):
        url = self.base_url + path
        logger.info("url: " + url)
        r = requests.get(url=url, headers=headers, params=params)
        return r


class HttpRequest_Session:
    """
        request请求类，支持post、get请求
        此类支持session保持
    """
    def __init__(self, url=base_config.Config.base_url):
        self.base_url = url
        self.session = requests.session()

    def post(self, path, headers, payload):
        url = self.base_url + path
        logger.info("url: " + url)
        r = self.session.post(url=url, headers=headers, data=json.dumps(payload))
        return r

    def get(self, path, headers, params=None):
        url = self.base_url + path
        logger.info("url: " + url)
        r = self.session.get(url=url, headers=headers, params=params)
        return r
