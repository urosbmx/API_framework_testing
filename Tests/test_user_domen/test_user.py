from itertools import count

import pytest
import requests
import logging


class Test_user:

    @pytest.mark.xray("API-10")
    def test_count_response(self):
        api_url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(api_url)
        logging.info("Test Started")
        data = r.json()
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"
        logging.info("Test checking status code")
        assert r.status_code == 200
        logging.info("Test checking count of element in array")
        assert len(data) == 10
