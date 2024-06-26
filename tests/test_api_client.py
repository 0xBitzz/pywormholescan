import pytest
import responses
import requests


@responses.activate
def test_get_endpoint(api_client):
    sample_json_data = {"status": "OK"}
    responses.add(
        responses.GET,
        f"{api_client.base_url}/api/v1/health",
        json=sample_json_data,
        status=200,
    )

    result = api_client.get("/api/v1/health")
    assert result == sample_json_data


@responses.activate
def test_failed_get_endpoint(api_client):
    responses.add(
        responses.GET,
        f"{api_client.base_url}/api/v1/health",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get("/api/v1/health")
