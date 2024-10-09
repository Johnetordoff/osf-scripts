import requests
from scripts import token, urls

def create_new_schema_response(env, registration_guid, token):
    return requests.post(
        f'{urls[env]}schema_responses/',
        json={
            'data': {
                'type': 'schema-responses',
                'relationships': {
                    'registration': {
                        'data': {
                            'id': registration_guid,
                            'type': 'registrations'
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


def delete_schema_response(env, schema_id, token):
    return requests.delete(
        f'{urls[env]}schema_responses/{schema_id}',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_schema_responses(env, schema_id, token, revision_justification=None, revision_responses=None):
    return requests.patch(
        f'{urls[env]}schema_responses/{schema_id}/',
        json={
                'data': {
                    'type': 'schema-responses',
                    'attributes': {
                        'revision_justification': revision_justification,
                        'revision_responses': revision_responses
                    }
                }
            },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def create_action(env, schema_id, token=None, auth=None, trigger='submit'):
    return requests.post(
        f'{urls[env]}schema_responses/{schema_id}/actions/',
        json={
            'data':
                {
                    'type': 'schema-response-actions',
                    'attributes': {
                        'trigger': trigger,
                    },
                    'relationships': {
                        'target': {
                            'data': {
                                'id': schema_id,
                                'type': 'schema-responses'
                            }
                        }
                    }
                }
        },
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        },
    )
