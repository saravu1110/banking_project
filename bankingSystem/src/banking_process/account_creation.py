import os.path
import json
from src.utils.utils import generate_account_number, get_current_date

# Create local db json file under tests folder
LOCAL_DB_DIRECTORY_PATH = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) + '/tests/local_db.json')


class AccountCreation:

    def __init__(self):
        self.__account_holder_name = None
        self.__account_number = None
        self.__balance = 0
        self.__deposit_transaction_per_day = 0
        self.__withdrawal_transaction_per_day = 0
        self.__last_transaction_date = get_current_date()

    def create_new_account(self, account_holder_name):
        try:
            self.__account_holder_name = account_holder_name
            self.__account_number = generate_account_number()

            create_account = {
                self.__account_number: {
                        'Account_Holder_Name': self.__account_holder_name,
                        'Balance': self.__balance,
                        'Deposit_Transaction_Per_Day': self.__deposit_transaction_per_day,
                        'Withdrawal_Transaction_Per_Day': self.__withdrawal_transaction_per_day,
                        'Last_Transaction_Date': self.__last_transaction_date
                }
            }
            # LOCAL_DB_DIRECTORY_PATH act as local database
            with open(LOCAL_DB_DIRECTORY_PATH) as open_file:
                local_db = json.load(open_file)
                local_db.update(create_account)
                with open(LOCAL_DB_DIRECTORY_PATH, "w") as outfile:
                    json.dump(local_db, outfile, indent=4, skipkeys=True)

            return self.__account_number

        except FileNotFoundError as e:
            # If file not found creating new local  database file
            with open(LOCAL_DB_DIRECTORY_PATH, "w") as outfile:
                json.dump({}, outfile, indent=4)
            # Recursive concept
            return self.create_new_account(account_holder_name)
