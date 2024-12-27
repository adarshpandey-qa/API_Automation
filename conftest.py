
import pytest
from datetime import datetime
import os
import json

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Add timestamp to report filename
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)  # Ensure the reports directory exists
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")

@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Test data file not found: {json_file_path}")
    with open(json_file_path) as json_path:
        data = json.load(json_path)
    return data

    