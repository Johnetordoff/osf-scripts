import requests
from scripts import token, urls


def create_project(env, attributes, token):
    """Creates a new project and returns its ID."""
    response = requests.post(
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

    if response.status_code != 201:
        print_error("creating project", response)
        return None

    project_id = response.json()['data']['id']
    print_success("Project created successfully!", {"Project ID": project_id})
    return project_id


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

    # Step 1: Create a new project
    attributes = {
        'title': 'My New Project',
        'description': 'This project was created via the OSF API.',
        'category': 'project'
    }
    create_project(env, attributes, token)


if __name__ == '__main__':
    main()
