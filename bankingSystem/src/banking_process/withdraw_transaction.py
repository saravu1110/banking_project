from src.banking_process.account_details import AccountDetails
from src.utils.utils import write_data_to_local_database, check_transaction_limit_per_day

MINIMUM_WITHDRAW_ACCOUNT = 1000
MAXIMUM_WITHDRAW_ACCOUNT = 25000
MIN_BALANCE_LIMIT = 0
MAX_TRANSACTION_PER_DAY = 3


class Withdraw(AccountDetails):

    def __init__(self, account_number):
        super().__init__(account_number)

    def process_withdraw_transaction(self, amount_to_be_debited):
        try:
            if self.check_withdraw_is_applicable(amount_to_be_debited):
                return self.withdraw_amount(self.get_account_details(), amount_to_be_debited)

        except Exception as e:
            return str(e)

    def check_withdraw_is_applicable(self, amount_to_be_debited):
        try:
            account_details = self.get_account_details()

            if amount_to_be_debited < MINIMUM_WITHDRAW_ACCOUNT:
                raise Exception(f"Minimum withdrawal amount is 1000 for account {self._account_number}")
            elif amount_to_be_debited > MAXIMUM_WITHDRAW_ACCOUNT:
                raise Exception(f"Maximum withdrawal amount is 25000 for account {self._account_number}")

            total_amount_to_be_withdrawn = account_details['Balance'] - amount_to_be_debited
            if total_amount_to_be_withdrawn < MIN_BALANCE_LIMIT:
                raise Exception("Insufficient Balance")

            self.check_transaction_limit_per_day(account_details)

            return True

        except Exception as e:
            raise Exception(str(e))

    def check_transaction_limit_per_day(self, account_details):
        account_details = check_transaction_limit_per_day(account_details, "withdraw")
        self.local_database_data[self._account_number] = account_details
        write_data_to_local_database(self.local_database_data)

    def withdraw_amount(self, account_details, amount_to_be_debited):
        total_amount = account_details['Balance'] - amount_to_be_debited
        account_details['Balance'] = total_amount
        account_details['Withdrawal_Transaction_Per_Day'] = account_details['Withdrawal_Transaction_Per_Day'] + 1
        self.local_database_data[self._account_number] = account_details
        write_data_to_local_database(self.local_database_data)
        return total_amount
