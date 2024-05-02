from itertools import count

import pytest
import requests
import logging


# TODO This is place where we can take endpoints for testing
# LINK https://jsonplaceholder.typicode.com


logger = logging.getLogger(__name__)


class Test_JsonPlaceHolder:

    @pytest.mark.xray("API-7")
    def test_GET(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/1"
        logger.info("Test Started")
        r = requests.get(api_url)
        data = r.json()
        logger.info(f"Test status code {r.status_code}")
        assert r.status_code == 200
        logger.info(f"Test Content-Type {r.headers["Content-Type"]}")
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"
        logger.info(f"Test response title --> {data["title"]}")
        assert data["title"] == "delectus aut autem"

    @pytest.mark.xray("API-8")
    def test_with_incorrect_URL(self):
        api_url = f"https://jsonplaceholder.typicode.com/todo"
        logging.info("Test Started")
        r = requests.get(api_url)
        logger.info(f"Test Content-Type {r.headers["Content-Type"]}")
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"
        logger.info(f"Test status code {r.status_code}")
        assert r.status_code == 404

    @pytest.mark.xray("API-9")
    def test_count_response(self):
        api_url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(api_url)
        logging.info("Test Started")
        data = r.json()
        logger.info(f"Test Content-Type {r.headers["Content-Type"]}")
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"
        logging.info(f"Test checking status code {r.status_code}")
        assert r.status_code == 200
        logging.info("Test checking count of element in array")
        assert len(data) == 10

