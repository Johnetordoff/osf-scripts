import requests

from scripts import urls

def list_registration_schema_blocks(env, schema_response_id, token):
    """
    Retrieve a list of Registration Schema Blocks for a Schema Response.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param schema_response_id: The unique identifier of the Schema Response.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}schema_responses/{schema_response_id}/schema_blocks/"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def get_registration_schema_block(env, schema_response_id, schema_response_block_id, token):
    """
    Retrieve a Registration Schema Block by its ID.

    :param env: Environment (e.g., 'production', 'staging', 'test')
    :param schema_response_id: The unique identifier of the Schema Response.
    :param schema_response_block_id: The unique identifier of the Schema Response Block.
    :param token: OSF personal access token for authentication.
    :return: Response object from requests library.
    """
    url = f"{urls[env]}schema_responses/{schema_response_id}/schema_blocks/{schema_response_block_id}"
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)
