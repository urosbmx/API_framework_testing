import pytest
import requests
import os
import logging

logger = logging.getLogger(__name__)

class Test_links_all_sites:

    @pytest.mark.xray("API-1")
    def test_all_links(self,caplog):
        api_url = f"https://jsonplaceholder.typicode.com/posts"
        logger.info("Test Started")
        r = requests.get(api_url)
        logger.info(f"Validation status code {r.status_code}")
        assert r.status_code == 200
