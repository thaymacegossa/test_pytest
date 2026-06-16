import pytest

#promotes a base url for all tests

@pytest.fixture
def base_url():
    return "https://compassuol.serverest.dev"