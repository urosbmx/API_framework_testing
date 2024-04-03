import pytest
import requests

class Test_links_all_sites:

    @pytest.mark.parametrize("url", ["posts", "comments", "albums", "photos", "todos", "users"])
    def test_all_links(self, url):
        api_url = f"https://jsonplaceholder.typicode.com/{url}"
        r = requests.get(api_url)
        assert r.status_code == 200