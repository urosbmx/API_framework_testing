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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    evidences = getattr(report, "evidences", [])
    if report.when == "call":
        data = open("myoutput.log", "rb").read()
        evidences.append(evidence.jpeg(data=data, filename="myoutput.log"))
    report.evidences = evidences
