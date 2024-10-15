import requests

from scripts import urls


def list_preprint_providers(env, token, params=None):
    """
    List all preprint providers.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}preprint_providers/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def get_preprint_provider(env, preprint_provider_id, token):
    """
    Retrieve details of a specific preprint provider.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param preprint_provider_id: The unique identifier of the preprint provider.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}preprint_providers/{preprint_provider_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def list_preprints_for_provider(env, preprint_provider_id, token, params=None):
    """
    List all preprints from a specified preprint provider.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param preprint_provider_id: The unique identifier of the preprint provider.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}preprint_providers/{preprint_provider_id}/preprints/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def list_taxonomies_for_provider(env, preprint_provider_id, token, params=None):
    """
    List all taxonomies for a specified preprint provider.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param preprint_provider_id: The unique identifier of the preprint provider.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}preprint_providers/{preprint_provider_id}/taxonomies/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def list_licenses_for_provider(env, preprint_provider_id, token, params=None):
    """
    List all licenses allowed by a specified preprint provider.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param preprint_provider_id: The unique identifier of the preprint provider.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}preprint_providers/{preprint_provider_id}/licenses/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)
