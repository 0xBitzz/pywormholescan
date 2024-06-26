import pytest
import requests
import responses


@responses.activate
def test_get_governor_available_notional_by_chain(guardian):
    sample_json_data = {"entries": [{"chainId": 1}]}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/available_notional_by_chain",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_governor_available_notional_by_chain()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_available_notional_by_chain(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/available_notional_by_chain",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_governor_available_notional_by_chain()


@responses.activate
def test_get_guardians_enqueued_vaas(guardian):
    sample_json_data = {"entries": [{"emitterChain": 21}]}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/enqueued_vaas",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_enqueued_vaas()
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_enqueued_vaas(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/enqueued_vaas",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_enqueued_vaas()


@responses.activate
def test_get_guardians_is_vaa_enqueued(guardian):
    sample_json_data = {"isEnqueued": True}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/is_vaa_enqueued/21/0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5/134913",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_is_vaa_enqueued(
        21, "0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5", 134913
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_is_vaa_enqueued(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/is_vaa_enqueued/21/0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5/134913",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_is_vaa_enqueued(
            21,
            "0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5",
            134913,
        )


@responses.activate
def test_get_guardians_token_list(guardian):
    sample_json_data = {"entries": {"originChainId": 1}}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/token_list",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_token_list()
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_token_list(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/governor/token_list",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_token_list()


@responses.activate
def test_get_guardians_hearbeats(guardian):
    sample_json_data = {
        "entries": [
            {
                "rawheartBeat": {"nodeName": "Staking Fund"},
            }
        ]
    }
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/heartbeats",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_hearbeats()
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_hearbeats(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/heartbeats",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_hearbeats()


"""
@responses.activate
def test_get_guardians_signed_batch_vaa(guardian):
    sample_json_data = {}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/signed_batch_vaa/21/0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5/134913",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_signed_batch_vaa(
        21, "0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5", 134913
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_signed_batch_vaa(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/signed_batch_vaa/21/0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5/134913",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_signed_batch_vaa(
            21,
            "0xccceeb29348f71bdd22ffef43a2a19c1f5b5e17c5cca5411529120182672ade5",
            134913,
        )
"""


@responses.activate
def test_get_guardians_signed_vaa(guardian):
    sample_json_data = {"vaaBytes": "AQAAAAQNAD"}
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/signed_vaa/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json=sample_json_data,
        status=200,
    )

    result = guardian.get_guardians_signed_vaa(
        23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911", 90116
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_signed_vaa(guardian):
    responses.add(
        responses.GET,
        f"{guardian.base_url}/v1/signed_vaa/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        guardian.get_guardians_signed_vaa(
            23,
            "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
            90116,
        )
