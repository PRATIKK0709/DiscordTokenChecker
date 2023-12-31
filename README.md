# Discord Token Checker

The provided Python script serves as a Discord token checker, allowing users to verify the validity of Discord access tokens. These tokens are commonly used for authentication and authorization purposes in Discord API requests. The script utilizes the `http.client` module to make a GET request to the Discord API endpoint responsible for fetching information about the authenticated user's guild events. For each token listed in the `tokens.txt` file, the script checks whether the associated Discord account has the necessary permissions to access the specified API endpoint. Valid tokens are then saved to a `valid_tokens.json` file, and detailed logs are recorded in a `token_checker.log` file. The script employs basic error handling to capture and log exceptions during token verification. Users can easily run the script, inputting their Discord tokens, and receive information about the validity of each token along with saved logs and a file containing the valid tokens.


- Valid tokens will be saved to `valid_tokens.json`, and logs will be written to `token_checker.log`.

## Configuration

- `token_checker.py`: Main script file.
- `tokens.txt`: File containing Discord tokens to check.
- `token_checker.log`: Log file for script activity.
- `valid_tokens.json`: JSON file storing valid Discord tokens.

## Dependencies

- `http.client`: Standard library module for making HTTP requests.
- `json`: Standard library module for working with JSON data.
- `logging`: Standard library module for logging messages.
- `os`: Standard library module for interacting with the operating system.

