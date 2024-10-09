import requests
from scripts import urls, token


def get_addon(env, node_id, provider_id, token, auth=None):
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_addons(env, node_id, token, auth=None):
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/?page[size]=100',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_addon(env, node_id, provider_id, token, payload, auth=None):
    return requests.patch(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
        json=payload
    )


def add_addon(env, node_id, provider_id, token, auth=None):
    return requests.post(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )


def post_addon(env, node_id, provider_id, token, auth=None):
    payload = {
        'data': {
            'relationships': {
                'provider': {
                    'data': {
                        'id': provider_id,
                        'type': 'addons',
                    },
                }
            },
            'type': 'nodes',
        },
    }
    return requests.post(
        f'{urls[env]}nodes/{node_id}/addons/',
        auth=auth,
        json=payload,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )


def delete_addon(env, node_id, provider_id, token, auth=None):
    return requests.delete(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )
