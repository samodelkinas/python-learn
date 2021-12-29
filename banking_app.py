import datetime
import os


def write_transaction(type, amount, balance, date=datetime.datetime.now()):
    with open('transactions', 'a') as transactions:
        transactions.write(f"{date}\t{type}\t{amount}\t{balance}\n")
    with open('balance', 'w') as balance_file:
        balance_file.write(f"{balance}")


def read_balance():
    if not os.path.isfile('balance'):
        return 0.00
    with open('balance', 'r') as balance:
        return float(balance.read())


class Bank:
    def __init__(self, balance):
        self.current_balance = balance

    @property
    def get_balance(self):
        return self.current_balance

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount
        write_transaction('d', amount, self.current_balance)

    def withdraw(self, amount):
        self.current_balance = self.current_balance - amount
        write_transaction('w', amount, self.current_balance)


bank = Bank(read_balance())

while True:
    transaction_type = input(
        "Choose [w] to withdraw or [d] to deposit, [b] for balance:")
    if transaction_type not in ['w', 'd', 'b']:
        print("choose w, d or b")
        continue
    if transaction_type == 'b':
        print(bank.get_balance)
        continue
    amount = input("Enter amount (float):")
    try:
        amount = float(amount)
    except Exception:
        print('Please enter floating point number')
        continue
    if transaction_type == 'd':
        bank.deposit(amount)

    if transaction_type == 'w':
        bank.withdraw(amount)
