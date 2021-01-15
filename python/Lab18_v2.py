# Lab 18 - ATM - Create a class that uses the given code, add transactions to show what user did

class ATM:
    def __init__(self):
        self.leger = 0
        self.interest = .001
        self.transactions = []
    
    def balance(self):
        self.transactions.append(f"user checked balance of {balance}")
        return self.leger
    
    def deposit(self, amount):
        self.leger += amount
        self.transactions.append(f"user deposited ${amount}")

    def check_withdrawal(self, amount):
        if self.leger >= amount:
            self.transactions.append(f"user withdrew #{amount}")
            return True
        else:
            self.transactions.append(f"user did not have enough balance for ${amount} withdrawl")
            return False

    def withdraw(self, amount):
        self.leger -= amount

    def calc_interest(self):
        interest_gain = self.leger * self.interest
        self.transactions.append(f"user checked interest earned of {amount}")
        return interest_gain

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
        
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        for item in atm.transactions:
            print(item, end='\n')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')