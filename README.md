# Discord Token Checker

The provided Python script checks the validity of Discord access tokens by making requests to the Discord API. It reads tokens from a file, sends requests to the Discord API to verify each token, and logs the results. Valid tokens are saved to a JSON file, and logs are recorded in a separate log file. The script provides a basic way to assess the validity of Discord tokens and manage the results.

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

