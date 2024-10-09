import requests
from scripts import token, urls


def update_file_metadata(env, file_id, token, attributes, metadata_record_id):
    return requests.patch(
        f'{urls[env]}files/{file_id}/metadata_records/{metadata_record_id}/',
        json={
                'data': {
                    'id': metadata_record_id,
                    'type': 'metadata_records',
                    'attributes': attributes
                }
            },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
