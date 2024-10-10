from scripts import token
from scripts.preprints import (
    create_new_preprint,
    upload_file_to_preprint,
    set_preprint_primary_file,
    create_preprint_review_action,
    update_subject_and_licenses,
    update_preprint_institution_affiliation
)


def create_preprint(env, attributes, token):
    """Creates a new preprint and returns its ID."""
    response = create_new_preprint(env, attributes, token)
    if response.status_code != 201:
        print_error("creating preprint", response)
        return None

    preprint_id = response.json()['data']['id']
    print_success("Preprint created successfully!", {"Preprint ID": preprint_id})
    return preprint_id


def update_subjects_and_license(env, preprint_id, license_id, subject_ids, token):
    """Updates the preprint's subjects and license."""
    response = update_subject_and_licenses(env, preprint_id, license_id, subject_ids, token)
    if response.status_code != 200:
        print_error("updating subjects and license", response)
        return False

    print_success("Subjects and license updated successfully.", response.json())
    return True


def upload_and_set_primary_file(env, preprint_id, file_path, file_name, token):
    """Uploads a file to the preprint and sets it as the primary file."""
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
    """Submits the preprint for review."""
    review_response = create_preprint_review_action(env, preprint_id, trigger, token)
    if review_response.status_code != 201:
        print_error("submitting preprint for review", review_response)
        return False

    print_success("Preprint submitted for review successfully.", review_response.json())
    return True


def update_institution_affiliation(env, preprint_id, institution_ids, token):
    """Updates the preprint's institutional affiliations."""
    response = update_preprint_institution_affiliation(env, preprint_id, institution_ids, token)
    if response.status_code != 200:
        print_error("updating institution affiliations", response)
        return False

    print_success("Institution affiliations updated successfully.", response.json())
    return True


def extract_file_id(file_data):
    """Extracts the file ID from the upload response."""
    try:
        return file_data['data']['id'].split('/')[-1]
    except (KeyError, IndexError, TypeError):
        return None


def print_success(message, data):
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


def create_multiple_preprints(env, preprint_list, token):
    """Creates multiple preprints based on the provided list of preprint attributes."""
    for preprint_data in preprint_list:
        attributes = preprint_data['attributes']
        license_id = preprint_data['license_id']
        subject_ids = preprint_data['subject_ids']
        file_path = preprint_data['file_path']
        file_name = preprint_data['file_name']
        institution_ids = preprint_data['institution_ids']

        # Step 1: Create the preprint
        preprint_id = create_preprint(env, attributes, token)
        if not preprint_id:
            continue

        # Step 2: Update subjects and license
        if not update_subjects_and_license(env, preprint_id, license_id, subject_ids, token):
            continue

        # Step 3: Upload file and set it as the primary file
        if not upload_and_set_primary_file(env, preprint_id, file_path, file_name, token):
            continue

        # Step 4: Update institution affiliations
        if not update_institution_affiliation(env, preprint_id, institution_ids, token):
            continue

        # Step 5: Submit the preprint for review
        if not submit_preprint_review(env, preprint_id, 'submit', token):
            continue

        # Step 6: Accept the preprint
        submit_preprint_review(env, preprint_id, 'accept', token)


def main():
    env = 'staging3'  # Choose the environment: 'production', 'staging', 'staging2', 'staging3', or 'test'

    # List of preprints to create
    preprint_list = [
        {
            'attributes': {
                'title': 'Preprint 1',
                'description': 'This is the first preprint',
                'provider': 'osf',
            },
            'license_id': '59bac33acb0c480001872bc8',  # https://api.staging3.osf.io/v2/licenses/
            'subject_ids': [['59c152d305ce91001c0242b4']], # https://api.staging3.osf.io/v2/subjects/
            'file_path': 'fixtures/test1.txt',
            'file_name': 'test1.txt',
            'institution_ids': ['cos', 'yls']
        },
        {
            'attributes': {
                'title': 'Preprint 2',
                'description': 'This is the second preprint',
                'provider': 'osf',
            },
            'license_id': '59bac33acb0c480001872bc8',
            'subject_ids': [['59c152d305ce91001c0242b4']],
            'file_path': 'fixtures/test2.txt',
            'file_name': 'test2.txt',
            'institution_ids': ['cos', 'yls']
        }
    ]

    # Create multiple preprints
    create_multiple_preprints(env, preprint_list, token)


if __name__ == '__main__':
    main()
