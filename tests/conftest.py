import pytest
import responses
from pywormholescan import Network, WormholescanAPI, GuardianAPI
from pywormholescan._internal import APIClient


@pytest.fixture
def mock_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture(params=[Network.MAINNET, Network.TESTNET])
def api_client(request):
    return APIClient(network=request.param)


@pytest.fixture(params=[Network.MAINNET, Network.TESTNET])
def guardian(request):
    return GuardianAPI(network=request.param)


@pytest.fixture(params=[Network.MAINNET, Network.TESTNET])
def wormholescan(request):
    return WormholescanAPI(network=request.param)
