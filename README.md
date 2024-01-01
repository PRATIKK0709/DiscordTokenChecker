# Discord Token Checker

<img src="https://cdn.discordapp.com/attachments/1137109705139957880/1190924861539893278/discord-mark-blue.png?ex=65a39235&is=65911d35&hm=42b02394ae0d9f8aa2a8ca8651a4287ea757ea15c2194a2cab479313c54ab9cd" alt="Discord Logo" width="65.85" height="50">

The provided Python script checks the validity of Discord access tokens(account tokens) by making requests to the Discord API. It reads tokens from a file, sends requests to the Discord API to verify each token, and logs the results. Valid tokens are saved to a JSON file, and logs are recorded in a separate log file. The script provides a basic way to assess the validity of Discord tokens and manage the results.



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

