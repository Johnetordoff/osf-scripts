import requests
from scripts import urls, waterbutler_urls


def create_new_preprint(env, attributes, token):
    return requests.post(
        f'{urls[env]}preprints/',
        json={
            'data': {
                'type': 'preprints',
                'attributes': attributes
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_preprint_contributors(env, preprint_id, token):
    return requests.get(
        f'{urls[env]}preprints/{preprint_id}/contributors/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_preprint_contributor(env, preprint_id, user_id, token):
    return requests.get(
        f'{urls[env]}preprints/{preprint_id}/contributors/{user_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def add_preprint_contributor(env, preprint_id, user_id, send_email: bool, token):
    return requests.post(
        f'{urls[env]}preprints/{preprint_id}/contributors/?send_email={send_email.lower()}',
        json={
          "data": {
            "type": "contributors",
            "attributes": {},
            "relationships": {
              "user": {
                "data": {
                  "type": "users",
                  "id": user_id
                }
              }
            }
          }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def edit_preprint_contributor(env, preprint_id, user_id, attributes, contributor_id, token):
    return requests.patch(
        f'{urls[env]}preprints/{preprint_id}/contributors/{user_id}/',
        json={
            "data":
                {
                    "id": contributor_id,
                    "attributes": attributes,
                    "relationships": {},
                    "type": "contributors"
                }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_preprint_institution_affiliation(env, preprint_id, institution_ids, token):
    return requests.put(
        f'{urls[env]}preprints/{preprint_id}/relationships/institutions/',
        json={
            'data': [
                {'type': 'institutions', 'id': inst_id} for inst_id in institution_ids
            ]
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def remove_all_preprint_institutions(env, preprint_id, token):
    return requests.put(
        f'{urls[env]}preprints/{preprint_id}/relationships/institutions/',
        json={'data': []},
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def upload_file_to_preprint(env, preprint_id, file_path, file_name, token):
    # Get the base URL for the environment
    base_url = waterbutler_urls[env]
    # Append query parameters for uploading
    # Read the file data
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/octet-stream',
    }

    # Make the PUT request to upload the file
    response = requests.put(
        f'{base_url}v1/resources/{preprint_id}/providers/osfstorage/?name={file_name}',
        data=file_data,
        headers=headers
    )

    return response


def set_preprint_primary_file(env, preprint_id, file_id, token):
    url = f'{urls[env]}preprints/{preprint_id}/'
    payload = {
        "data": {
            "id": preprint_id,
            "type": "preprints",
            "attributes": {},
            "relationships": {
                "primary_file": {
                    "data": {
                        "type": "files",
                        "id": file_id
                    }
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.patch(url, json=payload, headers=headers)
    return response


def create_preprint_review_action(env, preprint_id, trigger, token, comment=''):
    """
    """
    url = f'{urls[env]}preprints/{preprint_id}/review_actions/'
    payload = {
        "data": {
            "type": "review_actions",
            "attributes": {
                "trigger": trigger,
                "comment": comment
            },
            "relationships": {
                "target": {
                    "data": {
                        "type": "preprints",
                        "id": preprint_id
                    }
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response


def update_subject_and_licenses(env, preprint_id, license_id, subject_ids, token):
    """
    Adds subjects and a license to a preprint.

    Parameters:
    - env: The environment key (e.g., 'production', 'staging', 'staging3').
    - preprint_id: The unique identifier of the preprint.
    - license_id: The unique identifier of the license.
    - subject_ids: A list of subject IDs to associate with the preprint.
    - token: Your personal access token for authentication.

    Returns:
    - Response object from the PATCH request.
    """
    url = f'{urls[env]}preprints/{preprint_id}/'
    payload = {
        "data": {
            "id": preprint_id,
            "type": "preprints",
            "attributes": {},
            "relationships": {
                "license": {
                    "data": {
                        "type": "licenses",
                        "id": license_id
                    }
                },
                "subjects": {
                    "data": [
                        {
                            "type": "subjects",
                            "id": subject_id
                        } for subject_id in subject_ids
                    ]
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.patch(url, json=payload, headers=headers)
    return response


def create_review_action(env, preprint_id, trigger, token):
    """
    Creates a review action for a preprint (e.g., submit, accept).

    Parameters:
    - env (str): The environment key (e.g., 'production', 'staging3').
    - preprint_id (str): The unique identifier of the preprint.
    - trigger (str): The action to trigger (e.g., 'submit', 'accept').
    - token (str): Personal access token for authentication.

    Returns:
    - Response object from the POST request.
    """
    url = f'{urls[env]}preprints/{preprint_id}/review_actions/'
    payload = {
        "data": {
            "type": "review_actions",
            "attributes": {
                "trigger": trigger
            },
            "relationships": {
                "target": {
                    "data": {
                        "type": "preprints",
                        "id": preprint_id
                    }
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response
