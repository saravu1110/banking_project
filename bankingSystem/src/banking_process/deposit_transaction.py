from src.banking_process.account_details import AccountDetails
from src.utils.utils import write_data_to_local_database, check_transaction_limit_per_day

MINIMUM_DEPOSIT_ACCOUNT = 500
MAXIMUM_DEPOSIT_ACCOUNT = 50000
MAX_BALANCE_LIMIT = 100000
MAX_TRANSACTION_PER_DAY = 3


class Deposit(AccountDetails):

    def __init__(self, account_number):
        super().__init__(account_number)

    def process_deposit_transaction(self, amount_to_be_credited):
        try:
            if self.check_deposit_is_applicable(amount_to_be_credited):
                return self.deposit_amount(self.get_account_details(), amount_to_be_credited)

        except Exception as e:
            return str(e)

    def check_deposit_is_applicable(self, amount_to_be_credited):
        try:
            account_details = self.get_account_details()

            if amount_to_be_credited < MINIMUM_DEPOSIT_ACCOUNT:
                raise Exception(f"Minimum deposit amount is 500 for account {self._account_number}")
            elif amount_to_be_credited > MAXIMUM_DEPOSIT_ACCOUNT:
                raise Exception(f"Maximum deposit amount is 50000 for account {self._account_number}")

            total_amount_to_be_deposited = account_details['Balance'] + amount_to_be_credited
            if total_amount_to_be_deposited > MAX_BALANCE_LIMIT:
                raise Exception("Account balance cannot exceed ₹1,00,000, Please try will lesser deposit amount")

            self.check_transaction_limit_per_day(account_details)

            return True

        except Exception as e:
            raise Exception(str(e))

    def check_transaction_limit_per_day(self, account_details):
        account_details = check_transaction_limit_per_day(account_details, "deposit")
        self.local_database_data[self._account_number] = account_details
        write_data_to_local_database(self.local_database_data)

    def deposit_amount(self, account_details, amount_to_be_credited):
        total_amount = account_details['Balance'] + amount_to_be_credited
        account_details['Balance'] = total_amount
        account_details['Deposit_Transaction_Per_Day'] = account_details['Deposit_Transaction_Per_Day'] + 1
        self.local_database_data[self._account_number] = account_details
        write_data_to_local_database(self.local_database_data)
        return total_amount
