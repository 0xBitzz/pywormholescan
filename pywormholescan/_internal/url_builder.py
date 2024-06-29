__all__ = ["build_url"]


def build_url(*args, **kwargs) -> str:
    """
    Builds the complete URL for an API endpoint with path and/or query interpolation.

    Args:
        *args: Positional arguments to be interpolated into the path.
        **kwargs: Keyword arguments to be used as query parameters.

    Returns:
        The complete URL string.
    """
    path_params = "/".join(str(param) for param in args)

    query_params = ""
    if kwargs:
        queries = "&".join(
            f"{_convert_to_camel_case(k)}={v}" for k, v in kwargs["kwargs"].items()
        )
        query_params = f"?{queries}"

    url = f"{path_params}{query_params}" if query_params else path_params
    return url


def _convert_to_camel_case(query: str) -> str:
    """
    Takes a query in snake_case and converts it to camelCase.

    Args:
        query (str): Query param to convert.
    """
    splitted_query = query.split("_")
    return f"{splitted_query[0]}" + "".join(
        [splitted_query[i].title() for i in range(len(splitted_query)) if i != 0]
    )
