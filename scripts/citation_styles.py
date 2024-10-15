import requests

from scripts.urls import urls


def list_citation_styles(env, token, params=None):
    """
    List all citation styles.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}citations/styles/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def get_citation_style(env, style_id, token):
    """
    Retrieve details of a specific citation style.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param style_id: The unique identifier of the citation style.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}citations/styles/{style_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)
