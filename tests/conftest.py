import pytest
from utils.auth import get_auth_headers

# promotes a base url for all tests

@pytest.fixture
def base_url():
    return "https://compassuol.serverest.dev"


@pytest.fixture
def auth_headers(base_url):
    """Fixture that provides authentication headers with a valid token."""
    return get_auth_headers(base_url)