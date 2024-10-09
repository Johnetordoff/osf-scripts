import requests
from scripts import urls, token


def get_collections(env, collection_id, token, auth=None):
    return requests.get(
        f'{urls[env]}collections/{collection_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def create_collection(env, attributes, token, auth=None):
    return requests.post(
        f'{urls[env]}collections/',
        json={
            "data": {
                "type": "collections",
                "attributes": attributes
            }
        },
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def delete_collection(env, collection_id, token, auth=None):
    return requests.delete(
        f'{urls[env]}collections/{collection_id}/',
        auth=auth,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def add_provider_collection(env, provider_id, attributes, token, auth=None):
    return requests.post(
        f'{urls[env]}providers/collections/{provider_id}/submissions/',
        auth=auth,
        json={
            'data': {
                'type': 'collected-metadata',
                'attributes': attributes
            }
        },
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )


def collection_approve_pending(env, collection_id, node_id, comment, token, auth=None):
    return requests.post(
        f'{urls[env]}collection_submission_actions/',
        auth=auth,
        json={
            'data': {
                'type': 'collection-submission-actions',
                'attributes': {
                    'comment': comment,
                    'trigger': 'accept'
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': f'{node_id}-{collection_id}',
                            'type': 'collection-submission'
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


def collection_resubmit(env, collection_id, node_id, comment, token, auth=None):
    return requests.post(
        f'{urls[env]}collection_submission_actions/',
        auth=auth,
        json={
            'data': {
                'type': 'collection-submissions-actions',
                'attributes': {
                    'comment': comment,
                    'trigger': 'resubmit'
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': f'{node_id}-{collection_id}',
                            'type': 'collection-submission'
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


def collection_remove(env, collection_id, node_id, comment, token, auth=None):
    return requests.post(
        f'{urls[env]}collection_submission_actions/',
        auth=auth,
        json={
            'data': {
                'type': 'collection-submissions-actions',
                'attributes': {
                    'comment': comment,
                    'trigger': 'remove'
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': f'{node_id}-{collection_id}',
                            'type': 'collection-submission'
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


def collection_cancel(env, collection_id, node_id, comment, token, auth=None):
    return requests.post(
        f'{urls[env]}collection_submission_actions/',
        auth=auth,
        json={
            'data': {
                'type': 'collection-submissions-actions',
                'attributes': {
                    'comment': comment,
                    'trigger': 'cancel'
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': f'{node_id}-{collection_id}',
                            'type': 'collection-submission'
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


def collection_reject(env, collection_id, node_id, comment, token, auth=None):
    return requests.post(
        f'{urls[env]}collection_submission_actions/',
        auth=auth,
        json={
            'data': {
                'type': 'collection-submission-actions',
                'attributes': {
                    'comment': comment,
                    'trigger': 'reject'
                },
                'relationships': {
                    'target': {
                        'data': {
                            'id': f'{node_id}-{collection_id}',
                            'type': 'collection-submission'
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
