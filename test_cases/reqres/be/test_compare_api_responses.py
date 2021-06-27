import requests
import json
import logging
logger = logging.getLogger(__name__)

url1 = "https://reqres.in/api/users/3"
url2 = "https://reqres.in/api/users/2"


def run_request(url, method="GET"):
    response = requests.request(method, url)
    return response


def compare_data(url1, url2):
    resp1 = json.loads(run_request(url1).content)
    resp2 = json.loads(run_request(url2).content)
    return compare_dicts(resp1, resp2)


def compare_dicts(d1, d2):

    for k1, v1 in d1.items():
        k = k1
        if type(v1) == dict:
            k = f"{k}>>{k1}"
            if compare_dicts(v1, d2[k1]) is False:
                return False
        else:
            if v1 != d2[k1]:
                # logger.error (f"Expected {v1} Actual {d2[k1]} at {k}")
                return False
    return True


def test_compare_data():
    logger.info("Compare data")
    assert compare_data(url1, url2), logger.error("Fail")
