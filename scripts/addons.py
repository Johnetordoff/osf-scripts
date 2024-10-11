import requests
from scripts import urls


def get_addons(env, token):
    return requests.get(
        f'{urls[env]}/addons/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_node_addon(env, node_id, provider_id, token):
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_node_addons(env, node_id, token):
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_node_addon(env, node_id, provider_id, token, payload):
    return requests.patch(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
        json=payload
    )


def add_node_addon(env, node_id, provider_id, token):
    return requests.post(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )


def post_addon(env, node_id, provider_id, token):
    return requests.post(
        f'{urls[env]}nodes/{node_id}/addons/',
        json={
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
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )


def delete_addon(env, node_id, provider_id, token):
    return requests.delete(
        f'{urls[env]}nodes/{node_id}/addons/{provider_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )
