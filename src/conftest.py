import os

import pytest
from dotenv import find_dotenv, load_dotenv


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    env = os.getenv("ENV", "dev")
    env_file = find_dotenv(f".env.{env}")
    load_dotenv(env_file)
    yield
