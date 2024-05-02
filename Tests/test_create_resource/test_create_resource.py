import json

import pytest
import requests
import logging

logger = logging.getLogger(__name__)


class Test_create_content:
    def test_create_content(self, create_body):
        api_url = 'https://jsonplaceholder.typicode.com/posts'
        header = {'Content-type': 'application/json; charset=UTF-8', }
        logger.info("Test Started")
        r = requests.post(api_url, headers=header, data=create_body)
        data = r.json()
        logger.info(f"Response code is{r.status_code}")
        assert r.status_code == 201
        logger.info(f"Validation body {data}")
        assert data["title"] == "title"



