import http.client
import json
from urllib.parse import urlencode


def make_request(env, method, endpoint, token=None, params=None, body=None):
    """
    Make an HTTP request using http.client.

    Args:
        env (str): The environment base URL (e.g., "api.osf.io").
        method (str): HTTP method (GET, POST, PATCH, DELETE).
        endpoint (str): API endpoint.
        token (str, optional): Personal access token for authorization.
        params (dict, optional): Query parameters for the URL.
        body (dict, optional): JSON payload for the request.

    Returns:
        dict: Parsed JSON response or None in case of errors.
    """
    conn = http.client.HTTPSConnection(env)
    headers = {"Content-Type": "application/vnd.api+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    if params:
        endpoint += f"?{urlencode(params)}"

    try:
        conn.request(method, endpoint, body=json.dumps(body) if body else None, headers=headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        if response.status in {200, 201}:
            return json.loads(data)
        else:
            print(f"Error {response.status}: {data.decode()}")
            return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None


def list_users(env, token, params=None):
    """List all users."""
    endpoint = "/v2/users/"
    return make_request(env, "GET", endpoint, token=token, params=params)


def get_user(env, user_id, token):
    """Retrieve a user by ID."""
    endpoint = f"/v2/users/{user_id}/"
    return make_request(env, "GET", endpoint, token=token)


def update_user(env, user_id, attributes, token):
    """Update a user's information."""
    endpoint = f"/v2/users/{user_id}/"
    body = {"data": {"type": "users", "id": user_id, "attributes": attributes}}
    return make_request(env, "PATCH", endpoint, token=token, body=body)


def list_user_institutions(env, user_id, token):
    """List all institutions affiliated with a user."""
    endpoint = f"/v2/users/{user_id}/institutions/"
    return make_request(env, "GET", endpoint, token=token)


def list_user_nodes(env, user_id, token, params=None):
    """List all nodes that the user contributes to."""
    endpoint = f"/v2/users/{user_id}/nodes/"
    return make_request(env, "GET", endpoint, token=token, params=params)


def list_user_preprints(env, user_id, token, params=None):
    """List all preprints that the user contributes to."""
    endpoint = f"/v2/users/{user_id}/preprints/"
    return make_request(env, "GET", endpoint, token=token, params=params)


def list_user_registrations(env, user_id, token, params=None):
    """List all registrations that the user contributes to."""
    endpoint = f"/v2/users/{user_id}/registrations/"
    return make_request(env, "GET", endpoint, token=token, params=params)


def list_user_addons(env, user_id, token):
    """List all addons authorized by the user."""
    endpoint = f"/v2/users/{user_id}/addons/"
    return make_request(env, "GET", endpoint, token=token)


def get_user_addon(env, user_id, provider, token):
    """Retrieve details of an authorized user addon."""
    endpoint = f"/v2/users/{user_id}/addons/{provider}/"
    return make_request(env, "GET", endpoint, token=token)


def list_user_addon_accounts(env, user_id, provider, token):
    """List all addon accounts authorized by the user for a specific provider."""
    endpoint = f"/v2/users/{user_id}/addons/{provider}/accounts/"
    return make_request(env, "GET", endpoint, token=token)


def get_user_addon_account(env, user_id, provider, account_id, token):
    """Retrieve details of a specific addon account authorized by the user."""
    endpoint = f"/v2/users/{user_id}/addons/{provider}/accounts/{account_id}/"
    return make_request(env, "GET", endpoint, token=token)
