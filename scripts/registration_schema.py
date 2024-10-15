import requests
from scripts import urls


def list_registration_schemas(env, token):
    return requests.get(
        f'{urls[env]}schemas/registrations/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_registration_schema(env, registration_schema_id, token):
    return requests.get(
        f'{urls[env]}schemas/registrations/{registration_schema_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
