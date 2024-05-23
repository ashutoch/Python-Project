import datetime

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.datetime.now()

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction('Deposit', amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(Transaction('Withdraw', amount))
            return True
        else:
            print('Insufficient balance')
            return False

    def transfer(self, recipient_account_number, amount, all_accounts):
        accounts = [Account(user['account_number'], 0) for user in all_accounts]

        recipient = next((acc for acc in accounts if acc.account_number == recipient_account_number), None)

        if recipient:
            if self.withdraw(amount):
                recipient.deposit(amount)
                print("Transfer successful")
            else:
                print("Insufficient balance")
        else:
            print("Recipient account not found")

    def get_transaction_history(self):
        return self.transaction_history

    def get_transaction_history(self):
        return self.transaction_history

class Authentication:
    def __init__(self, users):
        self.users = users

    def authenticate(self, user_id, pin):
        for user in self.users:
            if user['user_id'] == user_id and user['pin'] == pin:
                return user['account_number']
        return None

class Console:
    def display_main_menu(self):
        print('1. Transactions History')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Transfer')
        print('5. Check Balance')
        print('6. Quit')

    def get_user_input(self):
        choice = int(input('Enter your choice: '))
        return choice

    def get_amount(self):
        amount = float(input('Enter the amount: '))
        return amount

    def get_recipient_account_number(self):
        recipient_account_number = int(input('Enter the recipient account number: '))
        return recipient_account_number

class ATM:
    def __init__(self, authentication):
        self.authentication = authentication

    def run(self):
        account_number = self.authentication.authenticate(input('Enter your user ID: '), input('Enter your pin: '))
        if account_number is not None:
            account = Account(account_number, 10000)  #initial balance 
            console = Console()
            while True:
                console.display_main_menu()
                choice = console.get_user_input()
                if choice == 1:
                    transactions = account.get_transaction_history()
                    for transaction in transactions:
                        print(f'{transaction.timestamp} - {transaction.transaction_type} - ₹{transaction.amount}')
                elif choice == 2:
                    amount = console.get_amount()
                    account.withdraw(amount)
                elif choice == 3:
                    amount = console.get_amount()
                    account.deposit(amount)
                elif choice == 4:
                    recipient_account_number = console.get_recipient_account_number()
                    amount = console.get_amount()
                    account.transfer(recipient_account_number, amount, authentication.users)
                elif choice == 5:
                    print(f'Your balance is ₹{account.balance}')  
                elif choice == 6:
                    print('Thank you for using the ATM. Goodbye!')
                    break
                else:
                    print('Invalid choice. Please try again.')

                print(f'Your current balance is ₹{account.balance}\n')
        else:
            print('Invalid user ID or pin.')

users = [
    {'user_id': '1234', 'pin': '1111', 'account_number': 100001},
    {'user_id': '4321', 'pin': '2222', 'account_number': 100002},
]

authentication = Authentication(users)

atm = ATM(authentication)
atm.run()

