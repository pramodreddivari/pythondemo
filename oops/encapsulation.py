class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Instance variable for balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance


# Example usage
obj = BankAccount(1000)  # Creating an instance with an initial balance of 1000
obj.deposit(500)         # Depositing 500
obj.withdraw(200)        # Withdrawing 200
print(f"Current balance: {obj.get_balance()}")
# Output: Current balance: 1300

class BankAccount:
    def __init__(self,accno,intialbalance):
        self.accno=accno#public variable
        self._intialbalance=intialbalance #protected variable
        self.__pin=1234 #private variable
        #public method
    def getbalance(self):
            return self._intialbalance
        
        #Public method to access private data safely
        
    def withdraw(self,amount,pin):
            if pin!=self.__pin:
                print("Incorrect PIN. Cannot withdraw.")
            elif amount> self._intialbalance:
                print("Insufficient balance for withdrawal.")
            else:
                self._intialbalance -= amount
                print(f"Withdrew {amount}. New balance is {self._intialbalance}.")
    def deposit(self,amount):
            if amount>0:
                self._intialbalance += amount
                print(f"Deposited {amount}. New balance is {self._intialbalance}.")
            else:
                print("Deposit amount must be positive.")
        
          # Private method
    def __validate_transaction(self, amount):
        return amount > 0 and amount <= self._balance

# Create account
account = BankAccount("12345", 1000)

# Access public attribute
print(account.account_number)  # 12345

# Access protected attribute (not recommended but possible)
print(account._balance)        # 1000

# Try to access private attribute (won't work directly)
# print(account.__pin)         # AttributeError

# Access private attribute using name mangling (not recommended)
print(account._BankAccount__pin)  # 1234

# Use public methods
print(account.deposit(500))     # Deposited $500. Balance: $1500
print(account.withdraw(200, 1234))  # Withdrew $200. Balance: $1300
print(account.withdraw(200, 9999))  # Invalid PIN
    