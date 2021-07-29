from src.utils.utils import read_data_from_local_database


class AccountDetails:

    def __init__(self, account_number):
        self._account_number = account_number
        self.local_database_data = read_data_from_local_database()

    def get_account_details(self):
        try:
            # Query in local database with account number
            account_details = self.local_database_data[self._account_number]
            return account_details

        except Exception as e:
            raise Exception(f"Invalid Account Number - {self._account_number}")

    def get_account_balance(self):
        try:
            account_details = self.get_account_details()
            return account_details['Balance']

        except Exception as e:
            return str(e)
