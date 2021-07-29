from src.banking_process.account import Account


def create_new_account(name_of_new_account_holder):
    """
    This function with flow through create account mechanism
    :param name_of_new_account_holder:
    :return: account number
    """
    return Account().create_account(name_of_new_account_holder)


def get_account_balance(account_number):
    """
    This function will flow through account current balance mechanism
    :param account_number:
    :return: balance amount or appropriate response
    """
    return Account().get_balance(str(account_number))


def amount_deposit(account_number, amount_to_be_deposit):
    """
    This function will flow through deposit amount to it's respective account mechanism
    :param account_number:
    :param amount_to_be_deposit:
    :return: balance amount or appropriate response
    """
    return Account().deposit_amount(str(account_number), amount_to_be_deposit)


def amount_withdrawal(account_number, amount_to_be_withdrawn):
    """
    This function will flow through withdrawal amount to it's respective account mechanism
    :param account_number:
    :param amount_to_be_withdrawn:
    :return: balance amount or appropriate response
    """
    return Account().withdraw_amount(str(account_number), amount_to_be_withdrawn)


def transfer_amount_across_accounts(source_account_number, target_account_number, amount_to_be_transferred):
    """
    This function will flow through amount transfer between two accounts
    :param source_account_number:
    :param target_account_number:
    :param amount_to_be_transferred:
    :return: appropriate response
    """
    return Account().balance_transfer(str(source_account_number), str(target_account_number),
                                      amount_to_be_transferred)
