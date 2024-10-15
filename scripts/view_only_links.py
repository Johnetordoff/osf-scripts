import requests

from scripts import urls


def get_view_only_link(env, link_id, token):
    """
    Retrieve details about a specific view only link.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param link_id: The unique identifier of the view only link.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}view_only_links/{link_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)
