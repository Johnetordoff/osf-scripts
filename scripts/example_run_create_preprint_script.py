import argparse
from scripts import token
from scripts.preprints import (
    create_new_preprint,
    upload_file_to_preprint,
    set_preprint_primary_file,
    create_preprint_review_action,
    update_subject_and_licenses
)


def create_preprint(env, attributes, token):
    response = create_new_preprint(env, attributes, token)
    if response.status_code != 201:
        print_error("creating preprint", response)
        return None
    preprint_id = response.json()['data']['id']
    print_success("Preprint created successfully!", {"Preprint ID": preprint_id})
    return preprint_id


def update_subjects_and_license(env, preprint_id, license_id, subject_ids, token):
    response = update_subject_and_licenses(env, preprint_id, license_id, subject_ids, token)
    if response.status_code != 200:
        print_error("updating subjects and license", response)
        return False
    print_success("Subjects and license updated successfully.", response.json())
    return True


def upload_and_set_primary_file(env, preprint_id, file_path, file_name, token):
    upload_response = upload_file_to_preprint(env, preprint_id, file_path, file_name, token)
    if upload_response.status_code not in (200, 201):
        print_error("uploading file", upload_response)
        return False
    file_id = extract_file_id(upload_response.json())
    if not file_id:
        print("Error extracting file ID from upload response.")
        return False
    print_success("File uploaded successfully.", upload_response.json())
    primary_response = set_preprint_primary_file(env, preprint_id, file_id, token)
    if primary_response.status_code != 200:
        print_error("setting primary file", primary_response)
        return False
    print_success("Primary file set successfully.", primary_response.json())
    return True


def submit_preprint_review(env, preprint_id, trigger, token):
    review_response = create_preprint_review_action(env, preprint_id, trigger, token)
    if review_response.status_code != 201:
        print_error("submitting preprint for review", review_response)
        return False
    print_success("Preprint submitted for review successfully.", review_response.json())
    return True


def extract_file_id(file_data):
    try:
        return file_data['data']['id'].split('/')[-1]
    except (KeyError, IndexError, TypeError):
        return None


def print_success(message, data):
    print(f"{message}")
    if data:
        print("Details:")
        print(data)


def print_error(action, response):
    print(f"Error {action}. Status code: {response.status_code}")
    try:
        error_details = response.json()
        print("Response content:")
        print(error_details)
    except ValueError:
        print("Response content is not valid JSON.")


def main():
    """
    python3 scripts/example_run_create_preprint_script.py --file_path "path/to/file.txt" --token "your_token"
    :return:
    """
    parser = argparse.ArgumentParser(description="Preprint management script.")
    parser.add_argument('--env', type=str, default='staging3', help="The environment to use.")
    parser.add_argument('--title', type=str, default='My New Preprint', help="Title of the preprint.")
    parser.add_argument('--description', type=str, default='This preprint was created via the OSF API.',
                        help="Description of the preprint.")
    parser.add_argument('--provider', type=str, default='osf', help="Provider ID.")
    parser.add_argument('--license_id', type=str, default='59bac33acb0c480001872bc8', help="License ID.")
    parser.add_argument('--subject_ids', type=str, nargs='+', default=['59c152d305ce91001c0242b4'],
                        help="List of subject IDs.")
    parser.add_argument('--file_path', type=str, required=True, help="Path to the file to upload.")
    parser.add_argument('--file_name', type=str, default='test.txt', help="File name to use on OSF.")
    parser.add_argument('--token', type=str, required=True, help="Authentication token.")

    args = parser.parse_args()

    env = args.env
    token = args.token
    attributes = {
        'title': args.title,
        'description': args.description,
        'provider': args.provider,
    }

    preprint_id = create_preprint(env, attributes, token)
    if not preprint_id:
        return

    if not update_subjects_and_license(env, preprint_id, args.license_id, args.subject_ids, token):
        return

    if not upload_and_set_primary_file(env, preprint_id, args.file_path, args.file_name, token):
        return

    submit_preprint_review(env, preprint_id, 'submit', token)
    submit_preprint_review(env, preprint_id, 'accept', token)


if __name__ == '__main__':
    main()

