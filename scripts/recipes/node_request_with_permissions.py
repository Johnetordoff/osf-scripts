import os
import requests
import logging
from scripts import token, urls
from scripts.node_request import create_node_request_with_permission

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
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
    env = 'local'  # Choose the environment: 'production', 'staging', etc.
    target_node_id = "<node_id>"  # Replace with the actual node ID
    comment = "<test_comment>"
    requested_permissions = "<read/write/admin>"  # only node permissions

    try:
        logging.info(f"Creating a NodeRequest for node ID: {target_node_id} with permissions: {requested_permissions}")
        response = create_node_request_with_permission(env, target_node_id, comment, requested_permissions, token)

        if response.status_code in [200, 201]:  # Success
            log_success("NodeRequest with permissions created successfully!", response.json())
        elif response.status_code == 409:  # Conflict
            logging.warning("A NodeRequest already exists for this node.")
        else:
            log_error("creating NodeRequest with permissions", response)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the API request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
