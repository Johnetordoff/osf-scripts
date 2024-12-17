import requests
from scripts import urls


def create_node_request(env, target_node_id, comment, token):
    """
    Creates a new NodeRequest for the specified node.

    Args:
        env (str): Environment (e.g., 'staging', 'production').
        target_node_id (str): The ID of the target node for which the request is created.
        comment (str): A comment associated with the request.
        token (str): The authentication token.

    Returns:
        Response: The response object from the API request.
    """
    url = f"{urls[env]}nodes/{target_node_id}/requests/"
    payload = {
        "data": {
            "type": "node-requests",
            "attributes": {
                "request_type": "access",  # Assuming 'access' is the type of request being created
                "comment": comment
            }
        }
    }
    headers = {
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"Bearer {token}"
    }

    return requests.post(url, json=payload, headers=headers)


def create_node_request_with_permission(env, target_id, comment, requested_permission, token):
    """Creates a new node request for a specific target node with a requested permission."""
    print(f'{urls[env]}nodes/{target_id}/requests/')
    return requests.post(
        f'{urls[env]}nodes/{target_id}/requests/',
        json={
            'data': {
                'type': 'node-request',
                'attributes': {
                    'request_type': 'access',
                    'comment': comment,
                    'requested_permissions': requested_permission
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


def create_institutional_access_request(env, target_id, comment, institution_id, token, bcc_sender=False, reply_to=False, message_recipient=None, requested_permissions=None,
                                        ):
    """Creates an institutional access request for a specific target node."""
    payload = {
        'data': {
            'type': 'node-request',
            'attributes': {
                'comment': comment,
                'request_type': 'institutional_request',
                'requested_permissions': requested_permissions,
                'bcc_sender': bcc_sender,
                'reply_to': reply_to,
            },
            'relationships': {
                'institution': {
                    'data': {
                        'id': institution_id,
                        'type': 'institutions'
                    }
                }
            }
        }
    }
    if message_recipient:
        payload['data']['relationships'].update(
            {
                'message_recipient': {
                    'data': {
                            'id': message_recipient,
                            'type': 'users'
                        }
                }
            }
        )

    return requests.post(
        f'{urls[env]}nodes/{target_id}/requests/',
        json=payload,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'

        },
    )


def retrieve_node_request(env, request_id, token):
    """Retrieves the details of a specific node request."""
    return requests.get(
        f'{urls[env]}requests/nodes/{request_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_node_requests(env, node_id, token):
    """Lists all requests associated with a specific node."""
    return requests.get(
        f'{urls[env]}nodes/{node_id}/requests/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
