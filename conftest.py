import os
from dotenv import load_dotenv, dotenv_values
import logging
import pytest
from pytest_xray import evidence


@pytest.fixture(scope='session')
def setup_logging():
    logging.basicConfig(level=logging.INFO)


load_dotenv()
print(os.getenv("XRAY_API_BASE_URL"))

