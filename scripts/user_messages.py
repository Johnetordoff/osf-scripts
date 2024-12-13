import requests
from scripts import urls


def create_user_message(env, user_id, message_text, message_type, institution_id, token, bbb_sender=False, reply_to=False,):
    """Creates a new user message."""
    payload = {
        'data': {
            'type': 'user-message',
            'attributes': {
                'message_text': message_text,
                'message_type': message_type,
                'bcc_sender': bbb_sender,
                'reply_to': reply_to,
            },
            'relationships': {
                'institution': {
                    'data': {'id': institution_id, 'type': 'institutions'},
                },
            }
        }
    }
    return requests.post(
        f'{urls[env]}users/{user_id}/messages/',
        json=payload,
        headers={
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
    )
