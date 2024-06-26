import pytest
import requests
import responses


@responses.activate
def test_get_address(wormholescan):
    sample_json_data = {"key": "value"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/address/0x0",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_address("0x0")
    assert result == sample_json_data


@responses.activate
def test_failed_get_address(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/address/0x0",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_address("0x0")


@responses.activate
def test_get_global_txn_by_id(wormholescan):
    sample_json_data = {
        "id": "23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116"
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/global-tx/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_global_txn_by_id(
        23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911", 90116
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_global_txn_by_id(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/global-tx/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_global_txn_by_id(
            23,
            "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
            90116,
        )


@responses.activate
def test_get_governor_config(wormholescan):
    sample_json_data = {"data": [{"id": "000ac0076727b35fbea2dac28fee5ccb0fea768e"}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/config",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_config()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_config(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/config",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_config()


@responses.activate
def test_get_governor_config_by_guardian_address(wormholescan):
    sample_json_data = {"data": [{"id": "5893b5a76c3f739645648885bdccc06cd70a3cd3"}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/config/0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_config_by_guardian_address(
        "0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_config_by_guardian_address(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/config/0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_config_by_guardian_address(
            "0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3"
        )


@responses.activate
def test_get_governor_enqueued_vaas(wormholescan):
    sample_json_data = {"data": [{"chainId": 23}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/enqueued_vaas/",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_enqueued_vaas()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_enqueued_vaas(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/enqueued_vaas/",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_enqueued_vaas()


@responses.activate
def test_get_guardians_enqueued_vaas_by_chain(wormholescan):
    sample_json_data = {"data": [{"chainId": 23}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/enqueued_vaas/23",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_guardians_enqueued_vaas_by_chain("23")
    assert result == sample_json_data


@responses.activate
def test_failed_get_guardians_enqueued_vaas_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/enqueued_vaas/23",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_guardians_enqueued_vaas_by_chain("23")


@responses.activate
def test_get_governor_limit(wormholescan):
    sample_json_data = {"data": [{"availableNotional": 21987471}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/limit",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_limit()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_limit(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/limit",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_limit()


@responses.activate
def test_get_governor_notional_available(wormholescan):
    sample_json_data = {"data": [{"availableNotional": 21987214, "chainId": 1}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/available",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_notional_available()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_notional_available(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/available",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_notional_available()


@responses.activate
def test_get_governor_notional_available_by_chain(wormholescan):
    sample_json_data = {"data": [{"availableNotional": 21987285, "chainId": 1}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/available/1",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_notional_available_by_chain(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_notional_available_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/available/1",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_notional_available_by_chain(1)


@responses.activate
def test_get_governor_notional_limit_detail(wormholescan):
    sample_json_data = {"data": [{"chainId": 1, "notionalLimit": 25000000}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/limit",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_notional_limit_detail()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_notional_limit_detail(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/limit",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_notional_limit_detail()


@responses.activate
def test_get_governor_notional_limit_detail_by_chain(wormholescan):
    sample_json_data = {
        "data": [{"chainId": 1, "maxTransactionSize": 2500000, "nodeName": "MCF"}]
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/limit/1",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_notional_limit_detail_by_chain(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_notional_limit_detail_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/limit/1",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_notional_limit_detail_by_chain(1)


@responses.activate
def test_get_governor_max_notional_available_by_chain(wormholescan):
    sample_json_data = {
        "data": [{"chainId": 1, "maxTransactionSize": 2500000, "nodeName": "MCF"}]
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/max_available/1",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_max_notional_available_by_chain(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_max_notional_available_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/notional/max_available/1",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_max_notional_available_by_chain(1)


@responses.activate
def test_get_governor_status(wormholescan):
    sample_json_data = {"data": [{"nodeName": "Staking Fund"}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/status",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_status()
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_status(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/status",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_status()


@responses.activate
def test_get_governor_status_by_guardian_address(wormholescan):
    sample_json_data = {"data": {"chains": [{"chainId": 22}]}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/status/0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_governor_status_by_guardian_address(
        "0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_governor_status_by_guardian_address(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/governor/status/0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_governor_status_by_guardian_address(
            "0x5893B5A76c3f739645648885bDCcC06cd70a3Cd3"
        )


@responses.activate
def test_get_health_check(wormholescan):
    sample_json_data = {"status": "OK"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/health",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_health_check()
    assert result == sample_json_data


@responses.activate
def test_failed_get_health_check(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/health",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_health_check()


@responses.activate
def test_get_last_transactions(wormholescan):
    sample_json_data = [{"count": 270, "time": "2024-06-07T07:24:52.579403977Z"}]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/last-txs?timeSpan=1d&sampleRate=1h",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_last_transactions()
    assert result == sample_json_data


@responses.activate
def test_failed_get_last_transactions(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/last-txs?timeSpan=1d&sampleRate=1h",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_last_transactions()


@responses.activate
def test_get_observations(wormholescan):
    sample_json_data = [
        {
            "emitterChain": 1,
            "guardianAddr": "0x71AA1BE1D36CaFE3867910F99C09e347899C19C3",
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations()
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations()


@responses.activate
def test_get_observations_by_chain(wormholescan):
    sample_json_data = [
        {
            "emitterChain": 1,
            "guardianAddr": "0xf93124b7c738843CBB89E864c862c38cddCccF95",
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations_by_chain(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations_by_chain(1)


@responses.activate
def test_get_observations_by_emitter(wormholescan):
    sample_json_data = [
        {
            "emitterAddr": "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238",
            "emitterChain": 1,
            "guardianAddr": "0xf93124b7c738843CBB89E864c862c38cddCccF95",
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1/cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations_by_emitter(
        1, "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations_by_emitter(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1/cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations_by_emitter(
            1, "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238"
        )


@responses.activate
def test_get_observations_by_sequence(wormholescan):
    sample_json_data = [
        {
            "emitterAddr": "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238",
            "emitterChain": 1,
            "guardianAddr": "0x71AA1BE1D36CaFE3867910F99C09e347899C19C3",
            "sequence": 7044,
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1/cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238/7044",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations_by_sequence(
        1, "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238", 7044
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations_by_sequence(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1/cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238/7044",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations_by_sequence(
            1, "cf5f3614e2cd9b374558f35c7618b25f0d306d5e749b7d29cc030a1a15686238", 7044
        )


@responses.activate
def test_get_observations_by_chain(wormholescan):
    sample_json_data = [
        {
            "emitterChain": 1,
            "guardianAddr": "0xf93124b7c738843CBB89E864c862c38cddCccF95",
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations_by_chain(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/1",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations_by_chain(1)


"""
@responses.activate
def test_get_observations_by_id(wormholescan):
    sample_json_data = [
        {
            "emitterChain": 1,
            "guardianAddr": "0xf93124b7c738843CBB89E864c862c38cddCccF95",
        }
    ]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/:chain/:emitter/:sequence/:signer/:hash",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_observations_by_id(1)
    assert result == sample_json_data


@responses.activate
def test_failed_get_observations_by_id(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/observations/:chain/:emitter/:sequence/:signer/:hash",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_observations_by_id(1)
"""


@responses.activate
def test_get_protocol_stats(wormholescan):
    sample_json_data = [{"protocol": "portal_token_bridge", "total_messages": 4269667}]
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/protocols/stats",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_protocol_stats()
    assert result == sample_json_data


@responses.activate
def test_failed_get_protocol_stats(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/protocols/stats",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_protocol_stats()


@responses.activate
def test_get_ready_check(wormholescan):
    sample_json_data = {"ready": "OK"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/ready",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_ready_check()
    assert result == sample_json_data


@responses.activate
def test_failed_get_ready_check(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/ready",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_ready_check()


@responses.activate
def test_get_relay_by_vaa_id(wormholescan):
    sample_json_data = {
        "relayer": "xlabs-automatic-relayer",
        "status": "redeemed",
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/relays/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_relay_by_vaa_id(
        chain_id=23,
        emitter="00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
        seq="90116",
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_relay_by_vaa_id(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/relays/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_relay_by_vaa_id(
            chain_id=23,
            emitter="00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
            seq="90116",
        )


@responses.activate
def test_get_scorecards(wormholescan):
    sample_json_data = {"24h_messages": "188830"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/scorecards",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_scorecards()
    assert result == sample_json_data


@responses.activate
def test_failed_get_scorecards(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/scorecards",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_scorecards()


@responses.activate
def test_get_token_by_chain_and_address(wormholescan):
    sample_json_data = {"symbol": "W"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/token/1/85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_token_by_chain_and_address(
        1, "85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_token_by_chain_and_address(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/token/1/85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_token_by_chain_and_address(
            1, "85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ"
        )


@responses.activate
def test_get_top_100_corridors(wormholescan):
    sample_json_data = {"corridors": [{"emitter_chain": 1}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-100-corridors",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_top_100_corridors(time_span="2d")
    assert result == sample_json_data


@responses.activate
def test_failed_get_top_100_corridors(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-100-corridors",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_top_100_corridors(time_span="2d")


@responses.activate
def test_get_top_assets_by_volume(wormholescan):
    sample_json_data = {
        "assets": [{"emitterChain": 2, "symbol": "USDC", "tokenChain": 2}]
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-assets-by-volume",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_top_assets_by_volume(time_span="7d")
    assert result == sample_json_data


@responses.activate
def test_failed_get_top_assets_by_volume(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-assets-by-volume",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_top_assets_by_volume(time_span="7d")


@responses.activate
def test_get_top_chain_pairs_by_num_transfers(wormholescan):
    sample_json_data = {"chainPairs": [{"emitterChain": 1}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-chain-pairs-by-num-transfers",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_top_chain_pairs_by_num_transfers(time_span="7d")
    assert result == sample_json_data


@responses.activate
def test_failed_get_top_chain_pairs_by_num_transfers(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-chain-pairs-by-num-transfers",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_top_chain_pairs_by_num_transfers(time_span="7d")


@responses.activate
def test_get_top_symbols_by_volume(wormholescan):
    sample_json_data = {
        "assets": [
            {
                "emitterChain": 2,
                "symbol": "USDC",
                "tokenChain": 2,
            }
        ]
    }
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-symbols-by-volume",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_top_symbols_by_volume(time_span="7d")
    assert result == sample_json_data


@responses.activate
def test_failed_get_top_symbols_by_volume(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/top-symbols-by-volume",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_top_symbols_by_volume(time_span="7d")


@responses.activate
def test_get_transactions(wormholescan):
    sample_json_data = {"transactions": [{"symbol": "W"}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/transactions/",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_transactions()
    assert result == sample_json_data


@responses.activate
def test_failed_get_transactions(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/transactions/",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_transactions()


@responses.activate
def test_get_transaction_by_id(wormholescan):
    sample_json_data = {"id": {"emitterChain": 23}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/transactions/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_transaction_by_id(
        23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911", 90116
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_transaction_by_id(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/transactions/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_transaction_by_id(
            23,
            "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
            90116,
        )


@responses.activate
def test_get_all_vaas(wormholescan):
    sample_json_data = {"id": {"emitterChain": 23}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_all_vaas()
    assert result == sample_json_data


@responses.activate
def test_failed_get_all_vaas(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_all_vaas()


@responses.activate
def test_get_vaas_by_chain(wormholescan):
    sample_json_data = {"data": {"emitterChain": 23}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_vaas_by_chain("23")
    assert result == sample_json_data


@responses.activate
def test_failed_get_vaas_by_chain(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_vaas_by_chain("23")


@responses.activate
def test_get_vaas_by_emitter(wormholescan):
    sample_json_data = {"data": {"emitterChain": 23}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_vaas_by_emitter(
        23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_vaas_by_emitter(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_vaas_by_emitter(
            23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911"
        )


@responses.activate
def test_get_vaa_by_id(wormholescan):
    sample_json_data = {"data": {"emitterChain": 23}}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_vaa_by_id(
        23, "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911", "90116"
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_vaa_by_id(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/23/00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911/90116",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_vaa_by_id(
            23,
            "00000000000000000000000027428dd2d3dd32a4d7f7c497eaaa23130d894911",
            "90116",
        )


@responses.activate
def test_get_vaa_counts(wormholescan):
    sample_json_data = {"data": [{"chainId": 23}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/vaa-counts",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_vaa_counts()
    assert result == sample_json_data


@responses.activate
def test_failed_get_vaa_counts(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/vaas/vaa-counts",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_vaa_counts()


@responses.activate
def test_get_version(wormholescan):
    sample_json_data = {"user": "root"}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/version",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_version()
    assert result == sample_json_data


@responses.activate
def test_failed_get_version(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/version",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_version()


@responses.activate
def test_get_x_chain_activity(wormholescan):
    sample_json_data = {"txs": [{"chain": 23}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/x-chain-activity",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_x_chain_activity()
    assert result == sample_json_data


@responses.activate
def test_failed_get_x_chain_activity(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/x-chain-activity",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_x_chain_activity()


@responses.activate
def test_get_x_chain_activity_by_tops(wormholescan):
    sample_json_data = {"txs": [{"chain": 23}]}
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/x-chain-activity/tops?timeSpan=1d&from=2006-01-02T15:04:05Z07:00&to=2006-01-02T15:04:05Z07:00",
        json=sample_json_data,
        status=200,
    )

    result = wormholescan.get_x_chain_activity_by_tops(
        time_span="1d",
        from_="2006-01-02T15:04:05Z07:00",
        to="2006-01-02T15:04:05Z07:00",
    )
    assert result == sample_json_data


@responses.activate
def test_failed_get_x_chain_activity_by_tops(wormholescan):
    responses.add(
        responses.GET,
        f"{wormholescan.base_url}/api/v1/x-chain-activity/tops?timeSpan=1d&from=2006-01-02T15:04:05Z07:00&to=2006-01-02T15:04:05Z07:00",
        json={"error": "not found"},
        status=404,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        wormholescan.get_x_chain_activity_by_tops(
            time_span="1d",
            from_="2006-01-02T15:04:05Z07:00",
            to="2006-01-02T15:04:05Z07:00",
        )
