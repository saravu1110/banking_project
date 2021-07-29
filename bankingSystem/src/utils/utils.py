import os.path
import json
import random
from datetime import datetime

LOCAL_DB_DIRECTORY_PATH = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) + '/tests/local_db.json')


def generate_account_number():
    """Generate unique  4 digit account number"""
    return random.randint(1000, 9999)


def get_current_date():
    """Return current date"""
    return datetime.today().strftime('%d-%m-%Y')


def read_data_from_local_database():
    """read data form local db and convert into python dict"""
    with open(LOCAL_DB_DIRECTORY_PATH) as open_file:
        local_db_data = json.load(open_file)

    return local_db_data


def write_data_to_local_database(data):
    """write python dict into local database file"""
    with open(LOCAL_DB_DIRECTORY_PATH, "w") as outfile:
        json.dump(data, outfile, indent=4, skipkeys=True)

    return data


def check_transaction_limit_per_day(account_details, transaction_type):
    """check deposit and withdraw transaction per day"""
    current_date = get_current_date()
    # Check transaction limit for deposit transaction
    if transaction_type == "deposit":
        if account_details['Last_Transaction_Date'] == current_date and \
                account_details['Deposit_Transaction_Per_Day'] == 3:
            raise Exception("Only 3 deposits are allowed in a day")

    # Check transaction limit for withdrawal transaction
    elif transaction_type == "withdraw":
        if account_details['Last_Transaction_Date'] == current_date and \
                account_details['Withdrawal_Transaction_Per_Day'] == 3:
            raise Exception("Only 3 withdrawal are allowed in a day")

    # Reset transaction limit for next day
    if account_details['Last_Transaction_Date'] != current_date:
        account_details['Deposit_Transaction_Per_Day'] = 0
        account_details['Withdrawal_Transaction_Per_Day'] = 0
        account_details['Last_Transaction_Date'] = current_date

    return account_details

