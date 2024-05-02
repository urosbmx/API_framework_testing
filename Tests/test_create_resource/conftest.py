import pytest
import json
from Tests.test_create_resource.models import bodyModel
from faker import Faker
fake = Faker()


@pytest.fixture()
def create_data():
    return bodyModel(
        title="title",
        body=f"body {fake.name()}",
        userId=f"{fake.name()}"
    )

@pytest.fixture()
def create_body(create_data):
    return json.dumps(create_data.__dict__)