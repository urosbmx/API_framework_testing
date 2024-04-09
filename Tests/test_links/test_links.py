import pytest
import requests
import os

class Test_links_all_sites:

    @pytest.mark.xray("API-1")
    def test_all_links(self):
        api_url = f"https://jsonplaceholder.typicode.com/posts"
        r = requests.get(api_url)
        assert r.status_code == 200