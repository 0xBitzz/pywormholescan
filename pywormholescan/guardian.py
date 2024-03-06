from typing import Dict

from constants import BASE_URL
from pywormholescan.internal.url_builder import build_url
from pywormholescan.internal.api_request import make_request


class GuardianAPI:
    def __init__(self):
        self._base_url = f"{BASE_URL}/v1"

    def get_governor_available_notional_by_chain(self) -> Dict:
        """
        Get available notional by chainID
        Since from the wormhole-explorer point of view it is not a node, but has the information of all nodes,
        in order to build the endpoints it was assumed:
        There are N number of remainingAvailableNotional values in the GovernorConfig collection. N = number of guardians
        for a chainID. The smallest remainingAvailableNotional value for a chainID is used for the endpoint response.

        Endpoint - /v1/governor/available_notional_by_chain
        """
        url = build_url(self._base_url, f"/governor/available_notional_by_chain")
        response = make_request(url)
        return response

    def get_guardians_enqueued_vaas(self) -> Dict:
        """
        Get enqueued VAAs.

        Endpoint - /v1/governor/enqueued_vaas
        """
        url = build_url(self._base_url, f"/governor/enqueued_vaas")
        response = make_request(url)
        return response

    def get_guardians_is_vaa_enqueued(
        self, chain_id: int, emitter: str, seq: int
    ) -> Dict:
        """
        Check if vaa is enqueued.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/governor/is_vaa_enqueued/:chain_id/:emitter/:seq
        """
        url = build_url(
            self._base_url, f"/governor/is_vaa_enqueued/{chain_id}/{emitter}/{seq}"
        )
        response = make_request(url)
        return response

    def get_guardians_token_list(self) -> Dict:
        """
        Get token list
        Since from the wormhole-explorer point of view it is not a node, but has the information of all nodes,
        in order to build the endpoints it was assumed:
        For tokens with the same originChainId and originAddress and different price values for each node,
        the price that has most occurrences in all the nodes for an originChainId and originAddress is returned.

        Endpoint - /v1/governor/token_list
        """
        url = build_url(self._base_url, f"/governor/token_list")
        response = make_request(url)
        return response

    def get_guardian_set(self) -> Dict:
        """
        Get current guardian set.

        Endpoint - /v1/guardianset/current
        """
        url = build_url(self._base_url, f"/guardianset/current")
        response = make_request(url)
        return response

    def get_guardians_hearbeats(self) -> Dict:
        """
        Get heartbeats for guardians.

        Endpoint - /v1/heartbeats
        """
        url = build_url(self._base_url, f"/heartbeats")
        response = make_request(url)
        return response

    def get_guardians_signed_batch_vaa(
        self, chain_id: int, emitter: str, seq: int
    ) -> Dict:
        """
        Get a batch of VAA []byte from a chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/signed_batch_vaa/:chain_id/:emitter/sequence/:seq
        """
        url = build_url(self._base_url, f"/signed_batch_vaa/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response

    def get_guardians_signed_vaa(self, chain_id: int, emitter: str, seq: int) -> Dict:
        """
        Get a batch of VAA []byte from a chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/signed_vaa/:chain_id/:emitter/:seq
        """
        url = build_url(self._base_url, f"/signed_vaa/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response


g = GuardianAPI()
print(g.get_governor_available_notional_by_chain())
print(g.get_guardians_enqueued_vaas())
print(
    g.get_guardians_is_vaa_enqueued(
        1, "ec7372995d5cc8732397fb0ad35c0121e0eaa90d26f828a534cab54391b3a4f5", 797710
    )
)
print(g.get_guardians_token_list())
print(g.get_guardian_set())
print(g.get_guardians_hearbeats())
# print(
#     g.get_guardians_signed_batch_vaa(
#         1, "ec7372995d5cc8732397fb0ad35c0121e0eaa90d26f828a534cab54391b3a4f5", 797710
#     )
# )
print(
    g.get_guardians_signed_vaa(
        1, "ec7372995d5cc8732397fb0ad35c0121e0eaa90d26f828a534cab54391b3a4f5", 797710
    )
)
