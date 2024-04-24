import os
from dotenv import load_dotenv, dotenv_values
import logging
import pytest
from pytest_xray import evidence





load_dotenv()
print(os.getenv("XRAY_API_BASE_URL"))

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     evidences = getattr(report, "evidences", [])
#     if report.when == "call":
#
#         data = open("myoutput.txt", "rb").read()
#         evidences.append(evidence.text(data=data, filename="myoutput.txt"))
#     report.evidences = evidences
