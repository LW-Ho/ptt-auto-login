import json
import PyPtt
import time
from random import randrange

PTTACCOUNTS = {}

with open('accounts.json', 'r', encoding='utf-8') as file:
    PTTACCOUNTS = json.load(file)

def main():
    for account in PTTACCOUNTS['accounts']:
        api = PyPtt.API()
        api.login(
            ptt_id=account['ptt_id'],
            ptt_pw=account['ptt_pw']
        )
        api.logout()
        time.sleep(5)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600 + randrange(180))