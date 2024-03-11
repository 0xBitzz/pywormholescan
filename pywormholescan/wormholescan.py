from typing import Any, Dict

from pywormholescan.constants import BASE_URL
from pywormholescan.internal.url_builder import build_url
from pywormholescan.internal.api_request import make_request

class WormholescanAPI:
    def __init__(self) -> None:
        self._base_url_api = f"{BASE_URL}/api/v1"

    # ---------------  ADDRESS ---------------
    def get_address_by_id(self, address: str, **kwargs: Dict[str, Any]) -> Dict:
        """
        Lookup an address.

        Args:
            *address (str): The address to look up.

            page (int): Page number. Starts at 0.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/address/:address
        """
        url = build_url(self._base_url_api, f"/address/{address}", kwargs=kwargs)
        response = make_request(url)
        return response

    # ---------------  GLOBAL TX ID ---------------
    def get_global_txn_by_id(self, chain_id: int, emitter: str, seq: int) -> Dict:
        """
        Find a global transaction by VAA ID.
        Global transactions is a logical association of two transactions that are related to each other by a unique VAA ID.
        The first transaction is created on the origin chain when the VAA is emitted.
        The second transaction is created on the destination chain when the VAA is redeemed.
        If the response only contains an origin tx the VAA was not redeemed.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/global-tx/:chain_id/:emitter/:seq
        """
        url = build_url(self._base_url_api, f"/global-tx/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response

    # ---------------  GOVERNOR ---------------
    def get_governor_config(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns governor configuration for all guardians.

        Args:
            page (int): Page number.
            integer (int): Number of elements per page.

        Endpoint - /api/v1/governor/config
        """
        url = build_url(self._base_url_api, "/governor/config", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_governor_config_by_guardian_address(self, guardian_address: str) -> Dict:
        """
        Returns governor configuration for a given guardian.

        Args:
            *guardian_address (str): Address of the guardian.

        Endpoint - /api/v1/governor/config/:guardian_address
        """
        url = build_url(self._base_url_api, f"/governor/config/{guardian_address}")
        response = make_request(url)
        return response

    def get_governor_enqueued_vaas(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns enqueued VAAs for each blockchain.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/governor/enqueued_vaas/
        """
        url = build_url(self._base_url_api, "/governor/enqueued_vaas/", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_guardians_enqueued_vaas_by_chain(self, chain: str):
        """
        Returns all enqueued VAAs for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/governor/enqueued_vaas/:chain
        """
        url = build_url(self._base_url_api, f"/governor/enqueued_vaas/{chain}")
        response = make_request(url)
        return response

    def get_governor_limit(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Retrieves the current governor limit.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/limit
        """
        url = build_url(self._base_url_api, "/governor/limit", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_governor_notional_available(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns the amount of notional value available for each blockchain.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order.

        Endpoint - /api/v1/governor/notional/available
        """
        url = build_url(
            self._base_url_api, "/governor/notional/available", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def get_governor_notional_available_by_chain(
        self, chain: int, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns the amount of notional value available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/available/:chain
        """
        url = build_url(
            self._base_url_api, f"/governor/notional/available/{chain}", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def get_governor_notional_limit_detail(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns the detailed notional limit for all blockchains.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/limit
        """
        url = build_url(self._base_url_api, f"/governor/notional/limit", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_governor_notional_limit_detail_by_chain(
        self, chain: int, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns the detailed notional limit available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/limit/:chain
        """
        url = build_url(
            self._base_url_api, f"/governor/notional/limit/{chain}", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def get_governor_max_notional_available_by_chain(self, chain: int) -> Dict:
        """
        Returns the maximum amount of notional value available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

        Endpoint - /api/v1/governor/notional/max_available/:chain
        """
        url = build_url(self._base_url_api, f"/governor/notional/max_available/{chain}")
        response = make_request(url)
        return response

    def get_governor_status(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns the governor status for all guardians.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/status
        """
        url = build_url(self._base_url_api, f"/governor/status", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_governor_status_by_guardian_address(
        self, guardian_address: str, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns the governor status for a given guardian.

        Args:
            *guardian_address (str): Address of the guardian.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/status/:guardian_address
        """
        url = build_url(
            self._base_url_api, f"/governor/status/{guardian_address}", kwargs=kwargs
        )
        response = make_request(url)
        return response

    # ---------------  HEALTH ---------------
    def get_health_check(self) -> Dict:
        """
        Health check.

        Endpoint - /api/v1/health
        """
        url = build_url(self._base_url_api, f"/health")
        response = make_request(url)
        return response

    # ---------------  LAST-TXS ---------------
    def get_last_transactions(
        self, *, time_span: str = "1d", sample_rate: str = "1h"
    ) -> Dict:
        """
        Returns the number of transactions by a defined time span and sample rate.

        Args:
            time_span (str): Time Span, default: 1d, supported values: [1d, 1w, 1mo]. 1mo ​​is 30 days.
            sample_rate (str): Sample Rate, default: 1h, supported values: [1h, 1d]. Valid configurations with timeSpan: 1d/1h, 1w/1d, 1mo/1d.

        Endpoint - /api/v1/last-txs
        """
        kwargs = {"time_span": time_span, "sample_rate": sample_rate}

        url = build_url(self._base_url_api, f"/last-txs", kwargs=kwargs)
        response = make_request(url)
        return response

    # ---------------  OBSERVATIONS ---------------
    def get_observations(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns all observations, sorted in descending timestamp order.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations
        """
        url = build_url(self._base_url_api, f"/observations", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_observations_by_chain(self, chain: int, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns all observations for a given blockchain, sorted in descending timestamp order.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain
        """
        url = build_url(self._base_url_api, f"/observations/{chain}", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_observations_by_emitter(
        self, chain: int, emitter: str, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns all observations for a specific emitter address, sorted in descending timestamp order.

        Args:
            *chain (int): ID of the blockchain.
            *emitter (str): Address of the emitter.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain/:emitter
        """
        url = build_url(
            self._base_url_api, f"/observations/{chain}/{emitter}", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def get_observations_by_sequence(
        self, chain: int, emitter: str, sequence: int, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Find observations identified by emitter chain, emitter address and sequence.

        Args:
            *chain (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *sequence (int): Sequence of the VAA.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain/:emitter/:sequence
        """
        url = build_url(
            self._base_url_api,
            f"/observations/{chain}/{emitter}/{sequence}",
            kwargs=kwargs,
        )
        response = make_request(url)
        return response

    def get_observations_by_id(
        self,
        chain: int,
        emitter_address: str,
        sequence: int,
        signer: str,
        hash: str,
        **kwargs: Dict[str, Any],
    ) -> Dict:
        """
        Find a specific observation.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain/:emitter/:sequence/:signer/:hash
        """
        url = build_url(
            self._base_url_api,
            f"/observations/{chain}/{emitter_address}/{sequence}/{signer}/{hash}",
            kwargs=kwargs,
        )
        response = make_request(url)
        return response

    # ---------------  OPERATIONS ---------------
    def get_operations(self, **kwargs: Dict[str, Any]):
        """
        Find all operations.

        Args:
            address (str): Address of the emitter.
            tx_hash (str): Hash of the transaction.
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/operations/
        """
        url = build_url(self._base_url_api, "/operations", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_operation_by_id(
        self,
        chain_id: int,
        emitter: str,
        seq: int,
    ) -> Dict:
        """
        Find operations by ID (chainID/emitter/sequence).

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/operations/{chain_id}/{emitter}/{seq}
        """
        url = build_url(self._base_url_api, f"/operations/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response

    # ---------------  READY ---------------
    def get_ready_check(self) -> Dict:
        """
        Ready check.

        Endpoint - /api/v1/ready
        """
        url = build_url(self._base_url_api, f"/ready")
        response = make_request(url)
        return response

    # ---------------  RELAY ---------------
    def get_relay_by_vaa_id(self, chain_id: int, emitter: str, seq: int) -> Dict:
        """
        Get a specific relay information by chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/relays/:chain/:emitter/:sequence
        """
        url = build_url(self._base_url_api, f"/relays/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response

    # ---------------  SCORECARDS ---------------
    def get_scorecards(self) -> Dict:
        """
        Returns a list of KPIs for Wormhole.
        TVL is total value locked by token bridge contracts in USD.
        Volume is the all-time total volume transferred through the token bridge in USD.
        24h volume is the volume transferred through the token bridge in the last 24 hours, in USD.
        Total Tx count is the number of transaction bridging assets since the creation of the network (does not include Pyth or other messages).
        24h tx count is the number of transaction bridging assets in the last 24 hours (does not include Pyth or other messages).
        Total messages is the number of VAAs emitted since the creation of the network (includes Pyth messages).

        Endpoint - /api/v1/scorecards
        """
        url = build_url(self._base_url_api, f"/scorecards")
        response = make_request(url)
        return response

    # ---------------  TOKEN ---------------
    def get_token_by_chain_and_address(self, chain_id: int, token_address: str) -> Dict:
        """
        Returns a token symbol, coingecko id and address by chain and token address.

        Args:
            *chain_id (int): ID of the blockchain.
            *token_address (str): Token address.

        Endpoint - /api/v1/token/:chain_id/:token_address
        """
        url = build_url(self._base_url_api, f"/token/{chain_id}/{token_address}")
        response = make_request(url)
        return response

    # ---------------  TOP ---------------
    def get_top_100_corridors(self, *, time_span: str = "2d") -> Dict:
        """
        Returns a list of the top 100 tokens, sorted in descending order by the number of transactions.

        Args:
            time_span (str): Time span, supported values: 2d and 7d (default is 2d).

        Endpoint - /api/v1/top-100-corridors
        """
        kwargs = {"time_span": time_span}

        url = build_url(self._base_url_api, f"/top-100-corridors", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_top_assets_by_volume(self, *, time_span: str) -> Dict:
        """
        Returns a list of emitter_chain and asset pairs with ordered by volume.
        The volume is calculated using the notional price of the symbol at the day the VAA was emitted.

        Args:
            *time_span (str): Time span, supported values: 7d, 15d, 30d.

        Endpoint - /api/v1/top-assets-by-volume
        """
        kwargs = {"time_span": time_span}

        url = build_url(self._base_url_api, f"/top-assets-by-volume", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_top_chain_pairs_by_num_transfers(self, *, time_span: str) -> Dict:
        """
        Returns a list of the emitter_chain and destination_chain pair ordered by transfer count.

        Args:
            *time_span (str): Time span, supported values: 7d, 15d, 30d.

        Endpoint - /api/v1/top-chain-pairs-by-num-transfers
        """
        kwargs = {"time_span": time_span}

        url = build_url(
            self._base_url_api, "/top-chain-pairs-by-num-transfers", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def get_top_symbols_by_volume(self, *, time_span: str = "7d") -> Dict:
        """
        Returns a list of symbols by origin chain and tokens.
        The volume is calculated using the notional price of the symbol at the day the VAA was emitted.

        Args:
            time_span (str): Time span, supported values: 7d, 15d and 30d (default is 7d).

        Endpoint - /api/v1/top-symbols-by-volume
        """
        kwargs = {"time_span": time_span}

        url = build_url(self._base_url_api, f"/top-symbols-by-volume", kwargs=kwargs)
        response = make_request(url)
        return response

    # ---------------  TRANSACTIONS ---------------
    def get_transactions(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns transactions. Output is paginated.

        Args:
            page (int): Page number. Starts at 0.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC
            address (str): Filter transactions by Address.

        Endpoint - /api/v1/transactions/
        """
        url = build_url(self._base_url_api, f"/transactions/", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_transaction_by_id(self, chain_id: int, emitter: str, seq: int) -> Dict:
        """
        Find VAA (perhaps transaction?) metadata by ID.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/transactions/:chain_id/:emitter/:seq
        """
        url = build_url(self._base_url_api, f"/transactions/{chain_id}/{emitter}/{seq}")
        response = make_request(url)
        return response

    # ---------------  VAAs ---------------
    def get_all_vaas(self, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns all VAAs. Output is paginated and can also be be sorted.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.
            tx_hash (str): Transaction hash of the VAA.
            parsed_payload (bool): Include the parsed contents of the VAA, if available.
            app_id (str): Filter by application ID.

        Endpoint - /api/v1/vaas/
        """
        url = build_url(self._base_url_api, f"/vaas/", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_vaas_by_chain(self, chain_id: str, **kwargs: Dict[str, Any]) -> Dict:
        """
        Returns all the VAAs generated in specific blockchain.

        Args:
            *chain_id (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/vaas/:chain_id
        """
        url = build_url(self._base_url_api, f"/vaas/{chain_id}", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_vaas_by_emitter(
        self, chain: int, emitter: str, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns all observations for a specific emitter address, sorted in descending timestamp order.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.

            to_chain (int): Destination chain.
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC.

        Endpoint - /api/v1/vaas/:chain_id/:emitter
        """
        url = build_url(self._base_url_api, f"/vaas/{chain}/{emitter}", kwargs=kwargs)
        response = make_request(url)
        return response

    def get_vaa_by_id(
        self, chain: int, emitter: str, seq: str, **kwargs: Dict[str, Any]
    ) -> Dict:
        """
        Returns all observations for a specific emitter address, sorted in descending timestamp order.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

            parsed_payload (bool): Include the parsed contents of the VAA, if available.

        Endpoint - /api/v1/vaas/:chain_id/:emitter/:seq
        """
        url = build_url(
            self._base_url_api, f"/vaas/{chain}/{emitter}/{seq}", kwargs=kwargs
        )
        response = make_request(url)
        return response

    def parse_vaa(self) -> Dict:
        """
        Parse a VAA.

        Endpoint - /api/v1/vaas/parse
        """

    def get_vaa_counts(self) -> Dict:
        """
        Returns the total number of VAAs emitted for each blockchain.

        Endpoint - /api/v1/vaas/vaa-counts
        """
        url = build_url(self._base_url_api, f"/vaas/vaa-counts")
        response = make_request(url)
        return response

    # ---------------  VERSION ---------------
    def get_version(self) -> Dict:
        """
        Get version/release information.

        Endpoint - /api/v1/version
        """
        url = build_url(self._base_url_api, f"/version")
        response = make_request(url)
        return response

    # ---------------  X-CHAIN-ACTIVITY ---------------
    def get_x_chain_activity(
        self, *, time_span: str = "7d", by: str = "notional", apps: str = "apps"
    ) -> Dict:
        """
        Returns a list of chain pairs by origin chain and destination chain.
        The list could be rendered by notional or transaction count.
        The volume is calculated using the notional price of the symbol at the day the VAA was emitted.

        Args:
            time_span (str): Time span, supported values: 7d, 30d, 90d, 1y and all-time (default is 7d).
            by (str): Renders the results using notional or tx count (default is notional).
            apps (str): List of apps separated by comma (default is all apps).

        Endpoint - /api/v1/x-chain-activity
        """
        kwargs = {"time_span": time_span, "by": by, "all apps": apps}

        url = build_url(self._base_url_api, f"/x-chain-activity", kwargs=kwargs)
        response = make_request(url)
        return response

    # ---------------  SWAGGER ---------------
    def get_swagger_docs(self) -> Dict:
        """
        Returns the swagger specification of the Wormhole API.

        Endpoint - /swagger.json
        """
        url = build_url(BASE_URL, "/swagger.json")
        response = make_request(url)
        return response
