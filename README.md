# Discord Token Checker

This Python script checks the validity of Discord tokens by making requests to the Discord API.



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

