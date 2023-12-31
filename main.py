import http.client
import json
import os
import logging

LOG_FILE = 'token_checker.log'
TOKEN_FILE = 'tokens.txt'
VALID_TOKEN_FILE = 'valid_tokens.json'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def check(token, conn):
    try:
        conn.request('GET', '/api/v9/users/@me/guild-events', headers={'Authorization': token})
        response = conn.getresponse()
        if response.status == 401 or "Verify account." in response.read().decode():
            return False
        return True
    except Exception as e:
        logging.error(f'Error checking token: {e}')
        return False

def save_valid_tokens(valid_tokens):
    if valid_tokens:
        data = {token: True for token in valid_tokens}
        with open(VALID_TOKEN_FILE, 'w') as save_file:
            json.dump(data, save_file, indent=2)
        logging.info('Valid token(s) are saved to valid_tokens.json file!')

def read_tokens_from_file(file_path=TOKEN_FILE):
    try:
        with open(file_path, 'r') as tokens:
            return tokens.read().split('\n')
    except FileNotFoundError:
        logging.error(f'Token file not found: {file_path}')
        return []

def process_tokens(tokens, conn):
    valid_tokens = []
    for token in tokens:
        if len(token) > 15 and token not in valid_tokens and check(token, conn):
            logging.info(f'Valid: {token}')
            valid_tokens.append(token)
        else:
            logging.warning(f'Invalid: {token}')
    return valid_tokens

def main():
    conn = http.client.HTTPSConnection('discord.com')
    try:
        tokens_to_check = read_tokens_from_file()
        valid_tokens = process_tokens(tokens_to_check, conn)
        save_valid_tokens(valid_tokens)
        input('Enter to EXIT the program')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
