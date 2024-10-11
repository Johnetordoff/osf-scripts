import os
import requests
import logging
from scripts import token, urls
from scripts.nodes import create_node
from scripts.files import upload_file

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG to capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)


def log_success(message, data=None):
    """Logs a success message with optional data."""
    logging.info(f"{message}")
    if data:
        logging.info("Details:")
        logging.info(data)


def log_error(action, response=None):
    """Logs an error message with optional response details."""
    logging.error(f"Error {action}.")
    if response is not None:
        logging.error(f"Status code: {response.status_code}")
        try:
            error_details = response.json()
            logging.error("Response content:")
            logging.error(error_details)
        except ValueError:
            logging.error("Response content is not valid JSON.")
    else:
        logging.error("No response received.")


def main():
    env = 'staging3'  # Choose the environment: 'production', 'staging', 'staging2', 'staging3', or 'test'

    try:
        # Step 1: Create a new project
        attributes = {
            'title': 'My New Project',
            'description': 'This project was created via the OSF API.',
            'category': 'project'
        }

        logging.info("Creating a new project with attributes: %s", attributes)
        response = create_node(env, attributes, token)

        if response.status_code == 201:  # Success case
            data = response.json()['data']
            resource_id = data['id']
            log_success("Project created successfully!", {"Project ID": resource_id})
        else:
            log_error("creating project", response)
            return

        # Step 2: Upload a file
        file_path = '../fixtures/test.txt'
        file_name = 'test.txt'
        logging.info(f"Uploading file '{file_name}' to project with resource ID {resource_id}")

        upload_response = upload_file(env, resource_id, 'osfstorage', file_path, file_name, token)

        if upload_response.status_code in [200, 201]:  # Success case for file upload
            log_success(f"File '{file_name}' uploaded successfully.")
        else:
            log_error(f"uploading file '{file_name}'", upload_response)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the API request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
