import requests
from scripts import urls


# Create a new node (project or component)
def create_node(env, attributes, token):
    """Creates a new node (project or component) and returns its ID."""
    return requests.post(
        f'{urls[env]}nodes/',
        json={
            'data': {
                'type': 'nodes',
                'attributes': attributes
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def create_node_with_institutional_affiliation(env, attributes, institution_id, token):
    """Creates a new node (project or component) with institutional affiliation."""
    return requests.post(
        f'{urls[env]}nodes/',
        json={
            'data': {
                'type': 'nodes',
                'attributes': attributes,
                'relationships': {
                    'affiliated_institutions': {
                        'data': [
                            {
                                'type': 'institutions',
                                'id': institution_id
                            }
                        ]
                    }
                }
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def create_node_with_region(env, attributes, region_id, token):
    """Creates a new node (project or component) with institutional affiliation."""
    return requests.post(
        f'{urls[env]}nodes/',
        json={
            'data': {
                'type': 'nodes',
                'attributes': attributes,
                'relationships': {
                    'region': {
                        'data': {
                            'type': 'regions',
                            'id': region_id
                        }
                    },
                }
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


# Retrieve the details of a given node
def retrieve_node(env, node_id, token):
    """Retrieves the details of a given node (project or component)."""
    return requests.get(
        f'{urls[env]}nodes/{node_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def update_node(env, node_id, attributes=None, token=None):
    """Updates a node by setting the values of the specified attributes."""
    if not attributes:
        attributes = {}

    return requests.patch(
        f'{urls[env]}nodes/{node_id}/',
        json={
            'data': {
                'type': 'nodes',
                'id': node_id,
                'attributes': attributes
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def delete_node(env, node_id, token):
    """Permanently deletes a node."""
    return requests.delete(
        f'{urls[env]}nodes/{node_id}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def list_addons(env, node_id, token):
    """Lists all addons connected to a node or project."""
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )



def list_addon_folders(env, node_id, provider, token):
    """Lists all folders retrieved from the associated third-party service for a node."""
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/{provider}/folders/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def retrieve_addon(env, node_id, provider, token):
    """Retrieves details of an individual addon connected to a node."""
    return requests.get(
        f'{urls[env]}nodes/{node_id}/addons/{provider}/',
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


# Update a node addon
def update_addon(env, node_id, provider, account_id, folder_id, folder_path, url, label, token):
    """Updates a node addon by setting the specified attributes."""
    return requests.patch(
        f'{urls[env]}nodes/{node_id}/addons/{provider}/',
        json={
            'data': {
                'type': 'node_addons',
                'id': provider,
                'attributes': {
                    'external_account_id': account_id,
                    'folder_id': folder_id,
                    'folder_path': folder_path,
                    'url': url,
                    'label': label
                }
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
