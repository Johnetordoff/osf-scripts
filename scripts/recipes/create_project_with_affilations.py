import requests
from scripts import token, urls
from scripts.nodes import create_node_with_institutional_affiliation

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
    institution_id = 'cos'
    response = create_node_with_institutional_affiliation(env, attributes, institution_id, token)

    if response.status_code != 201:
        print_error("creating project", response)
        return None

    project_id = response.json()['data']['id']
    print_success("Project created successfully!", {"Project ID": project_id})
    return project_id


if __name__ == '__main__':
    main()
