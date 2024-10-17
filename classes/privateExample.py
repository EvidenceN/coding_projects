class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount methods can access self._balance, but code outside of
        # this class should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return  # Don't allow negative "deposits".
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  # Not enough in account, or withdraw is negative.
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice')  # We create an account for Alice.
acct.deposit(120)  # _balance can be affected through deposit()
acct.withdraw(40)  # _balance can be affected through withdraw()

# Changing _name or _balance outside of BankAccount is impolite, but allowed:
acct._balance = 1000000000
acct.withdraw(1000)

acct._name = 'Bob'  # Now we're modifying Bob's account ledger!
acct.withdraw(1000)  # This withdrawal is recorded in BobLedger.txt!



"""
Explanation why this is wrong

When you run privateExample.py, the ledger files it creates are inaccurate because we modified the _balance and _name outside the class, which resulted in invalid states. AliceLedger.txt inexplicably has a lot of money in it:

Balance is 0
Deposit 120
Balance is 120
Withdraw 40
Balance is 80
Withdraw 1000
Balance is 999999000

Now there’s a BobLedger.txt file with an inexplicable account balance, even though we never created a BankAccount object for Bob:

Withdraw 1000
Balance is 999998000
"""
