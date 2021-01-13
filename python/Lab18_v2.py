# Lab 18 - ATM - Create a class that uses the given code, add transactions to show what user did

class ATM():
    def __init__(self):
        self.leger = 0
        self.interest = .001
    
    def balance(self):
        return self.leger
    
    def deposit(self, amount):
        self.leger += amount
        return self.leger

    def check_withdrawal(self, amount):
        if self.leger > amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.leger -= amount
        return amount

    def calc_interest(self):
        interest_gain = self.leger * self.interest
        return interest_gain

transactions = [] # keep list of transactions
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
        transactions.append(f"user checked balance of {balance}")
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        transactions.append(f"user deposited ${amount}")
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            transactions.append(f"user withdrew #{amount}")
        else:
            print('Insufficient funds')
            transactions.append(f"user did not have enough balance for ${amount} withdrawl")
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
        transactions.append(f"user checked interest earned of {amount}")
    
    elif command == 'transactions':
        for item in transactions:
            print(item, end='\n')

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')