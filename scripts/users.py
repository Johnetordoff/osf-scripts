# scripts/users.py

import requests

from scripts.urls import urls


def list_users(env, token, params=None):
    """
    List all users.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def get_user(env, user_id, token):
    """
    Retrieve a user by ID.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def update_user(env, user_id, attributes, token):
    """
    Update a user's information.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param attributes: Dictionary of attributes to update.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'data': {
            'type': 'users',
            'id': user_id,
            'attributes': attributes
        }
    }
    return requests.patch(url, json=data, headers=headers)


def list_user_institutions(env, user_id, token):
    """
    List all institutions affiliated with a user.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/institutions/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def list_user_nodes(env, user_id, token, params=None):
    """
    List all nodes that the user contributes to.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/nodes/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def list_user_preprints(env, user_id, token, params=None):
    """
    List all preprints that the user contributes to.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/preprints/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def list_user_registrations(env, user_id, token, params=None):
    """
    List all registrations that the user contributes to.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user.
    :param token: OSF personal access token for authentication.
    :param params: Optional query parameters (e.g., filtering).
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/registrations/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers, params=params)


def list_user_addons(env, user_id, token):
    """
    List all addons authorized by the user.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/addons/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def get_user_addon(env, user_id, provider, token):
    """
    Retrieve details of an authorized user addon.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param provider: The unique identifier of the addon provider.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/addons/{provider}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def list_user_addon_accounts(env, user_id, provider, token):
    """
    List all addon accounts authorized by the user for a specific provider.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param provider: The unique identifier of the addon provider.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}users/{user_id}/addons/{provider}/accounts/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def get_user_addon_account(env, user_id, provider, account_id, token):
    """
    Retrieve details of a specific addon account authorized by the user.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param user_id: The unique identifier of the user ('me' for current user).
    :param provider: The unique identifier of the addon provider.
    :param account_id: The unique identifier of the addon account.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = (
        f"{urls[env]}users/{user_id}/addons/{provider}/accounts/{account_id}/"
    )
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)
