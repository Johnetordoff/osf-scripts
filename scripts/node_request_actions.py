import requests
from scripts import urls


def create_node_request(env, target_id, trigger, comment, token):
    """Creates a new node request for a specific target node."""
    return requests.post(
        f'{urls[env]}requests/nodes/',
        json={
            'data': {
                'type': 'node-request-actions',
                'attributes': {
                    'trigger': trigger,
                    'comment': comment
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': target_id,
                            'type': 'nodes'
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



def update_node_request(env, request_id, trigger, comment, token):
    """Updates an existing node request with a new trigger and/or comment."""
    return requests.patch(
        f'{urls[env]}requests/nodes/{request_id}/',
        json={
            'data': {
                'type': 'node-request-actions',
                'id': request_id,
                'attributes': {
                    'trigger': trigger,
                    'comment': comment
                }
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def delete_node_request(env, request_id, token):
    """Deletes a node request."""
    return requests.delete(
        f'{urls[env]}requests/nodes/{request_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
