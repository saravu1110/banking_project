from src.banking_process.deposit_transaction import Deposit
from src.banking_process.withdraw_transaction import Withdraw


class BalanceTransfer:

    @staticmethod
    def process_balance_transfer(source_account_number, target_account_number, transfer_amount):
        try:
            withdraw = Withdraw(source_account_number)
            deposit = Deposit(target_account_number)
            source_account_status = deposit.check_deposit_is_applicable(transfer_amount)
            target_account_status = withdraw.check_withdraw_is_applicable(transfer_amount)

            if source_account_status is True and target_account_status is True:
                deposit.deposit_amount(deposit.get_account_details(), transfer_amount)
                withdraw.withdraw_amount(withdraw.get_account_details(), transfer_amount)

                return "Successful"

        except Exception as e:
            return str(e)
