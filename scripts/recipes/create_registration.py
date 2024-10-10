import requests
from scripts import token, urls
from scripts.registrations import (
    create_draft_registration,
    update_draft_registration,
    register_draft
)


def make_draft_registration(env, schema_id, provider_id, token):
    """Creates a new draft registration and returns its ID."""
    response = create_draft_registration(env, schema_id, provider_id, token=token)

    if response.status_code != 201:
        print_error("creating draft registration", response)
        return None

    draft_registration_id = response.json()['data']['id']
    print_success("Draft registration created successfully!", {"Draft registration ID": draft_registration_id})
    return draft_registration_id


def update_draft_registration_with_details(env, draft_registration_id, title, description, token):
    """Updates a draft registration with a title and description."""
    attributes = {
        'title': title,
        'description': description
    }

    response = update_draft_registration(env, draft_registration_id, attributes, token)

    if response.status_code != 200:
        print_error("updating draft registration", response)
        return None

    print_success("Draft registration updated successfully with title and description.")
    return response.json()


def print_success(message, data=None):
    """Prints a success message with optional data."""
    print(f"{message}")
    if data:
        print("Details:")
        print(data)


def print_error(action, response):
    """Prints an error message with response details."""
    print(f"Error {action}. Status code: {response.status_code}")
    try:
        error_details = response.json()
        print("Response content:")
        print(error_details)
    except ValueError:
        print("Response content is not valid JSON.")


def main():
    env = 'staging3'  # Choose the environment: 'production', 'staging', 'staging2', 'staging3', or 'test'
    provider_id = 'osf'
    schema_id = '5df3deef83a30f000151b8a5'  # Staging 3 Open-ended schema ID

    # Step 1: Create a new draft registration
    draft_registration_id = make_draft_registration(env, schema_id, provider_id, token)
    if not draft_registration_id:
        return

    # Step 2: Update the draft registration with a title and description
    title = 'Test Registration'
    description = 'This registration was created and updated via API.'
    update_draft_registration_with_details(env, draft_registration_id, title, description, token)

    # Step 3: Register the draft
    resp = register_draft(env, draft_registration_id, provider_id, token)
    if resp.status_code == 201:
        print_success("Draft registration successfully registered.")
        print(resp.json())
    else:
        print_error("registering draft", resp)


if __name__ == '__main__':
    main()
