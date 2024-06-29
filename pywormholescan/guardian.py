from pywormholescan._internal import APIClient, Network


class GuardianAPI:
    def __init__(self, network: Network) -> None:
        """Initializes the object with the appropriate Base URL, based on the selected network: (Network.MAINNET | Network.TESTNET)."""
        self._api_client = APIClient(network=network)
        self.base_url = self._api_client.base_url

    def get_governor_available_notional_by_chain(self) -> dict:
        """
        Get available notional by chainID
        Since from the wormhole-explorer point of view it is not a node, but has the information of all nodes,
        in order to build the endpoints it was assumed:
        There are N number of remainingAvailableNotional values in the GovernorConfig collection. N = number of guardians
        for a chainID. The smallest remainingAvailableNotional value for a chainID is used for the endpoint response.

        Endpoint - /v1/governor/available_notional_by_chain
        """
        response = self._api_client.get("/v1/governor/available_notional_by_chain")
        return response

    def get_guardians_enqueued_vaas(self) -> dict:
        """
        Get enqueued VAAs.

        Endpoint - /v1/governor/enqueued_vaas
        """
        response = self._api_client.get("/v1/governor/enqueued_vaas")
        return response

    def get_guardians_is_vaa_enqueued(
        self, chain_id: int, emitter: str, sequence: int
    ) -> dict:
        """
        Check if vaa is enqueued.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/governor/is_vaa_enqueued/:chain_id/:emitter/:seq
        """
        response = self._api_client.get_with_path_builder("/v1/governor/is_vaa_enqueued", chain_id, emitter, sequence)
        return response

    def get_guardians_token_list(self) -> dict:
        """
        Get token list
        Since from the wormhole-explorer point of view it is not a node, but has the information of all nodes,
        in order to build the endpoints it was assumed:
        For tokens with the same originChainId and originAddress and different price values for each node,
        the price that has most occurrences in all the nodes for an originChainId and originAddress is returned.

        Endpoint - /v1/governor/token_list
        """
        response = self._api_client.get("/v1/governor/token_list")
        return response

    def get_guardian_current_set(self) -> dict:
        """
        Get current guardian set.

        Endpoint - /v1/guardianset/current
        """
        response = self._api_client.get("/v1/guardianset/current")
        return response

    def get_guardians_hearbeats(self) -> dict:
        """
        Get heartbeats for guardians.

        Endpoint - /v1/heartbeats
        """
        response = self._api_client.get("/v1/heartbeats")
        return response

    def get_guardians_signed_batch_vaa(
        self, chain_id: int, emitter: str, sequence: int
    ) -> dict:
        """
        Get a batch of VAA []byte from a chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/signed_batch_vaa/:chain_id/:emitter/sequence/:seq
        """
        response = self._api_client.get_with_path_builder("/v1/signed_batch_vaa", chain_id, emitter, sequence)
        return response

    def get_guardians_signed_vaa(self, chain_id: int, emitter: str, sequence: int) -> dict:
        """
        Get a batch of VAA []byte from a chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /v1/signed_vaa/:chain_id/:emitter/:seq
        """
        response = self._api_client.get_with_path_builder("/v1/signed_vaa", chain_id, emitter, sequence)
        return response
