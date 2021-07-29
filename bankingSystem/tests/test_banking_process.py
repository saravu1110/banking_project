import pytest
import os
from src.main import create_new_account, get_account_balance, amount_withdrawal, amount_deposit, \
    transfer_amount_across_accounts
from src.utils.utils import LOCAL_DB_DIRECTORY_PATH
from mock import patch
from os import path
import datetime


@pytest.fixture(autouse=True, scope="module")
def test_pre_processor():
    """ Create test data in local_db.json , If already existed then its deleted the entry before creating test data"""
    # Setup: Create test data
    # Delete a record if existed, to avoid duplicate creation of test data
    if path.exists(LOCAL_DB_DIRECTORY_PATH):
        # Removing local db file if exist. To avoid duplicate test data
        os.remove(LOCAL_DB_DIRECTORY_PATH)


def test_banking_process(test_pre_processor):
    mock_account_one = 1001
    mock_account_two = 1002

    print("Account Creation Test")

    # Account creation one
    with patch("src.utils.utils.random.randint", return_value=mock_account_one):
        account_number = create_new_account("saravana")
        assert mock_account_one == account_number
        print(f"Input : saravana")
        print(f'Output : Account number for Account holder saravana is {mock_account_one}')

    # Account creation two
    with patch("src.utils.utils.random.randint", return_value=mock_account_two):
        account_number = create_new_account("kumar")
        assert mock_account_two == account_number
        print(f"Input : kumar")
        print(f'Outpu : Account number for Account holder kumar is {mock_account_two}')

    print("Amount Deposit Test")

    # Invalid Amount number
    response = amount_deposit(123123, 5000)
    assert response == f"Invalid Account Number - {123123}"
    print(f"Input: Deposit {123123} {5000}")
    print("Output:", f"Invalid Account Number - {123123}")

    # 1st deposit
    response = amount_deposit(mock_account_one, 500)
    assert response == 500
    print(f"Input: Deposit {mock_account_one} {500}")
    print("Output:", response)

    # 2nd deposit
    response = amount_deposit(mock_account_one, 1000)
    assert response == 1500
    print(f"Input: Deposit {mock_account_one} {1000}")
    print("Output:", response)

    # Minimum deposit amount
    response = amount_deposit(mock_account_one, 100)
    assert str(response) == f"Minimum deposit amount is 500 for account {mock_account_one}"
    print(f"Input: Deposit {mock_account_one} {100}")
    print("Output:", response)

    # Maximum deposit amount
    response = amount_deposit(mock_account_one, 60000)
    assert str(response) == f"Maximum deposit amount is 50000 for account {mock_account_one}"
    print(f"Input: Deposit {mock_account_one} {60000}")
    print("Output:", response)

    # 3rd deposit
    response = amount_deposit(mock_account_one, 10000)
    assert response == 11500
    print(f"Input: Deposit {mock_account_one} {10000}")
    print("Output:", response)

    # Only 3 deposit allowed per day
    response = amount_deposit(mock_account_one, 10000)
    assert str(response) == "Only 3 deposits are allowed in a day"
    print(f"Input: Deposit {mock_account_one} {10000}")
    print("Output:", response)

    print("Account Balance Test")

    response = get_account_balance(str(mock_account_one))
    assert response == 11500
    print(f"Input: Balance {mock_account_one}")
    print(f"Output: ", response)

    response = get_account_balance(str(1231232132))
    assert str(response) == "Invalid Account Number - 1231232132"
    print(f"Input: Balance {1231232132}")
    print(f"Output: ", response)

    print("Amount Withdrawal test")

    # Invalid Amount number
    response = amount_withdrawal(111111, 5000)
    assert response == f"Invalid Account Number - {111111}"
    print(f"Input: Deposit {111111} {5000}")
    print("Output:", f"Invalid Account Number - {111111}")

    # Minimum withdrawal amount
    response = amount_withdrawal(mock_account_one, 500)
    assert str(response) == f"Minimum withdrawal amount is 1000 for account {mock_account_one}"
    print(f"Input: Withdraw {mock_account_one} {500}")
    print("Output:", response)

    # Maximum withdrawal amount
    response = amount_withdrawal(mock_account_one, 30000)
    assert str(response) == f"Maximum withdrawal amount is 25000 for account {mock_account_one}"
    print(f"Input: Withdraw {mock_account_one} {500}")
    print("Output:", response)

    # Insufficient balance
    response = amount_withdrawal(mock_account_one, 20000)
    assert str(response) == "Insufficient Balance"
    print(f"Input: Withdraw {mock_account_one} {20000}")
    print("Output:", response)

    # 1st withdraw
    response = amount_withdrawal(mock_account_one, 1000)
    assert response == 10500
    print(f"Input: Withdraw {mock_account_one} {1000}")
    print("Output:", 10500)

    # 2nd withdraw
    response = amount_withdrawal(mock_account_one, 1900)
    assert response == 8600
    print(f"Input: Withdraw {mock_account_one} {1900}")
    print("Output:", response)

    # 3rd withdraw
    response = amount_withdrawal(mock_account_one, 1000)
    assert response == 7600
    print(f"Input: Withdraw {mock_account_one} {1000}")
    print("Output:", response)

    # Only 3 withdraw allowed per day
    response = amount_withdrawal(mock_account_one, 5000)
    assert str(response) == "Only 3 withdrawal are allowed in a day"
    print(f"Input: Withdraw {mock_account_one} {5000}")
    print("Output:", response)

    print("Amount Transfer test")

    source_mock_account = 1003
    target_mock_account = 1004

    # Account creation one
    with patch("src.utils.utils.random.randint", return_value=source_mock_account):
        source_account_number = create_new_account("source_account")
        # Deposit amount to source account to test amount transfer
        amount_deposit(source_account_number, 45000)
        amount_deposit(source_account_number, 35000)

    # Account creation two
    with patch("src.utils.utils.random.randint", return_value=target_mock_account):
        target_account_number = create_new_account("target_account")

    # Successful
    response = transfer_amount_across_accounts(source_mock_account, target_mock_account, 5000)
    assert response == "Successful"
    print(f"Input: Transfer {source_mock_account} {target_mock_account} {5000}")
    print("Output:", response)

    # Minimum withdrawal
    response = transfer_amount_across_accounts(source_mock_account, target_mock_account, 500)
    assert response == f"Minimum withdrawal amount is 1000 for account {source_mock_account}"
    print(f"Input: Transfer {source_mock_account} {target_mock_account} {500}")
    print("Output:", response)

    # Maximum withdrawal
    response = transfer_amount_across_accounts(source_mock_account, target_mock_account, 30000)
    assert response == f"Maximum withdrawal amount is 25000 for account {source_mock_account}"
    print(f"Input: Transfer {source_mock_account} {target_mock_account} {500}")
    print("Output:", response)

    # Account amount exceeds 1,00,000 on target account
    # Adding amount to target account to test as below, To test account amount exceeds 1,00,000
    amount_deposit(target_account_number, 45000)
    amount_deposit(target_account_number, 45000)
    response = transfer_amount_across_accounts(source_mock_account, target_mock_account, 25000)
    assert response == "Account balance cannot exceed ₹1,00,000, Please try will lesser deposit amount"
    print(f"Input: Transfer {source_mock_account} {target_mock_account} {25000}")
    print("Output:", response)

    print("Account amount exceeds 1,00,000")
    # Account balance exceed 1,00,000
    response = amount_deposit(source_mock_account, 45000)
    assert str(response) == "Account balance cannot exceed ₹1,00,000, Please try will lesser deposit amount"
    print(f"Input: Deposit {source_mock_account} {45000}")
    print("Output:", response)

    print("Test deposit transaction limit reset on next day")
    next_date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d-%m-%Y')
    with patch("src.utils.utils.get_current_date", return_value=next_date):
        # 1st deposit with next day
        response = amount_deposit(mock_account_one, 500)
        assert response == 8100
        print(f"Input: Deposit {mock_account_one} {500}")
        print("Output:", response)

    print("Test withdrawal transaction limit reset on next day")
    with patch("src.utils.utils.get_current_date", return_value=next_date):
        # 1st withdrawal with next day
        response = amount_withdrawal(mock_account_one, 1000)
        assert response == 7100
        print(f"Input: Deposit {mock_account_one} {1000}")
        print("Output:", response)
