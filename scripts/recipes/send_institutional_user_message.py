import os
import requests
import logging
from scripts.user_messages import create_user_message
from scripts import token

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
    env = 'local'  # Choose the environment: 'production', 'staging', 'staging2', 'staging3', or 'test'
    user_id = "<user_id>"  # Replace with the recipient user ID
    institution_id = "<institution_id>"  # Replace with the institution ID
    message_text = "<message_text>"  # Replace with your message text
    message_type = "institutional_request"  # Replace with the appropriate message type
    bcc_sender = True # send to a bcc to the sender to remind them of email
    reply_to = True  # adds a header to the email, so users will know who to reply to.

    try:
        logging.info(f"Creating a UserMessage for user ID: {user_id}")
        response = create_user_message(
            env,
            user_id,
            message_text,
            message_type,
            institution_id,
            token,
            bcc_sender,
            reply_to
        )

        if response.status_code in [200, 201]:  # Success
            log_success("UserMessage created successfully!", response.json())
        elif response.status_code == 400:  # Bad request
            logging.warning("Failed to create UserMessage due to bad request.")
        else:
            log_error("creating UserMessage", response)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the API request: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
