import requests
from scripts import token, urls


def create_new_draft_registation(env, schema_id, branched_from, token):
    return requests.post(
        f'{urls[env]}draft_registrations/',
        json={
            'data': {
                'type': 'draft_registrations',
                'attributes': {
                    'branched_from': branched_from
                },
                'relationships': {
                    'registration_schema': {
                        'data': {
                            'id': schema_id,
                            'type': 'registration_schemas'
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


def update_draft_registation(env, draft_id, attributes, token):
    return requests.patch(
        f'{urls[env]}draft_registrations/{draft_id}/',
        json={
            'data': {
                'id': draft_id,
                'type': 'draft_registrations',
                'attributes': attributes
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def delete_draft_registation(env, draft_id, token):
    return requests.delete(
        f'{urls[env]}draft_registrations/{draft_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def get_draft_registration_contributors(env, draft_id, token):
    return requests.get(
        f'{urls[env]}draft_registrations/{draft_id}/contributors/?format=json',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def add_draft_registration_contributor(env, draft_id, user_id, token):
    return requests.post(
        f'{urls[env]}draft_registrations/{draft_id}/contributors/',
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
