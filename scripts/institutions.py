import requests
from scripts import urls


def list_institutions(env, token):
    return requests.get(
        f'{urls[env]}institutions/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_institution(env, institution_id, token):
    return requests.get(
        f'{urls[env]}institutions/{institution_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_institution_users(env, institution_id, token):
    return requests.get(
        f'{urls[env]}institutions/{institution_id}/users/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_institution_nodes(env, institution_id, token):
    return requests.get(
        f'{urls[env]}institutions/{institution_id}/nodes/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_institution_registrations(env, institution_id, token):
    return requests.get(
        f'{urls[env]}institutions/{institution_id}/registrations/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
