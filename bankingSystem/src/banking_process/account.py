from src.banking_process.account_creation import AccountCreation
from src.banking_process.account_details import AccountDetails
from src.banking_process.deposit_transaction import Deposit
from src.banking_process.withdraw_transaction import Withdraw
from src.banking_process.balance_transfer import BalanceTransfer


class Account:

    @staticmethod
    def create_account(account_holder_name):
        return AccountCreation().create_new_account(account_holder_name)

    @staticmethod
    def get_balance(account_number):
        return AccountDetails(account_number).get_account_balance()

    @staticmethod
    def deposit_amount(account_number, amount_to_be_credited):
        return Deposit(account_number).process_deposit_transaction(amount_to_be_credited)

    @staticmethod
    def withdraw_amount(account_number, amount_to_be_debited):
        return Withdraw(account_number).process_withdraw_transaction(amount_to_be_debited)

    @staticmethod
    def balance_transfer(source_account_number, target_account_number, transfer_amount):
        return BalanceTransfer().process_balance_transfer(source_account_number, target_account_number, transfer_amount)
