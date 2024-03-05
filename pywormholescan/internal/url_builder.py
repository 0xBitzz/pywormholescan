from pywormholescan.internal.utils import convert_to_camel_case


def build_url(base_url: str, path: str, **kwargs) -> str:
    """
    Builds the complete URL for an API endpoint with path and/or query interpolation.

    Args:
        path: The API endpoint path with placeholders for parameters (e.g., /api/v1/governor/limit).
        kwargs: Keyword arguments to be interpolated into the path placeholders.

    Returns:
        The complete URL string.
    """
    query_params = ""
    if "kwargs" in kwargs.keys():
        queries = "?"
        for k, v in kwargs["kwargs"].items():
            k = convert_to_camel_case(k)
            queries += f"{k}={v}&"
        query_params += queries[:-1]

    url = base_url + path + query_params if query_params else base_url + path
    return url
