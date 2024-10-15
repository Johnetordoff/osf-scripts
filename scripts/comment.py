import requests

from scripts import urls


def get_comment(env, comment_id, token):
    """
    Retrieve the details of a comment.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param comment_id: The unique identifier of the comment.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}comments/{comment_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def update_comment(env, comment_id, attributes, token):
    """
    Update a comment by setting the provided attributes.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param comment_id: The unique identifier of the comment.
    :param attributes: Dictionary of attributes to update.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}comments/{comment_id}/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'data': {
            'type': 'comments',
            'id': comment_id,
            'attributes': attributes
        }
    }
    return requests.put(url, json=data, headers=headers)


def delete_comment(env, comment_id, token):
    """
    Delete a comment.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param comment_id: The unique identifier of the comment.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}comments/{comment_id}/"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    return requests.delete(url, headers=headers)
