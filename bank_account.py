class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit Successful! New Balance is: {self.balance}"
        else:
            return "Invalid Deposit amount"
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful! New balance is: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds" 
        
    def get_balance(self):
        return f"Account balance: {self.balance}"
    
# Create a bank accountfor John with an initial balance of $1000
john_account = BankAccount("John", 1000)

# Check balance
print(john_account.get_balance())

# Deposit Money
print(john_account.deposit(500))

# Check balance
print(john_account.get_balance())

# Withdraw money
print(john_account.withdraw(200))

# Withdraw more money than the balance
print(john_account.withdraw(2000))