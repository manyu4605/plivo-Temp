'''
Author : Abhimanyus@hpe.com
'''

import sys
sys.path.insert(0,'../libraries')
from plivoAPI import PlivoAPI
import pytest

# Dealing with command line options
def pytest_addoption(parser):
    parser.addoption("--auth_id", action="store", help="Authentication ID")
    parser.addoption("--auth_token", action="store", help="Authentication Token")
    parser.addoption("--seed", action="store", default=7692225329,help="Seed Number to be used")
    parser.addoption("--country_iso", action="store", default="US",help="")

# Setup environment fixture
@pytest.fixture(scope="session", autouse=True)
def plivoDriver(request):
    auth_id = request.config.getoption('--auth_id')
    auth_token = request.config.getoption('--auth_token')

    driver = PlivoAPI(auth_id,auth_token)
    return driver

@pytest.fixture(scope="session", autouse=True)
def seed(request):
    num = request.config.getoption('--seed')
    country = request.config.getoption('--country_iso')
    return num,country
