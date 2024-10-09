import requests
from scripts import token, urls

resource_id = '62f970b901120c000a80e44e'


def get_resource(env, resource_id, token):
    return requests.get(
        f'{urls[env]}resources/{resource_id}',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_resource(env, resource_id, token, attributes):
    return requests.patch(
        f'{urls[env]}resources/{resource_id}/',
        json={
            "data": {
                "id": resource_id,
                "attributes": attributes,
                "relationships": {},
                "type": "resources"
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def create_resource(env, resource_id, token, attributes):
    return requests.patch(
        f'{urls[env]}resources/{resource_id}',
        json={
            "data": {
                "id": "",
                "attributes": attributes,
                "relationships": {},
                "type": "resources"
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )