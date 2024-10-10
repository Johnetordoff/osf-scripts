import requests
from scripts import token, urls


def create_draft_registration(env, schema_id, provider_id, token):
    """Create a new draft registration."""
    return requests.post(
        f'{urls[env]}draft_registrations/',
        json={
            'data': {
                'type': 'draft_registrations',
                'relationships': {
                    'registration_schema': {
                        'data': {
                            'type': 'registration-schemas',
                            'id': schema_id
                        }
                    },
                    'provider': {
                        'data': {
                            'type': 'registration-providers',
                            'id': provider_id
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



def create_draft_registation_from_project(env, schema_id, branched_from, token):
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


def update_draft_registration(env, draft_id, attributes, token):
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


def register_draft(env, draft_registration_id, provider_id, token, embargo_end_date=None):
    """Register a draft registration."""
    return requests.post(
        f'{urls[env]}registrations/',
        json={
            'data': {
                'type': 'registrations',
                'attributes': {
                    'embargo_end_date': embargo_end_date,
                    'draft_registration': draft_registration_id
                },
                'relationships': {
                    'provider': {
                        'data': {
                            'type': 'registration-providers',
                            'id': provider_id
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

