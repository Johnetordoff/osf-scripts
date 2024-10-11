from scripts import token
from scripts.addons import add_node_addon, get_addons
from scripts.nodes import create_node


def create_project_enable_add_addons(env, project_attributes, token):
    # Step 1: Create a new project
    response = create_node(env, project_attributes, token)
    if not response:
        print("Failed to create the project.")
        return

    project_id = response.json()['data']['id']
    print(f"Project {project_id} created successfully.")

    response = get_addons(env, token)
    addons = response.json()['data']
    for addon in addons:
        response = add_node_addon(env, project_id, addon['id'], token)


# Example usage
def main():
    env = 'staging3'  # Choose the environment: 'production', 'staging', 'staging2', 'staging3', or 'test'

    project_attributes = {
        'title': 'My New Project with S3 Addon',
        'description': 'This project was created via the OSF API and an S3 addon was added.',
        'category': 'project'
    }

    s3_provider_id = 's3'  # Assuming 's3' is the provider ID for the S3 addon

    create_project_enable_add_addons(env, project_attributes, token)


if __name__ == '__main__':
    main()
