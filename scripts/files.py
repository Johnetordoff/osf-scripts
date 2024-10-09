import requests

from scripts import urls, token


def add_tags_to_file(env, file_id, token, attributes):
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
