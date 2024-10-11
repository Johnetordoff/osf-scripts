import os

HERE = os.path.split(os.path.abspath(__file__))[0]


def create_env_file():
    # Define test values
    test_values = {
        'TOKEN': 'test_token',
        'USERNAME': 'test_username',
        'PASSWORD': 'test_password'
    }

    # Create and write test values to the .env file
    with open(os.path.join(HERE, '.env'), 'w') as env_file:
        for key, value in test_values.items():
            env_file.write(f"{key}={value}\n")
    print(".env file was missing and has been created with test values.")


def get_credentials():
    credentials = {}  # Create a dictionary to store credentials

    # Check if the environment variables are set, else use fallback values
    with open(os.path.join(HERE, '.env'), 'r') as env_file:
        for line in env_file.read().splitlines():
            key, value = line.split('=', 1)
            key = key.strip().lower()  # Make sure the key is in lowercase
            credentials[key] = value.strip()

    # Return the credentials as individual values
    return credentials.get('token'), credentials.get('username'), credentials.get('password')

token, username, password = get_credentials()

urls = {
    'production': 'https://api.osf.io/v2/',  # Production V2
    'local': 'http://localhost:8000/v2/',  # Local V2
    'local_v1': 'http://localhost:5000/api/v1/',  # Local V1
    'staging': 'https://api.staging.osf.io/v2/',  # Staging 1 V2
    'staging2': 'https://api.staging2.osf.io/v2/',  # Staging 2 V2
    'staging3': 'https://api.staging3.osf.io/v2/',  # Staging 3 V2
    'test': 'https://api.test.osf.io/v2/',  # Test 2 V2
}

waterbutler_urls = {
    'production': 'https://files.us.osf.io/',  # Production V2
    'local': 'http://localhost:7777/',  # Local V2
    'staging': 'https://files.us.staging.osf.io/',  # Staging 1 V2
    'staging2': 'https://files.us.staging2.osf.io/',  # Staging 2 V2
    'staging3': 'https://files.us.staging3.osf.io/',  # Staging 3 V2
    'test': 'https://files.us.test.osf.io/',  # test V2
}
