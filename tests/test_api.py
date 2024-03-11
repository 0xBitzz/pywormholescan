from pywormholescan.wormholescan import WormholescanAPI
from unittest.mock import patch

@patch('pywormholescan.internal.api_request.make_request')
def test_get_global_txn_by_id(mock_make_request):
    wormholescan_api = WormholescanAPI()

    mock_response_data = {"status": "completed"}
    mock_make_request.return_value = mock_response_data

    global_txn_data = wormholescan_api.get_global_txn_by_id(chain_id=1, emitter="ec7372995d5cc8732397fb0ad35c0121e0eaa90d26f828a534cab54391b3a4f5", seq=797710)

    assert "status" in mock_response_data.keys()
    assert isinstance(global_txn_data, dict)
    assert "id" in global_txn_data.keys()
