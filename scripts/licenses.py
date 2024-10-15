import requests

from scripts import urls


def list_licenses(env, token):
    return requests.get(
        f'{urls[env]}licenses/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_license(env, license_id, token):
    return requests.get(
        f'{urls[env]}licenses/{license_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
