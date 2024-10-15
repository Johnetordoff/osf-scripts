import os
import requests

from scripts import urls, waterbutler_urls

HERE = os.path.split(os.path.abspath(__file__))[0]


def update_file(env, file_id, token, attributes):
    return requests.patch(
        f'{urls[env]}files/{file_id}/',
        json={
                'data': {
                    'id': file_id,
                    'type': 'files',
                    'attributes': attributes
                }
            },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def upload_file(env, resource_id, provider_id, file_path, file_name, token):
    base_url = waterbutler_urls[env]

    with open(file_path, 'rb') as f:
        file_data = f.read()

    return requests.put(
        f'{base_url}v1/resources/{resource_id}/providers/{provider_id}/?name={file_name}',
        data=file_data,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/octet-stream',
        }
    )


def upload_new_file_version(env, resource_id, provider_id, file_path, file_id, token):
    base_url = waterbutler_urls[env]
    with open(os.path.join(HERE, file_path), 'rb') as f:
        file_data = f.read()

    return requests.put(
        f'{base_url}v1/resources/{resource_id}/providers/{provider_id}/{file_id}',
        data=file_data,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/octet-stream',
        }
    )


def delete_file(env, resource_id, provider_id, file_id, token):
    return requests.delete(
        f'{waterbutler_urls[env]}v1/resources/{resource_id}/providers/{provider_id}/{file_id}',
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/octet-stream',
        }
    )


def get_file(env, file_id, token):
    return requests.get(
        f'{urls[env]}files/{file_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
