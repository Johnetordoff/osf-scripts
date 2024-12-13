import os
import requests
import logging
from scripts import token, urls
from scripts.node_request import create_institutional_access_request

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
    env = 'staging3'  # Choose the environment: 'production', 'staging', etc.
    target_node_id = "target_node_id"  # Replace with the actual node ID
    message_recipent_id = 'message_recipent_id'
    requested_permissions = "requested_permissions"
    comment = "comment"
    institution_id = "institution_id"  # Replace with the actual institution ID

    try:
        logging.info(f"Creating an InstitutionalRequest for node ID: {target_node_id} and institution: {institution_id}")
        response = create_institutional_access_request(env, target_node_id, comment, institution_id, token, message_recipent=message_recipent_id, requested_permissions=requested_permissions, bcc_sender=True, reply_to=True)

        if response.status_code in [200, 201]:  # Success
            log_success("Institutional access request created successfully!", response.json())
        elif response.status_code == 409:  # Conflict
            logging.warning("An InstitutionalRequest already exists for this node.")
        else:
            log_error("creating InstitutionalRequest", response)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the API request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
