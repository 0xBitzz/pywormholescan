def convert_to_camel_case(query: str) -> str:
    """
    Takes a query in snake_case and converts it to camelCase.

    Args:
        query (str): Query param to convert.
    """
    splitted_query = query.split("_")
    return f"{splitted_query[0]}" + "".join(
        [splitted_query[i].title() for i in range(len(splitted_query)) if i != 0]
    )
