from pywormholescan._internal import APIClient, Network


class WormholescanAPI:
    def __init__(self, network: Network) -> None:
        """Initializes the object with the appropriate Base URL, based on the selected network: (Network.MAINNET | Network.TESTNET)."""
        self._api_client = APIClient(network=network)
        self.base_url = self._api_client.base_url

    # ---------------  ADDRESS ---------------
    def get_address(self, address: str, **kwargs: dict) -> dict:
        """
        Lookup an address.

        Args:
            *address (str): The address to look up.

            page (int): Page number. Starts at 0.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/address/:address
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/address", address, kwargs=kwargs
        )
        return response

    # ---------------  GLOBAL TX ID ---------------
    def get_global_txn_by_id(self, chain_id: int, emitter: str, seq: int) -> dict:
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
        response = self._api_client.get_with_url_builder(
            "/api/v1/global-tx", chain_id, emitter, seq
        )
        return response

    # ---------------  GOVERNOR ---------------
    def get_governor_config(self, **kwargs: dict) -> dict:
        """
        Returns governor configuration for all guardians.

        Args:
            page (int): Page number.
            integer (int): Number of elements per page.

        Endpoint - /api/v1/governor/config
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/config", kwargs=kwargs
        )
        return response

    def get_governor_config_by_guardian_address(self, guardian_address: str) -> dict:
        """
        Returns governor configuration for a given guardian.

        Args:
            *guardian_address (str): Address of the guardian.

        Endpoint - /api/v1/governor/config/:guardian_address
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/config", guardian_address
        )
        return response

    def get_governor_enqueued_vaas(self, **kwargs: dict) -> dict:
        """
        Returns enqueued VAAs for each blockchain.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/governor/enqueued_vaas/
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/enqueued_vaas", kwargs=kwargs
        )
        return response

    def get_guardians_enqueued_vaas_by_chain(self, chain: str) -> dict:
        """
        Returns all enqueued VAAs for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/governor/enqueued_vaas/:chain
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/enqueued_vaas", chain
        )
        return response

    def get_governor_limit(self, **kwargs: dict) -> dict:
        """
        Retrieves the current governor limit.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/limit
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/limit", kwargs=kwargs
        )
        return response

    def get_governor_notional_available(self, **kwargs: dict) -> dict:
        """
        Returns the amount of notional value available for each blockchain.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order.

        Endpoint - /api/v1/governor/notional/available
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/notional/available", kwargs=kwargs
        )
        return response

    def get_governor_notional_available_by_chain(
        self, chain: int, **kwargs: dict
    ) -> dict:
        """
        Returns the amount of notional value available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/available/:chain
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/notional/available", chain, kwargs=kwargs
        )
        return response

    def get_governor_notional_limit_detail(self, **kwargs: dict) -> dict:
        """
        Returns the detailed notional limit for all blockchains.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/limit
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/notional/limit", kwargs=kwargs
        )
        return response

    def get_governor_notional_limit_detail_by_chain(
        self, chain: int, **kwargs: dict
    ) -> dict:
        """
        Returns the detailed notional limit available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/notional/limit/:chain
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/notional/limit", chain, kwargs=kwargs
        )
        return response

    def get_governor_max_notional_available_by_chain(self, chain: int) -> dict:
        """
        Returns the maximum amount of notional value available for a given blockchain.

        Args:
            *chain (int): ID of the blockchain.

        Endpoint - /api/v1/governor/notional/max_available/:chain
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/notional/max_available", chain
        )
        return response

    def get_governor_status(self, **kwargs: dict) -> dict:
        """
        Returns the governor status for all guardians.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/status
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/status", kwargs=kwargs
        )
        return response

    def get_governor_status_by_guardian_address(
        self, guardian_address: str, **kwargs: dict
    ) -> dict:
        """
        Returns the governor status for a given guardian.

        Args:
            *guardian_address (str): Address of the guardian.

            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/governor/status/:guardian_address
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/governor/status", guardian_address, kwargs=kwargs
        )
        return response

    # ---------------  HEALTH ---------------
    def get_health_check(self) -> dict:
        """
        Health check.

        Endpoint - /api/v1/health
        """
        response = self._api_client.get("/api/v1/health")
        return response

    # ---------------  LAST-TXS ---------------
    def get_last_transactions(
        self, *, time_span: str = "1d", sample_rate: str = "1h"
    ) -> dict:
        """
        Returns the number of transactions by a defined time span and sample rate.

        Args:
            time_span (str): Time Span, default: 1d, supported values: [1d, 1w, 1mo]. 1mo ​​is 30 days.
            sample_rate (str): Sample Rate, default: 1h, supported values: [1h, 1d]. Valid configurations with timeSpan: 1d/1h, 1w/1d, 1mo/1d.

        Endpoint - /api/v1/last-txs
        """
        kwargs = {"time_span": time_span, "sample_rate": sample_rate}

        response = self._api_client.get_with_url_builder(
            "/api/v1/last-txs", kwargs=kwargs
        )
        return response

    # ---------------  OBSERVATIONS ---------------
    def get_observations(self, **kwargs: dict) -> dict:
        """
        Returns all observations, sorted in descending timestamp order.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/observations", kwargs=kwargs
        )
        return response

    def get_observations_by_chain(self, chain: int, **kwargs: dict) -> dict:
        """
        Returns all observations for a given blockchain, sorted in descending timestamp order.

        Args:
            *chain (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/observations", chain, kwargs=kwargs
        )
        return response

    def get_observations_by_emitter(
        self, chain: int, emitter: str, **kwargs: dict
    ) -> dict:
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
        response = self._api_client.get_with_url_builder(
            "/api/v1/observations", chain, emitter, kwargs=kwargs
        )
        return response

    def get_observations_by_sequence(
        self, chain: int, emitter: str, sequence: int, **kwargs: dict
    ) -> dict:
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
        response = self._api_client.get_with_url_builder(
            "/api/v1/observations", chain, emitter, sequence, kwargs=kwargs
        )
        return response

    def get_observations_by_id(
        self,
        chain: int,
        emitter_address: str,
        sequence: int,
        signer: str,
        hash: str,
        **kwargs: dict,
    ) -> dict:
        """
        Find a specific observation.

        Args:
            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values : ASC, DESC

        Endpoint - /api/v1/observations/:chain/:emitter/:sequence/:signer/:hash
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/observations",
            chain,
            emitter_address,
            sequence,
            signer,
            hash,
            kwargs=kwargs,
        )
        return response

    # ---------------  OPERATIONS ---------------
    def get_operations(self, **kwargs: dict) -> dict:
        """
        Find all operations.

        Args:
            address (str): Address of the emitter.
            tx_hash (str): Hash of the transaction.
            page (int): Page number.
            page_size (int): Number of elements per page.

        Endpoint - /api/v1/operations/
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/operations", kwargs=kwargs
        )
        return response

    def get_operation_by_id(
        self,
        chain_id: int,
        emitter: str,
        seq: int,
    ) -> dict:
        """
        Find operations by ID (chainID/emitter/sequence).

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/operations/{chain_id}/{emitter}/{seq}
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/operations", chain_id, emitter, seq
        )
        return response

    # ------------- STATS ---------------
    def get_protocol_stats(self) -> dict:
        """
        Returns the representative stats for the top protocols.

        Endpoint = /api/v1/protocols/stats
        """
        response = self._api_client.get("/api/v1/protocols/stats")
        return response

    # ---------------  READY ---------------
    def get_ready_check(self) -> dict:
        """
        Ready check.

        Endpoint - /api/v1/ready
        """
        response = self._api_client.get("/api/v1/ready")
        return response

    # ---------------  RELAY ---------------
    def get_relay_by_vaa_id(self, chain_id: int, emitter: str, seq: int) -> dict:
        """
        Get a specific relay information by chainID, emitter address and sequence.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/relays/:chain/:emitter/:sequence
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/relays", chain_id, emitter, seq
        )
        return response

    # ---------------  SCORECARDS ---------------
    def get_scorecards(self) -> dict:
        """
        Returns a list of KPIs for Wormhole.
        TVL is total value locked by token bridge contracts in USD.
        Volume is the all-time total volume transferred through the token bridge in USD.
        24h volume is the volume transferred through the token bridge in the last 24 hours, in USD.
        Total Tx count is the number of txn bridging assets since the creation of the network (does not include Pyth or other messages).
        24h tx count is the number of transaction bridging assets in the last 24 hours (does not include Pyth or other messages).
        Total messages is the number of VAAs emitted since the creation of the network (includes Pyth messages).

        Endpoint - /api/v1/scorecards
        """
        response = self._api_client.get("/api/v1/scorecards")
        return response

    # ---------------  TOKEN ---------------
    def get_token_by_chain_and_address(self, chain_id: int, token_address: str) -> dict:
        """
        Returns a token symbol, coingecko id and address by chain and token address.

        Args:
            *chain_id (int): ID of the blockchain.
            *token_address (str): Token address.

        Endpoint - /api/v1/token/:chain_id/:token_address
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/token", chain_id, token_address
        )
        return response

    # ---------------  TOP ---------------
    def get_top_100_corridors(self, *, time_span: str = "2d") -> dict:
        """
        Returns a list of the top 100 tokens, sorted in descending order by the number of transactions.

        Args:
            time_span (str): Time span, supported values: 2d and 7d (default is 2d).

        Endpoint - /api/v1/top-100-corridors
        """
        kwargs = {"time_span": time_span}

        response = self._api_client.get_with_url_builder(
            "/api/v1/top-100-corridors", kwargs=kwargs
        )
        return response

    def get_top_assets_by_volume(self, *, time_span: str) -> dict:
        """
        Returns a list of emitter_chain and asset pairs with ordered by volume.
        The volume is calculated using the notional price of the symbol at the day the VAA was emitted.

        Args:
            *time_span (str): Time span, supported values: 7d, 15d, 30d.

        Endpoint - /api/v1/top-assets-by-volume
        """
        kwargs = {"time_span": time_span}

        response = self._api_client.get_with_url_builder(
            "/api/v1/top-assets-by-volume", kwargs=kwargs
        )
        return response

    def get_top_chain_pairs_by_num_transfers(self, *, time_span: str) -> dict:
        """
        Returns a list of the emitter_chain and destination_chain pair ordered by transfer count.

        Args:
            *time_span (str): Time span, supported values: 7d, 15d, 30d.

        Endpoint - /api/v1/top-chain-pairs-by-num-transfers
        """
        kwargs = {"time_span": time_span}

        response = self._api_client.get_with_url_builder(
            "/api/v1/top-chain-pairs-by-num-transfers", kwargs=kwargs
        )
        return response

    def get_top_symbols_by_volume(self, *, time_span: str = "7d") -> dict:
        """
        Returns a list of symbols by origin chain and tokens.
        The volume is calculated using the notional price of the symbol at the day the VAA was emitted.

        Args:
            time_span (str): Time span, supported values: 7d, 15d and 30d (default is 7d).

        Endpoint - /api/v1/top-symbols-by-volume
        """
        kwargs = {"time_span": time_span}

        response = self._api_client.get_with_url_builder(
            "/api/v1/top-symbols-by-volume", kwargs=kwargs
        )
        return response

    # ---------------  TRANSACTIONS ---------------
    def get_transactions(self, **kwargs: dict) -> dict:
        """
        Returns transactions. Output is paginated.

        Args:
            page (int): Page number. Starts at 0.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC
            address (str): Filter transactions by Address.

        Endpoint - /api/v1/transactions/
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/transactions", kwargs=kwargs
        )
        return response

    def get_transaction_by_id(self, chain_id: int, emitter: str, seq: int) -> dict:
        """
        Find VAA (perhaps transaction?) metadata by ID.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

        Endpoint - /api/v1/transactions/:chain_id/:emitter/:seq
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/transactions", chain_id, emitter, seq
        )
        return response

    # ---------------  VAAs ---------------
    def get_all_vaas(self, **kwargs: dict) -> dict:
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
        response = self._api_client.get_with_url_builder("/api/v1/vaas", kwargs=kwargs)
        return response

    def get_vaas_by_chain(self, chain_id: str, **kwargs: dict) -> dict:
        """
        Returns all the VAAs generated in specific blockchain.

        Args:
            *chain_id (int): ID of the blockchain.

            page (int): Page number.
            page_size (int): Number of elements per page.
            sort_order (str): Sort results in ascending or descending order. Available values: ASC, DESC.

        Endpoint - /api/v1/vaas/:chain_id
        """
        response = self._api_client.get_with_url_builder(
            "/api/v1/vaas", chain_id, kwargs=kwargs
        )
        return response

    def get_vaas_by_emitter(self, chain: int, emitter: str, **kwargs: dict) -> dict:
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
        response = self._api_client.get_with_url_builder(
            "/api/v1/vaas", chain, emitter, kwargs=kwargs
        )
        return response

    def get_vaa_by_id(
        self,
        chain: int,
        emitter: str,
        seq: str,
        payload: bool = None,
        **kwargs: dict,
    ) -> dict:
        """
        Find a VAA by ID.

        Args:
            *chain_id (int): ID of the blockchain.
            *emitter (str): Address of the emitter.
            *seq (int): Sequence of the VAA.

            parsed_payload (bool): Include the parsed contents of the VAA, if available.

        Endpoint - /api/v1/vaas/:chain_id/:emitter/:seq
        """
        if payload:
            kwargs["payload"] = payload

        response = self._api_client.get_with_url_builder(
            "/api/v1/vaas", chain, emitter, seq, kwargs=kwargs
        )
        return response

    def parse_vaa(self, vaa: dict):
        """
        Parse a VAA.

        Endpoint - /api/v1/vaas/parse
        """
        return self._api_client.post("/api/v1/vaas/parse/", json=vaa)

    def get_vaa_counts(self) -> dict:
        """
        Returns the total number of VAAs emitted for each blockchain.

        Endpoint - /api/v1/vaas/vaa-counts
        """
        response = self._api_client.get("/api/v1/vaas/vaa-counts")
        return response

    # ---------------  VERSION ---------------
    def get_version(self) -> dict:
        """
        Get version/release information.

        Endpoint - /api/v1/version
        """
        response = self._api_client.get("/api/v1/version")
        return response

    # ---------------  X-CHAIN-ACTIVITY ---------------
    def get_x_chain_activity(
        self, *, time_span: str = "7d", by: str = "notional", apps: str = "apps"
    ) -> dict:
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

        response = self._api_client.get_with_url_builder(
            "/api/v1/x-chain-activity", kwargs=kwargs
        )
        return response

    def get_x_chain_activity_by_tops(
        self,
        *,
        time_span: str,
        from_: str,
        to: str,
        app_id: str = None,
        source_chain: str = None,
        target_chain: str = None,
        **kwargs: dict,
    ) -> dict:
        """
        Search for a specific period of time the number of transactions and the volume.

        Args:
            time_span (str): Time span, supported values: 7d, 30d, 90d, 1y and all-time (default is 7d).
            from (str): Renders the results using notional or tx count (default is notional).
            to (str): List of apps separated by comma (default is all apps).

        Endpoint - /api/v1/x-chain-activity/tops
        """
        kwargs = {
            "time_span": time_span,
            "from": from_,
            "to": to,
        }
        if app_id:
            kwargs["app_id"] = app_id
        if source_chain:
            kwargs["source_chain"] = source_chain
        if target_chain:
            kwargs["target_chain"] = target_chain

        response = self._api_client.get_with_url_builder(
            "/api/v1/x-chain-activity/tops", kwargs=kwargs
        )
        return response
